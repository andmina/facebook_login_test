from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Path to the ChromeDriver executable
chromedriver_path = '/usr/local/bin/chromedriver'

# Create a Service object with the path to the ChromeDriver executable
service = Service(executable_path=chromedriver_path)

# Start the Chrome driver with the Service object
driver = webdriver.Chrome(service=service)

# Navigate to the Facebook login page
driver.get('https://www.facebook.com/')

# Find the email field and enter your email address
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys('example@example.xyzzzz')

# Find the password field and enter your password
password_field = driver.find_element(By.NAME, 'pass')
password_field.send_keys('examplepass')

# Click the login button
login_button = driver.find_element(By.NAME, 'login')
login_button.click()

# Wait for the page to load
driver.implicitly_wait(10)

# Check that the user is logged in by looking for aria-label Home
try:
    home_label = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Home']")
    assert home_label is not None, "Login failed"
    print("Login successful")
except AssertionError as error:
    print(error)

# Close the browser
driver.quit()
