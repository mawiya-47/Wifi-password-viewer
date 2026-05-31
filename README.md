<h1 align="center">📶 WiFi Password Viewer</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Ethical-Hacking-red?style=for-the-badge"/>
</p>

<p align="center">
  A simple yet powerful Python tool to view all saved WiFi passwords on your own device. 🔐
</p>

---

## 🚀 Features

- ✅ Works on **Windows, Linux, and macOS**
- ✅ Shows **all saved WiFi networks** with their passwords
- ✅ Clean tabular output — easy to read
- ✅ Zero dependencies — uses only Python standard library
- ✅ Lightweight & fast

---

## 📸 Preview

```
📶 WiFi Password Viewer — Windows
========================================
SSID                           PASSWORD
-------------------------------------------------------
MyHomeWiFi                     password123
OfficeNetwork                  office@2024
PublicHotspot                  No Password / Open Network
```

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/mawiya-47/Wifi-password-viewer.git

# Navigate to folder
cd Wifi-password-viewer
```

No external libraries needed. Pure Python! 🐍

---

## ▶️ Usage

### Windows
```bash
python wifi_password_viewer.py
```
> ⚠️ Run **Command Prompt as Administrator** for best results.

### Linux
```bash
sudo python3 wifi_password_viewer.py
```
> ⚠️ `sudo` is required to read `/etc/NetworkManager/system-connections/`

### macOS
```bash
python3 wifi_password_viewer.py
```
> ⚠️ You may be prompted to allow **Keychain access**. Allow it to retrieve passwords.

---

## 🛠️ How It Works

| OS      | Method Used                                              |
|---------|----------------------------------------------------------|
| Windows | `netsh wlan show profile <name> key=clear`              |
| Linux   | Reads `/etc/NetworkManager/system-connections/` files   |
| macOS   | `security find-generic-password` via Keychain           |

---

## ⚖️ Disclaimer

> 🔴 This tool is made for **educational and ethical purposes only.**
> Use it **only on your own device** or with **explicit permission** of the device owner.
> Unauthorized access to networks or devices is **illegal** and punishable by law.
> The developer is **not responsible** for any misuse of this tool.

---

## 👨‍💻 Author

**mawiya-47**
- GitHub: [@mawiya-47](https://github.com/mawiya-47)

---

## ⭐ Support

Agar ye tool useful laga toh **Star ⭐** zaroor karo!
It motivates me to build more cool stuff. 🙌

---

<p align="center">Made with ❤️ in Python</p>
