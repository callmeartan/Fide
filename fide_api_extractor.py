"""
Alternative FIDE data extractor using the fide-api REST API
This is faster and more reliable than web scraping
"""

import requests
import pandas as pd
from typing import List, Dict, Optional
import time


class FIDEAPIExtractor:
    """Extract FIDE player data using the fide-api REST API"""
    
    # You can use the hosted API or run it locally
    API_BASE_URL = "https://fide-api.vercel.app"
    # If running locally with Docker: API_BASE_URL = "http://localhost:8000"
    
    def __init__(self, api_url: str = None):
        """
        Initialize the API extractor
        
        Args:
            api_url: Optional custom API URL (default: public hosted API)
        """
        self.api_url = api_url or self.API_BASE_URL
        self.session = requests.Session()
    
    def get_player_by_id(self, fide_id: str) -> Optional[Dict]:
        """Get player data by FIDE ID"""
        try:
            url = f"{self.api_url}/player/{fide_id}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Normalize the data structure
            player_data = {
                'FIDE ID': str(data.get('fide_id', fide_id)),
                'Name': data.get('name', 'N/A'),
                'Federation': data.get('federation', 'N/A'),
                'Title': data.get('title', 'N/A'),
                'B-Year': data.get('birth_year', 'N/A'),
                'Age': 'N/A',
                'Rating std': data.get('standard_rating', 'N/A'),
                'Rating rapid': data.get('rapid_rating', 'N/A'),
                'Rating blitz': data.get('blitz_rating', 'N/A'),
                'World Rank': data.get('world_rank', 'N/A'),
            }
            
            # Calculate age
            if player_data['B-Year'] != 'N/A':
                try:
                    birth_year = int(player_data['B-Year'])
                    player_data['Age'] = str(2025 - birth_year)
                except:
                    player_data['Age'] = 'N/A'
            
            return player_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching FIDE ID {fide_id}: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error for FIDE ID {fide_id}: {str(e)}")
            return None
    
    def get_top_players(self, limit: int = 100) -> List[Dict]:
        """Get top players from the API"""
        try:
            url = f"{self.api_url}/top"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Return the requested number of players
            return data[:limit] if isinstance(data, list) else []
        except Exception as e:
            print(f"Error fetching top players: {str(e)}")
            return []
    
    def extract_multiple_players(self, fide_ids: List[str]) -> List[Dict]:
        """
        Extract data for multiple players by FIDE ID
        
        Note: This API doesn't support name search, only FIDE IDs
        """
        all_players = []
        
        for fide_id in fide_ids:
            fide_id = fide_id.strip()
            
            if not fide_id.isdigit():
                print(f"Warning: '{fide_id}' is not a valid FIDE ID (must be numeric)")
                continue
            
            print(f"Fetching FIDE ID: {fide_id}")
            player_data = self.get_player_by_id(fide_id)
            
            if player_data:
                all_players.append(player_data)
            
            # Be polite to the API
            time.sleep(0.5)
        
        return all_players
    
    def export_to_excel(self, players_data: List[Dict], filename: str = "fide_players.xlsx"):
        """Export player data to Excel file"""
        if not players_data:
            print("No data to export!")
            return
        
        df = pd.DataFrame(players_data)
        
        # Replace N/A with empty strings
        df = df.replace('N/A', '')
        
        # Reorder columns for better readability
        column_order = ['FIDE ID', 'Name', 'Federation', 'Title', 'B-Year', 'Age',
                       'Rating std', 'Rating rapid', 'Rating blitz', 'World Rank']
        
        # Only include columns that exist in the dataframe
        column_order = [col for col in column_order if col in df.columns]
        df = df[column_order]
        
        # Export to Excel
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"\n✓ Data exported successfully to {filename}")
        print(f"  Total players: {len(players_data)}")


def main():
    """Main function to run the FIDE API extractor"""
    print("=" * 60)
    print("   FIDE Player Data Extractor (API Mode)")
    print("=" * 60)
    
    # Create extractor instance
    extractor = FIDEAPIExtractor()
    
    # Test API connectivity
    print("\nTesting API connectivity...")
    try:
        response = requests.get(f"{extractor.api_url}/top", timeout=5)
        if response.status_code == 200:
            print("✓ API is accessible")
        else:
            print("✗ API returned error status")
            return
    except Exception as e:
        print(f"✗ Cannot connect to API: {str(e)}")
        print("\nTry using the web scraping version (fide_extractor.py) instead.")
        return
    
    # Get user input
    print("\nEnter FIDE IDs (one per line, numbers only).")
    print("Press Enter twice when done:\n")
    
    fide_ids = []
    while True:
        line = input().strip()
        if not line:
            break
        fide_ids.append(line)
    
    if not fide_ids:
        print("No FIDE IDs provided. Exiting.")
        return
    
    # Extract player data
    print(f"\nProcessing {len(fide_ids)} FIDE ID(s)...\n")
    players_data = extractor.extract_multiple_players(fide_ids)
    
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
    filename = input("Enter output filename (default: fide_players_api.xlsx): ").strip()
    if not filename:
        filename = "fide_players_api.xlsx"
    if not filename.endswith('.xlsx'):
        filename += '.xlsx'
    
    extractor.export_to_excel(players_data, filename)
    print("=" * 60)


if __name__ == "__main__":
    main()
