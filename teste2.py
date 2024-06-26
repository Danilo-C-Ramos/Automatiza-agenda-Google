from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.firefox.launch()
page = browser.new_page()
page.goto("https://playwright.dev/")
page.screenshot(path="example.png")
browser.close()

playwright.stop()