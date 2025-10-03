# Python Installation Guide for Windows

Complete step-by-step guide to install Python on Windows for FIDE Extractor.

## Step 1: Download Python

1. **Open your web browser** (Chrome, Edge, Firefox, etc.)

2. **Go to:** [https://www.python.org/downloads/](https://www.python.org/downloads/)

3. **Click the big yellow button** that says:
   ```
   Download Python 3.x.x
   ```
   (The version number (3.x.x) will be the latest, like 3.12.0 or 3.13.0)

4. **Save the file** when prompted
   - The file will be named something like: `python-3.12.0-amd64.exe`
   - It will download to your Downloads folder

---

## Step 2: Run the Installer

1. **Find the downloaded file:**
   - Open **File Explorer** (Windows key + E)
   - Go to **Downloads** folder
   - Look for `python-3.x.x-amd64.exe`

2. **Double-click** the installer to run it

3. **If you see "User Account Control" dialog:**
   - Click **"Yes"** to allow the installer to make changes

---

## Step 3: Installation Screen - CRITICAL STEP!

You'll see the Python installer window. **THIS IS THE MOST IMPORTANT PART!**

### ⚠️ BEFORE clicking "Install Now":

**At the BOTTOM of the window, you'll see two checkboxes:**

```
┌─────────────────────────────────────────────────┐
│  Install Python 3.x.x (64-bit)                  │
│                                                 │
│  [Install Now]  (Recommended)                   │
│   Python will be installed for all users...     │
│                                                 │
│  [Customize installation]                       │
│                                                 │
│  ☐ Use admin privileges when installing...     │
│  ☐ Add python.exe to PATH                      │  ← CHECK THIS!
└─────────────────────────────────────────────────┘
```

### ✅ MUST DO:

**Check the box at the bottom:**
- ☑️ **"Add python.exe to PATH"** or **"Add Python to PATH"**

**This is CRITICAL!** If you don't check this, Python won't work from command line.

---

## Step 4: Choose Installation Type

You have two options:

### Option A: Install Now (Recommended for Most Users)

1. After checking "Add Python to PATH"
2. Click **"Install Now"**
3. Wait for installation (takes 2-5 minutes)
4. ✅ **SKIP to Step 6**

### Option B: Customize Installation (If you want to ensure tcl/tk)

1. After checking "Add Python to PATH"
2. Click **"Customize installation"**
3. Proceed to Step 5

---

## Step 5: Customize Installation (Optional Features)

If you chose "Customize installation", you'll see optional features:

### Screen 1: Optional Features

```
┌─────────────────────────────────────────────────┐
│  Optional Features                              │
│                                                 │
│  ☑ Documentation                                │
│  ☑ pip                                          │  ← KEEP CHECKED
│  ☑ tcl/tk and IDLE                             │  ← MAKE SURE CHECKED
│  ☑ Python test suite                           │
│  ☑ py launcher                                  │
│  ☑ for all users (requires admin privileges)   │
│                                                 │
│              [Next]                             │
└─────────────────────────────────────────────────┘
```

**Important boxes to check:**
- ☑️ **pip** (should be checked by default)
- ☑️ **tcl/tk and IDLE** (REQUIRED for GUI!)
- ☑️ py launcher (recommended)

Click **"Next"**

### Screen 2: Advanced Options

```
┌─────────────────────────────────────────────────┐
│  Advanced Options                               │
│                                                 │
│  ☑ Install for all users                       │
│  ☑ Associate files with Python                 │
│  ☑ Create shortcuts for installed applications │
│  ☑ Add Python to environment variables         │  ← CHECK THIS
│  ☐ Precompile standard library                 │
│  ☐ Download debugging symbols                  │
│                                                 │
│  Customize install location:                   │
│  C:\Program Files\Python3x\                    │
│                                                 │
│              [Install]                          │
└─────────────────────────────────────────────────┘
```

**Make sure checked:**
- ☑️ **Add Python to environment variables** (CRITICAL!)
- ☑️ Install for all users (recommended)

Click **"Install"**

---

## Step 6: Installation Progress

You'll see a progress bar:
```
Installing Python 3.x.x (64-bit)
[████████████████████░░░░] 80%
```

Wait for it to complete (usually 2-5 minutes).

---

## Step 7: Installation Complete

When done, you'll see:
```
Setup was successful

Special thanks to Mark Hammond, without whose years of
freely shared work this installer would be much less capable.

Disable path length limit

[Close]
```

### Optional but Recommended:

Click **"Disable path length limit"** if you see this option.
- This removes Windows' 260 character path limit
- Requires administrator privileges
- Not critical but helpful

Then click **"Close"**

---

## Step 8: Verify Installation

Now let's make sure Python installed correctly:

### Test 1: Open Command Prompt

1. Press **Windows key** (on keyboard)
2. Type: **cmd**
3. Press **Enter**

You'll see a black window (Command Prompt)

### Test 2: Check Python Version

In the Command Prompt, type:
```cmd
python --version
```

Press **Enter**

**Expected result:**
```
Python 3.12.0
```
(or whatever version you installed)

**If you see this:** ✅ SUCCESS! Python is installed correctly!

**If you see "python is not recognized":** ❌ See Troubleshooting below

### Test 3: Check pip

Type:
```cmd
pip --version
```

Press **Enter**

**Expected result:**
```
pip 23.x.x from C:\... (python 3.12)
```

**If you see this:** ✅ pip is working!

---

## ✅ Installation Checklist

Before proceeding, verify:

- ☑️ Python installed
- ☑️ `python --version` works in Command Prompt
- ☑️ `pip --version` works in Command Prompt
- ☑️ "Add to PATH" was checked during installation
- ☑️ "tcl/tk and IDLE" was included

If all checked, **YOU'RE READY!** Proceed to install FIDE Extractor.

---

## 🔧 Troubleshooting

### Problem: "python is not recognized as an internal or external command"

**Cause:** Python was not added to PATH during installation.

**Solution:**

#### Quick Fix (Reinstall):
1. Go to Control Panel → Programs → Uninstall a program
2. Find Python 3.x.x and uninstall it
3. Go back to Step 1 of this guide
4. **MAKE SURE** to check "Add Python to PATH" this time!

#### Advanced Fix (Add PATH manually):
1. Press **Windows key**
2. Type **"environment variables"**
3. Click **"Edit the system environment variables"**
4. Click **"Environment Variables..."** button
5. Under "System variables", find **"Path"**
6. Click **"Edit..."**
7. Click **"New"**
8. Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python3x\`
9. Click **"New"** again
10. Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python3x\Scripts\`
11. Click **"OK"** on all windows
12. **Close and reopen Command Prompt**
13. Try `python --version` again

### Problem: GUI doesn't work / "No module named tkinter"

**Cause:** tcl/tk was not installed.

**Solution:**
1. Uninstall Python
2. Reinstall Python
3. Choose **"Customize installation"**
4. Make sure **"tcl/tk and IDLE"** is checked
5. Complete installation

### Problem: "Access Denied" during installation

**Cause:** Installer needs administrator rights.

**Solution:**
1. Right-click the Python installer
2. Choose **"Run as administrator"**
3. Click **"Yes"** when prompted
4. Follow installation steps again

---

## 🎯 Quick Summary

**TL;DR Version:**

1. Download from python.org
2. Run installer
3. ✅ **CHECK "Add Python to PATH"** (bottom of window)
4. Choose "Customize installation"
5. ✅ **CHECK "tcl/tk and IDLE"**
6. Click through and install
7. Test with `python --version` in Command Prompt

**That's it!**

---

## 📹 Visual Guide

Can't find the checkboxes? Look for:

**Main installer screen (FIRST screen you see):**
```
┌──────────────────────────────────────┐
│ Install Python 3.12                  │
│                                      │
│ [Install Now]                        │
│                                      │
│ [Customize installation]             │
│                                      │
│ ☐ Install launcher for all users    │
│ ☑ Add python.exe to PATH     ← THIS!│
└──────────────────────────────────────┘
```

The "Add Python to PATH" checkbox is at the **very bottom** of the installer window, below the "Install Now" and "Customize installation" buttons.

---

## 🔜 Next Steps

After Python is installed:

1. **Close this guide**
2. **Open:** `WINDOWS_GUIDE.md` or `WINDOWS_QUICK_START.txt`
3. **Follow:** Setup instructions to install FIDE Extractor
4. **Run:** `launch_gui.bat`

---

## 💡 Pro Tips

- **Python 3.12 or 3.13** is recommended (latest stable version)
- **64-bit version** is recommended (should download automatically)
- **Don't install from Microsoft Store** - use python.org instead
- **Keep Python updated** - new versions fix bugs and security issues

---

**Once Python is installed, you never have to do this again!**

Ready to continue? See [WINDOWS_GUIDE.md](WINDOWS_GUIDE.md) for next steps.

