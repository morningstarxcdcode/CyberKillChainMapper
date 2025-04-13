# live_mapper.py

import time

log_file_path = "/var/log/system.log"  # Mac system log file

# Kill Chain Stages
kill_chain = {
    "recon": ["nmap", "scan", "recon"],
    "weaponize": ["payload", "exploit builder"],
    "deliver": ["email", "usb", "attachment"],
    "exploit": ["executed", "malware", "run"],
    "install": ["backdoor", "installed", "setup"],
    "c2": ["C2", "command", "server"],
    "action": ["exfiltration", "steal", "delete", "data"]
}

def check_kill_chain_stage(line):
    for stage, keywords in kill_chain.items():
        if any(keyword.lower() in line.lower() for keyword in keywords):
            return stage.upper()
    return None

print("🛡️ Cyber Kill Chain Mapper (LIVE MODE)...")
print("📡 Scanning Mac system logs for threats...\n")

# Tail the log file
with open(log_file_path, "r") as file:
    # Go to the end of the file
    file.seek(0, 2)

    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue

        stage_detected = check_kill_chain_stage(line)
        if stage_detected:
            print(f"[⚠️  {stage_detected}] - Suspicious activity: {line.strip()}")
