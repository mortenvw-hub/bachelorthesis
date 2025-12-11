import re
import os

i = 0
with open("./../collection4.nt", "w") as r, os.scandir('./sources/') as d:
    for e in d:
        if e.is_dir():
            try:
                with open(f"./sources/{e.name}/sites.ttl", "r") as f:
                    mapping = {}
                    for l in f:
                        ls = l.strip(" .\n")
                        f, s, t = ls.split(" ",2)
                        res = []
                        for x in f, s, t:
                            if re.match(r"_:b\d+",x):
                                if not x in mapping:
                                    mapping[x] = f"_:c{i}"
                                    i += 1
                                res.append(mapping[x])
                            else:
                                res.append(x)
                        res.append(".\n")
                        r.write(" ".join(res))
            except:
                with open(f"./sources/{e.name}/siteof.ttl", "r") as f:
                    mapping = {}
                    for l in f:
                        ls = l.strip(" .\n")
                        f, s, t = ls.split(" ",2)
                        res = []
                        for x in f, s, t:
                            if re.match(r"_:b\d+",x):
                                if not x in mapping:
                                    mapping[x] = f"_:c{i}"
                                    i += 1
                                res.append(mapping[x])
                            else:
                                res.append(x)
                        res.append(".\n")
                        r.write(" ".join(res))

