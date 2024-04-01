import re
from functools import reduce

from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


class PlaywrightHelper:
    def __init__(self, url, selector, wait_until):
        self.url = url
        self.selector = selector
        self.wait_until_selector = wait_until

    def get_pagination_no_text(self, page, browser):
        page.wait_for_selector(self.wait_until_selector)
        texts = page.query_selector_all(self.selector)
        pagination = [int(text.inner_text()) for text in texts]
        page_number = reduce(lambda a, b: a if a > b else b, pagination)

        browser.close()
        return page_number

    def get_pagination_remove_text(self, page, browser):
        page.wait_for_selector(self.wait_until_selector)
        texts = page.query_selector_all(self.selector)
        pages = [re.sub(r'[^0-9]', '', text) for text in texts]

        browser.close()
        return int(pages)

    def get_page_num_src(self, method):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            stealth_sync(page)
            # page.set_default_timeout(0)
            page.goto(self.url, timeout=60000)
            total_pages = getattr(PlaywrightHelper, method)(self, page, browser)
        return total_pages


class PlaywrightPageSourceHelper:
    def __init__(self, url, selector, wait_until):
        self.url = url
        self.selector = selector
        self.wait_until_selector = wait_until

    def get_page_source_text(self, page, browser):
        page.wait_for_selector(self.wait_until_selector)
        page.locator(f"xpath = {self.selector}")
        texts = page.query_selector_all(self.selector)

        browser.close()

        return texts

    def get_page_source(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            stealth_sync(page)
            # page.set_default_timeout(0)
            page.goto(self.url, timeout=60000)
            page.wait_for_selector(self.wait_until_selector)

            html = page.content()

            browser.close()

            return html
