# Bachelorarbeit: LOD@VZG Knowledge Graph

> Technical architecture and documentation of the LOD@VZG Knowledge Graph

## Background

This repository was created as part of my Bachelorthesis at the Hochschule Hannover. It provides a knowledge graph for various data collections regarding library, archive and museum metadata. The knowledge graph is heavily influenced and modeled after the [NFDI4Objects Knowledge Graph](https://github.com/nfdi4objects/n4o-graph). More information to the used components can be found in the [NFDI4Objects Knowledge Graph manual](https://nfdi4objects.github.io/n4o-graph/).

## Components

- [n4o-graph-importer](https://github.com/nfdi4objects/n4o-graph-importer): scripts to import data into the triple store
- [n4o-fuseki](https://github.com/nfdi4objects/n4o-fuseki): RDF triple store
- [n4o-graph-apis](https://github.com/nfdi4objects/n4o-graph-apis): web interface and public SPARQL endpoint

## Install

Start by cloning the repository. Afterwards it is best to update eventually existing local images by pulling the lastest docker images. To do so run 

~~~sh
docker compose pull
~~~

in the root directory of this repository.

Afterwards a new set of containers for the LOD@VZG Knowledge Graph can be started with

~~~sh
docker compose up --force-recreate --remove-orphans -V
~~~

## Usage

The importer can be accessed at <http://localhost:5020> and the SPARQL web interface at <http://localhost:8000>.

The `data/` subdirectory contains scripts and sources to genrate, update and import collections into the graph. The included `Readme.md` contains more informations and instructions on how to use them. 

## License

This project and repository are modeled after the [NFDI4Objects Knowledge Graph](https://github.com/nfdi4objects/n4o-graph).

The files in the subdirectory `dockerfiles/api/`, excluding the `dockerfiles/api/queries/` folder, were copied from [n4o-graph-apis](https://github.com/nfdi4objects/n4o-graph-apis) and modified.

The file `dockerfiles/api/config.ttl` was copied from [n4o-fuseki](https://github.com/nfdi4objects/n4o-fuseki) and modified.