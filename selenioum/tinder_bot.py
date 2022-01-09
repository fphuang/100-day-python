from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "/Users/fp/development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.tinder.com')

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

time.sleep(2)
log_in_button = driver.find_element(by=By.XPATH, value="//*[@id='o-1556761323']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
log_in_button.click()

time.sleep(2)

facebook_button = driver.find_element(by=By.XPATH, value="//*[@id='o-1335420887']/div/div/div[1]/div/div[3]/span/div[2]/button")
facebook_button.click()

time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# driver.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=464891386855067&kid_directed_site=0&app_id=464891386855067&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D464891386855067%26cbt%3D1640632822168%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df365ff41e89f274%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff38cf8f77949db%2526relation%253Dopener%26client_id%3D464891386855067%26display%3Dpopup%26domain%3Dtinder.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Ftinder.com%252F%26locale%3Den_US%26logger_id%3Df32971052482b6c%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2efe230cdaf54%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff38cf8f77949db%2526relation%253Dopener%2526frame%253Df33ad20b6e9feec%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Duser_birthday%252Cuser_photos%252Cemail%252Cuser_likes%26sdk%3Djoey%26version%3Dv2.8%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2efe230cdaf54%26domain%3Dtinder.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff38cf8f77949db%26relation%3Dopener%26frame%3Df33ad20b6e9feec%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_US&pl_dbl=0')
driver.find_element(by=By.ID, value="email").send_keys("huang.fp@gmail.com")
driver.find_element(by=By.ID, value="pass").send_keys("@@@@@@@@@@@@@@@@@@@@@@")
driver.find_element(by=By.ID, value="loginbutton").click()

time.sleep(2)
driver.switch_to.window(base_window)

# accept button
time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[@id='o-1335420887']/div/div/div/div/div[3]/button[1]").click()

# enable button
time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[@id='o-1335420887']/div/div/div/div/div[3]/button[1]").click()

# I accept button
driver.find_element(by=By.XPATH, value="//*[@id='o-1556761323']/div/div[2]/div/div/div[1]/button").click()
# ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

# driver.find_element(by=By.XPATH, value="//*[@id='o-1556761323']/div/div[1]/div/aside/div/div/a").click()

time.sleep(5)
action = ActionChains(driver)
for n in range(10):
    button = driver.find_element(by=By.XPATH, value="//*[@id='o-1556761323']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button/span")
    button.click()
    time.sleep(5)
