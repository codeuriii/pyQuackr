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

    def select_country(self, contry: str):
        pays = [
            'australia', 'austria', 'belgium', 'brazil', 'canada',
            'china', 'denmark', 'finland', 'france', 'germany',
            'hungary', 'india', 'indonesia', 'ireland', 'israel',
            'italy', 'korea', 'latvia', 'mexico', 'morocco', 'netherlands',
            'norway', 'pakistan', 'poland', 'russia', 'south-africa',
            'spain', 'sweden', 'switzerland', 'ukraine', 'united-kingdom',
            'united-states'
        ]

        if not contry in pays:
            raise ValueError(f"{contry} is not in {pays}\nPlease select a valid country.")
        
        url = "https://quackr.io/temporary-numbers/" + contry
        self.driver.get(url)


    def get_temporary_numbers(self, lenght: int):
        pass
