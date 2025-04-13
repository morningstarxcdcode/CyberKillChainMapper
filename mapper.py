# mapper.py

# Dummy logs for testing
logs = [
    "nmap scan detected",
    "payload.exe created",
    "phishing email sent",
    "payload executed",
    "backdoor installed",
    "C2 server communication started",
    "data exfiltration to external IP"
]

# Kill Chain Stages
kill_chain = {
    "recon": ["nmap", "reconnaissance", "scan"],
    "weaponize": ["payload", "exploit builder"],
    "deliver": ["email", "usb", "sent"],
    "exploit": ["executed", "run", "clicked"],
    "install": ["installed", "backdoor", "setup"],
    "c2": ["C2", "command", "control", "server"],
    "action": ["data exfiltration", "steal", "delete"]
}

# Check each log line for stage
for log in logs:
    for stage, keywords in kill_chain.items():
        if any(keyword.lower() in log.lower() for keyword in keywords):
            print(f"[ALERT] Stage Detected: {stage.upper()} --> {log}")
