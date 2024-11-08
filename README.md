# Web Scraping Automation
This repository contains a Selenium-based web scraping project designed to automate the process of navigating through multiple button clicks on a webpage, downloading files, and handling page loads and redirects. It targets structured web pages with main and sub-level buttons, allowing for sequential interaction and downloading of content.

## Table of Contents
- [Features](#Features)
- [Project Structure](#Project-Structure)
- [Requirements](#Requirements)
- [Usage](#Usage)
- [Configuration](#Configuration)
- [Important Notes](#Important-Notes)
- [Copyright](#Copyright)
  
## Features
- **Automated Browser Setup**: Configures Chrome with customized download settings and disables unnecessary features for efficient scraping.
- **Button Clicking Management**: Iterates through main buttons and sub-buttons, handling potential invalid links and page navigation.
- **Custom Waiting Mechanism**: Waits for elements to load using `WebDriverWait` to ensure stable operation during navigation and downloads.
- **File Downloads**: Triggers file downloads by interacting with specified buttons and waits for downloads to complete.
  
## Project Structure
- **main.py**: Entry point of the project. Initializes the WebScraper with a target URL and starts the scraping process.
- **scraping.py**: The main orchestration class for the scraping process. It initializes the browser, navigates to the target URL, iterates through main buttons, and clicks sub-buttons.
- **setup_driver.py**: Handles the setup and teardown of the Chrome WebDriver. Configures Chrome options, including setting up a default download directory and allowing automatic downloads.
- **wait_driver.py**: Defines a waiting mechanism using WebDriverWait to handle dynamic page loading times.
- **clicking_button.py**: Manages the clicking of main and sub-buttons on the page. It checks for valid links before interacting with buttons, waits for spinners (loading elements) to disappear, and triggers downloads when appropriate.

## Requirements
- Python 3.x
- [Selenium WebDriver](https://www.selenium.dev/)
- Chrome browser and ChromeDriver
  
Install dependencies using:
```
pip install -r requirements.txt
```
> Note: Ensure that the correct version of ChromeDriver is installed for your Chrome version.

## Usage
1. Update the target URL in main.py. In this case I use 'https://www.fedlex.admin.ch/de/cc/internal-law/1' to get all the docs inside. This might not work in other URL.
```
scraper = WebScraper('URL')
```
2. Run the script:
```
python main.py
```
The script will open a browser, navigate through buttons, download files, and close the browser automatically.

## Configuration
- The default download location is set to `./downloads`. Modify this in `setup_driver.py` if needed.
- Adjust the `max_main_buttons` parameter in `main.py` to control the number of main buttons to click.

## Important Notes
- Make sure to adhere to the website’s `robots.txt` and terms of service before scraping.
- Ensure Chrome WebDriver version matches the installed version of Chrome.

## Copyright
Copyright©2024 ***Raka Arfi***

Released under MIT License
