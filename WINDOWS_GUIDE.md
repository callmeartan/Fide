# Windows Installation and Usage Guide

Complete guide for running FIDE Player Data Extractor on Windows.

## Prerequisites

### 1. Install Python

**Need help installing Python?** → See [WINDOWS_PYTHON_INSTALLATION.md](WINDOWS_PYTHON_INSTALLATION.md) for detailed step-by-step guide with screenshots explained.

**Quick version:**

1. Download Python 3.8 or higher from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **CRITICAL:** At the bottom of the first screen, check:
   - ✅ **Add Python to PATH** (MUST CHECK!)
4. Choose "Customize installation" and make sure:
   - ✅ **pip** is checked
   - ✅ **tcl/tk and IDLE** is checked (required for GUI)
5. Complete installation

### 2. Verify Installation

Open **Command Prompt** (cmd) or **PowerShell** and run:

```cmd
python --version
```

Should show: `Python 3.x.x`

**If you see an error:** Python is not in PATH. See [WINDOWS_PYTHON_INSTALLATION.md](WINDOWS_PYTHON_INSTALLATION.md) for troubleshooting.

## Installation Steps

### Step 1: Download the Project

Either:
- Download and extract the ZIP file
- Or clone with Git: `git clone <repository-url>`

### Step 2: Open Command Prompt

1. Navigate to the project folder
2. Right-click in the folder → "Open in Terminal" or "Open PowerShell window here"

Or manually:
```cmd
cd C:\Path\To\Fide
```

### Step 3: Create Virtual Environment

```cmd
python -m venv venv
```

This creates a `venv` folder in your project directory.

### Step 4: Activate Virtual Environment

**For Command Prompt (cmd):**
```cmd
venv\Scripts\activate.bat
```

**For PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

**Note:** If PowerShell shows an error about execution policy, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

You should see `(venv)` at the beginning of your command line.

### Step 5: Install Dependencies

```cmd
pip install -r requirements.txt
```

Wait for all packages to install.

## Running the Application

### Method 1: Using the Batch Launcher (Easiest)

Simply double-click:
```
launch_gui.bat
```

### Method 2: Command Line

**Step 1:** Open Command Prompt/PowerShell in the project folder

**Step 2:** Activate virtual environment:
```cmd
venv\Scripts\activate
```

**Step 3:** Launch GUI:
```cmd
python fide_gui.py
```

### Method 3: Command Line Tools

**Interactive extractor:**
```cmd
venv\Scripts\activate
python fide_extractor.py
```

**Batch from file:**
```cmd
venv\Scripts\activate
python extract_from_file.py players_input.txt output.xlsx
```

## Quick Reference

### Always Activate Virtual Environment First!

Before running any Python script:

**Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

**PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

### Common Commands

```cmd
# Launch GUI
python fide_gui.py

# Interactive mode
python fide_extractor.py

# Batch processing
python extract_from_file.py input.txt output.xlsx

# Example script
python example_batch.py
```

### Deactivate Virtual Environment

When done:
```cmd
deactivate
```

## Troubleshooting

### Issue 1: "python is not recognized"

**Problem:** Python not in PATH

**Solution:**
1. Uninstall Python
2. Reinstall from python.org
3. ✅ Check "Add Python to PATH" during installation

### Issue 2: "No module named 'tkinter'"

**Problem:** Tkinter not installed

**Solution:**
1. Uninstall Python
2. Reinstall with "tcl/tk and IDLE" option checked

### Issue 3: PowerShell execution policy error

**Problem:** Can't run activation script

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Or use Command Prompt instead of PowerShell.

### Issue 4: "pip is not recognized"

**Problem:** pip not installed or not in PATH

**Solution:**
```cmd
python -m pip install --upgrade pip
```

Or reinstall Python with pip option checked.

### Issue 5: Module import errors

**Problem:** Dependencies not installed

**Solution:**
```cmd
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue 6: Virtual environment not activating

**Problem:** Wrong activation command

**Solutions:**

**If using Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

**If using PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

**If still not working:**
```cmd
python -m venv venv --clear
venv\Scripts\activate
pip install -r requirements.txt
```

## File Paths in Windows

Use backslashes `\` or forward slashes `/`:

```cmd
# Both work:
python extract_from_file.py players_input.txt output.xlsx
python extract_from_file.py C:\Users\YourName\Desktop\players.txt C:\Users\YourName\Desktop\output.xlsx
```

## Creating Desktop Shortcut

1. Right-click `launch_gui.bat`
2. Send to → Desktop (create shortcut)
3. Double-click desktop shortcut to launch

## Updating the Application

If you get new code updates:

```cmd
cd C:\Path\To\Fide
venv\Scripts\activate
pip install -r requirements.txt --upgrade
```

## Performance Notes

On Windows:
- First run may be slower (Windows Defender scanning)
- Add project folder to Windows Defender exclusions for better performance
- GUI works best on Windows 10/11

## Alternative: Using Windows Terminal

Windows Terminal (recommended for Windows 11):

1. Install from Microsoft Store
2. Open Windows Terminal
3. Navigate to project folder
4. Run commands as shown above

## Need Help?

Common Windows paths:
- Desktop: `C:\Users\YourName\Desktop\Fide`
- Downloads: `C:\Users\YourName\Downloads\Fide`
- Documents: `C:\Users\YourName\Documents\Fide`

## Video Tutorial Steps

1. **Install Python** from python.org (check "Add to PATH")
2. **Download project** to Desktop or Documents
3. **Open folder** in File Explorer
4. **Shift + Right-click** → "Open PowerShell window here"
5. **Run commands:**
   ```powershell
   python -m venv venv
   venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python fide_gui.py
   ```

## Batch File Contents

The `launch_gui.bat` file contains:

```batch
@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
python fide_gui.py
pause
```

You can customize this if needed.

## Uninstallation

To remove:

1. Close all Python/GUI windows
2. Delete the project folder
3. No registry changes needed
4. Optional: Uninstall Python from Control Panel

---

**For the best experience on Windows, use the `launch_gui.bat` file!**

