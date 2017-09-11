try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import sys
import os
import time
import schedule
import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def fetch():
    try:
        chrome_options = Options()
        if(len(sys.argv) > 1):
            chrome_options.add_argument("--headless")
        chrome_options.binary_location = '/usr/bin/google-chrome'

        driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
        driver.get(settings.url_nlp)
        driver.delete_all_cookies()

        # driver.add_cookie({'name': 'JSESSIONID', 'value': settings.JSESSIONID, 'domain': 'akademik.itb.ac.id'})
        driver.add_cookie({'name': 'PHPSESSID', 'value': settings.PHPSESSID, 'domain': 'akademik.itb.ac.id'})
        driver.add_cookie({'name': '_auth', 'value': settings._auth, 'domain': 'akademik.itb.ac.id'})
        # driver.add_cookie({'name': 'bahasa', 'value': settings.bahasa, 'domain': 'akademik.itb.ac.id'})
        driver.add_cookie({'name': 'uitb', 'value': settings.uitb, 'domain': 'akademik.itb.ac.id'})

        driver.get(settings.url_nlp)
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight/4)" )

        # <button type="submit" id="form_save" name="form[save]" class="btn btn-sm btn-primary btn btn-primary">Kirim</button>

        # Tinggal ganti ini
        kirim_button = driver.find_element_by_id(settings.buttonid_nlp)
        if kirim_button.is_displayed():
            kirim_button.click()

        # driver.close()
        html = driver.page_source
        parsed_html = BeautifulSoup(html, 'lxml')
        # print(parsed_html)
        print (parsed_html.body.find('span', attrs={'data-notify':'message'}).text)

        driver.quit()
        print("Job done")
    except Exception:
        if("null" in str(driver)):
            print("Job not done")
        else:
            # driver.close()
            driver.quit()
            print("Job not done")

if __name__ == '__main__':
    while(True):
        fetch()
        if(len(sys.argv) > 2):
            time.sleep(int(sys.argv[2]))

    # schedule.every(0.1).minutes.do(fetch)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
