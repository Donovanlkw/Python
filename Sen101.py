# https://www.selenium.dev/documentation/webdriver/drivers/options/
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

    

# service = webdriver.ChromeService(port=1234)    
service = webdriver.ChromeService()

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.binary_location = chrome_bin


# driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(service=service; options=options)
    driver.get("https://www.example.com")



    fruits = driver.find_element(By.ID, "fruits")
    fruit = fruits.find_element(By.CLASS_NAME,"tomatoes")
    fruit = driver.find_element(By.CSS_SELECTOR,"#fruits .tomatoes")
    plants = driver.find_elements(By.TAG_NAME, "li")
    elements = driver.find_elements(By.TAG_NAME, 'div')
  


    # Get all the elements available with tag name 'p'

for e in elements:
    print(e.text)
    





'''
#https://www.python.org/downloads/windows/

#C:\Users\D\AppData\Local\Programs\Python\Python312>
  
pip install selenium

python.exe -m pip --version
python -m pip install -U selenium





#https://sites.google.com/chromium.org/driver/downloads\
Path = "C:\Program Files (x86)\chromedriver\chromedriver.exe"

import selenium
selenium.__version__
from selenium import webdriver
#Path = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
#driver =  webdriver.Chrome


################################
import selenium
from selenium import webdriver

#PATH= "C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver1 = webdriver.Chrome()
driver1.get("http://www.yahoo.com.hk")


service = Service()
options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service = service, options = options)
driver = webdriver.Chrome()
driver.get("http://www.google.com.hk")
print(driver.title)











Selenium-IDE 
Record:
Playback:
Browser Check: 
Check Elements: 
Spotting Errors: 
Exporting Tests: 

Selenium RC (Remote control)
Improved API:
Better Performance:
Support for Modern Web Technologies:


Selenium Web Driver
Direct Communication with Browsers: 
Support for Parallel Execution:
Rich Set of APIs:

Selenium GRID
'''










    
    https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/scripting-monitors/introduction-scripted-browser-monitors/

Visit a URL 

await $webDriver.get("https://mywebsite.com");
await $webDriver.get("https://my-website.com");
await $webDriver.findElement($selenium.By.linkText("Configuration Panel"));

$webDriver.get("https://my-website.com").then(function(){
    return $webDriver.findElement($selenium.By.linkText("Configuration Panel"));
});

await $webDriver.findElement($selenium.By.id("edit-submit"));
await $webDriver.findElement($selenium.By.linkText("Configuration Panel"));
await $webDriver.findElement($selenium.By.partialLinkText("Configuration Pa"));
await $webDriver.findElement($selenium.By.name("search-query-field"));
await $webDriver.findElement($selenium.By.xpath("//input[@placeholder = 'search-query-field']"));


Interactive with elements.
await $webDriver.findElement($selenium.By.linkText("Configuration Panel")).click();
await $webDriver.findElement($selenium.By.className("config-panel-02")).click();


await $webDriver.findElement($selenium.By.name("search-query-field")).sendKeys("EXAMPLE USER NAME");
await $webDriver.findElement($selenium.By.id("search-q-box")).sendKeys("EXAMPLE USER NAME");


await $webDriver.findElement($selenium.By.name("search-query-field")).clear();
await $webDriver.findElement($selenium.By.id("search-q-box")).clear();



//Declare the variable `WEBSITE_URL`
var assert = require('assert'),
  WEBSITE_URL = 'https://my-website.com/';

await $webDriver.get(WEBSITE_URL);
//Log our success to the console
console.log('Success for', WEBSITE_URL);



page_source = driver.page_source
 
# Print the page source
print(page_source)
 
fileToWrite = open("page_source.html", "w")
fileToWrite.write(page_source)
fileToWrite.close()
 
# Close the browser window
driver.quit()



  
