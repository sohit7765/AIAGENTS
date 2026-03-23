# Playwright Python Project

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
│   └── __init__.py
├── tests/                 # Test directory
│   ├── __init__.py
│   └── test_example.py
└── scripts/               # Utility scripts
    └── setup_browsers.py
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd c:\Users\sohit\OneDrive\Desktop\AIAgents
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

## License

MIT
