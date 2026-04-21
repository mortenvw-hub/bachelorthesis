# lobid URI to uri.gbv.de URI mapping {Mapping 1}

This mapping describes the relation between lobid URIs for organisations of the form `http://lobid.org/organisations/isil/$ISIL#!` and uri.gbv.de URIs for organisations of the form `http://uri.gbv.de/organization/$ISIL`. `$ISIL` corresponds to the International Standard Identifier for Libraries and Related Organizations of the organisation. The relation between the URIs is specified as an exact match using the `http://www.w3.org/2004/02/skos/core#exactMatch` property.

## Generate and Update

In order to create this mapping the source file for `collection3_lobid`, which is called `lobid.ndjson` and can be found in the collection folder after generating the collection, has to be loaded first. Afterwards running `make` in this directory will generate the mapping using the `create-mapping.py` programm and save it as `mapping1.nt` in the parent folder `data`. 