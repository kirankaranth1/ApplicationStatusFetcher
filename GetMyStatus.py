# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = webdriver.PhantomJS() # or add to your PATH
wd.set_window_size(1024, 768) # optional
#wd = WebDriver()
#wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

def get_status(univ_name,url,username_id,username,password_id,password,submitXpath,statusXpath):
    #print("Getting URL %s" %(str(url)))
    try:
        print("----------------------------------------------------------")
        print("Logging into %s portal" %(univ_name))
        wd.get(url) 
    except:
        print("Error accessing URL for %s" %(univ_name))
        return
    
    
    try:
        wd.find_element_by_xpath(username_id).click()
        wd.find_element_by_xpath(username_id).clear()
        wd.find_element_by_xpath(username_id).send_keys(username)
        wd.find_element_by_xpath(password_id).click()
        wd.find_element_by_xpath(password_id).clear()
        wd.find_element_by_xpath(password_id).send_keys(password)
        wd.find_element_by_xpath(submitXpath).click()
        status=wd.find_element_by_xpath(statusXpath).text

        print("Status of application: %s" %(str(status))) 
    except:
        print("Error fetching details from portal %s" %(univ_name))

def get_status_test(url,username_id,username,password_id,password,submitXpath,statusXpath):
    print(url,username_id,username,password_id,password,submitXpath,statusXpath)


def parse_input(filename):
    inputFile = open(filename, 'r')
    univ_count=0
    for line in inputFile:
        line=str(line).strip()
        if line.startswith("University Name:") or line.startswith("EndOfUniversityDetails"):
            #print(line)
            if(univ_count > 0 ):
                #print("Getting %s details" %(univ_name))
                get_status(univ_name,url,username_id,username,password_id,password,submitXpath,statusXpath)
            univ_count+=1
            try:
                univ_name=line.split("University Name:")[1]
            except:
                print("----------------------------------------------------------")

        
        else:
            if line.startswith("Status Check URL:"):
                url=line.split("Status Check URL:")[1].strip()
            if line.startswith("Username Xpath:"):
                username_id=line.split("Username Xpath:")[1].strip()
            if line.startswith("Username:"):
                username=line.split("Username:")[1].strip()
            if line.startswith("Password Xpath:"):
                password_id=line.split("Password Xpath:")[1].strip()
            if line.startswith("Password:"):
                password=line.split("Password:")[1].strip()
            if line.startswith("Submit button Xpath:"):
                submitXpath=line.split("Submit button Xpath:")[1].strip()
            if line.startswith("Status Xpath:"):
                statusXpath=line.split("Status Xpath:")[1].strip()


                
parse_input("UnivDetails.txt")
#get_status("https://apply.grad.ucsd.edu/login","session_email","kirankaranth1@gmail.com","session_password","Keshav1!","/html/body/div/div/main/div/div/div/form/input[3]","/html/body/div[1]/div/main/div/div/div/table/tbody/tr/td[5]")
