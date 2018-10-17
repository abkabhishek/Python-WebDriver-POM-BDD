
import traceback
import os
from sys import stdout as console
from datetime import datetime as dtm
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import logging
from behave import *
import json
from configparser import ConfigParser
import webbrowser

# from Services.file_finder import *


# Import Page modules
from POM.base_pom import *
from POM.home_page_pom import *



def propertyReader(PropFileName):
    parser = ConfigParser()
    parser.read(PropFileName)
    Env=parser.get('ENV', 'testingenv')
    headls=False
    if str(parser.get('ENV', 'headless'))=="true":
        headls=True
    config = {"browser": str(parser.get('ENV', 'browser')), "baseURL": str(parser.get(Env, 'testurl')), "headless": headls}
    return config


# # config={"browser":"chrome","baseURL":"https://quest1:quest123@crucible.startpage.com/en/","headless":False}
# config={"browser":"chrome","baseURL":"https://guestn:n!Q7c2LU@peak.startpage.com/en/","headless":False}

class COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def parse_process_save_Output(Data,OutFl):

    for i in range (len(Data)):
        if 'status' not in Data[i]:
            Data[i]['status']=''

        FFlag=False
        FStatus=""
        for j in range(len(Data[i]['elements'])):
            if 'status' not in Data[i]['elements'][j]:
                Data[i]['elements'][j]['status']=''

            SFlag=False
            SStatus=""
            for k in range(len(Data[i]['elements'][j]['steps'])):
                if 'result' not in Data[i]['elements'][j]['steps'][k]:
                    Data[i]['elements'][j]['steps'][k]['result'] = {"status": "skipped"}

                if Data[i]['elements'][j]['steps'][k]['result']['status']=="failed":
                    SFlag=True
                    SStatus="failed"
                elif SFlag==False and Data[i]['elements'][j]['steps'][k]['result']['status']=="skipped":
                    SFlag=True
                    SStatus="skipped"
            if SFlag==False:
                SStatus="passed"
            Data[i]['elements'][j]['status'] = SStatus

            if SStatus=="failed":
                FFlag=True
                FStatus="failed"
            elif FFlag==False and SStatus=="skipped":
                FFlag=True
                FStatus="skipped"

        if FFlag==False:
            FStatus="passed"
        Data[i]['status'] = FStatus

    with open(OutFl, 'w') as outfile:
        outfile.write('var RDReports=')
        # outfile.write(Data)
        json.dump(Data, outfile)




def before_scenario(context,scenario):
    # console.write('**************** Before scenario **************** \n')
    try:
        context.config.setup_logging(filename="debug.log", level=logging.DEBUG, format='%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        pconfig=propertyReader("properties.ini")
        context.Base = Base(**pconfig)
        context.Home = Homepage(context.Base)


        console.write('\n'+COLORS.HEADER+'[TEST]'+COLORS.ENDC+'\n')
    except WebDriverException as e:
        console.write(traceback.format_exc())
        console.write(COLORS.FAIL+'\n[FATAL] Driver was not initiated properly. Aborting.\n'+COLORS.ENDC)
        sys.exit(-999)

# def after_all(context):
#     console.write('**************** After all ***************** \n')
#     # context.Base.Teardown()


def after_scenario(context, scenario):
    # print("scenario status " + str(scenario.status))
    try:
        stat = str(scenario.status).split('.')[1].upper()
        if "PASSED" in stat:
            console.write('\n' + COLORS.OKGREEN + '[{0}]'.format(stat) + COLORS.ENDC + '\n')
        else:
            console.write('\n' + COLORS.FAIL + '[{0}]'.format(stat) + COLORS.ENDC + '\n')
    except:
        stat = str(scenario.status).upper()
        # stat = console.write('\n' + COLORS.FAIL + '[{0}]'.format(str(scenario.status)) + COLORS.ENDC + '\n')
        if "PASSED" in stat:
            console.write('\n' + COLORS.OKGREEN + '[{0}]'.format(stat) + COLORS.ENDC + '\n')
        else:
            console.write('\n' + COLORS.FAIL + '[{0}]'.format(stat) + COLORS.ENDC + '\n')


    if scenario.status == "failed":
        # if not os.path.exists("Output/Screenshots/Failed"):
        #     os.makedirs("Output/Screenshots/Failed")
        # os.chdir("failed_scenarios_screenshots")
        context.Base.driver.save_screenshot("./Output/Screenshots/Failed/"+scenario.name + "_failed.png")
    elif scenario.status == "passed":
        context.Base.driver.save_screenshot("./Output/Screenshots/Passed/" + scenario.name + "_passed.png")
    context.Base.Teardown()

def get_data(flname):

    with open(flname,'r',encoding='utf-8') as f:
        data = f.read()+']'
        # data = f.read()
        filename='./Output/Reports/json/report_'+str(dtm.now().day)+'_'+str(dtm.now().month)+'_'+str(dtm.now().year)+'.json'
        with open(filename,'w+') as f:
            json.dump(data, f)
        # print (data)
        rData = json.loads(data)
        # print (rData)
        return rData



def after_all(context):
    try:
        JSONReportFileName = './Output/Reports/report.json'

        rData = get_data(JSONReportFileName)

        parse_process_save_Output(rData,'./Output/Reports/report_buffer.js')
        if rData:
            file = os.path.abspath("./Output/Reports/index.html")
            url = "file:///{0}".format(file)
            console.write('\n' + COLORS.OKBLUE + '[INFO]' + COLORS.ENDC + ' Find report in {0}'.format(file) + '\n')
            # console.write("url -> {0} \n".format(url))
            webbrowser.open(url, new=1,autoraise=True)
    except Exception as err:
        print (err)



"""

##   STEP                                       #These run before and after every step.

def before_step(context, step):
    pass 

def after_step(context, step):
    pass




##   SCENARIO                                       #These run before and after each scenario is run.

def before_scenario(context, scenario):
    pass 

def after_scenario(context, scenario):
    pass



##   FEATURE                                       #These run before and after each feature file is exercised.

def before_feature(context, feature):
    pass 

def after_feature(context, feature):
    pass




##   ALL                                       #These run before and after the whole shooting match.

def before_all(context):
    pass 

def after_all(context):
    pass







#These run before and after a section tagged with the given name. They are invoked for each tag encountered in the order they’re found in the feature file. See controlling things with tags.

def before_tag(context, tag):
    pass 

def after_tag(context, tag):
    pass



"""
