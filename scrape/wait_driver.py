from selenium.webdriver.support.ui import WebDriverWait


class WaitDriver:
  """Handles the waiting time."""
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)
