from time import sleep
from selenium import webdriver


def login(username, password):
	global browser
	browser = webdriver.Chrome()
	browser.maximize_window()
	browser.get('https://www.edominations.com/en/login')
	python_button = browser.find_elements_by_xpath("//*[@id='login-box-inner']/form/div[1]/input")[0]
	python_button.send_keys(username)
	python_button = browser.find_elements_by_xpath("//*[@id='login-box-inner']/form/div[2]/input")[0]
	python_button.send_keys(password)
	sleep(60)


def daily(provera):
	## recover energy
	sleep(5)
	browser.get('https://www.edominations.com/en/index')
	python_button = browser.find_elements_by_id("energyButton")[0]
	sleep(5)
	python_button.click()
	sleep(5)

	## rad i to rad, refresh, rad
	browser.get('https://www.edominations.com/en/companies')
	python_button = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr/td[6]/form/button")[0]
	python_button.click()
	sleep(5)
	browser.get('https://www.edominations.com/en/companies')
	python_button = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr/td[6]/form/button")[0]
	python_button.click()                            
	sleep(5)
	browser.get('https://www.edominations.com/en/companies')
	python_button = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr/td[6]/form/button")[0]
	python_button.click()
	sleep(5)
	
	## rad u kompanijama
	browser.get('https://www.edominations.com/en/companies')
	python_button = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/form/div[2]/table/thead/tr/th[2]/div[1]/label/span")[0]
	python_button.click()                         
	sleep(5)
	python_button = browser.find_elements_by_id("compButton")[0]
	python_button.click()
	sleep(5)

	## ability
	browser.get('https://www.edominations.com/en/ability')
	python_button = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[1]/div/table/tbody/tr/td[6]/form/button")[0]
	python_button.click()
	sleep(5)
	
	## trening
	browser.get('https://www.edominations.com/en/training-grounds')
	python_button = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td[6]/form/button")[0]
	python_button.click()
	sleep(5)

	## ad
	browser.get('https://www.edominations.com/en/strategic-buildings')
	python_button = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[5]/form/button")[0]
	python_button.click()
	sleep(5)


	##org
	if provera == 1:
		browser.get('https://www.edominations.com/en/org/1/1158/5')
		python_button = browser.find_elements_by_id("checkeverything")[0]
		python_button.click()
		sleep(3)
		python_button = browser.find_elements_by_id("compButton")[0]
		python_button.click()
		sleep(3)
	else:
		browser.get('https://www.edominations.com/en/org/1/2531/5')
		python_button = browser.find_elements_by_id("checkeverything")[0]
		python_button.click()
		sleep(3)
		python_button = browser.find_elements_by_id("compButton")[0]
		python_button.click()
		sleep(3)

	## recover energy
	sleep(5)
	browser.get('https://www.edominations.com/en/index')
	python_button = browser.find_elements_by_id("energyButton")[0]
	sleep(5)
	python_button.click()
	sleep(5)

