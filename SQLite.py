# Importing the necessary packages
import sqlite3
from sqlite3 import Error
import pandas as pd
import argparse
from preprocessing import users_preprocessing, ads_preprocessing, ads_transaction_preprocessing, referrals_preprocessing

# Parsing the flah --dataset argument
parser = argparse.ArgumentParser(description='This is the parser for the GensDeConfiance data exercise - Romain Besombes')
parser.add_argument('--datasets', default=['ads','ads_transaction','referrals','users'], choices=['ads','ads_transaction','referrals','users'],
                    nargs='+', help='Choose the tables you want to import to SQL', required=False)
args = parser.parse_args()
datasets = args.datasets


def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file) # If the given database name does not exist then this call will create the database
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, df):
    """ create a SQL table from the given pandas Dataframe df
    :param conn: Connection object
    :param df: pandas Dataframe
    :return:
    """
    try:
        # Write the data to a sqlite table 
        df.to_sql(df.name, conn, if_exists='replace', index=False) 
    except Error as e:
        print(e)


def main():
    """ call the create_connection() and create_table() functions for each selected table
    """

    # Path for the database
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)

    for df_name in datasets:
        # Importing dataframes
        df_temp = pd.read_csv(df_name+'.csv', index_col=0)
        df_temp.name = df_name

        # Preprocessing
        if df_temp.name == 'users':
            df_temp = users_preprocessing(df_temp)
            df_temp.name = df_name

        elif df_temp.name == 'ads':
            df_temp = ads_preprocessing(df_temp)
            df_temp.name = df_name
        
        elif df_temp.name == 'ads_transaction':
            df_temp = ads_transaction_preprocessing(df_temp)
            df_temp.name = df_name
        
        elif df_temp.name == 'referrals':
            df_temp = referrals_preprocessing(df_temp)
            df_temp.name = df_name

        # create tables
        if conn is not None:
            create_table(conn, df_temp)
            print(f'table {df_name} created!')
        else:
            print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()