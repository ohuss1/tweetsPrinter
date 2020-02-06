from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import bs4
import string
driver=webdriver.Firefox(executable_path=r'C:\Users\OComp\Desktop\geckodriver-v0.23.0-win64\geckodriver.exe'
                         )#replace the path with your gecko exe path
#please read the readme to run this file

driver.get(sys.argv[1])
time.sleep(1)
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
#Soup=bs4.BeautifulSoup(tweets)
file=open("Tweetss.txt","wb+")
for tweet in tweets:
    #print(tweet.text)
    #print(('\n').encode())
    x=tweet.text
   
    x=x.encode('ascii',errors='ignore')
    file.write(x)#to create a text file with tweets
    file.write(('\n').encode())
    file.write(('\n').encode())
file.write(('end of scanned tweets').encode())
print('end')
file.close()
