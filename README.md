# ADFG SASAP Historical Fish Count Dataset

**96 years of historical fish count data (1922-2017) across 148 locations and 21 species**

## Dataset Overview

This repository contains the complete SASAP (Statewide Alaska Salmon Assessment Program) historical fish count dataset, converted to the ADFG standard format for compatibility with the Alaska Fish Count App.

### Statistics
- **Total Files**: 8,147 JSON files
- **Time Period**: 1922-2017 (96 years)
- **Locations**: 148 monitoring stations
- **Species**: 21 different fish species
- **Format**: ADFG JSONDataSet standard

## Data Structure

Each JSON file follows the ADFG standard format:

```json
{
  "COLUMNS": [
    "YEAR",
    "COUNTDATE",
    "FISHCOUNT",
    "SPECIESID",
    "COUNTLOCATIONID",
    "COUNTLOCATION",
    "SPECIES"
  ],
  "DATA": [
    [year, date, count, species_id, location_id, location_name, species_name],
    ...
  ],
  "metadata": {
    "location_id": 2000,
    "species_id": "410",
    "year": "1921",
    "totalRecords": 92,
    "totalCount": 652968,
    "source": "SASAP",
    "last_updated": "2025-10-02T17:53:43.852640"
  }
}
```

## Location Directory Structure

Files are organized by location ID in the following structure:
```
[LOCATION_ID]/
  [SPECIES_ID]/
    [YEAR]-[LOCATION]-[SPECIES].json
```

## Monitoring Locations (148 Total)

### Southeast Alaska
- akalura, anan, andrews, auke, ayakulik, bear, big, black, buskin, chelatna, chignik, chilkat, chilkoot, coghill, crescent, cripple, disappearance, dog, duck, eagle, eek, egegik, eshamy, falls, fish, ford, frazer, frosty, george, goodnews, hackett, harris, hatchery, hetta, horse, hugh, igushik, ilnik, italio, jordan, judd, kadashan, kah, kanalku, kanektok, karluk, karta, kasilof, kegan, kenai, ketili, king, klag, klakas, klawock, kluckshu, kogrukluk, kook, kuthai, kutlaku, kvichak

### Southcentral Alaska
- lake, larson, litnik, little, malina, mcdonald, mclees, middle, miles, mill, morris, mortensens, mountain, naha, nahlin, nakina, naknek, natzuhini, nelson, neva, nushagak, orzinski, pasagshak, pauls, peterson, pilot, pleasant, politofski, portage, ratz, red, redfish, redoubt, salmon, salt, saltery, sandy, sarkar, sashin, seal, sitkoh, situk, slippery, snake, speel, sturgeon, summer

### Interior Alaska
- tahltan, takotna, tatlawiksuk, tatsamenie, telaquana, thin, thorsheim, togiak, uganik, ugashik, upper, ward, warm, whale, windfall, wood, yehring

## Species Coverage

The dataset includes data for 21 fish species:
- **Salmon**: Chinook (430), Sockeye (410), Coho (440), Pink (420), Chum (450)
- **Steelhead**: Upstream (470), Downstream (460)
- **Whitefish**: Least Cisco (510), Humpback (520), Broad (550)
- **Other**: Sheefish/Inconnu (540), Mixed (560), Non-target (999)

## Data Sources

- **Primary Source**: SASAP (Statewide Alaska Salmon Assessment Program)
- **Original Format**: Converted from legacy SASAP format
- **Conversion Date**: October 2, 2025
- **Standard**: ADFG JSONDataSet format v3.0.0

## Usage

This dataset is designed for use with the Alaska Fish Count App and follows the same data structure as other ADFG datasets. Files can be accessed directly via GitHub raw URLs:

```
https://raw.githubusercontent.com/alaskafishcounts/adfg-sasap-dataset/master/[LOCATION_ID]/[SPECIES_ID]/[FILENAME].json
```

## Historical Coverage

- **Earliest Data**: 1922 (Chignik River)
- **Latest Data**: 2017
- **Most Complete Locations**: Karluk, Chignik River, Pilot Station
- **Data Gaps**: Some locations have intermittent coverage

## Quality Assurance

- All files validated for JSON syntax
- Metadata verified for consistency
- Column structure standardized
- Data integrity preserved during conversion

## Repository Information

- **Repository**: https://github.com/alaskafishcounts/adfg-sasap-dataset
- **Organization**: Alaska Fish Counts
- **License**: Public Domain
- **Last Updated**: October 2, 2025

## Related Datasets

- [ADFG Sport Dataset](https://github.com/alaskafishcounts/adfg-sport-dataset)
- [ADFG Commercial Dataset](https://github.com/alaskafishcounts/adfg-commercial-dataset)
- [Alaska Fish Count App](https://github.com/alaskafishcounts/afcapp-repo-0101)

## Contact

For questions about this dataset, please contact the Alaska Fish Counts project team.

---

*This dataset represents one of the most comprehensive historical fish count collections in Alaska, spanning nearly a century of salmon and other fish species monitoring data.*
