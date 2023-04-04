import psycopg2

import psycopg2
connection = psycopg2.connect(
    user = 'postgres',
    password = '0556476163',
    host = 'localhost',
    port = '5432',
    database = 'hospital'
)

cursor = connection.cursor()

def show(cursor):
    print(*[desc[0].ljust(15) for desc in cursor.description], sep='')
    print('-'*80)
    print('\n'.join(''.join(str(z).ljust(35) for z in i) for i in cursor.fetchall()))


# query = '''
# CREATE TABLE sobe (
#     id SERIAL PRIMARY KEY,
#     hekim_id INT
# );
# '''

# query = '''
# CREATE TABLE hekim(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50)
# )
# '''

# query = '''
# CREATE TABLE meqale(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100) NOT NULL,
#     həkim_id INT,
#     category_id INT
# )
# '''

# query = '''
# CREATE TABLE kateqoriya(
#     id SERIAL PRIMARY KEY,
#     həkim VARCHAR(50)
# )
# '''






# query = '''
# ALTER TABLE sobe
# ADD CONSTRAINT hekim_fk
# FOREIGN KEY (hekim_id)
# REFERENCES hekim(id)
# '''

# query = '''
# ALTER TABLE meqale
# ADD CONSTRAINT hekim_fk
# FOREIGN KEY (həkim_id)
# REFERENCES hekim(id)
# '''

# query = '''
# ALTER TABLE meqale
# ADD CONSTRAINT category_fk
# FOREIGN KEY (category_id)
# REFERENCES kateqoriya(id)
# '''






# query = '''
# SELECT * FROM meqale
# '''


cursor.execute(query)
connection.commit()
# show(cursor)