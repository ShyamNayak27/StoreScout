# StoreScout : Valorant 🎮

An automated Python script that monitors your system's idle state, launches Valorant, captures daily store screenshots, and manages the application lifecycle. The script intelligently waits for idle periods before checking the store, making it non-intrusive to your regular computer usage.

## Features ✨

- 🕒 Automated daily store checking (every 24 hours)
- 💻 Intelligent idle state detection
- 🚀 Automatic Valorant launch and closure
- 📸 Automated store navigation and screenshot capture
- 💾 Timestamp-based screenshot naming
- 🔄 Continuous operation with smart timing adjustments

## Prerequisites 📋

- Python 3.x
- Required Python packages:
  - `pyautogui`
  - `win32api`
  - `psutil`
  - `AppOpener`

## Installation 🚀

1. Clone this repository:
```bash
git clone https://github.com/ShyamNayak27/valorant-store-checker.git
cd valorant-store-checker
```

2. Install required packages:
```bash
pip install pyautogui win32api psutil AppOpener
```

## Configuration ⚙️

The script uses default screen coordinates for the Valorant store (146, 866). If your screen resolution differs, you may need to adjust these coordinates in the `store_screenshot()` function.

Key timings in the script:
- Idle check interval: 30 minutes
- Application launch wait time: 80 seconds
- Screenshot delay: 2 seconds
- Daily check interval: 24 hours (86400 seconds)

## Usage 💻

Simply run the script:
```bash
python valorant_store_checker.py
```

The script will:
1. Monitor system for idle state
2. Launch Valorant when system is idle
3. Navigate to store and capture screenshot
4. Close Valorant automatically
5. Wait for 24 hours before next check
6. Repeat the process

## How It Works 🔧

1. **Idle Detection**: Checks if the system has been idle for 30 minutes
2. **Process Management**: 
   - Verifies if Valorant is running
   - Launches or closes the application as needed
3. **Screenshot Process**:
   - Navigates to store automatically
   - Captures and saves screenshot with timestamp
4. **Timing System**:
   - Maintains 24-hour interval between checks
   - Adjusts timing if delays occur

## File Structure 📁

```
valorant-store-checker/
├── valorant_store_checker.py
└── screenshots/
    └── screenshot_YYYYMMDD_HHMMSS.png
```

## Security Notice 🔒

- The script requires Valorant to be installed on your system
- No login credentials are stored or required
- Uses Windows API for idle detection

## Customization 🔧

You can modify these variables in the script:
- Idle check interval (currently 1800 seconds)
- Application launch wait time (currently 80 seconds)
- Screenshot delay (currently 2 seconds)
- Store coordinates (currently 146, 866)

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer ⚠️

This project is not affiliated with Riot Games or Valorant. Use at your own risk.

## Support 🆘

For issues or suggestions:
- Open an issue on GitHub
- Submit a pull request
- Contact: [https://www.linkedin.com/in/shyamnnayak/]

---
Made with ❤️ by [Shyam Narayan Nayak]
