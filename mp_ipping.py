import os

while True:

    print('\nTyp het IP-adres 1 gedeelte per keer in\ntyp nu het eerste gedeelte van het IP adres: ', end='')
    ip_adres1 = int(input())
    print('Typ het tweede gedeelte van het IP adres: ', end='')
    ip_adres2 = int(input())
    print('Typ het derde gedeelte van het IP adres: ', end= '')
    ip_adres3 = int(input())
    print('Typ het vierde gedeelte van het IP adres: ', end= '')
    ip_adres4 = int(input())

    ip_adres = (str(ip_adres1) + '.' + str(ip_adres2) + '.' + str(ip_adres3) + '.' + str(ip_adres4))
    print(ip_adres)
    os.system('ping {}'.format(ip_adres))

    print('\nWil je doorgaan? ', end='')
    antwoord = str(input())
    if antwoord == 'nee':
        break