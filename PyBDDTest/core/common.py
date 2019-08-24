
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import stdout as console



def FindElem(driver,Locator,Element,Number=None):

    try:
        if Number==None:
            elem=driver.find_element(Locator, Element)
        else:
            item1,item2=getattr(Locator, Element)
            item2=item2.format(Number)
            console.write(item1)
            console.write(item2)
            elem = driver.find_element(item1,item2)
        return elem
    except NoSuchElementException:
        console.write("Element not found")
        return False


def FindElems(driver,Locator,Element):
    try:
        elems=driver.find_elements(*getattr(Locator, Element))
    except NoSuchElementException:
        console.write("Element not found")
        return False
    else:
        return elems


def get_result_interface_language(lang):
    return {
        "en": "english",
        "gb": "english_uk",
        "de": "deutsch",
        "da": "dansk",
        "es": "espanol",
        "fi": "suomi",
        "fr": "francais",
        "it": "italiano",
        "nl": "nederlands",
        "pl": "polski",
        "pt": "portugues",
        "sv": "svenska",
        "no": "norsk"
        }.get(lang,False)








def do_wait_for_visibility(driver,element = False,by = False,time_out = 5,interval = 100):
    wait = WebDriverWait(driver, time_out)

    if (element):
        return wait.until(EC.visibility_of_element_located(element))

    else:
        return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,by)))




def check_text_in_page_headers(driver,texts):
    elems = driver.find_elements_by_css_selector('h1')
    # console.write(str(elems))
    if len(elems)>0:
        for i in range(len(elems)):
            # console.write(str(elems[i].text))
            # console.write(texts)
            if texts == elems[i].text:
                return True
    else:
        console.write("No Element found")
        return False


def is_link_visible(driver,link_text):
    try:
        return driver.find_element_by_link_text(link_text).is_displayed()
    except:
        return False

def do_click_on_link(driver,link_text):
    try:
        driver.find_element_by_link_text(link_text).click()
        return True
    except:
        return False

def get_link_count(driver,link_text):
    """Use link_text and then length of list to get count"""
    elems = driver.find_elements_by_link_text(link_text)

    return len(elems)