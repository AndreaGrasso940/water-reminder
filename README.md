# Water Reminder

A lightweight Python daemon for Linux that sends desktop notifications to remind you to drink water throughout the day.

## How it works

The script runs as a **systemd user service** that starts automatically at login. It checks the current time every 30 minutes and sends a desktop notification via `notify-send` during the configured time window.

## Requirements

- Linux with systemd
- Python 3
- `libnotify` (`notify-send`)
- A desktop environment that supports desktop notifications (tested on KDE Plasma)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AndreaGrasso940/water-reminder.git
cd water-reminder
```

### 2. Edit the script (optional)

Open `drink_water_reminder.py` and customize:

```python
topic = "water-reminder"   # Notification title
message = "bevi l'acqua"   # Notification message

if 8 <= current_time < 20: # Time window (8:00 - 20:00)
    ...
time.sleep(1800)           # Interval in seconds (1800 = 30 minutes)
```

### 3. Create the systemd user service

```bash
mkdir -p ~/.config/systemd/user
```

Create the file `~/.config/systemd/user/water-reminder.service`:

```ini
[Unit]
Description=Water Reminder
After=graphical-session.target

[Service]
ExecStartPre=/bin/sleep 10
ExecStart=/usr/bin/python3 /path/to/drink_water_reminder.py
Restart=always

[Install]
WantedBy=default.target
```

> Replace `/path/to/` with the actual path to the script.

### 4. Enable and start the service

```bash
systemctl --user daemon-reload
systemctl --user enable water-reminder
systemctl --user start water-reminder
```

### 5. Verify it's running

```bash
systemctl --user status water-reminder
```

You should see `Active: active (running)`.

## Usage

### Stop the reminder

```bash
systemctl --user stop water-reminder
```

### Start it again

```bash
systemctl --user start water-reminder
```

### Disable autostart

```bash
systemctl --user disable water-reminder
```

### View logs

```bash
journalctl --user -u water-reminder --since today
```

## Troubleshooting

### Notifications not showing

Make sure `libnotify` is installed:

```bash
# Arch Linux
sudo pacman -S libnotify

# Ubuntu/Debian
sudo apt install libnotify-bin
```

Test manually:

```bash
notify-send "water-reminder" "bevi l'acqua"
```

### D-Bus error on startup

If you see `Failed to show notification: Cannot autolaunch D-Bus`, it means the service started before your desktop session was ready. The `ExecStartPre=/bin/sleep 10` in the service file should fix this. If it persists, increase the sleep value.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

MIT License — feel free to use, modify, and distribute.
