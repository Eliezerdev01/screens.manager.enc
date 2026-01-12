import requests

# Use a session object to keep cookies alive
session = requests.Session()

login_url = "https://eliezerkenya.onrender.com"
dashboard_url = "https://eliezerkenya.onrender.com/dashboard"

payload = {
    "username": "eliezerkenya",
    "password": "6789067890"
}

# 1. Perform the login
response = session.post(login_url, data=payload)

# 2. Check if login was successful
if response.status_code == 200:
    # 3. Access the dashboard using the same session
    dashboard_page = session.post(dashboard_url)
    print(dashboard_page.text)