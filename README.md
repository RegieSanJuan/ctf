# � CTF Solutions Arsenal

<div align="center">

![CTF Banner](https://img.shields.io/badge/CTF-Solutions-brightgreen?style=for-the-badge&logo=hackaday&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-FF6B6B?style=for-the-badge&logo=shield&logoColor=white)

**🎯 Elite collection of Capture The Flag challenge solutions and exploits**

[![GitHub Stars](https://img.shields.io/github/stars/RegieSanJuan/ctf?style=social)](https://github.com/RegieSanJuan/ctf)
[![GitHub Forks](https://img.shields.io/github/forks/RegieSanJuan/ctf?style=social)](https://github.com/RegieSanJuan/ctf)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 🎮 Challenge Categories

<div align="center">

| 🛡️ **PWN**       | 🔐 **CRYPTO**  | 🔍 **REVERSE**  | 🌐 **WEB**   | 🔧 **MISC**       |
| ---------------- | -------------- | --------------- | ------------ | ----------------- |
| Buffer Overflows | AES Decryption | Binary Analysis | PHP Exploits | Protocol Analysis |
| ROP Chains       | XOR Cipher     | ELF Reversing   | Hash Bypass  | Format Strings    |
| Stack Exploits   | Custom Crypto  | Obfuscation     | Web Shells   | Memory Dumps      |

</div>

---

## 🏆 Featured Challenges

<table>
<tr>
<td width="50%">

### 💥 PWN Challenges

- **[Executable Stack](ctf/executable_stack.py)** - Classic buffer overflow with shellcode injection
- **[Non-Executable Stack](ctf/non_executable.py)** - ROP chain exploitation with libc leaks
- **[Hidden Flag Function](ctf/hidden_flag.py)** - Return-to-function exploit
- **[Heaped Notes](ctf/heaped_notes.py)** - Heap exploitation techniques

</td>
<td width="50%">

### 🔐 CRYPTO Challenges

- **[Encrypted Flag](ctf/encrypted_flag.py)** - AES-256-CBC brute force attack
- **[Flag Bootloader](ctf/flag_bootloader.py)** - XOR obfuscation reversal
- **[Encrypted Password](ctf/encrypted_password.py)** - XOR key recovery
- **[Predictable Vectors](ctf/predictable_vectors.py)** - Cryptographic oracle attack

</td>
</tr>
<tr>
<td width="50%">

### 🔍 REVERSE ENGINEERING

- **[Hidden Flag Function](ctf/hidden_flag_function)** - Binary analysis and function discovery
- **[Angr-y Binary](ctf/angr-y.py)** - Automated binary analysis with angr framework
- **[Magic Bytes](ctf/magic.py)** - File format analysis and extraction

</td>
<td width="50%">

### 🌐 WEB & MISC

- **[Compare The Pair](ctf/pair.php)** - PHP hash collision exploit
- **[Custom Protocol](ctf/custom_protocol.py)** - Network protocol analysis
- **[Heartbleed PoC](ctf/heartbleed-PoC/)** - OpenSSL vulnerability exploitation
- **[Environment Read](ctf/confused_environment_read.py)** - Format string vulnerability

</td>
</tr>
</table>

---

## �️ Tech Stack & Tools

<div align="center">

![Pwntools](https://img.shields.io/badge/Pwntools-FF6B6B?style=flat-square&logo=python&logoColor=white)
![Ghidra](https://img.shields.io/badge/Ghidra-4CAF50?style=flat-square&logo=ghost&logoColor=white)
![GDB](https://img.shields.io/badge/GDB-2196F3?style=flat-square&logo=gnu&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square&logo=burpsuite&logoColor=white)

</div>

### � Core Dependencies

```bash
pip install pwntools cryptography requests angr
```

---

## � Quick Start

<details>
<summary><b>🔥 Click to expand setup instructions</b></summary>

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/RegieSanJuan/ctf.git
cd ctf
```

### 2️⃣ Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install system tools (Ubuntu/Debian)
sudo apt-get install gdb radare2 binutils
```

### 3️⃣ Run a Challenge

```bash
cd ctf
python3 executable_stack.py
```

</details>

---

## 📊 Statistics

<div align="center">

| **Metric**             | **Count** |
| ---------------------- | --------- |
| 🎯 Total Challenges    | **25+**   |
| 💥 PWN Exploits        | **8**     |
| 🔐 Crypto Solutions    | **6**     |
| 🔍 Reverse Engineering | **5**     |
| 🌐 Web Exploits        | **3**     |
| 🔧 Miscellaneous       | **3**     |

</div>

---

## 🎓 Learning Resources

<div align="center">

[![PWN](https://img.shields.io/badge/Learn-PWN-red?style=for-the-badge)](https://pwn.college/)
[![Crypto](https://img.shields.io/badge/Learn-Cryptography-blue?style=for-the-badge)](https://cryptohack.org/)
[![Reverse](https://img.shields.io/badge/Learn-Reversing-green?style=for-the-badge)](https://challenges.re/)

</div>

---

## 🤝 Contributing

<div align="center">

**Found a bug? Have a new exploit? Want to improve documentation?**

[![Contribute](https://img.shields.io/badge/Contribute-Now-brightgreen?style=for-the-badge&logo=github)](CONTRIBUTING.md)
[![Issues](https://img.shields.io/badge/Report-Issues-red?style=for-the-badge&logo=github)](https://github.com/RegieSanJuan/ctf/issues)
[![Discussions](https://img.shields.io/badge/Join-Discussions-purple?style=for-the-badge&logo=github)](https://github.com/RegieSanJuan/ctf/discussions)

</div>

---

## ⚠️ Disclaimer

<div align="center">

> **🔒 Educational Purpose Only**
>
> These tools and exploits are provided for educational purposes and authorized security testing only.
> The author is not responsible for any misuse or damage caused by these tools.
>
> Always ensure you have proper authorization before testing on any systems.

</div>

---

<div align="center">

### 📫 Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RegieSanJuan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/RegieSanJuan)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/RegieSanJuan)

---

**⭐ Star this repository if you found it helpful!**

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=RegieSanJuan.ctf)

</div>
