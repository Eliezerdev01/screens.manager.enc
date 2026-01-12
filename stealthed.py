from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth

# Use the recommended class-based approach for 2026
with sync_playwright() as p:
    # 1. Class-based stealth ensures all contexts and pages inherit evasions
    stealth = Stealth()
    
    # 2. Launch with a realistic User-Agent (Update this to a current 2026 version)
    browser = p.chromium.launch(headless=True)
    
    # 3. Create a context with human-like viewport and locale
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    )
    
    page = context.new_page()
    
    # 4. Apply stealth to this specific page (or use stealth.use_sync(p) for global)
    stealth.apply_stealth_sync(page)
    
    new = page.goto("https://eliezerkenya.onrender.com/login", timeout=60000)
    page.fill('input[name="username"]', "eliezerkenya")
    page.fill('input[name="password"]', "6789067890")
    page.click('button[type="submit"]')
    page.wait_for_url("**/dashboard", timeout=60000)
    
    print("Successfully logged in!", "here comes the commands page")
    
    page.goto("https://eliezerkenya.onrender.com/dashboard", timeout=60000)
    
    dashboard_title = page.inner_text("html")
    print(f"Dashboard Title: {dashboard_title}")    
    with open("stealthed.html", "w", encoding="utf-8") as f:
        f.write(page.content())
        
    browser.close()
