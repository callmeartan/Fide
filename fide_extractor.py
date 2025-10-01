import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict, Optional
import re
import time


class FIDEDataExtractor:
    """Extract FIDE player data and export to Excel"""
    
    BASE_URL = "https://ratings.fide.com"
    SEARCH_URL = f"{BASE_URL}/profile"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_player_by_id(self, fide_id: str) -> Optional[Dict]:
        """Get player data by FIDE ID"""
        try:
            url = f"{self.SEARCH_URL}/{fide_id}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            return self._parse_player_page(response.text, fide_id)
        except Exception as e:
            print(f"Error fetching FIDE ID {fide_id}: {str(e)}")
            return None
    
    def search_player_by_name(self, name: str) -> List[Dict]:
        """Search players by name"""
        try:
            search_url = f"{self.BASE_URL}/search.php"
            params = {
                'search': name
            }
            response = self.session.get(search_url, params=params, timeout=10)
            response.raise_for_status()
            
            return self._parse_search_results(response.text)
        except Exception as e:
            print(f"Error searching for name '{name}': {str(e)}")
            return []
    
    def _parse_player_page(self, html: str, fide_id: str) -> Optional[Dict]:
        """Parse player profile page"""
        soup = BeautifulSoup(html, 'html.parser')
        
        try:
            # Extract player name from title or profile-title-container
            name = "N/A"
            title_tag = soup.find('title')
            if title_tag:
                # Title format: "Last, First FIDE Profile"
                name_text = title_tag.text.replace(' FIDE Profile', '').strip()
                if name_text:
                    name = name_text
            
            # If not in title, try profile-title-container
            if name == "N/A":
                name_elem = soup.find('div', class_='profile-title-container')
                if name_elem:
                    name = name_elem.text.strip()
            
            # Initialize data structure
            data = {
                'FIDE ID': fide_id,
                'Name': name,
                'Federation': 'N/A',
                'B-Year': 'N/A',
                'Rating std': 'N/A',
                'Rating rapid': 'N/A',
                'Rating blitz': 'N/A',
                'Title': 'N/A'
            }
            
            # Extract ratings from profile-game divs
            std_game = soup.find('div', class_='profile-standart')
            if std_game:
                rating_text = std_game.text.strip()
                # Extract numbers from text like "1525STANDARD inactive"
                rating_match = re.search(r'(\d+)', rating_text)
                if rating_match:
                    data['Rating std'] = rating_match.group(1)
            
            rapid_game = soup.find('div', class_='profile-rapid')
            if rapid_game:
                rating_text = rapid_game.text.strip()
                rating_match = re.search(r'(\d+)', rating_text)
                if rating_match:
                    data['Rating rapid'] = rating_match.group(1)
            
            blitz_game = soup.find('div', class_='profile-blitz')
            if blitz_game:
                rating_text = blitz_game.text.strip()
                rating_match = re.search(r'(\d+)', rating_text)
                if rating_match:
                    data['Rating blitz'] = rating_match.group(1)
            
            # Extract country from profile-info-country
            country_elem = soup.find('div', class_='profile-info-country')
            if country_elem:
                country = country_elem.text.strip()
                if country:
                    data['Federation'] = country
            
            # Extract birth year and title from profile-info-row divs
            info_rows = soup.find_all('div', class_='profile-info-row')
            for row in info_rows:
                text = row.text.strip()
                if 'B-Year' in text:
                    # Extract the year
                    year_match = re.search(r'(\d{4})', text)
                    if year_match:
                        data['B-Year'] = year_match.group(1)
                elif 'FIDE title' in text:
                    # Extract title
                    title_div = row.find('div', class_='profile-info-title')
                    if title_div:
                        title = title_div.text.strip()
                        if title and title.lower() != 'none':
                            data['Title'] = title
            
            return data
            
        except Exception as e:
            print(f"Error parsing player page: {str(e)}")
            return None
    
    def _parse_search_results(self, html: str) -> List[Dict]:
        """Parse search results page"""
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        
        try:
            # Find all player rows in search results
            rows = soup.find_all('tr', class_='search-result')
            
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 5:
                    fide_id = cells[0].text.strip()
                    name = cells[1].text.strip()
                    federation = cells[2].text.strip()
                    
                    results.append({
                        'FIDE ID': fide_id,
                        'Name': name,
                        'Federation': federation
                    })
        except Exception as e:
            print(f"Error parsing search results: {str(e)}")
        
        return results
    
    def extract_multiple_players(self, identifiers: List[str]) -> List[Dict]:
        """
        Extract data for multiple players
        identifiers can be FIDE IDs or names
        """
        all_players = []
        
        for identifier in identifiers:
            identifier = identifier.strip()
            
            # Check if it's a FIDE ID (numeric)
            if identifier.isdigit():
                print(f"Fetching FIDE ID: {identifier}")
                player_data = self.get_player_by_id(identifier)
                if player_data:
                    all_players.append(player_data)
            else:
                # Search by name
                print(f"Searching for name: {identifier}")
                search_results = self.search_player_by_name(identifier)
                
                if search_results:
                    # Get detailed data for first result
                    fide_id = search_results[0]['FIDE ID']
                    player_data = self.get_player_by_id(fide_id)
                    if player_data:
                        all_players.append(player_data)
            
            # Be polite to the server
            time.sleep(1)
        
        return all_players
    
    def export_to_excel(self, players_data: List[Dict], filename: str = "fide_players.xlsx"):
        """Export player data to Excel file"""
        if not players_data:
            print("No data to export!")
            return
        
        df = pd.DataFrame(players_data)
        
        # Reorder columns for better readability
        column_order = ['FIDE ID', 'Name', 'Federation', 'Title', 'B-Year', 
                       'Rating std', 'Rating rapid', 'Rating blitz']
        
        # Only include columns that exist in the dataframe
        column_order = [col for col in column_order if col in df.columns]
        df = df[column_order]
        
        # Export to Excel
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"\n✓ Data exported successfully to {filename}")
        print(f"  Total players: {len(players_data)}")


def main():
    """Main function to run the FIDE data extractor"""
    print("=" * 60)
    print("        FIDE Player Data Extractor")
    print("=" * 60)
    
    # Create extractor instance
    extractor = FIDEDataExtractor()
    
    # Get user input
    print("\nEnter FIDE IDs or player names (one per line).")
    print("Press Enter twice when done:\n")
    
    identifiers = []
    while True:
        line = input().strip()
        if not line:
            break
        identifiers.append(line)
    
    if not identifiers:
        print("No identifiers provided. Exiting.")
        return
    
    # Extract player data
    print(f"\nProcessing {len(identifiers)} identifier(s)...\n")
    players_data = extractor.extract_multiple_players(identifiers)
    
    if not players_data:
        print("No data could be extracted.")
        return
    
    # Display extracted data
    print("\n" + "=" * 60)
    print("Extracted Player Data:")
    print("=" * 60)
    for player in players_data:
        print(f"\nName: {player.get('Name', 'N/A')}")
        print(f"FIDE ID: {player.get('FIDE ID', 'N/A')}")
        print(f"Federation: {player.get('Federation', 'N/A')}")
        print(f"Title: {player.get('Title', 'N/A')}")
        print(f"Standard: {player.get('Rating std', 'N/A')}")
        print(f"Rapid: {player.get('Rating rapid', 'N/A')}")
        print(f"Blitz: {player.get('Rating blitz', 'N/A')}")
    
    # Export to Excel
    print("\n" + "=" * 60)
    filename = input("Enter output filename (default: fide_players.xlsx): ").strip()
    if not filename:
        filename = "fide_players.xlsx"
    if not filename.endswith('.xlsx'):
        filename += '.xlsx'
    
    extractor.export_to_excel(players_data, filename)
    print("=" * 60)


if __name__ == "__main__":
    main()
