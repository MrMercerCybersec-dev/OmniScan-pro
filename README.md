# OmniScan-Pro v2.0

             >> Autonomous Multi-Language Security Orchestrator <<

---

### 🌐 Overview
**OmniScan-Pro** is an advanced, multi-language security orchestration platform. It unifies professional network infrastructure mapping with low-level system forensics and an air-gapped local AI pipeline (`Ollama`/`Llama3`). 

---
### ⚠️ Legal & Ethical Disclaimer
This software framework is engineered solely for academic research, defensive posture validation, and authorized network penetration auditing.
---
             >> Autonomous Multi-Language Security Orchestrator <<
### 🌐 Overview
**OmniScan-Pro** is an advanced, multi-language security orchestration platform. It unifies professional network infrastructure mapping with low-level system forensics and an air-gapped local AI pipeline (`Ollama`/`Llama3`). 

By processing high-overhead telemetry collection through native, compiled subsystems, it ensures absolute **Data Sovereignty** and local data integrity during critical infrastructure audits.

---

### 🏗️ Polyglot Architecture & Module Breakdown

| Module | Engine Language | Operational Layer | Functional Objective |
| :--- | :--- | :--- | :--- |
| **Core & UX** | `Python 3` | User / Logic Layer | Manages Tkinter GUI / Argparse CLI & coordinates local Ollama LLM strings. |
| **Tracer** | `Go` | Network Layer | High-speed concurrent DNS routing & GeoIP metadata ingestion. |
| **Forensics** | `C` | OS Kernel / POSIX | Native high-speed pattern matching across system authentication audit streams. |

---

### 🚀 Key Capabilities

* **Air-Gapped Core Intelligence:** Leverages local LLMs to parse multi-tool security outputs, preventing telemetry exposure to third-party cloud APIs.
* **Active Boundary Profiling:** Automated service discovery via `Nmap` integrated with the `vulners` script assessment database.
* **Web Application Auditing:** Out-of-the-box configuration checking and server vulnerability mining via `Nikto`.
* **Infrastructure Geolocation:** Deep DNS boundary resolution paired with autonomous network routing tracing.
* **System Integrity Verification:** Real-time log scraping targeting brute-force footprints and authorization anomalies.

---

### 🛠️ Quick Build & Compilation Chain

#### 1. Native Environment Prep
Install the necessary system compilers and core network binaries:
```bash
sudo apt update && sudo apt install git python3 nmap nikto whois gcc golang -y

curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
ollama pull llama3
git clone [https://github.com/MrMercerCybersec-dev/omniscan-pro.git](https://github.com/MrMercerCybersec-dev/omniscan-pro.git)
cd omniscan-pro

# Install dependencies
pip install -r requirements.txt

# Compile native engines
go build -o tracer tracer.go
gcc -o forensics forensics.c
chmod +x tracer forensics


```GUI access
sudo python3 omniscan_pro.py
```CLI access
sudo python3 omniscan_pro.py --cli --target yourtarget.com
