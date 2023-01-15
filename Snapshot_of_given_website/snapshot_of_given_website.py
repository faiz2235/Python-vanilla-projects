# -*- config: utf-8 -*-
"""
    - The version of 'chrome driver' need to match the version of your google
    chrome.
    - 'XX.X.XXXX.XX.X' is chrome driver version.
    *How to find your google chrome version*
    1. Click on the Menu icon in the upper right corner of the screen.
    2. Click on Help, and then About Google Chrome.
    3. Your Chrome browser version number can be found here.
    ## Execute
    `python snapshot_of_given_website.py <url>`
    Snapshot is in current directory after this script runs.
"""

import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


script_name = sys.argv[0]


options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

try:
    url = sys.argv[1]
    driver.get(url)
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    driver.save_screenshot('screenshot.png')
    driver.quit()
    print('Done!')
except IndexError:
    print(f'Usage: {script_name} URL')
