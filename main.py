# from selenium import webdriver
from seleniumwire import webdriver
import config
from selenium.webdriver.chrome.options import Options


proxy_options = {
    "proxy": {
        "https": f"http://{config.proxy_login}:{config.proxy_password}@{config.proxy_server}:{config.proxy_port}"
    }
}
print(proxy_options)
option = webdriver.ChromeOptions()
option.add_argument(f"--user-data-dir={config.data_dir}")
option.add_argument(f"--profile-directory={config.profile_dir}")
option.add_argument("start-maximized")  # open Browser in maximized mode
option.add_argument(f"{config.user_agent}")
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=option,seleniumwire_options=proxy_options)
driver.get("https://www.google.com")
input("Press the <ENTER> key to continue...")
