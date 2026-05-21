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

# Go through all mapping directorys and upload metadata to the importer
for dir in mapping*/; do
    dir=${dir%/}
    mapping=${dir%_*}
    mapping=${mapping##*g}
    
    [ -e "$dir/${dir##*_}-metadata.json" ] || continue

    curl --silent --fail -X POST -H "Content-Type: application/json" -d @./$dir/${dir}-metadata.json "${importer}mappings/"
done

# Go through all mapping data and upload the to the importer
for file in prepared_data/mapping*.nt; do
    source=${file##*/}
    mapping=${file%.*}
    mapping=${mapping##*g}
    
    curl --silent --fail -X POST "${importer}mappings/${mapping}/receive?from=${source}"
    curl --silent --fail -X POST "${importer}mappings/${mapping}/load" 
done