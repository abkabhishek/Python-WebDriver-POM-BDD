import time
import sys
import pytest
from sys import stdout as console
sys.path.append('.')




from POM.base_pom import *
from POM.home_page_pom import *



# run by :  python -m pytest UnitTests/test__homepage.py -v
# or
# run by :  pytest -s UnitTests/test__homepage.py -v


# config = {"browser": "chrome", "baseURL": "https://www.startpage.com/"}


class Page:

    def __init__(self,url):
        config = {"browser": "chrome", "baseURL": url,"headless":False}
        Page.Base=Base(**config)
        Page.Home=Homepage(Page.Base)


@pytest.fixture(scope="module",autouse=True,params=["https://www.google.com/"])
def P(request):
    # Page.start(request.param)
    Page(request.param)

    def TearDo():
        Page.Base.Teardown()
    request.addfinalizer(TearDo)

@pytest.fixture(scope="class",autouse=True)
def tcitem(request):
    print('\nStart\n')
    def endit():
        print ("\nEnding it \n")
    request.addfinalizer(endit)
# @pytest.fixture()
# def Home():
#     return Page.Home




def test_1():
    Page.Base.do_open_page()
    time.sleep(3)
    Page.Home.perform_search("Hero")
    time.sleep(5)
    assert "Google" in Page.Base.get_page_title()