#!/usr/bin/env python3

import datetime
from datetime import datetime as dt
from datetime import date
import pyautogui
import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

today_date = date.today()
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
day_of_week_coord = [(151, 499), (413, 499), (692, 499), (950, 499), (1228, 499), (1494, 499), (1773, 499)]
dow = dt.today().weekday()
d2 = today_date.strftime("%B %d, %Y")
print(datetime.datetime.now())
print(f'Today\'s Date: {d2}')
today_coords = day_of_week_coord[dow]

print(f'Today\'s Coords: {today_coords}')


def after_info():
    pyautogui.alert(text=f'Have a Nice Day, Mr. Cesta. \n{today_date.strftime("%B %d, %Y")} \n(this alert will auto '
                         f'close...)',
                    title='Billy Price\'s EO Program',
                    timeout=5000)
    driver.quit()
    return exit()


def login1(emp_number='034756', emp_password='Peteyc44!', emp_security_answer='None'):
    schedule.cancel_job(clk)
    driver.get(
        'https://vress.wynnresorts.com/ess/Default.aspx?#/roster')
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//*[@id='okta-signin-username']").send_keys(emp_number, Keys.TAB)
    driver.find_element(By.XPATH, "//*[@id='okta-signin-password']").send_keys(emp_password, Keys.ENTER)
    driver.implicitly_wait(8)
    try:
        if driver.find_element(By.NAME, 'answer'):
            driver.find_element(By.NAME, "answer").send_keys(emp_security_answer, Keys.ENTER)
            driver.implicitly_wait(5)
    except:
        print("Security Backup Password Not Required...")
        click()
    pyautogui.sleep(10)
    click()

def click():
    clk.scheduler.cancel_job(click_awake)
    x = 0
    a = today_coords[0]
    b = today_coords[1]
    while x <= 10:
        pyautogui.click(a, b)
        pyautogui.click(1362, 554)  # EO LIST
        pyautogui.click(1070, 705)  # EO LIST SUBMIT
        pyautogui.click(1170, 705)  # 1st close
        pyautogui.click(1427, 727)  # 2nd close
        x += 1
    # driver.quit()
    after_info()
    return exit()


def click_awake():
    pyautogui.alert(text='Stayin\' Fresh...', timeout=2000)

    pyautogui.moveTo(100, 200)


hours = str('10')
mins = str('14')  # for the login and start click
seconds_login = str('00')  # Login on the minute before avail time launches the WIRE
clk_hrs = str('10')
clk_mins = str('14')  # for the login and start click
seconds_click = str('58')  # start clicking 3 seconds before avail time

schedule.every().day.at(f"{hours}:{mins}:{seconds_login}").do(login1)
schedule.every().day.at(f"{clk_hrs}:{clk_mins}:{seconds_click}").do(click)

time_str = dt.now().strftime(":%S")
print(time_str)
clk = schedule.every().minute.at(time_str).do(click_awake)

while True:
    schedule.run_pending()

