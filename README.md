# EICAR Test File Generator 🚀

This repository provides a script to generate **EICAR test files** of exactly **68 KB** in various formats:
- 📄 **TXT**
- 📝 **PDF**
- 📊 **XLS/XLSX**
- 📦 **ZIP**

## 🎯 Purpose & Applications
- ✅ **Antivirus detection testing**
- 🔍 **Security research & malware simulations**
- 🌐 **Network monitoring validation**
- 🔒 **CSP & file restriction testing**

## 🛠 Installation
Before running the script, install the required dependencies:
```bash
pip install fpdf pandas openpyxl xlwt
```

## 🚀 Usage
1. **Run the script**:
   ```bash
   python3 generate_eicar_file.py
   ```
2. **Choose the format in which the 68 KB EICAR test file should be generated:**
   ```
   1. txt
   2. pdf
   3. xls
   4. xlsx
   5. zip
   ```
3. **Enter the number (1-5) for format selection.**

## 📏 File Size Verification
To verify the file size in Linux:
```bash
ls -lh eicar_test_68kb.*
```
Or use `stat`:
```bash
stat eicar_test_68kb.*
```

## 📜 About the EICAR Test File
Any antivirus product supporting the **EICAR test file** should detect it in any file that starts with the **first 68 characters** and has a total length of **exactly 68 bytes**:
```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```
The first 68 characters form the known string. It may be optionally appended by any combination of whitespace characters, with the total file length not exceeding 128 characters.

🔗 **Reference:** [EICAR Official Website](https://www.eicar.org/download-anti-malware-testfile/)

## 📄 License
This project is released under the **MIT License**.

---




