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
- Git LFS

Steps
1. Run `docker-compose up --detach` to bring up the Docker containers
   - Use `docker-compose stop/start` to pause/unpause containers
   - Use `docker-compose down` to stop and remove the containers
   - Use `docker-compose down --volumes` to also remove the data
   - Use `docker-compose up --build` to build images before starting containers
2. Run `uv run setup-all` to setup the DB
3. During development, run `uv run ruff format` to format the code

## Design Overview

Docker is used to manage services we depend on like PostgreSQL and Metabase.
Containerisation decouples these services from the machine we're running the project on -
we don't need to install the services on the host machine which can be a complex step.
Instead we can easily run these dependencies on any machine that can run Docker.
It also makes upgrading easier. In the future, a Docker image can also be created for the
Python ETL part of the project to make the whole project easy to run anywhere.

## Structuring the Raw Data

We have to organise and store the raw data before we can process it.
We'll organise the CSV files under the data/ directory by status, organisation, and account.

Some assumptions we make to simplify the requirements at the cost of extendability:
- All accounts are held by the same account holder.
- The account number will be read from its directory name.
- We only process financial statements of transactions.

> In a production system, user uploaded files could be stored in a cloud storage service like AWS S3.
We wouldn't necessarily need an opinionated directory structure or siloed buckets, as upload metadata (stored in a DB table)
would point to the uploaded files and tie them to their respective banks, accounts, owners, descriptions, and more.

The two states for the data are "raw" and "processed".
CSVs are finicky and brittle. We'll almost certainly have to do some cleaning
(e.g. remove junk lines, sort data manually if timestamps lack precision, fix encoding issues).
Given that this is a public repository, we don't want to store raw-text sensitive data.
The "raw" directory will contain gitignored files that live locally on my computer.
The "processed" directory will contain cleaned and encrypted files that are staged in git.
We'll use anonymous names for the orgs (e.g. org1, org2, org3).

I debated whether to anonymise the actual transaction data. In practice we wouldn't want to because
the data would lose meaning. But for presentation purposes I might do basic anonymisation.

We'll use an off-the-shelf algorithm from the Advanced Encryption Standard (AES) for encryption at rest.

CSVs files are assets, not source files, and can become quite large. We'll use Git LFS to store them.

<details>
<summary>Click to expand a visual of the proposed directory hierarchy</summary>

```
data/
├── raw/
│   ├── org_a/
│   │   ├── account_a1/
│   │   │   ├── statement_2021.csv
│   │   │   └── statement_2022.csv
│   │   └── account_a2/
│   │       ├── statement_2021.csv
│   │       └── statement_2022.csv
│   └── org_b/
│       └── account_b1/
│           ├── statement_2021.csv
│           └── statement_2022.csv
└── processed/  # <--- programmatically mirrors the raw hierarchy, files are cleaned and encrypted
    ├── org_a/
    │   ├── account_a1/
    │   │   ├── statement_2021.csv.enc
    │   │   └── statement_2022.csv.enc
    │   └── account_a2/
    │       ├── statement_2021.csv.enc
    │       └── statement_2022.csv.enc
    └── org_b/
        └── account_b1/
            ├── statement_2021.csv.enc
            └── statement_2022.csv.enc
```

</details>

