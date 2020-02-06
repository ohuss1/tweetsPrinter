from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

driver=webdriver.Firefox(executable_path=r'C:\Users\OComp\Desktop\geckodriver-v0.23.0-win64\geckodriver.exe'
                         )

driver.get(sys.argv[1])
numpages=0;
if len((sys.argv[2]))==2:
    if(int(sys.argv[2])>10):
        numpages=10
else:
    numpages=10
        
time.sleep(1)
body=driver.find_element_by_tag_name('body')
for i in range(numpages):
	#body.send_keys(Keys.PAGE_DOWN)
	#body.send_keys(Keys.PAGE_DOWN)
	#time.sleep(0.8)#when you move down the stuff above stays there and new
	#stuff gets loaded
	print(i)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(3)


    

tweets = driver.find_elements_by_class_name('tweet-text')
for tweet in tweets:
    print(tweet.text)
    print('\n')
    
