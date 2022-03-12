from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

moodle_url = 'http://52.39.5.126/'
hmpg_title = 'Software Quality Assurance Testing'

print()
print('------------------------- Moodle App Scenario by CCTB Cohort 3 --------------------------------------')
print()
print('set up, log in admin, create user, search user, log out, log in new user,
      log out, log in admin, delete new user, log out, tear down')


def setUp():
    print()
    print(f'--------------------------------------- SET UP FUNCTION --------------------------------------------')
    print()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(moodle_url)
    if driver.current_url == moodle_url and driver.title == hmpg_title:
        print(f'Moodle app launched successfully.')
        print(f'homepage url:{driver.current_url}, title: {driver.title}')
        sleep(0.25)
    else:
        print(f'Moodle did not launch. Check your code or app.')
        print(f'current url: {driver.current_url}, page title: {driver.title}')


setUp()
