# Data Engineering part

## Importing csv files in SQLite database

### Main commands

You can install the required libraries by running the following command:

```
pip install -r requirements.txt
```

I have defined one command line argument:
- The ```--datasets``` flag allows you to select which csv files you want to import into SQLite database

To import all csv files, you can run the following command:
```
python SQLite.py
```

Or if you want to import only the ads.csv file for example, you can run:
```
python SQLite.py --datasets ads
```

If you need more help with command line arguments, you can run:
```
python SQLite.py --help
```

### Code description

The different pieces of code can be found in the ```SQLite.py``` file and in the ```preprocessing.py``` file.
```SQLite.py``` is the entry point to my project. It starts by creating a database connection to the SQLite database. Then it imports the selected csv files and calls the preprocessing functions defined in ```preprocessing.py```. Finally, it creates the SQL tables.



## How to run SQL queries on the created tables?

To query the SQL tables, you first need to run the following command:
```sqlite3 pythonsqlite.db```

Then you should be able to see the available tables with ```.tables``` and the first 10 lines with:
```
SELECT * FROM ads LIMIT 10 ;
```

## Why did I choose SQLite?

- SQLite is perfect for basic development and small projects where scalability is not the priority
- SQLite is easy to set-up and use
- SQLite library is very portable and not heavy
  
However, I think that in reality, **MySQL** would be a better choice because:
- it is more adapted for large databases
- it is easily scalable
- it has user management system for multiple user access (contrary to SQLite)
- it supports more datatypes

# Data Science / Data analysis part

The analysis is conducted in the notebook **```Data_Analysis.ipynb```**. You can find the description of the objective of the analysis, the graphs of the analysis and the conclusion and next steps. 


Thanks for reading and don't hesitate to ask if something is unclear!

Romain Besombes