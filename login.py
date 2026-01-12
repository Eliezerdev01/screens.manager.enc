from flask import Flask
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    # Launch browser (set headless=False if you want to see it happen)
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 1. Navigate to the login page
    page.goto("https://eliezerkenya.onrender.com/login")

    # 2. Type in credentials
    # Replace 'input[name="username"]' with the actual CSS selector of the fields
    page.fill('input[name="username"]', "eliezerkenya")
    page.fill('input[name="password"]', "6789067890")

    # 3. Click Login
    page.click('button[type="submit"]')

    # 4. Wait for the dashboard to load
    page.wait_for_url("**/dashboard")
    page.goto("https://eliezerkenya.onrender.com/commands")
    # 5. Access data on the dashboard
    print("Successfully logged in!")
    dashboard_title = page.inner_text("h1")
    print(f"Dashboard Title: {dashboard_title}")

    browser.close()