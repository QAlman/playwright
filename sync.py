#to run this: python3 sync.py
from playwright.sync_api import sync_playwright

from requests import head

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://ria.ru/")
    page.screenshot(path="testresult/example.png")
    browser.close()