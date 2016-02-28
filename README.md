# ApplicationStatusFetcher
This script logs in to multiple Graduate University Application Portals, checks the status of the application and displays it. The script can spawn a firefox instance or run silently in the background, depending on user input.

Usage  
--------  

```bash
python GetMyStatus.py MyUnivs.config <silent>
```
Requirements    
--------
 * [Python 2.7+](https://www.python.org/downloads/)
 * [Selenium Webdriver](http://selenium-python.readthedocs.org/installation.html)
 * [PhantomJS in python](http://stackoverflow.com/questions/13287490/is-there-a-way-to-use-phantomjs-in-python) (Optional - Required only during silent run)

Input configuration   
--------
 
The input is completely controlled by the contents of the first argument passed through the script. The template for the configuration for each university is as mentioned below:  

```
-------------------------------------------------------------------
University Name: Name of the University 
-------------------------------------------------------------------
Status Check URL: 		URL of the login portal  
Username: 				Enter_Username_Here  
Password: 				Enter_Password_Here  
Username Xpath: 		Xpath for the Username field  
Password Xpath: 		Xpath for the Password field  
Submit button Xpath:	Xpath for the Login/Submit button  
Status Xpath:			Xpath for the field that displays status of application   
Intermediate click: 	Xpath for the element that needs to be clicked after login before the status check. If no such click is required set this to NA  
Additional Field: 		Xpath for the additonal element(if any) that needs to be clicked/input before login. Set this to NA if not required. 
Additional Field Value: Value that needs to be input to the Additional Field. If a click is required on Additional Field set this to _click_. If Additional Field is NA, set this to NA too. 
```
 
Multiple configurations in the above format can be present in the input config file (see MyUnivs.config). 
The configurations for the following University portals already exist in MyUnivs.config
* University of Texas Austin
* University of Caligornia, San Diego
* University of California, Irvine
* Georgia Institute of Technology
* Pennsylvania State University
* Texas A&M , CollegeStation (CSE Portal)
* University of Chicago
* North Carolina State University (Gradwatch Portal)
* University of California, Santa Barbara


