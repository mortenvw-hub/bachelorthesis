from rdflib import Graph
import os

print("Writing to collection file")

g = Graph()

with os.scandir('./sources/') as sources_dir:
    # Go through all contents of the source directory and take data from the contained directories
    for dir in sources_dir:
        if dir.is_dir():
            # Data is found as sites.ttl and/or sitesof.ttl. This checks if either exists
            if os.path.isfile(f"./sources/{dir.name}/sites.ttl"):
                g.parse(f"./sources/{dir.name}/sites.ttl")
            if os.path.isfile(f"./sources/{dir.name}/siteof.ttl"):
                g.parse(f"./sources/{dir.name}/siteof.ttl")
    g.serialize("./../prepared_data/collection4.nt", format="nt", encoding="utf-8")


