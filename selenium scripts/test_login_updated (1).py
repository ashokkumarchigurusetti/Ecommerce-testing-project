
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1️⃣ Start Chrome browser
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
driver.maximize_window()

# 2️⃣ Click on 'Signup / Login'
driver.find_element(By.LINK_TEXT, "Signup / Login").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

# 3️⃣ Enter email and password
driver.find_element(By.NAME, "email").send_keys("22kf1a0521@sseptp.org")
driver.find_element(By.NAME, "password").send_keys("Ashok@123")
driver.find_element(By.XPATH, "//button[text()='Login']").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'Logged in as')]")))

# 4️⃣ Verify login success by checking 'Logged in as' label
logged_in_text = driver.find_element(By.XPATH, "//li[contains(text(), 'Logged in as')]").text
assert "Logged in as" in logged_in_text, "❌ Login failed"
print("✅ Test Passed: Successfully logged in as user.")

# 5️⃣ Close the browser
driver.quit()
