#!/usr/bin/env python3
"""
Setup script to install Playwright browsers
"""

import subprocess
import sys


def install_browsers():
    """Install Playwright browsers"""
    print("Installing Playwright browsers...")
    try:
        subprocess.run(
            [sys.executable, "-m", "playwright", "install"],
            check=True,
        )
        print("✓ Browsers installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing browsers: {e}")
        sys.exit(1)


def install_dependencies():
    """Install project dependencies"""
    print("Installing project dependencies...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
        )
        print("✓ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing dependencies: {e}")
        sys.exit(1)


if __name__ == "__main__":
    print("Setting up Playwright Python project...")
    print("-" * 50)
    
    install_dependencies()
    install_browsers()
    
    print("-" * 50)
    print("✓ Setup complete! Ready to use Playwright.")
    print("\nNext steps:")
    print("1. Create your test files in the 'tests/' directory")
    print("2. Run tests with: pytest tests/")
    print("3. Refer to the README.md for more information")
