# Drivers Coop Data Engineering Takehome

This is a takehome technical project for applicants to The Drivers Cooperative.

Please read this README in its entirety before getting started.

## How to take this test

The goal is to write a script similar to the ones we use in production at TDC.
In the followup discussion after you finish working on the takehome, you'll
discuss your solution and how you arrived at it.

Please don't spend more than 3-5 hours on this project. If you don't have a full solution at the end of 3-5 hours, think about how you would complete the project and send it in.

To submit, create a branch called `first-last` and commit your changes there.
Next, push your branch to a repo on your personal GitHub and share to
`jasonprado`. Email `jobs@drivers.coop` or your previous contact (probably
Jason) to let us know you're done. In your email also include answers to the
questions at the bottom of this README.

## Getting Started via GitPod

This repo is configured to work with [Gitpod](https://gitpod.io/), and so if you'd rather skip
any local installation that may be required, you can:

1. Clone this and push its code to one you create, privately, on your own github.

2. Then, take the current URL and add 'https://gitpod.io/#' to the beginning of the URL, so
   it would look something like: http://gitpod.io/#https://github.com/driverscoop/data-takehome.

GitPod will ask you to sign in and then present you with a ready to go development
environment with PostgreSQL, Python, and all dependencies installed.

You'll also be logged into git locally already, and can create your branch to submit
and push your solution from there.

If you run into issues with this setup, please let us know at jobs@drivers.coop!

## Getting Started Locally

1. Get PostgreSQL up and running. You can see instructions
   [here (for Mac OS)](https://postgresapp.com/) or
   [here (for Windows)](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).
   If it's taking more than a few minutes, send an email to
   [jason@drivers.coop](mailto:jason@drivers.coop) and we'll set up a
   small remote database for you. In order to run the migrations and tests,
   you'll need Postgresql running locally on 5432. If you'd like to use a
   remote Postgres or local postgres running on a different port, just
   set `export DATABASE_URL=<your database url>`.

2. Install Python 3 and `pip install -r requirements.txt`.

3. Create the database to run the tests. You may find it easiest to pop into `psql`:

```
$ psql
psql (12.2, server 11.8)
Type "help" for help.

root=# create database tdc_test;
CREATE DATABASE
```

## Background

The data storage systems we use at TDC pull in data from a variety of sources such as logistics partners and credit card processors. We load this data into relational databases from JSON or CSV files fetched over the web.

The URLs of the data files can be found at the top of `etljob/etljob.py`. These
are simplified versions of real formats we use; our actual models have many more
fields.

## Objective

In this project you will find references to three sample data files that
represent a simplified structure of TDC's data model. The files represent
drivers, trips, and credit card charges. Your goal is to load all three of these
files into a PostgreSQL database in an ETL (Extract-Transform-Load) job. The end
result should be three tables: `drivers`, `trips`, and `charges`, each filled
with the appropriate data fetched from the web.

## Notes

* The `drivers`, `trips`, and `charges` tables should have reasonable schemas
  with uniqueness and foreign key constraints.
* The script should create the `drivers`, `trips`, and `charges` tables if they
  do not exist. If they exist the script should not lose data currently in them.
* Running the script multiple times with new inputs should add new data while
  updating existing rows, as defined by their `id` fields. This is referred to
  as an _upsert_.
* Running the script multiple times with the same input should not modify the
  database and should not error.
* Don't needlessly take up resources but focus on correctness and clarity over
  potential runtime performance.
* You will probably want to load the CSV data into a temporary table and then
  figure out how to merge it into the main table.

## Documentation

* PostgreSQL can load data directly from CSV very quickly using `COPY FROM`.
  This is accessible through psycopg2:
  https://www.psycopg.org/docs/cursor.html#cursor.copy_from
  * PostgreSQL also
  has features for loading JSON but Jason hasn't been able to make them work, so
  either teach Jason how or consider converting JSON files to CSV for input.
* _Upserts_ in PostgreSQL are implemented using `INSERT ON CONFLICT`:
  https://www.postgresqltutorial.com/postgresql-upsert/


## Questions
Please include answers to these two questions in your email to us upon
completing the project.

1. Sometimes our credit card processor fails and a charge is dropped even if the
   trip is completed and logged. What query will find trips without charges?
1. It's important to find drivers who have _churned_–that is, drivers who have
   done trips previously but not in the past two weeks. How can you find such
   drivers? (For the purposes of this question consider `NOW() = 2021-07-11`)


## Acknowledgements

Huge thanks to [Politics Rewired](https://politicsrewired.com/) for the
structure of this document.
