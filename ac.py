from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import funkcije
from datetime import datetime
import pyautogui
import random


r_avail = [False,False,False]
r_compl = [False,False,False]
f_r = ['','','']

def battle_checker():
    brojac = 1
    runda = 1
    trazena_rec = 'war/'
    fight = '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[{}]/a[2]'.format(brojac)
    funkcije.browser.get('https://www.edominations.com/en/wars')
    try:
        for i in range(25):
            global r_avail, r_compl, f_r
            nap = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[{}]/div[1]/span/b'.format(brojac))[0].get_attribute('innerHTML')
            odb = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[{}]/div[3]/span/b'.format(brojac))[0].get_attribute('innerHTML')
            href_attr = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[{}]/a[2]'.format(brojac))[0].get_attribute('href')
            zbir = int(nap) + int(odb)
            
            if zbir == 5:
                runda = 3
                r_avail[2] = True
                if trazena_rec not in href_attr:
                    f_r[2] = href_attr
            elif zbir == 2:
                runda = 2
                r_avail[1] = True
                if trazena_rec not in href_attr:
                    f_r[1] = href_attr
            elif zbir == 0:
                runda = 1
                r_avail[0] = True
                if trazena_rec not in href_attr:
                    f_r[0] = href_attr
            
            brojac += 2
    except:
        pass
        
def hit_ac():
    global r_avail, r_compl, f_r
    while True:
        
        r_avail = [False,False,False]
        battle_checker()
        try:
            python_button = funkcije.browser.find_elements_by_id("energyButton")[0]
            sleep(5)
            python_button.click()
            sleep(5)
            energija = (funkcije.browser.find_element_by_id("energyBarT").text).split('/')[0]

            if r_avail[2] == True and r_compl[2] == False and int(energija) >= 2000: # 3 runda
                funkcije.browser.get('https://www.edominations.com/en/wars')
                funkcije.browser.get(f_r[2])
                sleep(5)
                python_button = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[19]/div/a[3]/img')[0]
                python_button.click()                                   
                sleep(5)                                                
                python_button = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[19]/div/div[4]/div/ul/li[16]/a/img')[0]
                python_button.click()                                   
                sleep(5)
                for i in range(20):
                    python_button = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[19]/div/a[2]')[0]
                    python_button.click()                                   
                    sleep(3)
                r_compl[2] = True
                ac_log('Kompletirana treca runda u ' + str(datetime.now().time().strftime('%H:%M:%S')))

            elif r_avail[1] == True and r_compl[1] == False and int(energija) >= 1500: # 2 runda
                funkcije.browser.get('https://www.edominations.com/en/wars')
                funkcije.browser.get(f_r[1])
                sleep(5)
                python_button = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[19]/div/a[3]/img')[0]
                python_button.click()    
                print(python_button)                               
                sleep(5)
                python_button = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[19]/div/div[4]/div/ul/li[11]/a/img')[0]
                python_button.click()                                   
                sleep(5)
                for i in range(15):
                    python_button = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[19]/div/a[2]')[0]
                    python_button.click()
                    sleep(3)
                r_compl[1] = True
                ac_log('Kompletirana druga runda u ' + str(datetime.now().time().strftime('%H:%M:%S')))
            
            elif r_avail[0] == True and r_compl[0] == False and int(energija) >= 1000: # 1 runda
                funkcije.browser.get('https://www.edominations.com/en/wars')
                funkcije.browser.get(f_r[0])
                sleep(5)
                python_button = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[19]/div/a[3]/img')[0]
                python_button.click()
                sleep(5)
                python_button = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[19]/div/div[4]/div/ul/li[6]/a/img')[0]
                python_button.click()
                sleep(5)
                for i in range(10):
                    python_button = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[19]/div/a[2]')[0]
                    python_button.click()                                   
                    sleep(3)
                r_compl[0] = True
                ac_log('Kompletirana prva runda u ' + str(datetime.now().time().strftime('%H:%M:%S')))

            if r_compl[0] == True and r_compl[1] == True and r_compl[2] == True:
                ac_nagrade()
                r_compl = [False,False,False]

            vreme = random.randint(10,30)*60 + 1800
            ac_log('Cekam u ' + str(datetime.now().time().strftime('%H:%M:%S')) + ' i cekacu ' + str(vreme) + ' sekundi')
            print('Cekam u ' + str(datetime.now().time().strftime('%H:%M:%S')) + ' i cekacu ' + str(vreme) + ' sekundi')
            sleep(vreme) 

        except Exception as err:
            f = open('log.txt','a')
            f.write(str(err))
            f.close()
            pass

def ac_nagrade():
	# AC nagrade i novi
    funkcije.browser.get('https://www.edominations.com/en/index')
    ac_rec = 'armedcomb'
    mod = 3
    for i in range(3,7):
        try:
            src_attr = funkcije.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[1]/a[{}]/img'.format(i))[0].get_attribute('src')
            if ac_rec in src_attr:
                mod = i
        except:
            pass

    python_button = funkcije.browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[1]/a[{}]/img".format(mod))[0]
    python_button.click()                                      
    sleep(5)  
    python_button = funkcije.browser.find_element_by_xpath("//*[@id='eOpen1']/img")
    python_button.click()
    sleep(5)
    python_button = funkcije.browser.find_element_by_xpath("//*[@id='eOpen2']/img")
    python_button.click()
    sleep(5)
    python_button = funkcije.browser.find_element_by_xpath("//*[@id='eOpen3']/img")
    python_button.click()
    sleep(5)
    python_button = funkcije.browser.find_element_by_xpath("//*[@id='eOpen']/img")
    python_button.click()
    sleep(5)
    x = str(datetime.now().time().strftime('%H_%M'))
    funkcije.browser.save_screenshot('ac_vreme[{}].png'.format(x))
    ac_log('Pokupljene AC nagrade u ' + str(datetime.now().time().strftime('%H:%M:%S')))
    python_button = funkcije.browser.find_element_by_xpath("//*[@id='exampleModal_Events']/div/div/div/div[3]/a")
    python_button.click()
    sleep(5)
    a = funkcije.browser.switch_to.alert
    a.accept()
    

def ac_log(poruka):
    danx = str(datetime.now().strftime("%d-%m"))
    f = open('ac_log[{}].txt'.format(danx),'a')
    f.write(poruka)
    f.write('\n')
    f.close()