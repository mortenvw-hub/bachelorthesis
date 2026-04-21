from rdflib import Graph
import json

with open("context.jsonld") as f:
    context = json.load(f)
# Turn URLs into literals because of invalid characters for URIs
del context["@context"]["url"]["@type"]
# Add reference to avoid local URIs caused by a typo in the source
context["@context"]["Organisation"] = "https://schema.org/Organization"

with open("lobid.ndjson", "r") as f:    
    g = Graph()    
    for line in f:
        temp = json.loads(line)
        # Remove old context reference in the data and use modified context
        del temp["@context"]
        g.parse(data=temp , format="json-ld", context=context)

print("Writing to collection file")        
g.serialize(destination="./../collection3.nt", format="nt", encoding="utf-8")