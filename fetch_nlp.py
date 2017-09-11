import sys
import os
import time
import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def fetch(url_matkul):
    chrome_options = Options()
    if(len(sys.argv) > 1):
        chrome_options.add_argument("--headless")
    chrome_options.binary_location = '/usr/bin/google-chrome'

    driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
    driver.get(url_matkul)
    driver.delete_all_cookies()

    driver.add_cookie({'name': 'JSESSIONID', 'value': settings.JSESSIONID, 'domain': 'akademik.itb.ac.id'})
    driver.add_cookie({'name': 'PHPSESSID', 'value': settings.PHPSESSID, 'domain': 'akademik.itb.ac.id'})
    driver.add_cookie({'name': '_auth', 'value': settings._auth, 'domain': 'akademik.itb.ac.id'})
    driver.add_cookie({'name': 'bahasa', 'value': settings.bahasa, 'domain': 'akademik.itb.ac.id'})
    driver.add_cookie({'name': 'uitb', 'value': settings.uitb, 'domain': 'akademik.itb.ac.id'})

    driver.get(url_matkul)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight/4)" )

    # <button type="submit" id="form_save" name="form[save]" class="btn btn-sm btn-primary btn btn-primary">Kirim</button>

    # Tinggal ganti ini
    kirim_button = driver.find_element_by_id("form_save")
    if kirim_button.is_displayed():
        kirim_button.click()

    # magnifying_glass = driver.find_element_by_id("js-open-icon")
    # if magnifying_glass.is_displayed():
    #   magnifying_glass.click()
    # else:
    #   menu_button = driver.find_element_by_css_selector("a.")
    #   menu_button.click()
    #
    # search_field = driver.find_element_by_id("site-search")
    # search_field.clear()
    # search_field.send_keys("Olabode")
    # search_field.send_keys(Keys.RETURN)

    driver.close()

if __name__ == '__main__':
    while(true):
        fetch(settings.url_nlp)
