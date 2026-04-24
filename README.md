🔐 QuantumVault</h1>

<p align="center">
  <strong>Quantum-Grade Secure File Transfer System</strong>
</p>

<p align="center">
  A powerful, enterprise-grade file transfer application featuring multi-layer encryption, <br>
  a stunning cyberpunk-inspired UI, and military-grade security protocols.
</p>

---

## ✨ Features

### 🛡️ Multi-Layer Encryption
- **RSA-4096** - Asymmetric encryption for secure key exchange
- **AES-256-GCM** - Primary encryption layer with authenticated encryption
- **ChaCha20** - Secondary encryption layer for additional security
- **Blowfish** - Tertiary encryption layer for defense-in-depth

### 🎨 Premium UI/UX
- Modern dark cyberpunk-inspired theme
- Glassmorphism design elements
- Real-time status indicators with animations
- Responsive and intuitive interface
- Smooth hover effects and transitions

### 🚀 Core Capabilities
- **Secure File Transfer** - Send files with end-to-end encryption
- **Key Management** - Generate and manage RSA-4096 keypairs
- **Real-time Progress** - Live transfer progress tracking
- **Cross-Platform** - Works on Windows, Linux, and macOS
- **CLI & GUI** - Use command-line or graphical interface

---

## 📸 Screenshots

<p align="center">
  <i>Coming soon - Add your screenshots here!</i>
</p>

<!-- Uncomment and add your screenshots
<p align="center">
  <img src="screenshots/main-menu.png" alt="Main Menu" width="800">
</p>
-->

---

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Install

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/QuantumVault.git
   cd QuantumVault
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or run the installer script:
   ```bash
   python install.py
   ```

3. **Launch QuantumVault**
   ```bash
   # GUI Mode
   python gui.py
   
   # CLI Mode
   python Main.py
   ```

---

## 📖 Usage

### GUI Mode (Recommended)

Simply run `python gui.py` to launch the graphical interface.

#### Sending Files
1. Click **"Send File"** from the main menu
2. Enter the receiver's IP address and port
3. Select the file you want to send
4. The file will be encrypted and transferred securely

#### Receiving Files
1. Click **"Receive File"** from the main menu
2. Generate RSA keys if you haven't already
3. Enter a port number to listen on
4. Share your IP address with the sender
5. Wait for the incoming file

#### Key Management
1. Click **"Key Vault"** from the main menu
2. Generate new RSA-4096 keys
3. Keys are stored in the `keys/` directory

### CLI Mode

```bash
# Generate RSA keypair
python Main.py generate-keys --path keys

# Send a file
python Main.py send --server-ip 192.168.1.100 --server-port 8080 --file-path /path/to/file

# Receive a file
python Main.py receive --server-port 8080 --private-key-path keys

# Launch GUI from CLI
python Main.py gui
```

---

## 🔒 Security Architecture

QuantumVault implements a **defense-in-depth** approach with multiple encryption layers:

```
┌─────────────────────────────────────────────────────────────┐
│                    Original File Data                        │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: AES-256-GCM (Authenticated Encryption)            │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: ChaCha20 (Stream Cipher)                          │
├─────────────────────────────────────────────────────────────┤
│  Layer 3: Blowfish (Block Cipher)                           │
├─────────────────────────────────────────────────────────────┤
│  Key Exchange: RSA-4096 with OAEP Padding                   │
└─────────────────────────────────────────────────────────────┘
```

### Key Features:
- **Perfect Forward Secrecy** - New symmetric keys for each transfer
- **Authenticated Encryption** - AES-GCM provides integrity verification
- **Secure Key Exchange** - RSA-4096 ensures only the recipient can decrypt
- **No Key Logging** - Symmetric keys are never stored on disk

---

## 📁 Project Structure

```
QuantumVault/
├── Main.py              # Core encryption/decryption & CLI
├── gui.py               # Premium CustomTkinter GUI
├── install.py           # Dependency installer
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── keys/                # RSA keypair storage (generated)
    ├── private_key.pem
    └── public_key.pem
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| GUI Framework | CustomTkinter |
| Cryptography | `cryptography` library |
| Networking | Python `socket` |
| CLI | `argparse` |
| UI Enhancements | `rich`, `colorama`, `tqdm` |

---

## 📋 Requirements

```
customtkinter
cryptography
rich
tqdm
colorama
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⚠️ Disclaimer

This software is provided for educational and legitimate security purposes only. The developers are not responsible for any misuse of this software. Always ensure you have proper authorization before transferring files over networks.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)

---

<p align="center">
  <strong>🔐 QuantumVault - Where Security Meets Elegance</strong>
</p>

<p align="center">
  Made with ❤️ and lots of encryption
</p>
