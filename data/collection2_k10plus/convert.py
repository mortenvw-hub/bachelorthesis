from rdflib import Graph, Literal, URIRef, BNode
import re

g = Graph()
id_pred = URIRef("http://purl.org/dc/elements/1.1/identifier")
name_pred = URIRef("http://xmlns.com/foaf/0.1/name")

print("Reading source data")
with open("k10plus.tsv") as f:
    # Skip the table head
    next(f)
    for line in f:
        entries = line.split("\t")
        # Skip rows with less than three or more than four columns
        if len(entries) > 4 or len(entries) < 3:
            print("Invalid input format!")
            continue
        iln = Literal(f"(ILN){entries[0].strip()}")
        eln = Literal(f"(ELN){entries[1].strip()}")
        name = Literal(entries[2].strip(), lang="de")
        # Check if the ISIL is valid and use a Blank node if it is not
        if len(entries) == 4 and re.match(r"^[A-Z]{1,4}\-[A-Za-z0-9\-/:]{1,11}$",entries[3].strip()):
            isil = URIRef(f"http://uri.gbv.de/organization/isil/{entries[3].strip()}")
        else:
            # Print invalid ISIL if it is not intenionally left empty
            if any(x not in {"-"," ","\n"} for x in entries[3]):
                print(f"Invalid ISIL: {entries[3].strip()}")
            isil = BNode()
        # Try adding the triples to the graph
        try:
            g.add((isil, id_pred, iln))
            g.add((isil, id_pred, eln))
            g.add((isil, name_pred, name))
        except:
            print("Invalid row. Skipping")
            continue
print("Writing to collection file")
g.serialize(destination="./../collection2.nt", format="nt", encoding="utf-8")