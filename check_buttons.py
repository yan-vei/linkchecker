import os
import time
import datetime
from selenium import webdriver

dir = os.path.dirname(__file__)
error_log = open("error_log.txt", "w")

def setupDriver():
    global driver, setup, wait

    setup = open("setup.txt", "r")
    settings = []
    for line in setup:
        settings.append(line.rstrip().split(" - "))

    if (settings[1][1] == "Chrome"):
        driver = webdriver.Chrome(executable_path=(os.path.join(dir, "drivers\\chromedriver.exe")))
    elif (settings[1][1] == "Firefox"):
        driver = webdriver.Firefox(executable_path=(os.path.join(dir, "drivers\\geckodriver.exe")))
    else:
        error_log.write("[" + str(datetime.datetime.now())[:19] + "] Invalid browser. Chrome/Firefox expected, " + str(settings[1][1]) + " found")
        raise Exception("Invalid browser. Chrome/Firefox expected, " + str(settings[1][1]) + " found")

    wait = settings[2][1]
    driver.get(settings[0][1])
    time.sleep(int(wait))

class ButtonLinkChecker:

    def __init__(self, buttonName, selector, target):
        self.buttonName = buttonName
        self.selector = selector
        self.target = target
        self.button = driver.find_element_by_css_selector(selector)

    def check(self):
        try:
            assert(self.button.is_displayed())
        except(AssertionError):
            error_log.write("[" + str(datetime.datetime.now())[:19] + "] " + self.buttonName + " element is not found\n")

        self.button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(int(wait))
        try:
            dest = "screenshots\\" + self.buttonName + " " + (datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")) + ".png"
            driver.save_screenshot(os.path.join(dir, dest))
            assert (self.target in driver.title or self.target in driver.current_url)
        except(AssertionError):
            error_log.write("[" + str(datetime.datetime.now())[:19] + "] " + self.buttonName + " link is broken. Leads to: " + driver.current_url + "\n")

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

setupDriver()

links = open("links.txt", "r")
buttonItems = []

for line in links:
    data = line.rstrip().split(" - ")
    buttonItems.append(ButtonLinkChecker(data[0], data[1], data[2]))

for buttonElement in buttonItems:
    buttonElement.check()


