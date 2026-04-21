from rdflib import Graph, URIRef
import json

g = Graph()
pred = URIRef("http://www.w3.org/2004/02/skos/core#exactMatch")

try:
    # Run through all organizations in the lobid file
    with open("./../collection3_lobid/lobid.ndjson") as file:
        for line in file:
            institute = json.loads(line)

            lobid = URIRef(institute["id"])

            # Try to read out the ISIL and create corresponding uri.gbv.de URI
            try:
                gbv = URIRef("http://uri.gbv.de/organization/isil/" + institute["isil"])
                g.add((lobid, pred, gbv))
            except:
                continue

    print("Writing to file")
    g.serialize(destination="./../mapping1.nt", format="nt", encoding="utf-8")

except:
    print("In order to creat this mapping the source for collection3_lobid has to be downloaded first.")