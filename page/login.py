from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set True for headless mode
        page = browser.new_page()

        # Open login page
        page.goto("https://practicetestautomation.com/practice-test-login/")

        # Enter credentials
        page.locator("#username").fill("student")
        page.locator("#password").fill("Password123")

        # Click login button
        page.locator("#submit").click()

        # Assert success message
        page.wait_for_selector("text=Logged In Successfully")
        assert page.title() == "Logged In Successfully | Practice Test Automation"

        print("✅ Login test passed successfully!")
        browser.close()


if __name__ == "__main__":
    test_login()