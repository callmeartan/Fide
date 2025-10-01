# GUI User Guide

## 🖥️ FIDE Data Extractor - Graphical Interface

The GUI application provides the easiest way to extract FIDE player data without any command-line knowledge.

## 🚀 How to Launch

### Mac/Linux:
```bash
cd /path/to/Fide
./launch_gui.sh
```

### Windows:
Double-click `launch_gui.bat` or run:
```cmd
launch_gui.bat
```

### Manual Launch:
```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
python fide_gui.py
```

## 📖 Using the GUI

### Step 1: Enter Player Information

In the input text area, enter FIDE IDs or player names (one per line):

```
22538496
12528374
Magnus Carlsen
Gukesh D
```

**Supported formats:**
- ✅ FIDE ID (e.g., `1503014`)
- ✅ Full name (e.g., `Magnus Carlsen`)
- ✅ Partial name (e.g., `Carlsen`)
- ✅ Mix of IDs and names

### Step 2: Extract Data

1. Click the **"🔍 Extract Data"** button
2. Wait for the progress indicator (usually 1-2 seconds per player)
3. Data will appear in the table below

### Step 3: View Results

The extracted data is displayed in a sortable table with columns:
- **FIDE ID** - Player's unique identifier
- **Name** - Full name
- **Federation** - Country code
- **Title** - Chess title (GM, IM, WGM, etc.)
- **B-Year** - Birth year
- **Std** - Standard rating
- **Rapid** - Rapid rating
- **Blitz** - Blitz rating

**Tips:**
- Click column headers to sort
- Scroll horizontally/vertically to view all data
- Alternating row colors for easy reading

### Step 4: Export Data

Click one of the export buttons to save your data:

- **📊 Excel** - `.xlsx` format (recommended for spreadsheets)
- **📄 CSV** - Comma-separated values (compatible with any spreadsheet program)
- **📋 JSON** - JSON format (for developers/programmers)

A file dialog will open where you can:
1. Choose the location to save
2. Customize the filename
3. Click Save

Default filenames include timestamps: `fide_players_20231001_143022.xlsx`

## 🎯 Features

### Input Area
- Multi-line text input
- Placeholder text with examples
- Copy/paste support
- No limit on number of players

### Action Buttons
- **Extract Data** - Fetch player information
- **Clear** - Reset everything and start over
- **Export buttons** - Save to different formats

### Results Table
- Clean, organized display
- Sortable columns
- Alternating row colors
- Scrollable for large datasets
- Auto-sizing columns

### Progress Indicator
- Shows when extraction is in progress
- Prevents accidental double-clicks
- Status bar shows results count

### Status Bar
- Shows current status
- Displays success/error messages
- Shows export confirmation

## 💡 Tips & Tricks

### Tip 1: Bulk Processing
You can extract data for dozens of players at once:
1. Prepare a list in a text editor
2. Copy all IDs/names
3. Paste into the input area
4. Click Extract

### Tip 2: Save Your Input
The input area retains your last search until you clear it. You can:
- Re-run the same search
- Add more players
- Modify the list

### Tip 3: Export Multiple Formats
You can export the same data to multiple formats:
1. Extract once
2. Click Excel export
3. Click CSV export
4. Click JSON export

No need to re-extract!

### Tip 4: Keyboard Shortcuts
- `Tab` - Navigate between input and buttons
- `Enter` - Activate focused button
- `Ctrl+A` / `Cmd+A` - Select all in input area
- `Ctrl+C` / `Cmd+C` - Copy
- `Ctrl+V` / `Cmd+V` - Paste

## 🔧 Troubleshooting

### Problem: GUI doesn't start
**Solution:**
```bash
# Make sure venv is activated
source venv/bin/activate

# Try running manually
python fide_gui.py
```

### Problem: "No module named 'tkinter'"
**Solution:**
- Mac: `brew install python-tk`
- Ubuntu: `sudo apt-get install python3-tk`
- Windows: Reinstall Python with "tcl/tk" option checked

### Problem: No data extracted
**Possible causes:**
- Invalid FIDE ID
- Player name misspelled
- Internet connection issues
- FIDE website temporarily down

**Solution:**
- Verify FIDE IDs at https://ratings.fide.com/
- Check spelling of player names
- Test internet connection
- Try again later

### Problem: Export fails
**Solution:**
- Check you have write permissions
- Make sure filename doesn't contain invalid characters
- Close Excel/CSV file if already open
- Choose a different location

## 📊 Export Format Details

### Excel (.xlsx)
- Best for: Spreadsheet analysis
- Opens in: Excel, Google Sheets, LibreOffice Calc
- Features: Formatted columns, ready to use

### CSV (.csv)
- Best for: Universal compatibility, database import
- Opens in: Any spreadsheet program, text editors
- Features: Plain text, easy to process

### JSON (.json)
- Best for: Programming, web applications, APIs
- Opens in: Text editors, code editors, JSON viewers
- Features: Structured data, easy to parse

## 🎨 GUI Layout

```
┌─────────────────────────────────────────────────────┐
│  ♟️ FIDE Player Data Extractor                      │
├─────────────────────────────────────────────────────┤
│  Input FIDE IDs or Player Names                     │
│  ┌───────────────────────────────────────────────┐  │
│  │ 22538496                                      │  │
│  │ 12528374                                      │  │
│  │ Magnus Carlsen                                │  │
│  │                                               │  │
│  └───────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────┤
│  [🔍 Extract] [🗑️ Clear]  Export: [📊] [📄] [📋]    │
├─────────────────────────────────────────────────────┤
│  Extracted Data                                      │
│  ┌───────────────────────────────────────────────┐  │
│  │ ID    │ Name  │ Country │ Title │ Ratings   │  │
│  ├───────────────────────────────────────────────┤  │
│  │ ...   │ ...   │ ...     │ ...   │ ...       │  │
│  └───────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────┤
│  Status: Ready                                       │
└─────────────────────────────────────────────────────┘
```

## 🌟 Advantages of GUI vs Command Line

| Feature | GUI | Command Line |
|---------|-----|--------------|
| Ease of use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Visual feedback | ✅ Yes | ❌ No |
| Export options | 3 formats | 1 format |
| Data preview | ✅ Table view | ❌ Text only |
| Multiple exports | ✅ Easy | ⚠️ Re-run needed |
| Error messages | ✅ User-friendly | ⚠️ Technical |

## 🆘 Need Help?

- Check the main `README.md` for general information
- See `QUICKSTART.md` for installation steps
- Try command-line version if GUI has issues
- Report issues or ask questions

## 🎉 Enjoy!

The GUI makes FIDE data extraction simple and accessible to everyone!


