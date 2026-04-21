import re
import os

# Count number of encountered different blank nodes to generate new ids
node_counter = 0

print("Writing to collection file")

with open("./../collection4.nt", "w") as output, os.scandir('./sources/') as sources_dir:
    # Go through all contents of the source directory and take data from the contained directories
    for dir in sources_dir:
        if dir.is_dir():
            # Data is either found as sites.ttl or sitesof.ttl
            try:
                with open(f"./sources/{dir.name}/sites.ttl", "r") as file:
                    # Mapping to remember old blank node id and new blank node id relation for current file
                    mapping = {}
                    # Run through all triples in the file
                    for line in file:
                        line_clean = line.strip(" .\n")
                        sub, pred, obj = line_clean.split(" ",2)
                        res_triple = []
                        # Run through triple components and check if they are blank nodes
                        for component in sub, pred, obj:
                            if re.match(r"_:b\d+",component):
                                # If the component is a blank node and was not encountert before add it to the mapping
                                if not component in mapping:
                                    mapping[component] = f"_:c{node_counter}"
                                    node_counter += 1
                                # Add new blank node id to result triple
                                res_triple.append(mapping[component])
                            else:
                                # Keep original non blank node component
                                res_triple.append(component)
                        # Write triple to the output file
                        res_triple.append(".\n")
                        output.write(" ".join(res_triple))
            except:
                with open(f"./sources/{dir.name}/siteof.ttl", "r") as file:
                    # Mapping to remember old blank node id and new blank node id relation for current file
                    mapping = {}
                    # Run through all triples in the file
                    for line in file:
                        line_clean = line.strip(" .\n")
                        sub, pred, obj = line_clean.split(" ",2)
                        res_triple = []
                        # Run through triple components and check if they are blank nodes
                        for component in sub, pred, obj:
                            if re.match(r"_:b\d+",component):
                                # If the component is a blank node and was not encountert before add it to the mapping
                                if not component in mapping:
                                    mapping[component] = f"_:c{node_counter}"
                                    node_counter += 1
                                # Add new blank node id to result triple
                                res_triple.append(mapping[component])
                            else:
                                # Keep original non blank node component
                                res_triple.append(component)
                        # Write triple to the output file
                        res_triple.append(".\n")
                        output.write(" ".join(res_triple))

