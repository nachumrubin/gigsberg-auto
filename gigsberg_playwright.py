import json
from playwright.sync_api import sync_playwright

# Replace with your Gigsberg login credentials
EMAIL = "nachum.a.rubin@gmail.com"
PASSWORD = "Qq123456"

# Load configuration
with open("playwright_config.json", "r") as config_file:
    config = json.load(config_file)

base_url = config["base_url"]
browser_type = config["browser_type"]
headless = config["headless"]
timeout = config["timeout"]
credentials = config["credentials"]

with sync_playwright() as p:
    # Launch the browser based on config
    browser = p.chromium.launch(headless=headless)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Navigate to the Gigsberg login page
        page.goto(base_url)

        # Click the login button
        page.locator("#control_header").get_by_text("Log In").click()

        # Wait for the login form to load
        page.wait_for_selector("#login_email")  # Assuming the email input has ID "login_email"

        # Enter email and password
        page.fill("#login_email", credentials["email"])
        page.fill("#login_password", credentials["password"])

        # Submit the login form
        page.press("#login_password", "Enter")

        # Wait for the login process to complete, checking for the Login button text to change to the username
        page.get_by_role("link", name=credentials["user_name"]).wait_for()

        print("Login successful!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        browser.close()
