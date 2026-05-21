#!/bin/bash
set -euo pipefail

importer=$1

# Go through all collection directorys and upload metadata to the importer
for dir in collection*/; do
    dir=${dir%/}
    collection=${dir%_*}
    collection=${collection##*n}
    
    [ -e "$dir/${dir##*_}-metadata.json" ] || continue

    curl --silent --fail -X POST -H "Content-Type: application/json" -d @./$dir/${dir##*_}-metadata.json "${importer}collection/"
done

# Go through all collection data and upload the to the importer
for file in prepared_data/collection*.nt; do
    source=${file##*/}
    collection=${file%.*}
    collection=${collection##*n}
    
    curl --silent --fail -X POST "${importer}collection/${collection}/receive?from=${source}"
    curl --silent --fail -X POST "${importer}collection/${collection}/load" 
done

# Upload the mapping data and metadata to the importer
curl --silent --fail -X POST -H "Content-Type: application/json" -d @./mapping1/mapping1-metadata.json "${importer}mappings/"
curl --silent --fail -X POST "${importer}mappings/1/receive?from=mapping1.nt"
curl --silent --fail -X POST "${importer}mappings/1/load" 

