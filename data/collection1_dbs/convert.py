from rdflib import Graph

g = Graph()
g.parse("dbs.ttl")
g.parse("dbs.rdf")
g.serialize("./../collection1.nt", format="nt", encoding="utf-8")
