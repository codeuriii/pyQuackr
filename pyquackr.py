from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from myby import by

class PyQuackr:

    def __init__(self, headless: bool = True) -> None:
        options = Options()
        if headless:
            options.add_argument("headless")
        else:
            options.add_argument("start-maximized")

        self.driver = webdriver.Edge(options=options)
        self.wait = WebDriverWait(self.driver, 10)

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
            raise ValueError(
                f"{contry} is not in {pays}\nPlease select a valid country."
            )
        
        
        self.country = contry


    def get_temporary_numbers(self, lenght: int):
        box = self.driver.find_element(by.xpath, '//*[@id="wrapper"]/div/main/country-page/section/div/div[4]')
        all_nums = box.find_elements(by.tag_name, "a")
        all_hrefs = []

        for num in all_nums:
            href = num.get_attribute("href")
            href = href.split("/")[-1]
            all_hrefs.append(href)
        
        return all_hrefs[:lenght]
    

    def get_latest_message(self, number: str):
        backup = self.driver.current_url
        self.driver.get(f"https://quackr.io/temporary-numbers/{self.country}/{number}")
        self.wait.until(EC.visibility_of_element_located((by.xpath, '//*[@id="wrapper"]/div/main/messages/section/div/div/div/table/tbody/tr[1]/td[3]')))
        latest_item = self.driver.find_element(by.xpath, '//*[@id="wrapper"]/div/main/messages/section/div/div/div/table/tbody/tr[1]/td[3]')
        latest_message = latest_item.text
        
        self.driver.get(backup)
        return latest_message