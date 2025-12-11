collection: 
	> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/fachopac?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/hb?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/nl?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/oeb?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/olcssg?format=ttl" -O ->> dbs.ttl
#	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/opac?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/owc?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/proj?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/rk?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/test?format=ttl" -O ->> dbs.ttl
	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/zdb?format=ttl" -O ->> dbs.ttl

	wget --quiet -N --no-if-modified-since "https://uri.gbv.de/database/opac?format=rdfxml" -O -> dbs.rdf
	
	../venv/bin/python3 convert.py
	