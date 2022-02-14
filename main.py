import automater
import getpass

if __name__ == '__main__':
    bank_user = input('enter bank hapoalim username: ')
    bank_password = getpass.getpass(prompt='enter bank hapoalim password: ')
    print(bank_password)
    Automater = automater.Connector()
    print('connected')
    Automater.connect_driver()
    balance = Automater.get_bank_info(bank_user, bank_password)
    print(f'balance: {balance}')
    Automater.driver.close()