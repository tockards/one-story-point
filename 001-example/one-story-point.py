import argparse
import sqlite3
from database_setup import sqlite_file

def cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("query",help="Query either the features or story")
    return parser.parse_args()


def process(conn, query):
    with conn as cur:
        print(cur.execute(query).fetchall())



def main():
    args = cmd_args()
    connection = sqlite3.connect(sqlite_file)
    query = args.query
    process(connection, query)



if __name__ == '__main__':
    main()