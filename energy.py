from getpass import getpass


tpu = 10
run = True
while run:
    timeout = float(input("Enter the time taken: "))
    energy = tpu * timeout

    print('Energy', energy)

    cont = getpass('Should I continue? ')

    if cont == 'q':
        run = False



