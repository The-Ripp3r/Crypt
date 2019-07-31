#author:Jack-the-Ripper
#Contributors: Nick Walsh (IS&T MIT) aka MVP

from selenium import webdriver #originally a js library that makes browser functionality programmable
import time #time module to offset download dialogs and redirects
import os #directory rework

#targeted urls
web_urls=['https://fadata.mit.edu']

#retrieve profile to open specfic FF session
prof=webdriver.firefox.firefox_profile.FirefoxProfile(profile_directory='/home/jack/.mozilla/firefox/r25zdhu5.jack-test2') #sample profile directory; found at about:profiles in FF

#setup webdriver and request url
browser = webdriver.Firefox(firefox_profile=prof)
browser.get(web_urls[0])

#find html elements for user/pass and submit to get redirected to duo
#given above profile, duo is bypassed by cookies and the target is acquired
user_name = browser.find_element_by_name('j_username')#this is a unique html elements for my target webpage
user_name.send_keys("sample_username")
password = browser.find_element_by_name('j_password') #this is a unique html elements for my target webpage
password.send_keys("sample_password")
submit = browser.find_element_by_name('Submit')
time.sleep(0.5)
submit.click()

#cycles through rest of targets after initial authentication into MIT servers
#all targets are assumed to be under a single authority; in this case MIT
for i in range(1, len(web_urls)):
    time.sleep(3)
    browser.get(web_urls[i])

#once all targets are opened several download dialogs would have been completed

download_folder_dir='C://Users/user/Targets//' #sample current location
dropbox_folder_dir='C://Users/user/Dropbox//' #sample destination

#creates a list of names for all downloads
#***make sure to have knwon file extensions ON and have a dedicated folder for these targets
Targets=os.listdir('C://Users/mitadm/Targets') 

#move items into Dropbox
for i in Targets:
    os.rename(download_folder_dir + i, dropbox_folder_dir + i)