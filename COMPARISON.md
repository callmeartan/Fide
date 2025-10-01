# FIDE Data Extraction Methods Comparison

This project provides **two methods** to extract FIDE player data. Choose the one that best fits your needs.

## Method Comparison

| Feature | Web Scraping (`fide_extractor.py`) | REST API (`fide_api_extractor.py`) |
|---------|-----------------------------------|-----------------------------------|
| **Search by Name** | ✅ Yes | ❌ No (FIDE ID only) |
| **Search by FIDE ID** | ✅ Yes | ✅ Yes |
| **Reliability** | Medium (depends on website structure) | High (structured API) |
| **Speed** | Slower | Faster |
| **Setup Required** | None | None (uses public API) |
| **Internet Dependency** | FIDE website must be accessible | API must be accessible |
| **Data Fields** | Name, ID, Federation, Title, Ratings | Name, ID, Federation, Title, Ratings, World Rank |

## When to Use Each Method

### Use Web Scraping (`fide_extractor.py`) When:
- ✅ You only know player names (not FIDE IDs)
- ✅ You want to search by partial names
- ✅ You want direct access to FIDE's latest data
- ✅ The FIDE API is unavailable

### Use REST API (`fide_api_extractor.py`) When:
- ✅ You have FIDE IDs
- ✅ You need faster extraction
- ✅ You want more reliable/structured data
- ✅ You need additional fields like World Rank

## Quick Usage Examples

### Web Scraping Method
```bash
# Interactive mode with name search
python fide_extractor.py

# Input:
# Magnus Carlsen
# Gukesh D
# 22538496
```

### API Method
```bash
# API mode (FIDE IDs only)
python fide_api_extractor.py

# Input:
# 1503014
# 46616543
# 22538496
```

## Recommendation

**For Most Users:** Start with the **Web Scraping method** (`fide_extractor.py`) because:
- It supports both names and IDs
- More flexible for unknown FIDE IDs
- Direct access to FIDE data

**For Advanced Users:** Use the **API method** (`fide_api_extractor.py`) when:
- You have a list of FIDE IDs
- You need faster batch processing
- You're building automation

## Alternative: Self-Hosted API

If you want the best of both worlds, you can run the FIDE API locally:

```bash
# Clone and run the API
git clone https://github.com/cassiofb-dev/fide-api
cd fide-api
docker compose up -d

# Then use it in your Python scripts
import requests

response = requests.get('http://localhost:8000/player/1503014')
player_data = response.json()
```

Visit `http://localhost:8000/docs` for full API documentation.

## Files Overview

| File | Purpose |
|------|---------|
| `fide_extractor.py` | Main web scraping extractor |
| `fide_api_extractor.py` | API-based extractor |
| `example_batch.py` | Example batch extraction script |
| `extract_from_file.py` | Extract from text file of IDs |
| `players_input.txt` | Sample input file |

## Need Help?

- See `QUICKSTART.md` for quick setup
- See `README.md` for detailed documentation
- Check the example scripts for code samples
