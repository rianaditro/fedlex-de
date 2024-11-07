import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverSetup:
    """Handles the setup and teardown of the WebDriver."""
    def __init__(self):
        # Configure Chrome options
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")

        # Set the default download directory to the current working directory
        # and create it if it doesn't exist
        download_dir = os.path.join(os.getcwd(), "downloads")
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # Configure download preferences
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }

        # Set experimental options for the driver
        options.add_experimental_option("prefs", prefs)

        # Initiate the browser with options
        self.driver = webdriver.Chrome(options=options)

        # Set the download behavior to allow all downloads and save to the provided directory.
        self.driver.execute_cdp_cmd('Page.setDownloadBehavior', {'behavior': 'allow', 
                                                                 'downloadPath': download_dir})

    def close(self):
        """Close the WebDriver."""
        self.driver.quit()
