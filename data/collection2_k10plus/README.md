# Teilnehmende Einrichtungen am K10plus (Collection 2)

This collection contains information about institutions partaking in the K10plus-catalogue. The data source is provided as a tabular `.tsv`-file and is sourced from the [BSZ-GBV-Wiki for the K10plus](https://wiki.k10plus.de/spaces/K10PLUS/pages/27361288/Teilnehmende+Einrichtungen+am+K10plus) provided by the Library Service Centre for Baden-Württemberg (BSZ) and the Common Library Network (GBV). Additional information can be found there. The table contains columns with information to the institutions:

- Internal Library Number (ILN)
- External Library Number (ELN)
- Name of the institution
- Inernational Standard Identifier for Libraries and Related Organizations (ISIL)

## Generate and Update

To generate or update the collection modify the `k10plus.tsv` file and run `make` from this directory. This will convert the tabular data to a `collection2.nt` file using the script `convert.py`. The resulting file is saved in the parent folder `data`. 