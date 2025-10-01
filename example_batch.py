"""
Example script showing how to use the FIDE extractor in batch mode
"""

from fide_extractor import FIDEDataExtractor


def main():
    # Create extractor instance
    extractor = FIDEDataExtractor()
    
    # Define players to extract (can mix FIDE IDs and names)
    players_to_extract = [
        '22538496',      # FIDE ID
        '12528374',      # FIDE ID  
        '62506241',      # FIDE ID
        '1503014',       # Magnus Carlsen
        'Gukesh D',      # Search by name
        'Praggnanandhaa' # Search by partial name
    ]
    
    print("=" * 60)
    print("FIDE Batch Extractor - Example")
    print("=" * 60)
    print(f"\nExtracting data for {len(players_to_extract)} players...\n")
    
    # Extract all players
    players_data = extractor.extract_multiple_players(players_to_extract)
    
    # Show results
    print("\n" + "=" * 60)
    print("Results Summary:")
    print("=" * 60)
    
    for player in players_data:
        print(f"\n{player.get('Name', 'Unknown')}")
        print(f"  FIDE ID: {player.get('FIDE ID', 'N/A')}")
        print(f"  Country: {player.get('Federation', 'N/A')}")
        print(f"  Ratings: {player.get('Rating std', 'N/A')} / "
              f"{player.get('Rating rapid', 'N/A')} / "
              f"{player.get('Rating blitz', 'N/A')}")
    
    # Export to Excel
    output_file = "fide_players_batch.xlsx"
    extractor.export_to_excel(players_data, output_file)
    
    print("\n" + "=" * 60)
    print(f"Done! Check {output_file} for the results.")
    print("=" * 60)


if __name__ == "__main__":
    main()
