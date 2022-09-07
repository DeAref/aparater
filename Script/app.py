import time
import random
import requests
import io
from selenium import webdriver
send='https://api.telegram.org/bot1429170251:AAHZ-daLFm7-KwPiyNAu_G7UzoKxIyss74M/sendMessage?chat_id=-552265330&text='
#requests.get(send+'bot start')
#os.system("curl  "+send)
#frist url and start drivers
url = "C:\chromedriver.exe"
driver = webdriver.Chrome(url)
driver2 = webdriver.Chrome(url)
searchpage_url = "https://www.aparat.com/search/AppDUNY"
driver.get(searchpage_url)
print('driver url is '+ searchpage_url)
#requests.get(send+'driver url is '+ searchpage_url)
loginPage_url = "https://www.aparat.com/login"
driver2.get(loginPage_url)
print('driver url is https://www.aparat.com/login')
#requests.get(send+'driver url is https://www.aparat.com/login')
print('login process is start')
#requests.get(send+'login process is start')
#-----login
time.sleep(3)
username = "appduny"
password = "AppDuny1234"
field = driver2.find_element_by_id('username')
field.send_keys(username)
print('user name insert')
#requests.get(send+'user name insert')
driver2.find_element_by_xpath('//*[@id="main-container"]/section/div/div[2]/form/button').click()
time.sleep(2)
driver2.find_element_by_id('password').send_keys(password)
print('password insert')
#requests.get(send+'password insert')
driver2.find_element_by_xpath('//*[@id="main-container"]/section/div/div[1]/form/button').click()
print('login process is Complet')
#requests.get(send+'login process is Complet')

#scrape and follow and like
print("start to scarp and join")
#requests.get(send+"start to scarp and join")
driver.execute_script("window.scrollTo(10, 11000)")
#Link pack
#link_list=['https://www.aparat.com/search/فان','https://www.aparat.com/search/%D8%AF%D9%86%D8%A8%D8%A7%D9%84_%D8%AF%D9%86%D8%A8%D8%A7%D9%84','https://www.aparat.com/search/%D8%AF%D9%86%D8%A8%D8%A7%D9%84_%DA%A9%D9%86%DB%8C%D8%AF','https://www.aparat.com/search/%D8%A8%D8%A7%D8%B2%DB%8C_%D8%AC%D8%AF%DB%8C%D8%AF','https://www.aparat.com/search/فیلم','https://www.aparat.com/search/music','https://www.aparat.com/search/%D8%A2%D8%B4%D9%BE%D8%B2%DB%8C','https://www.aparat.com/search/hack','https://www.aparat.com/search/gameplay','https://www.aparat.com/search/%D8%A2%D8%B2%D9%85%D8%A7%DB%8C%D8%B4','https://www.aparat.com/search/%DA%AF%DB%8C%D9%85_%D9%BE%D9%84%DB%8C','https://www.aparat.com/search/%D8%AA%D8%B1%D9%81%D9%86%D8%AF','https://www.aparat.com/search/pubg','https://www.aparat.com/search/callofduty','https://www.aparat.com/search/%D8%AC%DB%8C_%D8%AA%DB%8C_%D8%A7%DB%8C','https://www.aparat.com/search/gtaV','https://www.aparat.com/search/%DA%86%DB%8C%D8%AA','https://www.aparat.com/search/cheat']
game_name= open('C:\gamelist.txt','r',encoding = "utf8")
link_list = game_name.readlines()
for link in link_list:
    driver.get('https://www.aparat.com/search/'+link)
    driver.execute_script("window.scrollTo(10, 1000)")
    driver.execute_script("window.scrollTo(10, 1000)")
    driver.execute_script("window.scrollTo(10, 1000)")
    driver.execute_script("window.scrollTo(10, 1000)")
    driver.execute_script("window.scrollTo(10, 1000)")
    driver.execute_script("window.scrollTo(10, 1000)")
    #requests.get(send+"Scroll sexy and big 02000px")
    for x in range(21):
        #scroll
        driver.execute_script("window.scrollTo(10, "+str(x)+"000)")
        print('scroll Down 1000px')
        #requests.get(send+'scroll Down 2000px')
        #----------
        content = driver.find_elements_by_class_name('title')[x].get_attribute('href')
        driver2.get(content)
        print('Driver2 go to video page')
        #requests.get(send+'Driver2 go to video page')
        followbtn_text = driver2.find_element_by_xpath("/html/body/main/div[1]/div/div/div/div/section[2]/div/div[2]/div[2]/button").get_attribute('data-status')
        print('Follow btn text is:'+followbtn_text)
        #requests.get(send+'Follow btn text is:'+followbtn_text)
        like = driver2.find_element_by_id('likeVideoButton')
        like.click()
        print('like ...')
        #requests.get(send+'like ...')
        if followbtn_text == 'unfollow':
            user_links = driver2.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[1]/div/a').get_attribute('href')
            print('start open file')

            #save id link if users
            f = open('C:\idlink.txt', 'a')
            print('apeand file')
            f.writelines('\n'+user_links)
            print('close file')
            f.close()
            follow = driver2.find_element_by_xpath("/html/body/main/div[1]/div/div/div/div/section[2]/div/div[2]/div[2]/button")
            follow.click()
            print('Bot Follow: '+user_links)
            #requests.get(send+'Bot Follow: '+user_links)
        #requests.get(send+'repeat again')
    driver.delete_all_cookies()
    driver2.delete_all_cookies()
    driver2.get(loginPage_url)
    #login Agian
    time.sleep(3)
    username = "appduny"
    password = "AppDuny1234"
    field = driver2.find_element_by_id('username')
    field.send_keys(username)
    print('user name insert')
    #requests.get(send+'user name insert')
    driver2.find_element_by_xpath('//*[@id="main-container"]/section/div/div[2]/form/button').click()
    time.sleep(2)
    driver2.find_element_by_id('password').send_keys(password)
    print('password insert')
    #requests.get(send+'password insert')
    driver2.find_element_by_xpath('//*[@id="main-container"]/section/div/div[1]/form/button').click()
    print('login process is Complet')
    #requests.get(send+'login process is Complet')



print('scarp complte')
#requests.get(send+'scarp complte')
#driver.switch_to_window(window_before)
#window_before = driver.window_handles[0]
#window_after = driver.window_handles[1]


