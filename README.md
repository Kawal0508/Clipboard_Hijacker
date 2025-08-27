# Local Clipboard Logger (Ethical, Local-Only)

## ⚠️ Disclaimer
This project is for educational purposes and personal productivity only. Use it on systems where you have explicit permission. Do not use this project to violate privacy or laws.

## Overview
This tool monitors your clipboard and appends copied text to a local file for your own records. It performs no network activity, does not attempt persistence, and stores data only on your machine.

## Features
- Real-time clipboard monitoring
- Local-only logging to a text file
- Simple, minimal codebase
- No network, no persistence

# Installation
```bash
pip install -r requirements.txt
```

# Per-file guide

## Clipboard_Hijacker_local_Test_Tool.py (primary script)
- Purpose: Local-only clipboard logger for ethical, consent-based use.
- Behavior: Reads clipboard text periodically, prints to console, appends to a local log with timestamps. No network or persistence.

Run:
```bash
python Clipboard_Hijacker_local_Test_Tool.py
```

- Log file path: `~/clipboard_log.txt`
- App log path: `~/clipboard_logger_app.log`
- Stop with Ctrl+C.

Build (optional):
```bash
pyinstaller --onefile --console --name ClipboardLogger Clipboard_Hijacker_local_Test_Tool.py
```

Configuration:
- Edit `LOG_PATH` and `POLL_INTERVAL_SECONDS` at the top of the file.

Ethical notes:
- Avoid storing sensitive data; clear/rotate logs regularly.
- Use only on systems/accounts where you have explicit permission.

## Clipboard_Hijacker_Tool.py (wrapper/entry point)
- Purpose: Convenience entry that should call the primary script’s `main`.
- Recommended content:
  - Import `main` from `Clipboard_Hijacker_local_Test_Tool.py` and invoke it.

Example wrapper:
```python
from Clipboard_Hijacker_local_Test_Tool import main

if __name__ == "__main__":
    main()
```

Run:
```bash
python Clipboard_Hijacker_Tool.py
```

Notes:
- Wrapper does not change behavior; logging remains local-only.

# Building a local executable (no network, no persistence)

You can package the script into a standalone Windows executable for your own use.

Prerequisites:
- Python 3.8+
- `pyinstaller` (already listed in `requirements.txt`)

Steps:
```bash
# From the project root
pyinstaller --onefile --console --name ClipboardLogger Clipboard_Hijacker_local_Test_Tool.py

# Resulting EXE will be at:
dist/ClipboardLogger.exe
```

Notes:
- The `--console` flag keeps a console window so you can stop with Ctrl+C and see logs.
- This executable behaves exactly like the script: local-only logging, no network.

# Optional: simple .bat launcher for local use

If you prefer to run the Python script via a batch file, create `run_clipboard_logger.bat` alongside the script with the following content and adjust the Python path as needed:

```bat
@echo off
setlocal
REM Update this Python path if necessary
set PYTHON_EXEC=python

%PYTHON_EXEC% "%~dp0Clipboard_Hijacker_local_Test_Tool.py"
endlocal
```

Double-clicking the `.bat` will launch the logger in a console window. This is strictly a local launcher and does not add any persistence.

# Important ethical boundary

This project does not include, and will not document, any techniques for concealing payloads, steganography, or any form of data exfiltration. The build instructions above are provided solely for benign, consent-based, local usage.

# Configuration
Small tweaks can be made by editing constants at the top of `clipboard_hijacker.py`:
- `LOG_PATH`: where clipboard entries are stored
- `POLL_INTERVAL_SECONDS`: how often the clipboard is checked

# Ethical Scope
- This project intentionally excludes email integration, webhooks, or any exfiltration.
- The code and this README do not include instructions for adding any outbound channels.
- If you need notifications or syncing, use legitimate, opt-in tools (e.g., cloud notes, password managers).

# Development
- Python 3.8+
- Windows 10/11 recommended (uses `pyperclip`)

# Troubleshooting
1. Clipboard read errors: some apps restrict access; try copying plain text.
2. Non-ASCII text issues: the logger writes UTF-8 and ignores invalid sequences.
3. Antivirus warnings: the script is local-only; consider adding a local exclusion if needed.

## License
Educational use only. You are responsible for complying with applicable laws and obtaining consent where required.
