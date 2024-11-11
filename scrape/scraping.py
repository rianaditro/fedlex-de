from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from scrape.setup_driver import DriverSetup
from scrape.clicking_button import ButtonClicker
from scrape.wait_driver import WaitDriver


class WebScraper:
  """Orchestrates the entire scraping process."""
  def __init__(self, url):
    self.url = url
    """
    use self.driver if it is a driver instance 
    use self.driver_setup if it is a DriverSetup instance
    """
    self.driver_setup = DriverSetup().driver
    self.wait = WaitDriver(self.driver_setup).wait

    """
    please note that self.wait will create a WaitDriver instance,
    and self.button_clicker will create a second WaitDriver instance inside ButtonClicker.
    no revision needed.   
    """
    self.button_clicker = ButtonClicker(self.driver_setup)

  def scrape(self, max_main_buttons=3):
    """Click main buttons and sub-buttons."""
    self.driver_setup.get(self.url)
    self.wait.until(EC.presence_of_element_located
                    ((By.XPATH, '//*[@id="content"]/div/table/tbody/tr')))

    for i in range(1, max_main_buttons + 1):
      # If the href contains '#', skipping the main button
      if not self.button_clicker.click_main_button(i):
        print(f"Skipping main button {i} because of the invalid link.")
        continue
      
      # Wait for the spinner to load before clicking sub-buttons
      self.button_clicker.wait_by_element()

      # If sub-button is clicked, navigate back to the main
      if self.button_clicker.click_sub_buttons():
        self.driver_setup.back()
        print('Going back to the main page')
        self.wait.until(EC.presence_of_element_located
                        ((By.XPATH, '//*[@id="content"]/div/table/tbody/tr')))

    self.driver_setup.close()
