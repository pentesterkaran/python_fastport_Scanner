# python_fastport_Scanner

# 🔍 Port Scanner

Welcome to the **Port Scanner** project! This tool is designed to scan and identify open ports on a given IP address or domain, making it a useful tool for network administrators and security enthusiasts.

## ✨ Features

- 📝 **Target Specification**: Scan specific IPs or domains.
- 🚀 **Port Range**: Define a range of ports to scan.
- ⚡ **Multithreading**: Speed up the scanning process with multiple threads.
- 💾 **Result Logging**: Save open ports to a text file.

## 🛠️ Installation

To use this tool, you'll need Python installed on your machine. Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/pentesterkaran/python_fastport_Scanner.git

```bash 
    cd python_fastport_Scanner


``` pip install -r requirements.txt ```

python port_scanner.py -i [TARGET] -s [START_PORT] -e [END_PORT] [-t THREADS]

python port_scanner.py -i example.com -s 1 -e 65535 -t 20
