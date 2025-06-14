import os
from ..abstract_webtools import *
from .urlManager import *
from urllib.parse import urlparse
from abstract_utilities import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import urllib3

# Suppress urllib3 warnings and debug logs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.getLogger("urllib3").setLevel(logging.WARNING)

# Suppress Selenium logs
logging.getLogger("selenium").setLevel(logging.WARNING)

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.binary_location = "/home/profiles/solcatcher/.cache/selenium/chrome/linux64/130.0.6723.58/chrome"
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--remote-debugging-port=9222")


class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class seleniumManager(metaclass=SingletonMeta):
    def __init__(self, url):
        if not hasattr(self, 'initialized'):  # Prevent reinitialization
            self.initialized = True
            parsed_url = urlparse(url)
            self.domain = parsed_url.netloc
            self.scheme = parsed_url.scheme
            self.base_url= f"{self.scheme}{self.domain}"
            self.site_dir = os.path.join(os.getcwd(), self.domain)
            os.makedirs(self.site_dir, exist_ok=True)
            self.drivers = {}
            self.page_type = []
    
    def get_url_to_path(self, url):
        url = eatAll(str(url), ['',' ','\n','\t','\\','/'])
        parsed_url = urlparse(url)
        if parsed_url.netloc == self.domain:
            paths = parsed_url.path.split('/')
            dir_path = self.site_dir
            for path in paths[:-1]:
                dir_path = os.path.join(dir_path, path)
                os.makedirs(dir_path, exist_ok=True)
            self.page_type.append(os.path.splitext(paths[-1])[-1] or 'html' if len(self.page_type) == 0 else self.page_type[-1])
            
            dir_path = os.path.join(dir_path, paths[-1])
            return dir_path

    def saved_url_check(self, url):
        path = self.get_url_to_path(url)
        return path

    def get_with_netloc(self, url):
        parsed_url = urlparse(url)
        if parsed_url.netloc == '':
            url = f"{self.scheme}://{self.domain}/{url.strip()}"
        return url

    def get_driver(self, url):
        if url and url not in self.drivers:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
            self.drivers[url] = driver
            driver.get(url)
        return self.drivers[url]
def normalize_url(url, base_url=None):
    """
    Normalize and resolve relative URLs, ensuring proper domain and format.
    """
    # If URL starts with the base URL repeated, remove the extra part
    manager = seleniumManager(url)
    base_url = manager.base_url
    if url.startswith(base_url):
        url = url[len(base_url):]

    # Resolve the URL against the base URL
    normalized_url = urljoin(base_url, url.split('#')[0])

    # Ensure only URLs belonging to the base domain are kept
    if not normalized_url.startswith(base_url):
        return None

    return normalized_url
# Function to get Selenium page source
def get_selenium_source(url):
    url_mgr = urlManager(url)
    if url_mgr.url:
        url = str(url_mgr.url)
        manager = seleniumManager(url)
        driver = manager.get_driver(url)
        try:
            # Get page source
            page_source = driver.page_source
            return page_source
        finally:
            # Don't quit the driver unless you're done with all interactions
            pass

