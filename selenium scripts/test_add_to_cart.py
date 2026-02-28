from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1️⃣ Launch browser and open site
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
driver.maximize_window()

# 2️⃣ Click on 'Signup / Login'
driver.find_element(By.LINK_TEXT, "Signup / Login").click()
time.sleep(2)

# 3️⃣ Enter login credentials
driver.find_element(By.NAME, "email").send_keys("22kf1a0521@sseptp.org")
driver.find_element(By.NAME, "password").send_keys("Ashok@123")
driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(3)

# 4️⃣ Navigate to 'Products'
driver.find_element(By.LINK_TEXT, "Products").click()
time.sleep(3)

# 5️⃣ Scroll and add the first product to cart
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)
driver.find_element(By.XPATH, "(//a[@data-product-id])[1]").click()
time.sleep(2)

# 6️⃣ Click 'View Cart'
driver.find_element(By.XPATH, "//u[text()='View Cart']").click()
time.sleep(2)

# 7️⃣ Verify product is in cart
cart_items = driver.find_elements(By.CLASS_NAME, "cart_description")
assert len(cart_items) > 0, "❌ Product not added to cart"
print("✅ Test Passed: Product successfully added to cart.")

# 8️⃣ Close browser
driver.quit()
