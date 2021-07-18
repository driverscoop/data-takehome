#!/usr/bin/env python3
import csv
import json
import os
import sys
import tempfile

import psycopg2 as pg
import requests

DRIVERS_URL = 'https://tdc-takehome-data-server-zl3yz.ondigitalocean.app/drivers.json'
TRIPS_URL = 'https://tdc-takehome-data-server-zl3yz.ondigitalocean.app/trips.csv'
CHARGES_URL = 'https://tdc-takehome-data-server-zl3yz.ondigitalocean.app/charges.csv'


def get_postgres_conn(database_url):
  conn = pg.connect(dsn=database_url)
  cursor = conn.cursor()
  return conn, cursor



def fetch_and_load_drivers(conn, cursor):
  pass


def fetch_and_load_trips(conn, cursor):
  pass


def fetch_and_load_charges(conn, cursor):
  pass


def main(argv):
  conn, cursor = get_postgres_conn(os.environ['DATABASE_URL'])
  fetch_and_load_drivers(conn, cursor)
  fetch_and_load_trips(conn, cursor)
  fetch_and_load_charges(conn, cursor)

if __name__ == '__main__':
  main(sys.argv[1:])
