import os
import time

while True:

    print('\nTyp de URL waar je graag naar toe wilt pingen')
    url_adres1 = 'www.'

    url_adres2 = str(input())

    if 'www.' in url_adres2:
        os.system('ping {}'.format(url_adres2))
    else:
        url_adreszonderwww = (str(url_adres1) + str(url_adres2))
        print(url_adreszonderwww)
        os.system('ping {}'.format(url_adreszonderwww))

    print('\nWil je doorgaan? ja/nee ', end='')
    antwoord = str(input())

    if antwoord == 'nee':
        print('\nBedankt voor het gebruiken van deze tool!', end='')
        time.sleep(2)
        break
    if antwoord == 'ja':
        print('De tool wordt opnieuw gestart!')
        time.sleep(2)