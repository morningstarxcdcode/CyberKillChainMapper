# 🛡️ Cyber Kill Chain Mapper V2 - LIVE Threat Tracker (MacOS)

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-MacOS-lightgrey.svg)
![Status](https://img.shields.io/badge/status-LIVE-red.svg)

> ⚔️ **Track threats in real-time using the Cyber Kill Chain model. Graph + PDF/CSV reports auto-generated.**

---

## 🚀 Project Description

CyberKillChainMapperV2 is a **real-time log monitoring tool** built for MacOS that detects suspicious system events using keywords mapped to **Cyber Kill Chain stages** like Recon, Exploit, Install, etc.

- 🔴 Detects suspicious activities from `/var/log/system.log`
- 📍 Maps events to Kill Chain stages
- 🧠 Assigns threat levels (1 to 5)
- 📈 Auto generates **Timeline Graph**
- 🧾 Creates **PDF & CSV reports** every 10 events
- ⚡ Built for **Live Security Monitoring**

---

## 🔐 Cyber Kill Chain Detection Stages

| Stage        | Keywords Tracked                                  |
|--------------|---------------------------------------------------|
| Recon        | `nmap`, `scan`, `recon`                           |
| Weaponize    | `payload`, `exploit builder`                      |
| Deliver      | `email`, `usb`, `attachment`                      |
| Exploit      | `executed`, `malware`, `run`                      |
| Install      | `backdoor`, `installed`, `setup`                  |
| C2           | `C2`, `command`, `server`                         |
| Action       | `exfiltration`, `steal`, `delete`, `data`         |

---

## 📷 Live Timeline Graph

When 10 events are detected, a **Plotly Timeline Graph** will pop up:

- 📍 X-axis → Time
- 🔥 Y-axis → Threat Level
- 🟥 Red color scale based on severity

---

## 🛠️ Built With

- 🐍 Python 3.13
- 📊 Plotly
- 📄 ReportLab
- 🐼 Pandas
- 💻 Terminal-based Real-time Monitoring

---

## ⚙️ How to Run

```bash
# Activate your virtual environment first
source venv/bin/activate

# Make sure you're in the correct directory!
cd v2_real_time/

# Run the main script
python live_mapper.py
