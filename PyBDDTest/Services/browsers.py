from selenium import webdriver
import os
import sys
from sys import stdout as console
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
sys.path.append('.')

class BROWSER:
	driver=None
	def __init__(self,browser='chrome',headless=None,executablepath='./driver/win/chrome/chromedriver.exe'):
		if 'win' in os.name:			# windows users

			if browser=='firefox':
				options = FirefoxOptions()
				options.add_argument("--start-maximized")
				if headless:
					options.add_argument('--headless')
				driver = webdriver.Firefox(
										firefox_options=options,
										executable_path= './driver/win/firefox/geckodriver.exe'
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
				driver = webdriver.Firefox(firefox_options=options)
				driver.implicitly_wait(2)
				BROWSER.driver=driver

			elif (browser=='chrome'):
				options = webdriver.ChromeOptions()
				if headless:
					options.add_argument('--headless')
				options.add_argument("--start-maximized")
				driver=webdriver.Chrome(chrome_options=options)
				driver.implicitly_wait(2)
				BROWSER.driver=driver

			elif browser == 'safari':
				driver=webdriver.Safari()
				driver.implicitly_wait(2)
				BROWSER.driver = driver




if __name__ == "__main__":
	WD=BROWSER(executablepath='../driver/win/chrome/chromedriver.exe')
	WD.driver.get("https://quest1:quest123@crucible.startpage.com/")
	elems=WD.driver.find_elements_by_css_selector('.search-form input[type="hidden"][name="language"]')
	console.write(elems[0].get_attribute("value"))

	# WD.driver.find_element_by_css_selector("nav>ul>li:nth-child(2)").click()
	WD.driver.find_element_by_css_selector("#query").send_keys("Water")
	WD.driver.find_element_by_css_selector("button.search-form__button").click()
	time.sleep(2)
	console.write(WD.driver.title)
	elemss=WD.driver.find_elements_by_css_selector('.search-form input[type="hidden"][name="lui"]')
	print (elemss)
	# console.write(elemss[0].get_attribute("value"))

	# elems=WD.driver.find_elements_by_css_selector("li.image-result")
	# console.write(elems[1].get_attribute("data-image-result-is-active"))
	# elems[1].click()
	# elem2=WD.driver.find_element_by_css_selector("li:nth-child(2)>div>div>.search-item__title")
	# console.write(str(elem2.is_displayed()))
	# console.write(str(elem2.is_enabled()))
	# console.write(str(elem2.is_selected()))
	# print (elem2.text)
	# elem=WD.driver.find_elements_by_css_selector("li:nth-child(2).image-result")
	# elem.click()
	# elem2=WD.driver.find_element_by_css_selector("li:nth-child(2)>div>div>.search-item__title")
	# console.write(str(elem2.is_displayed()))
	# console.write(str(elem2.is_enabled()))
	# console.write(str(elem2.is_selected()))
	# print (elem2.text)

	WD.driver.quit()
