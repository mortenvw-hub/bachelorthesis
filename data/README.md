# Data sets for the LOD@VZG Knowledge Graph

This subfolder contains the collections used in the LOD@VZG Knowledge Graph and scripts to generate, update and import them into the knowledge graph. The collections currently supplied are:

- GBV Datenbankverzeichnis (Collection 1)
- Teilnehmende Einrichtungen am K10plus (Collection 2)
- lobid-organisations: Gedächtnisinstitutionen im deutschsprachigen Raum (Collection 3)
- Standortinformationen für GBV-Bibliotheken (Collection 4)

## Requirements

In order to generate, update and import the collections the command line tools `bash`, `make` and `curl` are required. Furthermore `python` and the library [RDFLib](https://rdflib.readthedocs.io/en/stable/) are need. The required python library and a virtual environment can be created by running   

    make python

in this directory.

## Usage

Each individual collection is provided in a subdirectory with either some source to generate it or an external reference to download it from. The naming convention of the subdirectories follows `collection$ID_$ACRONYM`. Where `$ID` is the ordinal number of the collection and `$ACRONYM` is an alphanumeric sequence identifying the collection. Each subdirectory contains:

- a `Makefile`, to generate and update the collection, (mandatory),
- a `README.md`, that provides information about the collection and gives additional instructions (mandatory),
- an `$ACRONYM-metadata.json`, containing information about the collection (mandatory),
- some form of source files (optional),
- a `convert.py` script, to convert a source into a usable format (optional).

The collections can be generated and updated by running:

    make

in the corresponding subdirectory. The resulting `.nt` files will be saved in this directory and follow the naming convention `collection$ID.nt`.

The script `import.sh` can be used to upload all collection to the knowledge graph at once.

## References

The structure of this subdirectory was heavily inspired by the repository [BARTOC vocabularies](https://github.com/gbv/bartoc-vocabularies).