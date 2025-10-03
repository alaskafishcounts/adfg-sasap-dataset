#!/usr/bin/env python3
"""
Generate README table for SASAP dataset with GitHub links
"""

import json
import os

def load_manifest():
    """Load the manifest.json file"""
    with open('manifest.json', 'r') as f:
        return json.load(f)

def get_species_name(species_id):
    """Get species name from ID"""
    species_map = {
        "410": "sockeye",
        "420": "pink", 
        "430": "coho",
        "440": "chinook",
        "450": "chum",
        "460": "steelhead-up",
        "470": "steelhead-down",
        "480": "whitefish",
        "490": "sheefish",
        "500": "mixed",
        "999": "non-target"
    }
    return species_map.get(species_id, f"species-{species_id}")

def generate_location_table():
    """Generate the location table for README"""
    
    manifest = load_manifest()
    organized = manifest['organized']
    
    # Sort locations by ID
    sorted_locations = sorted(organized.items(), key=lambda x: int(x[0]))
    
    table_rows = []
    table_rows.append("| Location ID | Location Name | Species Available |")
    table_rows.append("|-------------|---------------|-------------------|")
    
    for location_id, location_data in sorted_locations:
        location_name = location_data['name']
        species_list = []
        
        # Get species for this location
        for species_id, species_data in location_data['species'].items():
            species_name = get_species_name(species_id)
            species_link = f"<a href=\"https://github.com/alaskafishcounts/adfg-sasap-dataset/tree/master/{location_id}/{species_id}\">{species_name}</a>"
            species_list.append(species_link)
        
        # Create location link
        location_link = f"<a href=\"https://github.com/alaskafishcounts/adfg-sasap-dataset/tree/master/{location_id}\">{location_name}</a>"
        
        # Format species list
        if species_list:
            species_text = ", ".join(species_list)
        else:
            species_text = "-"
        
        # Add row
        table_rows.append(f"| {location_id} | {location_link} | {species_text} |")
    
    return "\n".join(table_rows)

def main():
    """Main function"""
    print("Generating SASAP README table...")
    
    table = generate_location_table()
    
    # Write to file
    with open("location_table.md", "w") as f:
        f.write(table)
    
    print("✅ Location table generated successfully!")
    print("📁 Table saved as: location_table.md")
    print("\n" + "="*50)
    print("TABLE PREVIEW:")
    print("="*50)
    print(table[:2000] + "..." if len(table) > 2000 else table)

if __name__ == "__main__":
    main()
