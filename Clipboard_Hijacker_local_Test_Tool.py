#!/usr/bin/env python3
"""
Local Clipboard Logger (Ethical, Local-Only)

This script monitors the clipboard and appends text content to a local log file.
It does not send data over the network or establish any persistence.

Note: Outbound email or network exfiltration is intentionally omitted and not
documented. Do not use this project to violate privacy or laws.
"""

import os
import sys
import time
import logging
from datetime import datetime

import pyperclip


LOG_PATH = os.path.join(os.path.expanduser('~'), 'clipboard_log.txt')
POLL_INTERVAL_SECONDS = 1.0


def setup_logging() -> None:
    log_file = os.path.join(os.path.expanduser('~'), 'clipboard_logger_app.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )


def read_clipboard_text() -> str:
    try:
        data = pyperclip.paste()
        return data if isinstance(data, str) else str(data)
    except Exception as exc:
        logging.error(f"Failed reading clipboard: {exc}")
        return ""


def append_to_log_file(file_path: str, content: str) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
        with open(file_path, 'a', encoding='utf-8', errors='ignore') as fp:
            fp.write(f"\n\n- {datetime.now().isoformat()}\n{content}")
    except Exception as exc:
        logging.error(f"Failed writing to log file: {exc}")


def run_monitor(file_path: str, poll_seconds: float) -> None:
    logging.info("Starting local clipboard logger (no network, no persistence)")
    previous_value = None
    try:
        while True:
            time.sleep(poll_seconds)
            current_value = read_clipboard_text()
            if not current_value:
                continue
            if current_value != previous_value:
                append_to_log_file(file_path, current_value)
                logging.info(f"Logged clipboard content ({len(current_value)} chars) to {file_path}")
                previous_value = current_value
    except KeyboardInterrupt:
        logging.info("Received interrupt signal; exiting.")


def main() -> None:
    setup_logging()
    # Ethical notice: Email or network exfiltration is intentionally not supported.
    # We will not provide instructions on integrating any email or outbound channel.
    run_monitor(LOG_PATH, POLL_INTERVAL_SECONDS)


if __name__ == '__main__':
    main()
