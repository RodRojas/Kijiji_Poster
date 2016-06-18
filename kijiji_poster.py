import ads_text

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Firefox()


def login():
    browser.get('https://www.kijiji.ca/t-login.html')
    login_element = browser.find_element_by_id('LoginEmailOrNickname')
    login_element.send_keys('your email address here')  # your email address
    password_element = browser.find_element_by_id('login-password')
    password_element.send_keys('password')   # your password
    password_element.submit()

# this example uses Toronto Ontario for location

    province_element = browser.find_element_by_link_text('Ontario (M - Z)')
    province_element.click()

    city_element = browser.find_element_by_link_text('Toronto (GTA)')
    city_element.click()

    city2_element = browser.find_element_by_link_text('City of Toronto')
    city2_element.click()

    save_location = browser.find_element_by_id('LocUpdate')
    save_location.click()
    time.sleep(1)


# this is for posting string musical instruments

def pull_up_string_form():
    post_ad = browser.find_element_by_id('PostAdLink')
    post_ad.click()

    musical_instruments = browser.find_element_by_id('CategoryId17')
    musical_instruments.click()

    string = browser.find_element_by_link_text('string')
    string.click()

# this is for posting music lessons


def pull_up_teaching_form():
    post_ad = browser.find_element_by_id('PostAdLink')
    post_ad.click()

    music_lessons = browser.find_element_by_id('CategoryId86')
    music_lessons.click()

    select_plan = browser.find_element_by_xpath(
        '//*[@id="TieredPackages"]/tbody/tr[3]/td[1]/button')
    select_plan.click()


def fill_out_string_form(instrument):
    price = browser.find_element_by_id('priceAmount')
    price.send_keys(instrument['price_amount'])

    business = browser.find_elements_by_xpath('//*[@id="forsaleby_s"]')[1]
    business.click()

    title = browser.find_element_by_id('postad-title')
    title.send_keys(instrument['ad_title'])

    descript = browser.find_element_by_id('pstad-descrptn')
    descript.send_keys(instrument['description'])

    postal = browser.find_element_by_id('PostalCode')
    postal.send_keys(instrument['postal_code'])

    video = browser.find_element_by_id('YoutubeURL')
    video.send_keys(instrument['youtube'])

    finish = browser.find_element_by_xpath(
        '//*[@id="MainForm"]/div[6]/button[1]')
    finish.click()


def fill_out_teaching_form(teacher):
    title = browser.find_element_by_id('postad-title')
    title.send_keys(teacher['ad_title'])

    descript = browser.find_element_by_id('pstad-descrptn')
    descript.send_keys(teacher['description'])

    postal = browser.find_element_by_id('pstad-map-address')
    postal.send_keys(teacher['address'])

    finish = browser.find_element_by_xpath(
        '//*[@id="MainForm"]/div[6]/button[1]')
    finish.click()

# this new tab function is not quite ready, it does pull a new tab,
# but the previous
# window does not stay put


def new_tab():
    edit = browser.find_element_by_xpath(
        '//*[@id="ManageAdWidget"]/div[2]/div/div[2]/ul/li[1]/a')
    edit.click()
    post_ad = browser.find_element_by_id('PostAdLink')
    ActionChains(browser).context_click(
        post_ad).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)


def teacher_iteration():
    for item in ads_text.teacher_list:
        pull_up_teaching_form()
        fill_out_teaching_form(item)
        new_tab()


def instrument_iteration():
    for item in ads_text.instrument_list:
        pull_up_string_form()
        fill_out_string_form(item)
        new_tab()


def repost():
    login()
    instrument_iteration()
    teacher_iteration()

repost()
