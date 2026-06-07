from rdflib import Graph, Literal, URIRef, BNode
import re
import csv

g = Graph()
id_pred = URIRef("https://schema.org/identifier")
name_pred = URIRef("https://schema.org/name")

print("Reading source data")
with open("k10plus.tsv", newline='') as f:
    reader = csv.reader(f, delimiter="\t")
    # Skip the table head
    next(reader)
    for row in reader:
        # Skip rows with less than three or more than four columns
        if len(row) != 4:
            print("Invalid input format!")
            continue
        iln = Literal(f"(ILN){row[0].strip()}")
        eln = Literal(f"(ELN){row[1].strip()}")
        name = Literal(row[2].strip(), lang="de")
        # Check if the ISIL is valid and use a Blank node if it is not
        if len(row) == 4 and re.match(r"^([A-Za-z0-9]{1}|[A-Z]{2}|[A-Za-z0-9]{3,4})\-[A-Za-z0-9\-\/:]{1,11}$",row[3].strip()):
            isil = URIRef(f"http://uri.gbv.de/organization/isil/{row[3].strip()}")
        else:
            # Print invalid ISIL if it is not intenionally left empty
            if any(x not in {"-"," ","\n"} for x in row[3]):
                print(f"Invalid ISIL: {row[3].strip()}")
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
g.serialize(destination="./../prepared_data/collection2.nt", format="nt", encoding="utf-8")