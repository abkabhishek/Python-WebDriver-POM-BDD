import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from sys import stdout as console

from Services.browsers import *
import Services.common as COM





class Base:

    SearchBox = (By.NAME, "q")
    SearchButton = (By.CSS_SELECTOR, "button.search-form__button")

    def __init__(self,**kwargs):
        self.w = BROWSER(kwargs['browser'],kwargs['headless'])
        self.driver=self.w.driver
        self.baseURl=kwargs['baseURL']
        self.COM=COM

    def Teardown(self):
        try:
            self.driver.quit()
            # console.write("Driver quit")
        except:
            console.write("\n[ERROR] [Driver not found]\n")

    def do_open_page(self,URL=None):
        if URL:
            self.driver.get(URL)
        else:
            self.driver.get(self.baseURl)
        return True

    def get_page_title(self):
        return (self.driver.title)



    #################################################
    # Following are reusable methods
    #################################################



#------------- Search box and search methods -----------------

    def do_input_search_term(self,searchTerm,EnterKey=True):
        elem = COM.FindElem(self.driver,*Base.SearchBox)
        if (elem != False):
            if(EnterKey==True):
                elem.send_keys(Keys.RETURN)
            else:
                elem.clear()
                elem.send_keys(searchTerm)
            return True
        else:
            console.write("Not able to input")
            return False


    def do_perform_search(self,searchTerm):
        if self.do_input_search_term(searchTerm):
            return True
        else:
            return False

