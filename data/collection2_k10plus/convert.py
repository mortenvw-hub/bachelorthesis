from rdflib import Graph, Literal, URIRef, BNode
import re

g = Graph()
id_pred = URIRef("http://purl.org/dc/elements/1.1/identifier")
name_pred = URIRef("http://xmlns.com/foaf/0.1/name")

with open("k10plus.tsv") as f:
    next(f)
    for line in f:
        entries = line.split("\t")
        if len(entries) > 4 or len(entries) < 3:
            print("invalid input data!")
            continue
        iln = Literal(f"(ILN){entries[0].strip()}")
        eln = Literal(f"(ELN){entries[1].strip()}")
        name = Literal(entries[2].strip(), lang="de")
        if len(entries) == 4 and re.match(r"^[A-Z]{1,4}\-[A-Za-z0-9\-/:]{1,11}$",entries[3].strip()):
            isil = URIRef(f"http://uri.gbv.de/organization/isil/{entries[3].strip()}")
        else:
            isil = BNode()
        try:
            g.add((isil, id_pred, iln))
            g.add((isil, id_pred, eln))
            g.add((isil, name_pred, name))
        except:
            print("Invalid row. Skipping")
            continue
print("Writing to file")
g.serialize(destination="./../collection2.nt", format="nt", encoding="utf-8")