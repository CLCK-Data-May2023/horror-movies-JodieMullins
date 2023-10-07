import pandas as pd 
import sqlite3



# connection to database to work with data
conn = sqlite3.connect('db/movies.db')

# create cursor to click the data into place
click = conn.cursor()

# I don't want to re-write my query; I want it to pull from the file
# click.execute('sql/horror_movies.sql')

with open('sql/horror_movies.sql', 'r') as f:
    query_script = f.read()

click.executescript(query_script)

conn.commit()

final_view = pd.read_sql(query_script, conn)

print(final_view)



conn.close()

