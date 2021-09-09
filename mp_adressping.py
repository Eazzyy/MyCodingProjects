import os
import time

while True:
    
    print('\nWelkom bij de adress pinger! Welk soort adress wil je graag pingen? url/ip')
    antwoord = str(input())
    adress_url = 'url'
    adress_ip = 'ip'

    
    
    if antwoord == 'url':
        
        time.sleep(2)
        print('\nTyp de URL waar je graag naartoe wilt pingen')

        url_adres1 = 'www.'

        url_adres2 = str(input())

        if 'www.' in url_adres2:
            os.system('ping {}'.format(url_adres2))
        
        else:
            
            url_adreszonderwww = (str(url_adres1) + str(url_adres2))
            print(url_adreszonderwww)
            os.system('ping {}'.format(url_adreszonderwww))

        #print('\nWil je doorgaan? ja/nee ', end='')
        #antwoord = str(input())

        
        #if antwoord == 'nee':
            
        #    print('\nBedankt voor het gebruiken van deze tool!', end='')
        #    time.sleep(2)
        #    break
        
        #if antwoord == 'ja':
            
        #    print('Je wordt teruggebracht naar het startscherm!')
        #    time.sleep(2)
    
    
    
    if antwoord == 'ip':
        
        time.sleep(2)
        print('Typ het IP-adres 1 gedeelte per keer in\nTyp nu het eerste gedeelte van het IP-adres', end='')
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
        
    print('\nWil je doorgaan? ja/nee ', end='')
    antwoord = str(input())

        
    if antwoord == 'nee':
            
            print('\nBedankt voor het gebruiken van deze tool!', end='')
            time.sleep(2)
            break
        
    if antwoord == 'ja':
            
            print('Je wordt teruggebracht naar het startscherm!')
            time.sleep(2)