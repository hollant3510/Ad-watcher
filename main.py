import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random import randint
import numpy as np
import random



def get_random_ua():
    user_agent_list = [ 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19',
                        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19',
                        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10',
                        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4',
                        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4',
                        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2',
                        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0',
                        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0',
                        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5',
                        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10',
                        'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0',
                        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14',
                        'Mozilla/5.0 (X11; U; Windows NT 6; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.587.0 Safari/534.12',
                        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13',
                        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16',
                        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
                        'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1',
                        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
                        'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19',
                        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
                        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
                        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36]',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36']

    random.shuffle(user_agent_list)
    return user_agent_list[0]






def watch_on_engage_me(run_time):

    opts = Options()
    user_agent = "user-agent=" + 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'#get_random_ua()
    opts.add_argument(user_agent)



    #Connects to instagc

    path_to_chromedriver = 'C:/Users/tholl/PycharmProjects/adwatcher/venv/Lib/chromedriver.exe' # change path as needed
    browser = webdriver.Chrome(executable_path = path_to_chromedriver, chrome_options=opts)
    browser.delete_all_cookies()
    log_in_page = 'https://www.instagc.com/users/login'
    browser.get(log_in_page)


    #logs in on my account
    browser.find_element_by_id('username').send_keys('jdaniel')
    browser.find_element_by_id('password').send_keys('MnX36SbE')
    browser.find_element_by_xpath('//*[@id="login"]/form/section/div[3]').click()

    #goes to engage.me                                                                       need to add more info section
    browser.find_element_by_xpath('//*[@id="body"]/div/div[1]/div/ul/li[9]/a').click()
    browser.find_element_by_css_selector('#providers > div > div:nth-child(4) > a').click()


    #randomly selects smores.tv page and goes to it
    browser.switch_to_frame(browser.find_element_by_tag_name("iframe"))
    time.sleep((3))
    links = browser.find_elements_by_class_name('aw_linkcontain')
    #random.shuffle(links)
    links[0].click()
    browser.find_element_by_xpath('//*[@id="myModal"]/div/div[2]/div/div/div/div/div[2]/div[2]').click()

    while run_time > 0:

        # wait_time = (randint(1, 3))
        mult = (randint(1, 30))
        run_time = run_time - 1
        #if mult < 10:
            #browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div[4]').click()                   need to fix idk why
        #print('wait-time:', wait_time)
        time.sleep((1))

        for x in range(wait_time*mult):
            try:
                #browser.find_element_by_xpath('//*[@id="likes"]').click()
                browser.find_element_by_css_selector('#likes').click()
                #browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[1]').click()
                print('ran rand click')
            except:
                nothing = 0
                print('failed')
        temp = (randint(1, 100))
        if (wait_time == 3) and (temp == 50):
            browser.find_element_by_xpath('//*[@id="likes"]').click()


        #need to add //*[@id="share"] which is the reactions options



        #         else:
        #             browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div[4]').click()
        # try:
        #     browser.find_element_by_xpath('//*[@id="onesignal-popover-cancel-button"]').click()
        #     print('popover succeeded')
        # except:
        #     nothing = 0
        #     print('failed popover cancel')
        # try:
        #     browser.find_element_by_xpath('//*[@id="gotStatus"]').click()
        #     print('got status succeded')
        # except:
        #     nothing = 0
        #     print('failed got status')

    print('round done')
    browser.close()
    browser.quit()
    #watches while clicking captcha if pops up and randomly moving
    captcha = False
    for x in range(4000):
        if x % 10 == 0:
            captcha = True

        if captcha == False:

            time.sleep(wait_time)
            if wait_time == 1:
                browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div[2]/span[1]').click()
            else:
                browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div[4]').click()
        else:
            browser.find_element_by_xpath('//*[@id="stillWatching"]').click()

for x in range(70):
    print('round started:', x)
    time_to_run = (randint(1200, 3000))
    watch_on_engage_me(time_to_run)