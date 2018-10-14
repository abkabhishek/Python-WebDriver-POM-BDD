


from sys import stdout as console



import Services.common as COM





"""
> Opening Home page with URL                    >> Done

> first Focus                    >> Done
> page title                     >> Done

        > Default Category                                      $$$$$ It will through Test case by using selected category
> Selecting a Category             >>>  Partially Done
> Selected Category                >>>  Partially Done



> Input Text in Search Box
> Clear Text in the search box by using cross icon
> Slogan Text                                       >> Done

> Performing Search                                 >> Done             

> Opening Pop up
	> Add to browser
	> Set as Home


> Links Navigation
	>> Startmail
	>> Advanced
	>> Privacy policy
	>> Hamburger menu links
	>> Footer Links
	

> Opening Hamburger Menu	

"""



class Homepage:
    def __init__(self,Base):
        self.driver=Base.driver
        self.baseURL=Base.baseURl

    def do_open_homepage(self, url=None):
        if url == None:
            self.driver.get(self.baseURL)
        else:
            self.driver.get(url)

    def check_active_element(self,elem2):
        elem1 = self.driver.switch_to_active_element()
        if (elem1==elem2):
            return True
        else:
            console.write("Not able to check active Element")
            return False

    def check_first_focus(self):
        elem2 = COM.FindElem(self.driver, LOCATOR_HOMEPAGE, 'SearchBox')
        return self.check_active_element(elem2)


    def do_select_a_category(self,cat):
        """ Cat should be Web, Images or Videos """
        if cat=="Videos":
            cat="CatVideo"
        elif cat=="Images":
            cat="CatPics"
        else:                       #By Default Web category will be selected
            cat="CatWeb"

        elem=COM.FindElem(self.driver,LOCATOR_HOMEPAGE,cat)
        if elem!=False:
            elem.click()
            return True
        else:
            console.write ("Not able to select category")
            return False


    def check_selected_category(self,CatText):
        elem = COM.FindElem(self.driver, LOCATOR_HOMEPAGE, 'SelectedCat')
        if elem != False:
            # console.write(elem.text)
            if CatText==elem.text:
                return True
            else:
                return False
        else:
            print ("Not able to find selected category")
            return False

    def get_selected_category(self):
        return COM.FindElem(self.driver, LOCATOR_HOMEPAGE, "SelectedCat").text

    def get_tagline(self):
        elem=COM.FindElem(self.driver,LOCATOR_HOMEPAGE,"TagLine")
        if elem!=False:
            print (elem.text)
            return elem.text
        else:
            print ("Not able to find tagline")
            return False


    def is_correct_page(self):
        return len(COM.FindElems(self.driver, LOCATOR_HOMEPAGE,'Page_Identifier')) > 0



    def do_click_footer_link_by_namesequence(self,item):
        """

        :param link_name: It should  name of footer item, for space include item, please replace the space with underscore : About us >> About_us
        :return: true or false
        """

        itemname = 'Flink_'+str(*getattr(FOOTER_LINKS, item))
        elem = COM.FindElem(self.driver, *getattr(LOCATOR_HOMEPAGE, itemname))
        if elem:
            elem.click()
            return True
        else:
            console.write("Not able to find footer link")
            return False


    def do_click_footer_link_by_linktext(self, link_name):
        for e in COM.FindElems(self.driver, LOCATOR_HOMEPAGE, 'footer_links'):
            if link_name in e.text:
                e.click()
                return True

        return False

