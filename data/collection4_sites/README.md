# Standortinformationen für GBV-Bibliotheken (Collection 4)

This collection contains a registry of library locations of a number of libraries partaking in the Common Library Network (GBV). The data sources, found in the `sources` subdirectory, consist of individual folders named with an ISIL containing a `.ttl` file. They were provided by as `.txt` files by <https://github.com/gbv/libsites-config> and converted to the `ttl` format using various perl modules found in <https://github.com/gbv/libsites>. Both repositories are administrated by the GBV. For more in-depth information refer to the [Konfiguration der GBV-Standortverwaltung](https://verbundwiki.gbv.de/spaces/VZG/pages/35913745/Konfiguration+der+GBV-Standortverwaltung), German only.

## Generate and Update

To generate or update the collection modify the files in the sources subfolder and run `make` from this directory. This will convert all the existing `.ttl` files into a single `collection4.nt` file using the script `convert.py` while ensuring that the individual blank nodes provided in each file are uniquely identified and do not overlap. The resulting file is saved in the parent folder `data`. 

## License

The data basis provided by <https://github.com/gbv/libsites-config> is licensed under <https://creativecommons.org/publicdomain/mark/1.0/>.