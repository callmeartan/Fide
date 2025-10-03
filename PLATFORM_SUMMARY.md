# Platform-Specific Instructions Summary

Quick reference for running FIDE Player Data Extractor on different operating systems.

## 🪟 Windows Users

### Quick Start (3 Steps):

1. **Install Python from [python.org](https://python.org)**
   - ✅ Check "Add Python to PATH"
   - ✅ Check "tcl/tk and IDLE"

2. **Setup (First Time)**
   ```cmd
   cd C:\Path\To\Fide
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the GUI**
   - **Easiest:** Double-click `launch_gui.bat`
   - **Or:** `venv\Scripts\activate` then `python fide_gui.py`

📖 **Full Guide:** [WINDOWS_GUIDE.md](WINDOWS_GUIDE.md)  
📄 **Quick Reference:** [WINDOWS_QUICK_START.txt](WINDOWS_QUICK_START.txt)

---

## 🍎 macOS Users

### Quick Start (3 Steps):

1. **Install Python** (if not already installed)
   ```bash
   brew install python@3.13
   ```

2. **Install tkinter (Required for GUI)**
   ```bash
   brew install python-tk@3.13
   ```

3. **Setup**
   ```bash
   cd /path/to/Fide
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run the GUI**
   ```bash
   source venv/bin/activate
   python fide_gui.py
   # Or: ./launch_gui.sh
   ```

---

## 🐧 Linux Users

### Quick Start (Ubuntu/Debian):

1. **Install Python and tkinter**
   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-pip python3-venv python3-tk
   ```

2. **Setup**
   ```bash
   cd /path/to/Fide
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the GUI**
   ```bash
   source venv/bin/activate
   python fide_gui.py
   # Or: ./launch_gui.sh
   ```

### Fedora/RHEL:
```bash
sudo dnf install python3 python3-pip python3-tkinter
```

### Arch Linux:
```bash
sudo pacman -S python python-pip tk
```

---

## Common Commands (All Platforms)

### Activate Virtual Environment

| Platform | Command |
|----------|---------|
| Windows (cmd) | `venv\Scripts\activate.bat` |
| Windows (PowerShell) | `venv\Scripts\Activate.ps1` |
| macOS/Linux | `source venv/bin/activate` |

### Run Programs

```bash
# GUI (all platforms)
python fide_gui.py

# Interactive mode
python fide_extractor.py

# Batch from file
python extract_from_file.py input.txt output.xlsx

# Example script
python example_batch.py
```

### Deactivate Virtual Environment

```bash
deactivate  # Works on all platforms
```

---

## Troubleshooting by Platform

### Windows

| Issue | Solution |
|-------|----------|
| "python not recognized" | Reinstall with "Add to PATH" checked |
| "No module named tkinter" | Reinstall with "tcl/tk" checked |
| PowerShell execution policy | Run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |

### macOS

| Issue | Solution |
|-------|----------|
| GUI won't start | Install tkinter: `brew install python-tk@3.13` |
| "command not found: python" | Use `python3` instead |
| Permission denied | Run `chmod +x launch_gui.sh` |

### Linux

| Issue | Solution |
|-------|----------|
| GUI won't start | Install tkinter: `sudo apt-get install python3-tk` |
| "No module named pip" | Install pip: `sudo apt-get install python3-pip` |
| Permission denied | Run `chmod +x launch_gui.sh` |

---

## File Paths by Platform

### Windows
```
C:\Users\YourName\Desktop\Fide
C:\Users\YourName\Documents\Fide
```

### macOS
```
/Users/YourName/Desktop/Fide
/Users/YourName/Documents/Fide
```

### Linux
```
/home/YourName/Desktop/Fide
/home/YourName/Documents/Fide
```

---

## Recommended Method by Platform

| Platform | Recommended |
|----------|-------------|
| **Windows** | Use `launch_gui.bat` (double-click) |
| **macOS** | Use `launch_gui.sh` or GUI from command line |
| **Linux** | Use `launch_gui.sh` or GUI from command line |

---

## Getting Help

- **Windows users:** See [WINDOWS_GUIDE.md](WINDOWS_GUIDE.md)
- **All users:** See [README.md](README.md)
- **Quick start:** See [START_HERE.md](START_HERE.md)
- **Examples:** See [QUICKSTART.md](QUICKSTART.md)

---

**The GUI works identically on all platforms once installed!**
