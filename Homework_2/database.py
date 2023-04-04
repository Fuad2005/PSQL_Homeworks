import psycopg2
connection = psycopg2.connect(
    user = 'postgres',
    password = '0556476163',
    host = 'localhost',
    port = '5432',
    database = 'jobsad'
)

cursor = connection.cursor()

def show(cursor):
    print(*[desc[0].ljust(15) for desc in cursor.description], sep='')
    print('-'*80)
    print('\n'.join(''.join(str(z).ljust(35) for z in i) for i in cursor.fetchall()))


query = '''
UPDATE jobs SET salary = salary * 1.15 WHERE expiration_date < '2022-07-10' AND salary < 2000
'''
query = '''
DELETE FROM jobs WHERE title ~ 'PHP'
'''




query = '''
SELECT * FROM jobs
'''


cursor.execute(query)
show(cursor)