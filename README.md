# FIDE Player Data Extractor

A Python program to extract FIDE chess player data from [ratings.fide.com](https://ratings.fide.com/) and export it to Excel format.

## Features

- ✅ **Graphical User Interface (GUI)** - Easy-to-use interface
- ✅ Extract player data by FIDE ID
- ✅ Search players by name
- ✅ Support multiple players at once
- ✅ Export to **Excel, CSV, and JSON** formats
- ✅ Real-time data display in sortable table
- ✅ Extract comprehensive data:
  - FIDE ID
  - Player Name
  - Federation/Country
  - Title (GM, IM, FM, etc.)
  - Birth Year
  - Standard Rating
  - Rapid Rating
  - Blitz Rating

## Installation

1. **Clone or download this repository**

2. **Create virtual environment and install dependencies:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### 🖥️ GUI Application (Recommended - New!)

The easiest way to use this tool is through the **graphical interface**:

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Launch GUI
python fide_gui.py
```

Or use the launcher script:
```bash
./launch_gui.sh  # On Mac/Linux
```

**GUI Features:**
- 📝 Input multiple FIDE IDs or player names at once
- 📊 View extracted data in a beautiful sortable table
- 💾 Export to Excel (.xlsx), CSV (.csv), or JSON (.json)
- ⚡ Real-time progress indicator
- 🎯 User-friendly interface with clear instructions

**Screenshot:**
The GUI allows you to:
1. Enter FIDE IDs or names in the text area (one per line)
2. Click "Extract Data" to fetch player information
3. View results in an organized table
4. Export to your preferred format with one click

### 📟 Command Line Options

### Method 1: Interactive Mode

Run the program interactively:

```bash
python fide_extractor.py
```

Then enter FIDE IDs or player names (one per line), and press Enter twice when done.

**Example:**
```
Enter FIDE IDs or player names (one per line).
Press Enter twice when done:

22538496
12528374
Magnus Carlsen

```

### Method 2: Extract from File

Create a text file with FIDE IDs or names (one per line), then run:

```bash
python extract_from_file.py players_input.txt output.xlsx
```

**Example input file (players_input.txt):**
```
22538496
12528374
62506241
Magnus Carlsen
```

### Method 3: Batch Script

Use the provided example batch script:

```bash
python example_batch.py
```

This will extract data for predefined players and save to `fide_players_batch.xlsx`.

### Method 4: Programmatic Usage

You can also use it as a module in your own Python scripts:

```python
from fide_extractor import FIDEDataExtractor

# Create extractor
extractor = FIDEDataExtractor()

# Extract data for multiple players
identifiers = ['22538496', '12528374', 'Magnus Carlsen']
players_data = extractor.extract_multiple_players(identifiers)

# Export to Excel
extractor.export_to_excel(players_data, 'my_players.xlsx')
```

## Example FIDE IDs

Here are some example FIDE IDs you can test with:

- **22538496** - (Example player)
- **12528374** - (Example player)
- **62506241** - (Example player)
- **1503014** - Magnus Carlsen
- **8603677** - Gukesh D
- **44129165** - Praggnanandhaa R

## Output

The program exports data to an Excel file with the following columns:

| FIDE ID | Name | Federation | Title | B-Year | Rating std | Rating rapid | Rating blitz |
|---------|------|------------|-------|--------|------------|--------------|--------------|
| ... | ... | ... | ... | ... | ... | ... | ... |

## Notes

- The program respects FIDE's servers by adding a 1-second delay between requests
- If a name search returns multiple results, the program uses the first match
- FIDE IDs are numeric identifiers (e.g., 22538496)
- Player names can be partial (e.g., "Carlsen" will find Magnus Carlsen)

## Alternative: Using the FIDE API

There's also an open-source REST API available at [fide-api](https://github.com/cassiofb-dev/fide-api) that you can use:

```bash
# Using the hosted API
curl https://fide-api.vercel.app/player/1503014
```

Or run it locally with Docker:

```bash
git clone https://github.com/cassiofb-dev/fide-api
cd fide-api
docker compose up -d
```

## License

MIT License - feel free to use and modify as needed.

## Disclaimer

This tool scrapes publicly available data from FIDE's website. Please use it responsibly and in accordance with FIDE's terms of service.
