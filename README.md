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

2. Change directory to python_fastport_Scanner
    ```sh
    cd python_fastport_Scanner 
    ```

3. Install required modules
    ```sh 
    pip install -r requirements.txt 
    ```

## Usage

    
    python port_scanner.py -i [TARGET] -s [START_PORT] -e [END_PORT] [-t THREADS]
    

Arguments
* -i, --target: Target IP or domain to scan (required).
* -s, --start: Start port number (required).
* -e, --end: End port number (required).
* -t, --threads: Number of threads to use (optional, default is 10).


1. Example
    ```sh
    python port_scanner.py -i example.com -s 1 -e 65535 -t 20
    ```

### creator - pentesterkaran