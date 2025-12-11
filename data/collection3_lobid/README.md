# lobid-organisations: Gedächtnisinstitutionen im deutschsprachigen Raum (Collection 3)

This collection contains informations about libraries, archives and museums in German-speaking areas. The data is sourced from the [lobid.org project](https://lobid.org/organisations), which is run by the North Rhine-Westphalian Library Service Centre (hbz). The data found there is in turn stemming from the German [ISIL-directory](https://isil.staatsbibliothek-berlin.de/startseite) and master data of the [library statistic](https://www.hbz-nrw.de/produkte/bibliotheksstatistik).

## Generate and Update

To generate or update the collection run `make` from this directory. This will download the data from the [lobid-organisations API](https://lobid.org/organisations/api/de). Please refer to their [API usage-policy](https://lobid.org/usage-policy/) before attempting this. The data is probide in the `jsonld`-format and a corresponding `context.jsonld` is downloaded afterwards. 

Afterwards the `.jsonld` file is converted into a `collection3.nt` file using the script `convert.py`. This conversion also verifies the data and removes broken entries. This can take a lot of time. The resulting file is saved in the parent folder `data`.