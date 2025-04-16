

---

# 🛡️ **Cyber Kill Chain Mapper V2 - LIVE Threat Tracker (MacOS)** 🚨🕹️

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org)  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  
[![Platform](https://img.shields.io/badge/platform-MacOS-lightgrey.svg)](https://www.apple.com/macos/)  
[![Status](https://img.shields.io/badge/status-LIVE-red.svg)](https://github.com/morningstarxcdcode/CyberKillChainMapperV2)

> ⚔️ **Track, analyze, and defend against cyber threats in real-time with the Cyber Kill Chain model. Graphs, reports, and live monitoring – all at your fingertips.**

---

## 🚀 **Project Overview**

Welcome to **CyberKillChainMapperV2** – the ultimate **LIVE security monitoring tool** for MacOS that tracks suspicious activities on your system and maps them to **Cyber Kill Chain** stages. 

- 🚨 **LIVE Threat Tracking**: Detects and logs security events in real-time.
- 🧠 **Advanced Threat Analysis**: Maps events to Cyber Kill Chain stages and assigns severity scores (1-5).
- 📊 **Dynamic Timeline Graphs**: Visualizes detected events and threat levels.
- 📝 **Automated Reports**: Generates detailed **PDF** and **CSV** reports every 10 events.
- 🛠️ **Built for Live Security Monitoring**: Perfect for analysts and cybersecurity professionals.

---

## 🔐 **Cyber Kill Chain Detection Stages**

| **Stage**    | **Keywords Tracked**                                      |
|--------------|-----------------------------------------------------------|
| **Recon**    | `nmap`, `scan`, `recon`, `shodan`, `portscan`              |
| **Weaponize**| `payload`, `exploit`, `builder`, `dropper`                 |
| **Deliver**  | `email`, `usb`, `attachment`, `phishing`                   |
| **Exploit**  | `executed`, `malware`, `run`, `vulnerable`, `exploit`      |
| **Install**  | `backdoor`, `installed`, `setup`, `rat`                    |
| **C2**       | `C2`, `command`, `server`, `callback`, `control`           |
| **Action**   | `exfiltration`, `steal`, `delete`, `data`, `destroy`       |

---

## 📷 **Real-Time LIVE Timeline Graph** 📈

Visualize your system’s security in **real-time** with an interactive **Plotly Timeline Graph** that updates every 10 detected events. 

- **X-axis**: Time of detected events ⏳
- **Y-axis**: Threat Level 🛑
- **Color Scale**: Red 🔴 indicates higher severity and criticality.

Here’s how it looks:

<div align="center">
  <img src="https://media.giphy.com/media/26tPuwD3EZZ8HLoTY/giphy.gif" alt="Dynamic Timeline Graph Animation" width="600px">
  <em>Watch the action unfold with live threat tracking!</em>
</div>

---

## 🛠️ **Built With**

- 🐍 **Python 3.13** – The power behind the code.
- 📊 **Plotly** – Dynamic data visualization and interactive timeline graphs.
- 📄 **ReportLab** – Automated PDF and CSV reports for every 10 detected events.
- 🐼 **Pandas** – Efficient data handling and manipulation.
- 🖥️ **Terminal-based Real-time Monitoring** – Lightweight and fast with live event tracking.

---

## ⚙️ **How to Run**

Set up and launch **CyberKillChainMapperV2** on your MacOS system:

```bash
# 1. Activate your virtual environment (make sure it's already created)
source venv/bin/activate

# 2. Navigate to the project directory
cd v2_real_time/

# 3. Run the main script to start monitoring
python live_mapper.py
```

---

## 💡 **How to Contribute**

This project thrives on contributions from the community! If you want to improve the project, here’s how you can contribute:

1. **Fork the repository** to your own GitHub account.
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/your-username/CyberKillChainMapperV2.git
   ```
3. **Create a new feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make changes** and commit them:
   ```bash
   git commit -am 'Add new feature'
   ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a pull request** to merge your changes with the main repository.

---

## 📦 **Example Output**

- **Live Event Detection**:
  ```bash
  [INFO] Detecting suspicious activities...
  [EVENT 1] Recon stage detected: nmap scan on port 80.
  [EVENT 2] Exploit stage detected: malware executed.
  [EVENT 3] Install stage detected: backdoor installed.
  [GRAPH] Plotting live timeline graph...
  ```

- **PDF/CSV Report Generation**:
  After every 10 detected events, a **PDF** and **CSV** report will automatically generate and be saved in the `/reports` directory.

---

## 🖼️ **Screenshots & Visuals**

Take a look at the live demo!

<div align="center">
  <img src="https://media.giphy.com/media/l3q2t08x6ttVZlsZy/giphy.gif" alt="Real-Time Threat Timeline" width="600px">
  <em>Detecting threats and analyzing events in real time!</em>
</div>

---

## 🔥 **Why CyberKillChainMapperV2?**

- **Real-Time Monitoring**: This tool doesn’t just track past events – it continuously watches your system for new threats in real-time, providing **live updates** and instant alerts.
- **Kill Chain Mapping**: It maps suspicious activities directly to the **Cyber Kill Chain stages**, giving you a structured approach to threat analysis.
- **Automatic Reporting**: No need to manually generate reports. Every 10 events, this tool auto-generates detailed reports for you.
- **Complete Security**: From **reconnaissance** to **data exfiltration**, this tool provides a **comprehensive security solution** for your MacOS system.

---

## 📜 **License**

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for more details.

---

## 🤝 **Acknowledgements**

- **Plotly** – For their amazing data visualization tools.
- **ReportLab** – For making automated PDF and CSV generation possible.
- **Pandas** – For fast and efficient data management.
- **Cyber Kill Chain** – The ultimate model for understanding and mapping cyber attack methodologies.

---


## 🚨 **Support**

If you encounter any issues, have questions, or need help with setup, please **open an issue** in the GitHub repository, and I’ll get back to you as soon as possible!

--- 
