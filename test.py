from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
print(driver.title)



eyedropper_icon = driver.find_element(By.CLASS_NAME, "bx.bxs-eyedropper")

# Perform a hover action on the "bx bxs-eyedropper" element
actions = ActionChains(driver)
actions.move_to_element(eyedropper_icon).perform()

# Wait for some time to observe the results after performing the hover action
time.sleep(2)

# Find the element with class "fas fa-flask icon-lab"
flask_icon = driver.find_element(By.CLASS_NAME, "fas.fa-flask.icon-lab")

# Perform a hover action on the "fas fa-flask icon-lab" element
actions = ActionChains(driver)
actions.move_to_element(flask_icon).perform()

# Wait for some time to observe the results after performing the hover action

# Click on the search box icon to activate it
time.sleep(1)

# Click on the search box icon to activate it
time.sleep(1)
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
time.sleep(1)
search_bar.click()
time.sleep(1)

# Find the search box input by its CSS selector
search_box = driver.find_element(By.CSS_SELECTOR, ".search-box input[name='Marque']")

search_box.clear()

# Slowly type "Test_PCR" into the search box
search_text = "Test_PCR"
for char in search_text:
    search_box.send_keys(char)
    time.sleep(0.2)  # Add a delay of 0.2 seconds between each character

# Press the Enter key to perform the search
search_box.send_keys(Keys.ENTER)

# Wait for some time to observe the search results (you may adjust the sleep time as needed)
time.sleep(1)

# Click on the search box icon to activate it again
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
search_bar.click()

time.sleep(1)

# Find the search box input by its CSS selector
search_box = driver.find_element(By.CSS_SELECTOR, ".search-box input[name='Marque']")

search_box.clear()

# Slowly type "GMSR fS-chimie" into the search box
search_text = "GMSR fS-chimie"
for char in search_text:
    search_box.send_keys(char)
    time.sleep(0.2)  # Add a delay of 0.2 seconds between each character

# Press the Enter key to perform the search
search_box.send_keys(Keys.ENTER)

# Wait for some time to observe the search results (you may adjust the sleep time as needed)
time.sleep(1)

# Click on the search box icon to activate it again
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
search_bar.click()

# Wait for some time to observe the search results (you may adjust the sleep time as needed)
time.sleep(1)

# Find the element with class "bx-home-alt"
home_icon = driver.find_element(By.CLASS_NAME, "bx-home-alt")

# Perform a hover action on the "bx-home-alt" element
actions = ActionChains(driver)
actions.move_to_element(home_icon).perform()

home_icon = driver.find_element(By.CLASS_NAME, "bx-home-alt")
home_icon.click()

# Wait for some time to observe the results after performing the hover action
time.sleep(1)

# Find the element with id "region-A"
region_A = driver.find_element(By.ID, "region-A")

# Perform a hover action on the element with id "region-A"
actions = ActionChains(driver)
actions.move_to_element(region_A).perform()

# Wait for some time to observe the results after performing the hover action
time.sleep(1)

# Find the element with id "region-B"
region_B = driver.find_element(By.ID, "region-B")

# Perform a hover action on the element with id "region-B"
actions = ActionChains(driver)
actions.move_to_element(region_B).perform()

# Wait for some time to observe the results after performing the hover action
time.sleep(1)

# Click on the search box icon to activate it again
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
search_bar.click()

time.sleep(1)

# Find the element with class "bx bx-bar-chart-alt-2 icon"
bar_chart_button = driver.find_element(By.CLASS_NAME, "bx.bx-bar-chart-alt-2.icon")

# Perform a hover action on the button
actions = ActionChains(driver)
actions.move_to_element(bar_chart_button).perform()

# Wait for some time to observe the results after performing the hover action
time.sleep(1)

# Click on the button
bar_chart_button.click()

# Wait for some time to observe the results after performing the hover action

delete_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-danger[href='/supprimer_equipement/1']")

# Effectuer un "hover" sur le bouton avant de cliquer dessus
actions = ActionChains(driver)
actions.move_to_element(delete_button).perform()

# Attendre un certain temps pour observer le "hover"
time.sleep(2)

# Cliquer sur le bouton
delete_button.click()

# Wait for some time to observe the results after clicking the button
time.sleep(2)

delete_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-danger[type='submit']")

time.sleep(1)
actions = ActionChains(driver)
actions.move_to_element(delete_button).perform()

# Attendre un certain temps pour observer le "hover"


time.sleep(1)

delete_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-danger[href='/supprimer_equipement/1']")
delete_button.click()
time.sleep(2)
show_equipement_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-warning[href='/showEquipement/']")
time.sleep(1)
show_equipement_button.click()





# Close the WebDriver

