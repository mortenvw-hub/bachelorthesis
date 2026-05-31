# Bachelorthesis: LOD@VZG Knowledge Graph

> Technical architecture and documentation of the LOD@VZG Knowledge Graph

## Table of Contents

- [Background](#background)
- [Components](#components)
- [Install](#install)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Background

This repository was created as part of my Bachelorthesis at the Hochschule Hannover. It provides a knowledge graph for various data collections regarding library, database, archive and museum metadata. The knowledge graph is heavily influenced by and modeled after the [NFDI4Objects Knowledge Graph](https://github.com/nfdi4objects/n4o-graph). More information to the used components can be found in the [NFDI4Objects Knowledge Graph manual](https://nfdi4objects.github.io/n4o-graph/).

## Components

- [n4o-graph-importer](https://github.com/nfdi4objects/n4o-graph-importer): scripts to import data into the triple store
- [n4o-fuseki](https://github.com/nfdi4objects/n4o-fuseki): RDF triple store
- [n4o-graph-apis](https://github.com/nfdi4objects/n4o-graph-apis): web interface and public SPARQL endpoint

## Install

Start by cloning the repository. Run

    make init

in the root directory of this repository to create the `stage` and the `data/prepared_data` subdirectories. This requires the command line tool `make` to be available. Afterwards it is best to update eventually existing local images by pulling the lastest docker images. To do so run 

~~~sh
docker compose pull
~~~

in the same directory.

Afterwards a new set of containers for the LOD@VZG Knowledge Graph can be started with

~~~sh
docker compose up --force-recreate --remove-orphans -V
~~~

## Usage

The knowledge graph is currently set to a testing environment. This includes the frontend for the importer and the api as well as the base uri for the collections. This way all the api related webpages can be accessed and tested. To change this the `BASE` and `FRONTEND` variables in the dockercompose can be adjusted. Furthermore the URIs, that are set in the individual html code of the webpages in the `dockerfiles/api/templates/` folder, and the frontend URL in `data/import.sh` have to be adjusted.

The fuseki triple store can be made persistent in an easy accessable directory by uncommenting the corrsponding lines in the `docker-compose.yml`.

The importer can be accessed at <http://localhost:5020> and the SPARQL web interface at <http://localhost:8000>.

The `data/` subdirectory contains scripts and sources to genrate, update and import collections and a mapping into the graph. The included `README.md` contains more informations and instructions on how to use them. 

## Contributing

Feel free to use [GitHub issues](https://github.com/mortenvw-hub/bachelorthesis/issues) for suggestions and bug reports.

## License

This project and repository are modeled after the [NFDI4Objects Knowledge Graph](https://github.com/nfdi4objects/n4o-graph).

The files:

- `dockerfiles/api/app.py`
- `dockerfiles/api/static/style.css`

and the complete `dockerfiles/api/templates/` directory and it´s contents were copied from [n4o-graph-apis](https://github.com/nfdi4objects/n4o-graph-apis) and modified. Additionally the license file `LICENSE` was copyed from the same repository and saved under the name `MIT_LICENSE`. These files were provided under MIT License.

The file `dockerfiles/api/config.ttl` was copied from [n4o-fuseki](https://github.com/nfdi4objects/n4o-fuseki) and modified. Additionally the license file `LICENSE` was copyed from the same repository and saved under the name `APACHE_LICENSE`. These files were provided under [Apache License](http://www.apache.org/licenses/) 2.0.