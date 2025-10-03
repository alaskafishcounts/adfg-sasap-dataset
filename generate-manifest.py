#!/usr/bin/env python3
"""
Generate manifest.json for SASAP dataset to match sport dataset structure
"""

import json
import os
import glob
from datetime import datetime
from collections import defaultdict

def get_location_name_from_filename(filename):
    """Extract location name from filename"""
    # Remove path and extension
    basename = os.path.basename(filename).replace('.json', '')
    # Remove year prefix (first 4 digits)
    if basename[:4].isdigit():
        basename = basename[5:]
    # Remove species suffix (last part after last dash)
    parts = basename.split('-')
    if len(parts) > 1:
        # Remove species name (last part)
        basename = '-'.join(parts[:-1])
    return basename

def get_species_name_from_filename(filename):
    """Extract species name from filename"""
    basename = os.path.basename(filename).replace('.json', '')
    parts = basename.split('-')
    if len(parts) > 1:
        return parts[-1]
    return "unknown"

def get_year_from_filename(filename):
    """Extract year from filename"""
    basename = os.path.basename(filename).replace('.json', '')
    if basename[:4].isdigit():
        return int(basename[:4])
    return None

def get_species_id_from_path(filepath):
    """Extract species ID from file path"""
    parts = filepath.split('/')
    if len(parts) >= 2:
        return parts[-2]  # Species ID is the directory before filename
    return "unknown"

def generate_manifest():
    """Generate manifest.json for SASAP dataset"""
    
    # Find all JSON files
    json_files = glob.glob("**/*.json", recursive=True)
    
    # Organize data by location and species
    organized_data = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    location_info = {}
    species_info = {}
    
    print(f"Processing {len(json_files)} JSON files...")
    
    for filepath in sorted(json_files):
        # Skip manifest.json if it exists
        if filepath == "manifest.json":
            continue
            
        # Extract information from filepath
        parts = filepath.split('/')
        location_id = parts[0]
        species_id = parts[1] if len(parts) > 1 else "unknown"
        
        # Extract information from filename
        filename = os.path.basename(filepath)
        year = get_year_from_filename(filename)
        location_name = get_location_name_from_filename(filename)
        species_name = get_species_name_from_filename(filename)
        
        if year is None:
            continue
            
        # Store file information
        organized_data[location_id][species_id][str(year)] = filepath
        
        # Store location info
        if location_id not in location_info:
            location_info[location_id] = {
                "name": location_name.replace('-', ' ').title(),
                "slug": location_name,
                "region": "Alaska",  # Default region
                "total_files": 0,
                "species": {}
            }
        
        # Store species info
        if species_id not in species_info:
            species_info[species_id] = {
                "name": species_name.replace('-', ' ').title(),
                "slug": species_name
            }
    
    # Build the organized structure
    organized = {}
    index_locations = {}
    index_species = {}
    
    for location_id, location_data in organized_data.items():
        location_name = location_info[location_id]["name"]
        location_slug = location_info[location_id]["slug"]
        
        # Add to index
        index_locations[location_id] = location_slug
        
        # Build location structure
        location_structure = {
            "name": location_name,
            "slug": location_slug,
            "region": location_info[location_id]["region"],
            "total_files": 0,
            "species": {}
        }
        
        for species_id, species_data in location_data.items():
            species_name = species_info[species_id]["name"]
            species_slug = species_info[species_id]["slug"]
            
            # Add to species index
            if species_id not in index_species:
                index_species[species_id] = species_slug
            
            # Get years for this species
            years = sorted([int(year) for year in species_data.keys()])
            
            # Build species structure
            species_structure = {
                "name": species_name,
                "slug": species_slug,
                "files": species_data,
                "years": years,
                "latest_year": max(years) if years else None,
                "file_count": len(species_data)
            }
            
            location_structure["species"][species_id] = species_structure
            location_structure["total_files"] += len(species_data)
        
        organized[location_id] = location_structure
    
    # Calculate statistics
    total_files = sum(loc["total_files"] for loc in organized.values())
    all_years = set()
    for loc in organized.values():
        for species in loc["species"].values():
            all_years.update(species["years"])
    
    years_covered = len(all_years)
    min_year = min(all_years) if all_years else None
    max_year = max(all_years) if all_years else None
    
    # Build manifest
    manifest = {
        "version": "3.0.0",
        "metadata": {
            "generated": datetime.now().isoformat() + "Z",
            "generation_timestamp": datetime.now().isoformat(),
            "total_files": total_files,
            "format": "organized_by_location_year_species",
            "repository": "alaskafishcounts/adfg-sasap-dataset",
            "description": "SASAP Historical Fish Count Dataset",
            "source": "SASAP (Statewide Alaska Salmon Assessment Program)",
            "years_covered": years_covered,
            "locations_with_data": len(organized),
            "species_covered": len(index_species),
            "year_range": {
                "min": min_year,
                "max": max_year
            }
        },
        "index": {
            "locations": index_locations,
            "species": index_species
        },
        "organized": organized,
        "patterns": {
            "file_naming": "[YEAR]-[LOCATION]-[SPECIES].json",
            "directory_structure": "[LOCATION_ID]/[SPECIES_ID]/[FILENAME]",
            "location_id_format": "numeric",
            "species_id_format": "numeric"
        },
        "statistics": {
            "total_files": total_files,
            "total_locations": len(organized),
            "total_species": len(index_species),
            "years_covered": years_covered,
            "earliest_year": min_year,
            "latest_year": max_year
        }
    }
    
    return manifest

def main():
    """Main function"""
    print("Generating SASAP manifest...")
    
    manifest = generate_manifest()
    
    # Write manifest.json
    with open("manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✅ Manifest generated successfully!")
    print(f"📊 Statistics:")
    print(f"   - Total files: {manifest['statistics']['total_files']}")
    print(f"   - Total locations: {manifest['statistics']['total_locations']}")
    print(f"   - Total species: {manifest['statistics']['total_species']}")
    print(f"   - Years covered: {manifest['statistics']['years_covered']}")
    print(f"   - Year range: {manifest['statistics']['earliest_year']}-{manifest['statistics']['latest_year']}")
    print(f"📁 Manifest saved as: manifest.json")

if __name__ == "__main__":
    main()
