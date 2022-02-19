import automater
import getpass
import constants
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os

def get_old_balance():
    if not os.path.exists(f'./{constants.CONFIG_NAME}'):
        return None
    line = open(constants.CONFIG_NAME).readlines()[0].rstrip()
    try:
        return float(line[line.index('=')+1:])
    
    except Exception:
        print('config file error')

def send_mail(balance, password):
    print('sending mail')
    msg = MIMEText(f'''
    your new balance is: {balance}
    {abs(get_old_balance() - balance)} {'more' if get_old_balance() < balance else 'less'} than the old balance
    ''')
    msg['From']=constants.EMAIL
    msg['To']=constants.EMAIL
    msg['Subject']="updated account ballance"

    s = smtplib.SMTP_SSL(host=constants.MAIL_SERVER_EMAIL, port=constants.MAIL_SERVER_PORT)
    s.login(constants.EMAIL, password)
    print(f'logged in to: {constants.EMAIL}, {password}')
    s.sendmail(constants.EMAIL, constants.EMAIL, msg.as_string())
    s.quit()


def update_config(new_balance):
    if not os.path.exists(f'./{constants.CONFIG_NAME}'):
        with open(constants.CONFIG_NAME, 'w') as config:
            config.write(f'balance={constants.DEFAULT_BALANCE}')
    f = open(constants.CONFIG_NAME, 'r')
    text = f.read()
    f.close()
    lines = text.splitlines()
    lines[0] = lines[0][0:lines[0].index('=')+1] + str(new_balance)
    with open(constants.CONFIG_NAME, 'w') as config:
        config.write('\n'.join(lines))

def main():
    user = input('enter bank hapoalim username: ')
    bank_password = getpass.getpass(prompt='enter bank hapoalim password: ')
    email_password = getpass.getpass(prompt=f'enter {constants.EMAIL}\'s password: ')
    while True:
        Automater = automater.Connector()
        print('connected')
        Automater.connect_driver()
        balance = Automater.get_bank_info(user, bank_password)
        old_balance = get_old_balance()
        update_config(balance)
        if old_balance != constants.DEFAULT_BALANCE: # default balance
            send_mail(balance, email_password)
            print('email sent')
        Automater.driver.close()
        time.sleep(constants.HOUR)

if __name__ == '__main__':
    main()