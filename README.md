# FIDE Player Data Extractor

A Python application for extracting and exporting chess player data from the official FIDE ratings database.

## Overview

This tool enables automated extraction of player information from [ratings.fide.com](https://ratings.fide.com/), supporting both graphical and command-line interfaces with multiple export formats.

**Key Features:**
- Search by FIDE ID or player name
- Batch processing of multiple players
- Export to Excel, CSV, and JSON formats
- Graphical user interface and command-line options
- Real-time data extraction from official FIDE database

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Internet connection
- pip (Python package installer)

### Installation

1. **Clone or download this repository**

2. **Set up virtual environment**
   ```bash
   cd /path/to/Fide
   python3 -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # macOS/Linux
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### macOS Additional Setup (Required for GUI)

If you're on macOS and want to use the GUI, install tkinter:
```bash
brew install python-tk@3.13
# Then recreate the virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### First Run

**Option 1: Graphical Interface (Recommended)**
```bash
python fide_gui.py
```

**Option 2: Command Line**
```bash
python fide_extractor.py
```

## Usage

### GUI Application

The graphical interface provides the most user-friendly experience:

1. Launch the application:
   ```bash
   python fide_gui.py
   ```

2. Enter FIDE IDs or player names in the input area (one per line)

3. Click "Extract Data" to fetch player information

4. View results in the table

5. Export data using the Excel, CSV, or JSON buttons

### Command Line Interface

**Interactive Mode:**
```bash
python fide_extractor.py
```
Enter player IDs or names when prompted, then press Enter twice to process.

**Batch Mode:**
```bash
python extract_from_file.py input.txt output.xlsx
```
Create a text file with one FIDE ID or name per line.

### Programmatic Usage

```python
from fide_extractor import FIDEDataExtractor

# Initialize extractor
extractor = FIDEDataExtractor()

# Extract player data
players = ['1503014', '22538496']
data = extractor.extract_multiple_players(players)

# Export to Excel
extractor.export_to_excel(data, 'players.xlsx')

# Or export to CSV/JSON manually
import pandas as pd
import json

df = pd.DataFrame(data)
df.to_csv('players.csv', index=False)

with open('players.json', 'w') as f:
    json.dump(data, f, indent=2)
```

## Data Extracted

For each player, the following information is retrieved:

| Field | Description |
|-------|-------------|
| FIDE ID | Unique player identifier |
| Name | Player's full name |
| Federation | Country/federation code |
| Title | Chess title (GM, IM, FM, etc.) or N/A |
| B-Year | Birth year |
| Rating std | Standard chess rating |
| Rating rapid | Rapid chess rating |
| Rating blitz | Blitz chess rating |

## Export Formats

### Excel (.xlsx)
Spreadsheet format compatible with Microsoft Excel, Google Sheets, and LibreOffice Calc.

### CSV (.csv)
Comma-separated values format for universal compatibility and database imports.

### JSON (.json)
JavaScript Object Notation format for programmatic use and API integration.

## Project Structure

```
Fide/
├── fide_gui.py              # GUI application
├── fide_extractor.py        # Core extraction engine
├── fide_api_extractor.py    # Alternative API-based extractor
├── extract_from_file.py     # Batch file processor
├── example_batch.py         # Usage example
├── launch_gui.sh            # GUI launcher (Unix)
├── launch_gui.bat           # GUI launcher (Windows)
├── requirements.txt         # Python dependencies
├── players_input.txt        # Sample input file
└── README.md                # This file
```

## Documentation

- **[START_HERE.md](START_HERE.md)** - Beginner's guide with step-by-step instructions
- **[QUICKSTART.md](QUICKSTART.md)** - All usage methods and examples
- **[COMPARISON.md](COMPARISON.md)** - Comparison of extraction methods
- **[GUI_GUIDE.md](GUI_GUIDE.md)** - Detailed GUI usage instructions

## Finding FIDE IDs

1. Visit [ratings.fide.com](https://ratings.fide.com/)
2. Search for a player by name
3. The FIDE ID appears in the URL: `ratings.fide.com/profile/[ID]`

**Example IDs:**
- 1503014 (Magnus Carlsen)
- 46616543 (Gukesh D)
- 44129165 (Praggnanandhaa R)

## Troubleshooting

### GUI Won't Launch

**macOS:**
```bash
brew install python-tk@3.13
rm -rf venv && python3 -m venv venv
source venv/bin/activate && pip install -r requirements.txt
```

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Windows:**
Reinstall Python with "tcl/tk and IDLE" option enabled.

### Module Import Errors

Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Data Extraction Issues

- Verify FIDE ID is correct at [ratings.fide.com](https://ratings.fide.com/)
- Check internet connectivity
- Ensure FIDE website is accessible
- For name searches, try the exact spelling

### Title Shows "N/A"

This is expected behavior. FIDE titles (GM, IM, FM, etc.) are only awarded to players who meet specific rating and performance criteria. Most players do not have official FIDE titles.

## Technical Details

**Technologies:**
- Python 3.8+
- BeautifulSoup4 for HTML parsing
- Pandas for data manipulation
- OpenPyXL for Excel export
- Tkinter for GUI

**Extraction Method:**
- Web scraping from ratings.fide.com
- 1-second delay between requests (server-friendly)
- Robust error handling

**Data Source:**
All data is extracted from publicly available FIDE player profiles.

## Web Scraping vs API

This project includes two extraction methods:

### Web Scraping (Default)
- **File:** `fide_extractor.py`
- **Pros:** Name and ID search, direct from FIDE
- **Cons:** Slower, may break if website changes

### API Method (Alternative)
- **File:** `fide_api_extractor.py`
- **Pros:** Faster, structured data
- **Cons:** ID only, third-party dependency

See [COMPARISON.md](COMPARISON.md) for detailed comparison.

## Third-Party API Alternative

An open-source REST API is available at [fide-api](https://github.com/cassiofb-dev/fide-api):

```bash
# Hosted API
curl https://fide-api.vercel.app/player/1503014

# Self-hosted with Docker
git clone https://github.com/cassiofb-dev/fide-api
cd fide-api
docker compose up -d
```

## Best Practices

- Respect FIDE's servers (built-in delays are implemented)
- Use batch processing for multiple players
- Verify extracted data for critical applications
- Keep dependencies updated for security

## Performance Notes

- Processing speed: ~1 player per second (web scraping)
- API method: ~2 players per second
- GUI supports concurrent extraction with progress indication
- Batch files recommended for 10+ players

## Limitations

- Name search returns first match only
- Requires active internet connection
- Subject to FIDE website structure changes
- Rate limited by built-in delays

## Contributing

Contributions are welcome. Please ensure:
- Code follows existing style
- Documentation is updated
- Testing is performed before submission

## License

MIT License - See LICENSE file for details.

## Disclaimer

This tool is for personal and educational use. It extracts publicly available data from FIDE's website. Users are responsible for complying with FIDE's terms of service and applicable data usage policies.

## Support

For issues, questions, or feature requests:
1. Check existing documentation
2. Review troubleshooting section
3. Submit an issue with detailed information

## Changelog

### Version 1.0.0 (2025)
- Initial release
- GUI and CLI interfaces
- Multiple export formats
- Batch processing support
- Comprehensive documentation

---

**Developed for chess enthusiasts and data analysts**

*Compatible with FIDE website structure as of October 2025*
