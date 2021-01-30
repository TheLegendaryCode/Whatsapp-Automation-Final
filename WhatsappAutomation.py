from selenium import webdriver
import schedule
import time
print("My program can send a message through whatsapp at a fixed time to a person. Like if you want you can send a birthday wish at exactly 12:00 when you might be sleeping and you dont have to wake up and do it manually or if you have to send a good morning message every day the program can do it for you.")


to=input("Enter the person to send the message to: ")
message=input("Enter the message to be sent: ")
time=input("Enter the time for the message to be sent (Please enter in 24 hr format and in this format= xx:xx) :")

def send():
    browser=webdriver.Chrome()
    browser.get('http://web.whatsapp.com')#opens the link
    input("Press enter after scanning qr code")  # this has no importance this is to only continue after scanning qr code.
    user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(to))  #performs like a cntrl+f in inspect for the xpath given
    user.click() #clicks the title when it finds it
    whatsappBox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') #finds the box where the message is typed in whatsapp
    whatsappBox.send_keys(message) #types the message
    messageBox=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')#finds send button
    messageBox.click()
    print("Message sent")

schedule.every().day.at(time).do(send)

while True:
    schedule.run_pending()
   

