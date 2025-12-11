collection: 
	curl --header "Accept-Encoding: gzip" "https://lobid.org/organisations/search?q=*&format=bulk" | gzip -d > "lobid.ndjson"
	curl "https://lobid.org/organisations/context.jsonld" > context.jsonld

	../venv/bin/python3 convert.py