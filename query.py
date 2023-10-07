import pandas as pd
import sqlite3

# connect to the database
conn = sqlite3.connect('db/movies.db')

# create cursor object
click = conn.cursor()

# create table
click.execute('''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        name TEXT,
        genre TEXT,
        year INTEGER,
        ibdb_rating REAL
)
''')

conn.commit()


# Query the table
query = '''
SELECT id as 'Movie_ID', name as 'Movie_Title', imdb_rating as 'Rating'
FROM movies
WHERE genre = 'horror' AND year <= 1985
ORDER BY imdb_rating DESC 
LIMIT 3;
'''

# provide output of query as a DataFrame for visual ease / as required to standard
df = pd.read_sql(query, conn)

#Display the dataframe
print(df)

conn.close()