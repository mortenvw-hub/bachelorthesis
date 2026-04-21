# GBV database directory (GBV Datenbankverzeichnis) {Collection 1}

This collection contains information about catalogues and databases used in the Common Library Network (GBV). The data is sourced from <https://uri.gbv.de/database/> and additonal information can be found there. The dataset is divided in different database groups:

- Specialised information catalogues (Fachkataloge)
- University bibliographies (Hochschulbibliographien)
- National Licenses (Nationallizenzen)
- Public library catalogues (Kataloge öffentlicher Bibliotheken)
- Online Contents
- Library catalogues (Bibliothekskataloge)
- Library intern catalogues (Dienstkataloge)
- Various project specific datasets of individual libraries
- regional catalogues (Regionale Kataloge)
- Databases with the Zeitschriftendatenbank (ZDB) product seal
- Various individual databases

## Generate and Update

To generate or update the collection run `make` from this directory. This will download the different database groups directly from <https://uri.gbv.de/database/> and save them as `.ttl`- and `.rdf`-files. Afterwards the script `convert.py` will load all the data in a temporary graph and convert them to a single `collection1.nt` file. This file is saved in the parent folder `data`. 