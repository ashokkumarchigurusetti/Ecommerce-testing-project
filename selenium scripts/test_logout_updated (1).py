
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1️⃣ Start browser and go to site
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
driver.maximize_window()

# 2️⃣ Login
driver.find_element(By.LINK_TEXT, "Signup / Login").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
driver.find_element(By.NAME, "email").send_keys("22kf1a0521@sseptp.org")
driver.find_element(By.NAME, "password").send_keys("Ashok@123")
driver.find_element(By.XPATH, "//button[text()='Login']").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))

# 3️⃣ Click on Logout
driver.find_element(By.LINK_TEXT, "Logout").click()

# 4️⃣ Verify redirection to login/signup page
WebDriverWait(driver, 10).until(EC.url_contains("login"))
current_url = driver.current_url
assert "login" in current_url or "signup" in current_url, "❌ Logout failed"
print("✅ Test Passed: Successfully logged out and redirected to login page.")

# 5️⃣ Close browser
driver.quit()
