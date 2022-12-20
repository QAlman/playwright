#to run this, just: pytest -> https://playwright.dev/python/docs/test-runners
#pytest --headed
#pytest --browser chromium --browser webkit
#pytest --base-url https://www.saucedemo.com/ --browser chromium --headed
#Run tests with slow mo with the --slowmo argument.: --slowmo 1000 


#Configure Mypy typings for auto-completion
from playwright.sync_api import Page
import pytest
import asyncio
from playwright.async_api import async_playwright


#--Skip test by browser
@pytest.mark.skip_browser("firefox")
#--Run on a specific browser
@pytest.mark.only_browser("chromium")
def test_example_1(page: Page):
    page.goto("https://ria.ru/")
    # print(await page.title())
    # await browser.close()
    assert page.inner_text('title') == 'РИА Новости - события в Москве, России и мире сегодня: темы дня, фото, видео, инфографика, радио'


#--Skip test by browser
@pytest.mark.skip_browser("firefox")
#--Run on a specific browser
@pytest.mark.only_browser("chromium")
def test_example_2(page: Page):
    page.goto("https://ria.ru/")
    print(page.title())
    # await browser.close()
    #assert page.inner_text('title') == 'Swag Labs'




# #--Skip test by browser
# @pytest.mark.skip_browser("firefox")
# #--Run on a specific browser
# @pytest.mark.only_browser("chromium")
# async def test_example_2():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto("https://ria.ru/20221219/dollar-1839619131.html")
#         print(await page.title())
#         await browser.close()









    