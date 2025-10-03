# 🎯 START HERE - FIDE Player Data Extractor

Welcome! This guide will get you up and running in 5 minutes.

## ⚡ Quick Setup (Do This First)

### macOS/Linux:
```bash
# Navigate to the project folder
cd /path/to/Fide

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Windows:
```cmd
REM Navigate to the project folder
cd C:\Path\To\Fide

REM Create virtual environment
python -m venv venv

REM Activate it
venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt
```

**Or on Windows: Just double-click `launch_gui.bat`** (if venv already created)

✅ **Done!** You're ready to use the extractor.

## 🚀 Choose Your Method

### Option 1: GUI (Easiest) ⭐ RECOMMENDED

Perfect if you want a simple, visual interface:

```bash
python fide_gui.py
```

**What you get:**
- Pretty interface with buttons
- Visual table of results  
- Export to Excel, CSV, or JSON with one click
- No coding required!

👉 See `GUI_GUIDE.md` for detailed instructions

---

### Option 2: Command Line

Perfect if you prefer terminal/scripts:

**Interactive mode:**
```bash
python fide_extractor.py
```

**From a file:**
```bash
python extract_from_file.py players_input.txt output.xlsx
```

**Batch script:**
```bash
python example_batch.py
```

👉 See `QUICKSTART.md` for all command-line options

---

### Option 3: As a Python Module

Perfect if you're building your own application:

```python
from fide_extractor import FIDEDataExtractor

extractor = FIDEDataExtractor()
data = extractor.extract_multiple_players(['1503014', 'Magnus Carlsen'])
extractor.export_to_excel(data, 'output.xlsx')
```

👉 See `README.md` for API documentation

---

## 📂 File Guide

**Want to...**
- **Use the GUI?** → Run `python fide_gui.py` or see `GUI_GUIDE.md`
- **Quick start?** → Read `QUICKSTART.md`
- **Full documentation?** → Read `README.md`
- **Compare methods?** → Read `COMPARISON.md`
- **Use the API alternative?** → Check `fide_api_extractor.py`

**Core files:**
- `fide_extractor.py` - Main extraction engine (web scraping)
- `fide_gui.py` - Graphical user interface ⭐
- `fide_api_extractor.py` - API-based extractor (faster, IDs only)
- `extract_from_file.py` - Extract from text file
- `example_batch.py` - Example batch script

**Helper files:**
- `launch_gui.sh` - Launch GUI on Mac/Linux
- `launch_gui.bat` - Launch GUI on Windows
- `players_input.txt` - Sample input file
- `requirements.txt` - Python dependencies

---

## 🎓 5-Minute Tutorial

Let's extract data for Magnus Carlsen:

### Using GUI:

1. Run: `python fide_gui.py`
2. Type in the input box: `Magnus Carlsen`
3. Click "Extract Data"
4. Click "Excel" to save
5. Done! ✅

### Using Command Line:

1. Run: `python fide_extractor.py`
2. Type: `Magnus Carlsen`
3. Press Enter twice
4. Type filename or press Enter for default
5. Done! ✅

---

## 📊 What Data Do You Get?

For each player, you'll extract:

- ✅ FIDE ID
- ✅ Full Name
- ✅ Country/Federation
- ✅ Title (GM, IM, FM, etc.)
- ✅ Birth Year
- ✅ Standard Rating
- ✅ Rapid Rating
- ✅ Blitz Rating

## 🔍 How to Find FIDE IDs

1. Go to https://ratings.fide.com/
2. Search for a player
3. The ID is in the URL or profile

**Example IDs to try:**
- `1503014` - Magnus Carlsen
- `46616543` - Gukesh D
- `44129165` - Praggnanandhaa R
- `22538496` - (Your first test ID)
- `12528374` - (Your second test ID)

---

## 💾 Export Formats

| Format | Best For | Opens With |
|--------|----------|------------|
| **Excel** (.xlsx) | Spreadsheets, analysis | Excel, Google Sheets |
| **CSV** (.csv) | Universal, databases | Any spreadsheet app |
| **JSON** (.json) | Programming, APIs | Code editors, scripts |

*GUI supports all three! Command-line defaults to Excel.*

---

## ❓ Common Questions

**Q: Can I extract multiple players at once?**  
A: Yes! Enter one per line (up to hundreds).

**Q: Can I search by name or only by ID?**  
A: Both! The web scraper (`fide_extractor.py`) supports names.

**Q: Which is faster: GUI or command line?**  
A: Same speed! GUI is just easier to use.

**Q: Can I use this in my own Python project?**  
A: Absolutely! Import `FIDEDataExtractor` and use it.

**Q: Is there an API alternative?**  
A: Yes! See `fide_api_extractor.py` or the open-source [fide-api](https://github.com/cassiofb-dev/fide-api).

---

## 🐛 Something Not Working?

### Virtual environment not activated?
```bash
source venv/bin/activate
```

### Missing modules?
```bash
pip install -r requirements.txt
```

### GUI won't start?
```bash
# Mac
brew install python-tk

# Ubuntu
sudo apt-get install python3-tk
```

### Still stuck?
- Check `README.md` for detailed docs
- Try the command-line version instead
- Make sure you're connected to the internet

---

## 🎉 You're All Set!

**Try it now:**
```bash
python fide_gui.py
```

Enter your FIDE IDs (`22538496`, `12528374`) and click Extract!

---

## 📚 Learn More

- `GUI_GUIDE.md` - Complete GUI tutorial with screenshots
- `QUICKSTART.md` - All usage methods explained
- `README.md` - Full technical documentation
- `COMPARISON.md` - Compare different extraction methods

**Happy extracting! ♟️**

