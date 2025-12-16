from rdflib import Graph
import json

with open("context.jsonld") as f:
    context = json.load(f)

del context["@context"]["url"]["@type"]

with open("lobid.ndjson", "r") as f:    
    g = Graph()    
    for line in f:
        temp = json.loads(line)
        del temp["@context"]
        g.parse(data=temp , format="json-ld", context=context)
        
g.serialize(destination="./../collection3.nt", format="nt", encoding="utf-8")