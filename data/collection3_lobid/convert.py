from rdflib import Graph
import json


with open("lobid.ndjson", "r") as f:    
    g = Graph()
    for line in f:
        try:
            test = Graph()
            test.parse(data=line , format="json-ld", context="context.jsonld")
            test.serialize(format="nt")            
            g.parse(data=line , format="json-ld", context="context.jsonld")
        except:
            temp = json.loads(line)
            del temp["url"]
            g.parse(data=temp , format="json-ld", context="context.jsonld")

g.serialize(destination="./../collection3.nt", format="nt", encoding="utf-8")