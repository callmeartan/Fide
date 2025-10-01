# Quick Start Guide

## Setup (First Time Only)

1. **Create virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Running the Program

### 🖥️ Option 1: GUI Application (EASIEST - Recommended!)

**The simplest way to use the FIDE extractor:**

```bash
# Make sure venv is activated
source venv/bin/activate

# Launch the GUI
python fide_gui.py
```

Or just run:
```bash
./launch_gui.sh
```

**How to use the GUI:**
1. Enter FIDE IDs or player names in the text box (one per line)
2. Click "🔍 Extract Data" button
3. View the results in the table below
4. Click "📊 Excel", "📄 CSV", or "📋 JSON" to export

**That's it!** No command line knowledge needed.

### Option 2: Quick Test Script

Run the example batch script to see it in action:

```bash
python example_batch.py
```

This will extract data for several famous chess players and create `fide_players_batch.xlsx`.

### Option 3: Extract Your Own Players

**Step 1:** Edit `players_input.txt` and add your FIDE IDs or names (one per line):
```
22538496
12528374
Magnus Carlsen
Gukesh D
```

**Step 2:** Run the extraction:
```bash
python extract_from_file.py players_input.txt my_output.xlsx
```

### Option 4: Interactive Mode

Just run:
```bash
python fide_extractor.py
```

Then enter IDs/names when prompted.

## Where to Find FIDE IDs

1. Go to [https://ratings.fide.com/](https://ratings.fide.com/)
2. Search for a player by name
3. The FIDE ID will be in the URL or profile

**Examples:**
- Magnus Carlsen: `1503014`
- Gukesh D: `46616543`
- Praggnanandhaa R: `44129165`

## What Data is Extracted?

The program extracts:
- FIDE ID
- Full Name
- Federation (Country)
- Title (GM, IM, WGM, etc.)
- Birth Year
- Standard Chess Rating
- Rapid Chess Rating
- Blitz Chess Rating

## Troubleshooting

**Problem:** `ModuleNotFoundError`
**Solution:** Run `pip install -r requirements.txt`

**Problem:** No data extracted
**Solution:** 
- Check if FIDE ID is correct
- Check your internet connection
- FIDE website might be down (try again later)

**Problem:** Name search not working
**Solution:** Try using the exact FIDE ID instead

## Alternative: Using the FIDE API

If web scraping doesn't work well, you can use the existing FIDE API:

### Online API (No Setup Required)

```bash
# Get player by ID
curl https://fide-api.vercel.app/player/1503014

# Get top players
curl https://fide-api.vercel.app/top
```

### Run API Locally

```bash
git clone https://github.com/cassiofb-dev/fide-api
cd fide-api
docker compose up -d
```

Then visit `http://localhost:8000/docs` for the API documentation.

### Using the API in Python

```python
import requests
import pandas as pd

def get_player_from_api(fide_id):
    response = requests.get(f'https://fide-api.vercel.app/player/{fide_id}')
    return response.json()

# Get multiple players
players = [1503014, 46616543, 44129165]
data = [get_player_from_api(p) for p in players]

# Export to Excel
df = pd.DataFrame(data)
df.to_excel('players_via_api.xlsx', index=False)
```

## Need Help?

- Check the main `README.md` for detailed documentation
- Look at `example_batch.py` for code examples
- Visit the [FIDE API GitHub](https://github.com/cassiofb-dev/fide-api) for API alternative
