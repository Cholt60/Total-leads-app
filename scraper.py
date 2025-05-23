from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_cyberbackground(address):
    options = Options()
    options.add_argument("--headless")  # Run in background
    driver = webdriver.Chrome(options=options)

    url = "https://www.cyberbackgroundchecks.com/"
    driver.get(url)
    time.sleep(2)

    # Enter the address
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys(address)
    search_input.submit()

    time.sleep(5)

    try:
        result = driver.find_element(By.CSS_SELECTOR, "a[href*='/address/']")
        result.click()
        time.sleep(3)

        owner_name = driver.find_element(By.XPATH, "//th[text()='Name']/following-sibling::td").text
        occupancy = driver.find_element(By.XPATH, "//th[contains(text(),'Occupancy Type')]/following-sibling::td").text
        phone = driver.find_element(By.XPATH, "//th[text()='Phone']/following-sibling::td").text
        email = driver.find_element(By.XPATH, "//th[text()='Email']/following-sibling::td").text

        driver.quit()

        return {
            "owner_name": owner_name,
            "occupancy": occupancy,
            "phone": phone,
            "email": email
        }

    except Exception as e:
        driver.quit()
        return {
            "error": f"Could not find data for this address: {e}"
        }
