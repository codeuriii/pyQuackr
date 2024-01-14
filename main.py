from selenium import webdriver
from selenium.webdriver.edge.options import Options
from myby import by

class PyQuackr:

    def __init__(self, headless: bool = True) -> None:
        options = Options()
        if headless:
            options.add_argument("headless")
        else:
            options.add_argument("start-maximized")

        self.driver = webdriver.Edge(options=options)
        self.driver.get("https://quackr.io/")

        