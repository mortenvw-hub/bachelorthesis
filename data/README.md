# Data sets and mappings for the LOD@VZG Knowledge Graph

This subfolder contains the collections and a mapping used in the LOD@VZG Knowledge Graph and scripts to generate, update and import them into the knowledge graph. The collections currently supplied are:

- GBV database directory (GBV Datenbankverzeichnis) {Collection 1}
- K10plus participants (Teilnehmende Einrichtungen am K10plus) {Collection 2}
- lobid-organisations: Gedächtnisinstitutionen im deutschsprachigen Raum {Collection 3}
- Location information for GBV libraries (Standortinformationen für GBV-Bibliotheken) {Collection 4}.

The provided mapping is called:

- lobid URI to uri.gbv.de URI mapping {Mapping 1}.

## Requirements

In order to generate, update and import the collections and the mapping the command line tools `bash`, `make` and `curl` are required. Furthermore `python` and the library [RDFLib](https://rdflib.readthedocs.io/en/stable/) are need. The required python library and a virtual environment can be created by running   

    make python

in this directory.

## Usage

Each individual collection is provided in a subdirectory with either some source to generate it or an external reference to download it from. The naming convention of the subdirectories follows `collection$ID_$ACRONYM`. Where `$ID` is the ordinal number of the collection and `$ACRONYM` is an alphanumeric sequence identifying the collection. Each subdirectory contains:

- a `Makefile`, to generate and update the collection, (mandatory),
- a `README.md`, that provides information about the collection and gives additional instructions (mandatory),
- an `$ACRONYM-metadata.json`, containing information about the collection (mandatory),
- some form of source files (optional),
- a `convert.py` script, to convert a source into a usable format (optional).

Analogously the mapping is provided in the subfolder `mapping1`. The subdirectory contains:

- a `Makefile`, to generate and update the mapping,
- a `README.md`, that provides information about the mapping and gives additional instructions,
- an `mapping1-metadata.json`, containing information about the collection,
- a `create-mapping.py` script, to create the mapping.

The mapping can only be created if the source for `collection3_lobid` is available in the matching collection directory.


The collections and the mapping can be generated and updated by running:

    make

in the corresponding subdirectory. The resulting `.nt` files will be saved in this directory and follow the naming convention `collection$ID.nt` and `mapping1.nt`.

The script `import.sh` can be used to upload all collection and the mapping to the knowledge graph at once.

## References

The structure of this subdirectory was heavily inspired by the repository [BARTOC vocabularies](https://github.com/gbv/bartoc-vocabularies).