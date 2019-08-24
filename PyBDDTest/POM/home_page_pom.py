


from sys import stdout as console


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import core.common as COM
from core.com import *






class Homepage:


    # __________________________________________________________________________
    ############  >>>>>>>>>>        ELEMENTS       <<<<<<<<<<<<< ###############
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # SearchBox = Com2.Element((By.NAME, "q"))

    # Page_Identifier = (By.ID, "hplogo")

    ############  >>>>>>>>>>    --- X --- X ----   <<<<<<<<<<<<< ###############
    # --------------------------------------------------------------------------




    #~~~~~~~~~~~~~~~~~~~~~~        Constructor       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self,Base):
        self.driver=Base.driver
        self.baseURL=Base.baseURl
        CM = COM2(self.driver)

        self.SearchBox = CM.Element((By.NAME, "q"))

        self.Page_Identifier = (By.ID, "hplogo")



    # __________________________________________________________________________
    ############  >>>>>>>>>>        Methods       <<<<<<<<<<<<< ###############
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



    # ~~~~~~~~~~~~~~        Basic Home page methods       ~~~~~~~~~~~~~~~~~~~~~~~~~

    def is_correct_page(self):
        return len(COM.FindElems(self.driver, *Homepage.Page_Identifier)) > 0



    def do_open_homepage(self, url=None):
        if url == None:
            self.driver.get(self.baseURL)
        else:
            self.driver.get(url)

    def check_active_element(self,elem2):
        elem1 = self.driver.switch_to.active_element
        if (elem1==elem2):
            return True
        else:
            console.write("Not able to check active Element")
            return False

    def check_first_focus(self):
        elem2 = COM.FindElem(self.driver, *Homepage.SearchBox)
        return self.check_active_element(elem2)

    def perform_search(self,search_term):
        self.SearchBox(True)[0].send_keys(search_term)







