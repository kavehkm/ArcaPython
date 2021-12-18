first_name = 'kaveh'            # variable first_name defined in global

last_name = 'mehrbanian'        # variable last_name defined in global


def info():
    tel = '0937'                # tel variable defined in none-local scope, top of print_info but inside info function
    address = 'mashhad'         # address variable also defined inside info function but outside of print_info function

    def print_info():
        print(tel, address)     # print function defined in built-in scope

    print_info()


info()                          # call info function that defined in global scope
