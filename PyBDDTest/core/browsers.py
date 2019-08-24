import time
import os


from selenium import webdriver
from sys import stdout as console

from selenium.webdriver.firefox.options import Options as FirefoxOptions

class BROWSER:
	driver=None

	def __init__(self,browser='chrome',headless=None,executablepath='./Resoureces/drivers/chromedriver.exe'):
		if 'win' in os.name:			# windows users

			if browser=='firefox':
				options = FirefoxOptions()
				options.add_argument("--start-maximized")
				if headless:
					options.add_argument('--headless')
				driver = webdriver.Firefox(
										firefox_options=options,
										executable_path= './Resoureces/drivers/geckodriver.exe'
										)
				driver.implicitly_wait(2)
				BROWSER.driver=driver

			elif (browser=='chrome'):
				console.write('==============INIT=================')
				options = webdriver.ChromeOptions()
				if headless:
					options.add_argument('--headless')
				options.add_argument("--start-maximized")
				driver=webdriver.Chrome(
										executable_path=executablepath,
										chrome_options=options
										)
				driver.implicitly_wait(2)
				BROWSER.driver=driver

			elif browser == 'opera':
				pass

			elif browser == 'ie':
				pass

		else:						# linux, mac users
			if browser=='firefox':
				options = FirefoxOptions()
				options.add_argument("--start-maximized")
				if headless:
					options.add_argument('--headless')
				driver = webdriver.Firefox(options=options)
				driver.implicitly_wait(2)
				BROWSER.driver=driver

			elif (browser=='chrome'):
				options = webdriver.ChromeOptions()
				if headless:
					options.add_argument('--headless')
				options.add_argument("--start-maximized")
				driver=webdriver.Chrome(options=options)
				driver.implicitly_wait(2)
				BROWSER.driver=driver

			elif browser == 'safari':
				driver=webdriver.Safari()
				driver.implicitly_wait(2)
				BROWSER.driver = driver




if __name__ == "__main__":
	WD=BROWSER(executablepath='../Resoureces/drivers/chromedriver.exe')
	WD.driver.get("https://www.google.com/")
	time.sleep(3)
	WD.driver.quit()
