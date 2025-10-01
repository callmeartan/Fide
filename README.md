# FIDE Player Data Extractor

A Python program to extract FIDE chess player data from [ratings.fide.com](https://ratings.fide.com/) and export to multiple formats.

## ✨ Features

- 🖥️ **Graphical User Interface** - Easy-to-use GUI with no coding required
- 🔍 **Flexible Search** - Extract by FIDE ID or player name
- 📊 **Multiple Export Formats** - Excel (.xlsx), CSV (.csv), and JSON (.json)
- ⚡ **Batch Processing** - Extract multiple players at once
- 📈 **Complete Data** - Get ratings, titles, federation, and more
- 🎯 **Real-time Display** - View results in a sortable table

## 📦 What Data is Extracted?

For each player:
- FIDE ID
- Full Name
- Federation/Country
- Chess Title (GM, IM, FM, WGM, etc.)
- Birth Year
- Standard Chess Rating
- Rapid Chess Rating
- Blitz Chess Rating

## 🚀 Quick Start

### 1. Installation

```bash
# Navigate to the project folder
cd /Users/artan/Desktop/development/Fide

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the GUI (Recommended)

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Launch GUI
python fide_gui.py
```

Or use the launcher:
```bash
./launch_gui.sh  # Mac/Linux
launch_gui.bat   # Windows
```

### 3. Use it!

1. Enter FIDE IDs or player names (one per line)
2. Click **"🔍 Extract Data"**
3. View results in the table
4. Export to Excel, CSV, or JSON

**That's it!** ✅

## 📖 Usage Methods

### 🖥️ Method 1: GUI Application (Easiest)

The graphical interface is the simplest way to use the tool.

**Features:**
- Visual input area for multiple players
- Real-time progress indicator
- Sortable results table
- One-click export to 3 formats
- User-friendly error messages

**How to use:**
1. Launch: `python fide_gui.py`
2. Enter FIDE IDs or names (one per line)
3. Click "Extract Data"
4. Export to your preferred format

👉 See [GUI_GUIDE.md](GUI_GUIDE.md) for detailed instructions.

---

### 💻 Method 2: Command Line (Interactive)

For users who prefer terminal interaction:

```bash
python fide_extractor.py
```

Then enter FIDE IDs or player names when prompted (one per line), and press Enter twice when done.

**Example:**
```
Enter FIDE IDs or player names (one per line).
Press Enter twice when done:

1503014
Gukesh D
Magnus Carlsen

[Enter]
[Enter]
```

Output: `fide_players.xlsx`

---

### 📝 Method 3: Batch from File

Create a text file with FIDE IDs or names (one per line):

**players.txt:**
```
22538496
12528374
Magnus Carlsen
Gukesh D
```

Then run:
```bash
python extract_from_file.py players.txt output.xlsx
```

---

### 🐍 Method 4: Python Module

Use it programmatically in your own scripts:

```python
from fide_extractor import FIDEDataExtractor

# Create extractor
extractor = FIDEDataExtractor()

# Extract data
players = ['1503014', 'Magnus Carlsen', '22538496']
data = extractor.extract_multiple_players(players)

# Export to Excel
extractor.export_to_excel(data, 'my_players.xlsx')
```

**Export methods:**
```python
# Excel
extractor.export_to_excel(data, 'players.xlsx')

# CSV (do it manually)
import pandas as pd
df = pd.DataFrame(data)
df.to_csv('players.csv', index=False)

# JSON
import json
with open('players.json', 'w') as f:
    json.dump(data, f, indent=2)
```

## 🔧 Project Structure

```
Fide/
├── fide_gui.py              # ⭐ GUI Application (main)
├── fide_extractor.py        # Core extraction engine (web scraping)
├── fide_api_extractor.py    # Alternative API-based extractor
├── extract_from_file.py     # Batch file processor
├── example_batch.py         # Example usage script
│
├── launch_gui.sh            # GUI launcher (Mac/Linux)
├── launch_gui.bat           # GUI launcher (Windows)
│
├── README.md                # This file
├── START_HERE.md            # Quick start guide
├── GUI_GUIDE.md             # Detailed GUI tutorial
├── QUICKSTART.md            # All usage methods
├── COMPARISON.md            # Compare extraction methods
│
├── requirements.txt         # Python dependencies
├── players_input.txt        # Sample input file
└── .gitignore              # Git ignore rules
```

## 📊 Export Formats

| Format | Extension | Best For | Opens With |
|--------|-----------|----------|------------|
| Excel | `.xlsx` | Spreadsheet analysis, data manipulation | Excel, Google Sheets, LibreOffice |
| CSV | `.csv` | Universal compatibility, database import | Any spreadsheet app, text editors |
| JSON | `.json` | Programming, web APIs, data processing | Code editors, JSON viewers |

## 💡 Tips & Tricks

### Finding FIDE IDs
1. Visit [ratings.fide.com](https://ratings.fide.com/)
2. Search for a player by name
3. The ID is in the URL (e.g., `ratings.fide.com/profile/1503014`)

### Example FIDE IDs
- **1503014** - Magnus Carlsen (World Champion)
- **46616543** - Gukesh D (World Champion)
- **44129165** - Praggnanandhaa R
- **8603677** - Hou Yifan (Top Women)

### Search by Name
You can enter partial names:
- "Carlsen" will find Magnus Carlsen
- "Gukesh" will find Gukesh D
- Full names work too: "Magnus Carlsen"

### Batch Processing
The GUI and command-line tools can process dozens of players at once. Just enter one per line!

## 🐛 Troubleshooting

### GUI Won't Start (Missing tkinter)

**Mac:**
```bash
brew install python-tk@3.13
# Then recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Windows:**
Reinstall Python with the "tcl/tk and IDLE" option checked.

### No Data Extracted (Shows N/A)

**Possible causes:**
- Invalid FIDE ID
- Player name misspelled
- Internet connection issues
- FIDE website temporarily unavailable

**Solutions:**
- Verify FIDE IDs at [ratings.fide.com](https://ratings.fide.com/)
- Check your internet connection
- Try again later if FIDE website is down

### Import Errors

Make sure virtual environment is activated and packages are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## 🆚 Web Scraping vs API

This project includes **two extraction methods**:

### Web Scraping (`fide_extractor.py`)
- ✅ Search by name or ID
- ✅ Direct from FIDE website
- ⚠️ Slower (web parsing)
- ⚠️ May break if website changes

### API Method (`fide_api_extractor.py`)
- ✅ Faster
- ✅ Structured data
- ⚠️ FIDE ID only (no name search)
- ⚠️ Uses third-party API

👉 See [COMPARISON.md](COMPARISON.md) for detailed comparison.

## 📚 Additional Documentation

- **[START_HERE.md](START_HERE.md)** - Complete beginner's guide
- **[GUI_GUIDE.md](GUI_GUIDE.md)** - Detailed GUI tutorial with tips
- **[QUICKSTART.md](QUICKSTART.md)** - All methods explained
- **[COMPARISON.md](COMPARISON.md)** - Compare extraction approaches

## 🌐 Alternative: FIDE API

There's an open-source REST API available at [fide-api](https://github.com/cassiofb-dev/fide-api):

```bash
# Use hosted API
curl https://fide-api.vercel.app/player/1503014

# Or run locally with Docker
git clone https://github.com/cassiofb-dev/fide-api
cd fide-api
docker compose up -d
```

Visit `http://localhost:8000/docs` for API documentation.

## ⚙️ Technical Details

**Requirements:**
- Python 3.8+
- Internet connection
- Libraries: requests, beautifulsoup4, pandas, openpyxl

**Extraction Method:**
- Web scraping from ratings.fide.com
- Parses HTML using BeautifulSoup
- Respects server with 1-second delay between requests

**Data Source:**
All data is scraped from publicly available FIDE profiles at [ratings.fide.com](https://ratings.fide.com/).

## 📝 Notes

- The program respects FIDE's servers with built-in delays
- Name searches return the first matching result
- Inactive players still show their last known ratings
- Export files include timestamps to prevent overwrites

## 📄 License

MIT License - Feel free to use, modify, and distribute.

## ⚠️ Disclaimer

This tool scrapes publicly available data from FIDE's website for personal and educational use. Please use responsibly and in accordance with FIDE's terms of service.

## 🤝 Contributing

Found a bug or want to improve the tool? Feel free to submit issues or pull requests!

## 💬 Support

- Check the documentation files for detailed guides
- Try the example scripts to understand usage
- Report issues if you encounter problems

---

**Made with ♟️ for chess players and developers**

*Last updated: 2025 - Compatible with current FIDE website structure*
