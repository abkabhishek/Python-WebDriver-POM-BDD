import time
import sys
import pytest
from sys import stdout as console
sys.path.append('.')




from POM.base_pom import *
from POM.home_page_pom import *


def multiply(x,y):
    return x*y

# run by :  python -m pytest UnitTests/test__homepage.py -v
# or
# run by :  pytest -s UnitTests/test__homepage.py -v




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




def setup_module(module):
    print ("\nsetup_module      module:%s\n" % module.__name__)


def teardown_module(module):
    print ("\nteardown_module   module:%s\n" % module.__name__)

def setup_function(function):
    print ("\nsetup_function    function:%s\n" % function.__name__)

def teardown_function(function):
    print ("\nteardown_function function:%s\n" % function.__name__)

def test_numbers_3_4():
    Page.Base.do_open_page()
    time.sleep(3)
    console.write (Page.Base.get_page_title())
    print ('test_numbers_3_4  <============================ actual test code')

    assert multiply(3,4) == 12

def test_strings_a_3():
    print ('test_strings_a_3  <============================ actual test code')
    Page.Home.do_open_homepage()
    time.sleep(3)
    assert Page.Home.check_first_focus()==True

def test_strings_a_4():
    print ('test_strings_a_3  <============================ actual test code')
    Page.Home.do_open_homepage()
    time.sleep(3)
    # Page.Base.do_perform_search("Paris")
    assert Page.Base.do_perform_search("Paris")==True



class TestUM:

    def setup(self):
        print ("setup             class:TestStuff")

    def teardown(self):
        print ("teardown          class:TestStuff")

    def setup_class(cls):
        print ("\nsetup_class       class:%s\n" % cls.__name__)

    def teardown_class(cls):
        print ("\nteardown_class    class:%s\n" % cls.__name__)

    def setup_method(self, method):
        print ("\nsetup_method      method:%s\n" % method.__name__)

    def teardown_method(self, method):
        print ("\nteardown_method   method:%s\n" % method.__name__)

    def test_numbers_5_6(self):
        print ('test_numbers_5_6  <============================ actual test code')
        assert multiply(5,6) == 30

    def test_strings_b_2(self):
        print ('test_strings_b_2  <============================ actual test code')
        assert multiply('b',2) == 'bb'
