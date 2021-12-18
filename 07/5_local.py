first_name = 'kaveh'                # global
last_name = 'mehrbanian'            # " " "
tel = '0937'                        # " " "
address = 'mashhad'                 # " " "


def info():
    first_name = 'amin'             # local for info function, none-local for print_info function
    last_name = 'gh'                # "          "          "          "          "          "
    tel = '0935'                    # "          "          "          "          "          "
    address = 'tehran'              # "          "          "          "          "          "
    print(first_name, last_name, tel, address)

    def print_info():
        global first_name           # use global scope
        global last_name            # use global scope
        nonlocal tel                # use non-local
        address = 'yazd'            # create new address as local
        print(first_name, last_name, tel, address)

    print_info()


info()
