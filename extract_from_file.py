"""
Extract FIDE player data from a text file containing IDs/names
"""

import sys
from fide_extractor import FIDEDataExtractor


def main():
    # Check if input file is provided
    if len(sys.argv) < 2:
        print("Usage: python extract_from_file.py <input_file> [output_file]")
        print("\nExample: python extract_from_file.py players_input.txt players_output.xlsx")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "fide_players_output.xlsx"
    
    # Read identifiers from file
    try:
        with open(input_file, 'r') as f:
            identifiers = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found!")
        sys.exit(1)
    
    if not identifiers:
        print("No player identifiers found in the file!")
        sys.exit(1)
    
    print("=" * 60)
    print("FIDE Data Extractor - File Input Mode")
    print("=" * 60)
    print(f"\nInput file: {input_file}")
    print(f"Output file: {output_file}")
    print(f"Players to process: {len(identifiers)}")
    print("\n" + "=" * 60 + "\n")
    
    # Create extractor and process
    extractor = FIDEDataExtractor()
    players_data = extractor.extract_multiple_players(identifiers)
    
    if not players_data:
        print("\nNo data could be extracted!")
        sys.exit(1)
    
    # Export to Excel
    extractor.export_to_excel(players_data, output_file)
    
    # Show summary
    print("\n" + "=" * 60)
    print("Extraction Summary:")
    print("=" * 60)
    print(f"Total identifiers: {len(identifiers)}")
    print(f"Successfully extracted: {len(players_data)}")
    print(f"Failed: {len(identifiers) - len(players_data)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
