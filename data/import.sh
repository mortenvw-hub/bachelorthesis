#!/bin/bash

# Go through all collection directorys and upload metadata to the importer
for dir in collection*/; do
    dir=${dir%/}
    collection=${dir%_*}
    collection=${collection##*n}
    
    [ -e "$dir/${dir##*_}-metadata.json" ] || continue

    curl --silent --fail -X POST -H "Content-Type: application/json" -d @./$dir/${dir##*_}-metadata.json "http://localhost:5020/collection/"
done

# Go through all collection data and upload the to the importer
for file in collection*.nt; do
    collection=${file%.*}
    collection=${collection##*n}
    
    curl --silent --fail -X POST "http://localhost:5020/collection/${collection}/receive?from=${file}"
    curl --silent --fail -X POST "http://localhost:5020/collection/${collection}/load" 
done

# Upload the mapping data and metadata to the importer
curl --silent --fail -X POST -H "Content-Type: application/json" -d @./mapping1/mapping1-metadata.json "http://localhost:5020/mappings/"
curl --silent --fail -X POST "http://localhost:5020/mappings/1/receive?from=mapping1.nt"
curl --silent --fail -X POST "http://localhost:5020/mappings/1/load" 

