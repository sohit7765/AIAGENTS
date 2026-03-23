"""
Browser automation module for Playwright
"""

from playwright.async_api import async_playwright, Browser, Page
import os
from dotenv import load_dotenv

load_dotenv()


async def get_browser() -> Browser:
    """Initialize and return a Playwright browser instance"""
    playwright = await async_playwright().start()
    browser_type = os.getenv("BROWSER_TYPE", "chromium")
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    
    if browser_type == "firefox":
        browser = await playwright.firefox.launch(headless=headless)
    elif browser_type == "webkit":
        browser = await playwright.webkit.launch(headless=headless)
    else:
        browser = await playwright.chromium.launch(headless=headless)
    
    return browser


async def create_page(browser: Browser) -> Page:
    """Create a new browser page"""
    context = await browser.new_context()
    page = await context.new_page()
    return page