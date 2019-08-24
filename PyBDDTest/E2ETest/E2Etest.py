import time
import sys
sys.path.append(".")

from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from core.browsers import *


# options = Options()
# options.add_argument("--start-maximized")

# Create a new instance of the Firefox driver
# driver = webdriver.Chrome(chrome_options=options)

# driver = webdriver.Firefox()
# driver.set_window_size(1440, 900)
# driver.maximize_window()
# time.sleep(3)

WD = BROWSER(browser="firefox")

# go to the google home page
WD.driver.get("http://www.google.com")


# the page is ajaxy so the title is originally this:
print (WD.driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = WD.driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(WD.driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print (WD.driver.title)

finally:
    WD.driver.quit()