# Personal Finance Analyser

Easily analyse aggregated normalised personal financial data in one place.

To do so, we use the data warehouse and ETL patterns,
then we use Metabase for SQL analysis and data visualisation.
Time-permitting, we use libraries like scikit-learn for advanced analysis
such as categorisations and predictions.

## Getting Started

Dependencies
- [uv python package and project manager](https://github.com/astral-sh/uv)
- Python 3.13.2 (can be installed with `uv python install 3.13.2`)
- Docker

Steps
1. Run `docker-compose up --detach` to bring up the Docker containers
   - Use `docker-compose stop/start` to pause/unpause containers
   - Use `docker-compose down` to stop and remove the containers
   - Use `docker-compose down --volumes` to also remove the data
2. ...

## Design Overview

Docker is used to manage services we depend on like PostgreSQL and Metabase.
Containerisation decouples these services from the machine we're running the project on -
we don't need to install the services on the host machine which can be a complex step.
Instead we can easily run these dependencies on any machine that can run Docker.
It also makes upgrading easier. In the future, a Docker image can also be created for the
Python ETL part of the project to make the whole project easy to run anywhere.

