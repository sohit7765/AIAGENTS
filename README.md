# Playwright Python Project

[![CI](https://github.com/sohit7765/AIAgents/actions/workflows/playwright.yml/badge.svg)](https://github.com/sohit7765/AIAgents/actions/workflows/playwright.yml)
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://python.org)
[![Playwright](https://img.shields.io/badge/playwright-1.58.0-green.svg)](https://playwright.dev)

A Python project for browser automation and testing using Playwright.

## Project Structure

```
AIAgents/
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
├── pytest.ini             # Pytest configuration
├── playwright.ini         # Playwright configuration
├── .env.example           # Environment variables template
├── src/                   # Source code directory
│   ├── __init__.py
│   └── browser.py         # Browser automation utilities
├── tests/                 # Test directory
│   ├── __init__.py
│   ├── test_example.py    # Basic Playwright tests
│   └── test_registration_e2e.py  # E2E registration tests
└── scripts/               # Utility scripts
    └── setup_browsers.py  # Setup script for browsers and dependencies
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/sohit7765/AIAgents.git
   cd AIAgents
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

## Usage

### Running Tests
```bash
pytest tests/
```

### Running E2E Registration Tests
```bash
pytest tests/test_registration_e2e.py -v
```

### Running a Script
```bash
python scripts/setup_browsers.py
```

## Configuration

- **pytest.ini**: Pytest configuration for test discovery and execution
- **playwright.ini**: Playwright-specific settings
- **.env**: Environment variables (create from .env.example)

## Documentation

- [Playwright Python Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and testing. The CI pipeline:

- **Runs on**: Every push and pull request to main/master branches
- **Tests on**: Ubuntu and Windows with Chromium, Firefox, and WebKit browsers
- **Generates**: Test reports and screenshots as artifacts
- **Special E2E**: Runs comprehensive E2E registration tests on main branch pushes

### Workflow Features

- **Multi-browser testing**: Tests run on Chromium, Firefox, and WebKit
- **Cross-platform**: Tests on both Ubuntu and Windows
- **Parallel execution**: Matrix strategy for faster CI runs
- **Artifact uploads**: Screenshots and test results saved for 30 days
- **E2E focus**: Dedicated job for critical user journey tests

### Viewing Test Results

1. Go to the [Actions tab](https://github.com/sohit7765/AIAgents/actions) in your repository
2. Click on the latest workflow run
3. Download artifacts from the "Artifacts" section to view screenshots and test reports

**🚀 CI/CD Pipeline Active!** - Automated testing is now running on every code change.
