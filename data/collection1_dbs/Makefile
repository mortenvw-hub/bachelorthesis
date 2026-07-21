collection:
	> dbs.ttl
	curl -s "https://uri.gbv.de/database/?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/fachopac?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/hb?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/nl?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/oeb?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/olcssg?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/owc?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/proj?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/rk?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/test?format=ttl" >> dbs.ttl
	curl -s "https://uri.gbv.de/database/zdb?format=ttl" >> dbs.ttl

	curl -s "https://uri.gbv.de/database/opac?format=rdfxml" > dbs.rdf
	
	../venv/bin/python3 convert.py
	