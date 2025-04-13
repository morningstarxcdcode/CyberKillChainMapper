import time
import os
import plotly.express as px
import pandas as pd
from reportlab.pdfgen import canvas

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

# Store event data for graph and report generation
event_data = []

def check_kill_chain_stage(line):
    for stage, keywords in kill_chain.items():
        if any(keyword.lower() in line.lower() for keyword in keywords):
            return stage.upper()
    return None

def assign_threat_level(event):
    if 'malware' in event.lower() or 'backdoor' in event.lower():
        return 5  # High threat
    elif 'usb' in event.lower() or 'email' in event.lower():
        return 3  # Medium threat
    else:
        return 1  # Low threat

def generate_pdf(data):
    pdf_file_path = "threat_report.pdf"
    if os.path.exists(pdf_file_path):
        os.remove(pdf_file_path)  # Overwrite the file if it exists
    c = canvas.Canvas(pdf_file_path)
    y_position = 800
    for event in data:
        c.drawString(100, y_position, f"{event['time']} - {event['event']} - Threat Level: {event['threat_level']}")
        y_position -= 20
    c.save()

def generate_csv(data):
    csv_file_path = "threat_report.csv"
    df = pd.DataFrame(data)
    df.to_csv(csv_file_path, index=False)

def update_timeline_graph(data):
    df = pd.DataFrame(data)
    fig = px.scatter(
        df, 
        x='time', 
        y='threat_level', 
        color='threat_level', 
        color_continuous_scale='reds', 
        title="Threat Event Timeline",
        labels={'threat_level': 'Threat Level'}
    )
    fig.update_traces(
        marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')),
        text=df['event'], 
        textposition='top center'
    )
    fig.show()

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
            event_time = time.strftime("%Y-%m-%d %H:%M:%S")
            threat_level = assign_threat_level(line)
            event_data.append({'time': event_time, 'event': line.strip(), 'threat_level': threat_level})

            print(f"[⚠️  {stage_detected}] - Suspicious activity: {line.strip()}")

            # Generate reports and update graph after every 10 events
            if len(event_data) % 10 == 0:
                generate_csv(event_data)
                generate_pdf(event_data)
                update_timeline_graph(event_data)
