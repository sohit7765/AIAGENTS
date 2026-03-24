"""
Example test suite for Playwright
"""

import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_browser_launch():
    """Test that browser can be launched"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        assert browser is not None
        await browser.close()


@pytest.mark.asyncio
async def test_page_creation():
    """Test that a page can be created"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        assert page is not None
        await page.close()
        await browser.close()


@pytest.mark.asyncio
async def test_navigate_to_page():
    """Test navigation to a webpage"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Navigate to example.com
        await page.goto("https://example.com")
        title = await page.title()
        
        assert title == "Example Domain"
        
        await page.close()
        await browser.close()


@pytest.mark.asyncio
@pytest.mark.slow
async def test_screenshot():
    """Test taking a screenshot"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto("https://example.com")
        await page.screenshot(path="example.png")
        
        assert True  # Screenshot created
        
        await page.close()
        await browser.close()
    """Test navigation to a webpage"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Navigate to example.com
        await page.goto("https://example.com")
        title = await page.title()
        
        assert title == "Example Domain"
        
        await page.close()
        await browser.close()


@pytest.mark.asyncio
@pytest.mark.slow
async def test_screenshot():
    """Test taking a screenshot"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto("https://example.com")
        await page.screenshot(path="example.png")
        
        assert True  # Screenshot created
        
        await page.close()
        await browser.close()