# Extraction Methods Comparison

This project provides **multiple ways** to extract FIDE player data. Choose based on your needs.

## Quick Comparison

| Feature | GUI | CLI Interactive | Batch File | Python Module |
|---------|-----|-----------------|------------|---------------|
| **Ease of Use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Visual Feedback** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Export Formats** | 3 (Excel, CSV, JSON) | 1 (Excel) | 1 (Excel) | Custom |
| **Data Preview** | ✅ Table | ❌ Text | ❌ None | ❌ None |
| **Best For** | Beginners | Quick tasks | Automation | Integration |

## Detailed Comparison

### 🖥️ GUI Application (`fide_gui.py`)

**Pros:**
- ✅ No command-line knowledge needed
- ✅ Visual table display
- ✅ Multiple export formats
- ✅ Real-time progress indicator
- ✅ Easy error handling

**Cons:**
- ❌ Requires tkinter (needs extra setup on some systems)
- ❌ Not suitable for automation

**Best for:** Anyone who wants a simple, visual interface

**Usage:**
```bash
python fide_gui.py
```

---

### 💻 CLI Interactive (`fide_extractor.py`)

**Pros:**
- ✅ Quick for one-off extractions
- ✅ Works on any system
- ✅ Search by name or ID

**Cons:**
- ❌ Only Excel export
- ❌ No visual feedback
- ❌ Manual input required

**Best for:** Quick terminal users

**Usage:**
```bash
python fide_extractor.py
# Then enter IDs/names and press Enter twice
```

---

### 📝 Batch File Processing (`extract_from_file.py`)

**Pros:**
- ✅ Process many players at once
- ✅ Reusable input files
- ✅ Good for repeated tasks

**Cons:**
- ❌ Requires creating input file
- ❌ Only Excel export
- ❌ No real-time feedback

**Best for:** Batch processing, recurring extractions

**Usage:**
```bash
python extract_from_file.py input.txt output.xlsx
```

---

### 🐍 Python Module

**Pros:**
- ✅ Full programmatic control
- ✅ Custom export formats
- ✅ Integration with other tools
- ✅ Most flexible

**Cons:**
- ❌ Requires Python knowledge
- ❌ More code to write

**Best for:** Developers, automation, custom applications

**Usage:**
```python
from fide_extractor import FIDEDataExtractor

extractor = FIDEDataExtractor()
data = extractor.extract_multiple_players(['1503014'])
extractor.export_to_excel(data, 'output.xlsx')
```

---

## Web Scraping vs API

### Web Scraper (Default)

**File:** `fide_extractor.py`

**How it works:** Parses HTML from ratings.fide.com

**Pros:**
- ✅ Search by name OR ID
- ✅ Direct from official source
- ✅ Always up-to-date

**Cons:**
- ⚠️ Slower (parses HTML)
- ⚠️ May break if FIDE changes website
- ⚠️ 1-second delay between requests

---

### API Method (Alternative)

**File:** `fide_api_extractor.py`

**How it works:** Uses REST API (fide-api.vercel.app)

**Pros:**
- ✅ Faster
- ✅ Structured JSON data
- ✅ More reliable

**Cons:**
- ⚠️ FIDE ID only (no name search)
- ⚠️ Depends on third-party service
- ⚠️ May have rate limits

**Usage:**
```python
from fide_api_extractor import FIDEAPIExtractor

extractor = FIDEAPIExtractor()
data = extractor.extract_multiple_players(['1503014', '22538496'])
extractor.export_to_excel(data, 'output.xlsx')
```

---

## Recommendations

### For Beginners
👉 Use the **GUI** (`fide_gui.py`)
- Easiest to understand
- Visual feedback
- Multiple export options

### For Terminal Users
👉 Use **CLI Interactive** (`fide_extractor.py`)
- Quick and simple
- No GUI needed
- Good for occasional use

### For Batch Processing
👉 Use **Batch File** (`extract_from_file.py`)
- Process many players
- Repeatable
- Save input files for reuse

### For Developers
👉 Use **Python Module** or **API Method**
- Full control
- Integration with other tools
- Custom workflows

---

## When to Use Each

| Scenario | Recommended Method |
|----------|-------------------|
| First time user | GUI |
| Extract 1-5 players | GUI or CLI Interactive |
| Extract 10+ players | GUI or Batch File |
| Need name search | Web Scraper methods |
| Only have FIDE IDs | Any method (API is fastest) |
| Building an app | Python Module |
| Recurring task | Batch File |
| Visual data review | GUI |

---

## Performance

| Method | Speed | Notes |
|--------|-------|-------|
| Web Scraper | ~1 player/sec | 1-second delay between requests |
| API | ~2 players/sec | Faster, but depends on API availability |

Both methods are respectful of servers and include appropriate delays.

---

## Summary

**Easiest:** GUI  
**Fastest:** API Method  
**Most Flexible:** Python Module  
**Best for Automation:** Batch File  
**Best for Name Search:** Web Scraper (GUI or CLI)

Choose based on your needs! All methods produce the same quality data.

