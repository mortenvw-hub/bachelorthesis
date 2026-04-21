#!/bin/bash

for dir in */; do
    dir=${dir%/}
    collection=${dir%_*}
    collection=${collection##*n}
    
    [ -e "$dir/${dir##*_}-metadata.json" ] || continue

    curl --silent --fail -X POST -H "Content-Type: application/json" -d @./$dir/${dir##*_}-metadata.json "http://localhost:5020/collection/"
done

for file in collection*.nt; do
    collection=${file%.*}
    collection=${collection##*n}
    
    curl --silent --fail -X POST "http://localhost:5020/collection/${collection}/receive?from=${file}"
    curl --silent --fail -X POST "http://localhost:5020/collection/${collection}/load" 
done

curl --silent --fail -X POST -H "Content-Type: application/json" -d @./mapping1/mapping1-metadata.json "http://localhost:5020/mappings/"
curl --silent --fail -X POST "http://localhost:5020/mappings/5/receive?from=mapping1.nt"
curl --silent --fail -X POST "http://localhost:5020/mappings/5/load" 

