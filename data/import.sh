#!/bin/bash

for dir in */; do
    dir=${dir%/}
    collection=${dir%_*}
    collection=${collection##*n}
    
    [ -e "$dir/${dir##*_}-metadata.json" ] || continue

    curl -X POST -H "Content-Type: application/json" -d @./$dir/${dir##*_}-metadata.json "http://localhost:5020/collection/"
done

for file in *.nt; do
    collection=${file%.*}
    collection=${collection##*n}
    
    curl -X POST "http://localhost:5020/collection/${collection}/receive?from=${file}"
    curl -X POST "http://localhost:5020/collection/${collection}/load" 
done