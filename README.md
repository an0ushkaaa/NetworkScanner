# 🔍 Network Scanner CLI

A powerful yet minimal command-line tool to scan your local network, identify active devices, resolve hostnames, and detect open ports — built with Python.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## Features

- **Device Discovery** – Finds all active devices on your local network
- **Hostname Resolution** – Shows readable hostnames where available
- **Port Scanning** – Scans common ports to detect open services
- **CSV Export** – Saves scan results for later analysis
- Clean CLI interface with zero dependencies on fancy UIs


## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/network-scanner-cli.git
cd network-scanner-cli
````

2. **(Optional but recommended)** Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
.venv\Scripts\activate     # For Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the CLI tool with:

```bash
python cli.py
```

And follow the interactive prompts. That's it!

---

## 🛠 Built With

* [Python](https://www.python.org/) 3.11+
* [Scapy](https://scapy.net/) – For crafting packets
* `socket` and `csv` – Built-in Python modules

