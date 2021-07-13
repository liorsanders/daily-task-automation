import automater
import getpass

if __name__ == '__main__':
    bank_user = getpass.getpass(prompt='enter bank hapoalim username: ')
    bank_password = getpass.getpass(prompt='enter bank hapoalim password: ')

    Automater = automater.Connector()
    Automater.connect_driver()
    balance = Automater.get_bank_info(bank_user, bank_password)
    print(f'balance: {balance}')
    Automater.driver.close()