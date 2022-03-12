from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

moodle_url = 'http://52.39.5.126/'
hmpg_title = 'Software Quality Assurance Testing'

print()
print('------------------------- Moodle App Scenario by CCTB Cohort 3 --------------------------------------')
print()
print('set up, log in admin, create user, search user, log out, log in new user, '
      'log out, log in admin, delete new user, log out, tear down')


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

def log_in_admin():
    print(f'------------------------------LOGIN FUNCTION----------------------------------------------------')
    if driver.current_url == locators.moodle_url: # check we are on the homepage
        driver.find_element(By.LINK_TEXT, 'Log in').click()
    if driver.current_url == locators.moodle_login_page_url  and driver.title == locators.moodle_login_page_title:
        print(f'{locators.app} App Login page is displayed! Continue to log in.')
        sleep(0.25)
        driver.find_element(By.ID, 'username').send_keys(username)
        sleep(0.25)
        driver.find_element(By.ID, 'password').send_keys(password)
        sleep(0.25)
        driver.find_element(By.ID,'loginbtn').click() # method 1 using ID
        # validate login successful Dashboard page is displayed
        if driver.current_url == locators.moodle_dashboard_url and driver.title == locators.moodle_dashboard_title:
            assert driver.current_url == locators.moodle_dashboard_url
            assert driver.title == locators.moodle_dashboard_title
            print(f'Login is successful. {locators.app} Dashboard is displayed - Page title: {driver.title}')
        else:
            print(f'Dashboard is not displayed. Check your code or website and try again.')

def log_out():
    print(f'------------------------------LOGOUT FUNCTION---------------------------------------------------')
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()  # // means to search everywhere in the file;
    # . search anything that has after the .
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print(f'-----Logout is done! {datetime.datetime.now()}')

      
setUp()
log_in_admin()
log_out()
