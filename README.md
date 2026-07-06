# BLE HID Analyzer

BLE HID Analyzer is a MicroPython tool for ESP32 boards that discovers nearby Bluetooth Low Energy Human Interface Device (BLE HID) peripherals, connects to a selected target, inspects HID services and characteristics, enables notifications, decodes common HID reports, and saves a detailed JSON diagnostics report.

It is designed for debugging and analyzing BLE HID traffic such as keyboard, mouse, consumer-control, and vendor-specific reports.

## Features

- Scans for nearby BLE devices
- Connects to a selected target by MAC address or interactive scan selection
- Detects HID services and report characteristics
- Reads report reference descriptors
- Enables notification descriptors (CCCD)
- Decodes common HID event payloads, including:
  - keyboard input
  - mouse input
  - consumer-control input
  - raw/vendor data fallback
- Saves JSON diagnostics reports to a reports directory
- Stores known devices for repeated use

## Requirements

- An ESP32 board running MicroPython
- BLE support enabled in the firmware
- A serial terminal or REPL connection for running the script

## Installation

1. Copy the script to your ESP32 as `main.py`.
2. Optionally copy the example configuration to `config.json` and adjust it for your setup.
3. Reset or reboot the board and run the script from the serial console.

### Example upload with ampy

```bash
ampy --port COMx put ble_hid_analyzer.py main.py
```

If you use a different upload tool, the important requirement is that the file is available on the device as `main.py`.

## Configuration

Create a file named `config.json` with settings such as the following:

```json
{
  "auto_scan": true,
  "target_mac": "",
  "device_name": "",
  "verbose": "NORMAL",
  "save_reports": true,
  "reports_directory": "reports",
  "scan_timeout": 5,
  "connect_timeout": 20,
  "create_config_if_missing": false
}
```

### Configuration options

- `auto_scan`: If `true`, the tool scans for BLE devices and lets you choose one interactively.
- `target_mac`: A specific BLE device MAC address to connect to directly.
- `device_name`: Optional friendly name used for the target.
- `verbose`: Logging level (`QUIET`, `NORMAL`, or `DEBUG`).
- `save_reports`: Enables or disables report saving.
- `reports_directory`: Folder where JSON reports are stored.
- `scan_timeout`: How long the scan phase lasts in seconds.
- `connect_timeout`: How long the connection attempt waits in seconds.
- `create_config_if_missing`: If enabled, the script can create a default `config.json` when missing.

## Usage

Once the script is running:

1. If `auto_scan` is enabled, select a BLE device from the discovered list.
2. The tool will attempt to connect and inspect the HID service.
3. It will enable notifications for discovered report characteristics.
4. When you interact with the HID device, decoded events will be displayed.
5. The session will save a JSON diagnostics report when interrupted or completed.

## Output Files

The tool may generate:

- `reports/last_report.json`: the latest saved report
- `reports/<timestamp>.json`: timestamped session reports
- `known_devices.json`: a list of previously accepted devices
- `config.json`: your runtime configuration

## Notes

- The tool is intended for debugging and analysis; it does not perform any hostile or destructive actions.
- Some BLE HID devices expose non-standard or compact report layouts, so raw or vendor-specific fallback data may appear.
- If you plan to reuse the same device often, saving it to `known_devices.json` can simplify future sessions.

## License

MIT License  
