from selenium import webdriver
import os
import emoji
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code')
os.system('TASKKILL /F /IM cmd.exe')

while True:
    inp=input('I for image/T for text?: ')
    
    name = input('Enter the name of user or group : ')
    try:
        user = driver.find_element_by_xpath('//span[contains(text() , "{}")]'.format(name.title()))
        print(user)
    except:
        print('retry')
    user.click()
    
    if inp.lower()=='t':
        msg = input('Enter your message : ')
        msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
        
    elif inp.lower()=='i':
        attach_box=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div')
        attach_box.click()
        image_box=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input')
        try:
            filepath=input('filepath: ')
            image_box.send_keys(filepath)
        except e:
            print(e)
        msg = input('Enter your message : ')
        sleep(5)
        msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')
        msg_box.send_keys(msg)
        send=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
        send.click()
