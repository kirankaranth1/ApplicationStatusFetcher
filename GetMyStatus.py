# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import traceback
import sys

success = True

if len(sys.argv) > 2:
    if (sys.argv[2] == "silent"):
        wd = webdriver.PhantomJS() # or add to your PATH
        wd.set_window_size(1024, 768) # optional
        wd.implicitly_wait(60)
    else:
        wd = WebDriver()
        wd.implicitly_wait(60)

else:
    wd = WebDriver()
    wd.implicitly_wait(60)


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

def get_status(univ_name,url,username_id,username,password_id,password,submitXpath,intclick,statusXpath,add,add_val):
    
    try:
        print("----------------------------------------------------------")
        print("Logging into %s portal" %(univ_name))
        wd.get(url) 
    except:
        print("Error accessing URL for %s" %(univ_name))
        return
    
    
    try:
        if add != "NA":
            time.sleep(5)
            wd.find_element_by_xpath(add).click()
            if add_val != "_click_":
                wd.find_element_by_xpath(add).clear()
                wd.find_element_by_xpath(add).send_keys(add_val)
        wd.find_element_by_xpath(username_id).click()
        wd.find_element_by_xpath(username_id).clear()
        wd.find_element_by_xpath(username_id).send_keys(username)
        wd.find_element_by_xpath(password_id).click()
        wd.find_element_by_xpath(password_id).clear()
        wd.find_element_by_xpath(password_id).send_keys(password)
        
        wd.find_element_by_xpath(submitXpath).click()
        if intclick != "NA":
            wd.find_element_by_xpath(intclick).click()
            time.sleep(10)
        status=wd.find_element_by_xpath(statusXpath).text

        print("Status of application: %s" %(str(status))) 
    except:
        print("Error fetching details from portal %s" %(univ_name))
    wd.delete_all_cookies()

def parse_input(filename):
    inputFile = open(filename, 'r')
    univ_count=0
    for line in inputFile:
        line=str(line).strip()
        if line.startswith("University Name:") or line.startswith("EndOfUniversityDetails"):
            #print(line)
            if(univ_count > 0 ):
                #print("Getting %s details" %(univ_name))
                try:
                    get_status(univ_name,url,username_id,username,password_id,password,submitXpath,intclick,statusXpath,add,add_val)
                except:
                    print("Error getting status from %s" %(univ_name))
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
            if line.startswith("Intermediate click"):
                intclick=line.split("Intermediate click:")[1].strip()    
            if line.startswith("Additional Field:"):
                add=line.split("Additional Field:")[1].strip() 
            if line.startswith("Additional Field Value:"):
                add_val=line.split("Additional Field Value:")[1].strip() 

if __name__ == "__main__":
    input_file=sys.argv[1]                
    parse_input(input_file)