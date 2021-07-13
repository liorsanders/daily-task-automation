import automater


if __name__ == '__main__':
    Automater = automater.Connector()
    Automater.connect_driver()
    Automater.get_bank_info()