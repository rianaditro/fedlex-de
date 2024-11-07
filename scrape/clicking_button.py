import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from scrape.wait_driver import WaitDriver


class ButtonClicker:
  """Manages button clicks on main and sub levels."""
  def __init__(self, driver_setup):
    self.driver_setup = driver_setup
    self.wait = WaitDriver(driver_setup).wait
    
  def click_main_button(self, row_index):
    """Click the main button, return False if the href contains '#'."""
    # XPath for the main button based on the row index
    xpath = f'//*[@id="content"]/div/table/tbody/tr[{row_index}]/td[2]/a'

    # Find the main button
    button = self.driver_setup.find_element(By.XPATH, xpath)

    # Get the href attribute of the main button
    href = button.get_attribute('href')
    # If the href is not None and it contains '#', return False
    if href and '#' in href:
      return False
    
    # Click the main button and print a message
    button.click()
    print(f"Clicking main button {row_index}")
    
    # Return True to indicate the main button was clicked
    return True

  def click_sub_buttons(self):
    """Click all available sub-buttons on the new page."""
    sub_button_clicked = False  # Initialize a flag to track if any sub-button is clicked

    # Get all rows contains sub-buttons
    lines_xpath = '//*[@id="content"]/div/table/tbody/tr'
    lines = self.driver_setup.find_elements(By.XPATH, lines_xpath)  

    for j in range(1, len(lines) + 1):  # Iterate over each row
      # Construct XPath for sub-button
      xpath = f'//*[@id="content"]/div/table/tbody/tr[{j}]/td[2]/a'
      try:
        # Click the sub-button
        sub_button = self.driver_setup.find_element(By.XPATH, xpath)
        sub_button.click()
        sub_button_clicked = True  # Update flag to indicate a sub-button was clicked
        print(f"\tClicking sub button {j}")
        
        # Wait for the spinner to load before clicking download button
        self.wait_by_element()

        # Download file
        xpath = '//*[@id="versionContent"]/tbody/tr[1]/td[3]/div/a[2]'
        download_button = self.wait.until(EC.presence_of_element_located
                                          ((By.XPATH, xpath)))  # Wait for download button
        download_button.click()
        time.sleep(5)  # Wait until download is complete
        print("File download triggered.")

        # Navigate back to the sub-page
        self.driver_setup.back()
        print('\tGoing back to the sub-page')
        self.wait.until(EC.presence_of_element_located
                        ((By.XPATH, lines_xpath)))

      except (TimeoutException, NoSuchElementException):
        # Log if clicking the sub-button fails
        print(f"\tSkipping sub button {j} because of the invalid link.")
        
    return sub_button_clicked  # Return the flag indicating if any sub-button was clicked
  
  def wait_by_element(self):
    """Wait until the spinner element is not found, i.e. the page loading is finished."""

    # Keep checking until the spinner is gone.
    while True:
      try:
        spinner_xpath = '/html/body/app-root/div/div/mat-spinner/svg/circle'
        # If we can find the spinner element, it means the page is still loading
        self.driver_setup.find_element(By.XPATH, spinner_xpath)
      except:
        # If the spinner element is not found, it means the page is finished loading
        time.sleep(1)
        # Exit the loop once the spinner is no longer found
        break
