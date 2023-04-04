import psycopg2
from datetime import date



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

# query = '''
# CREATE TABLE jobs (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(300) NOT NULL,
#     gain INT NOT NULL,
#     expiration_date DATE NOT NULL,
#     lang BOOLEAN NOT NULL DEFAULT false,
#     city VARCHAR(50) NOT NULL
# );
# # '''
# query = '''
# ALTER TABLE jobs DROP COLUMN city;
# ALTER TABLE jobs RENAME COLUMN gain TO salary;
# ALTER TABLE jobs ADD COLUMN company VARCHAR(50);
# '''

# info_list = [
#     # basliq, sirket, maas, bitme tarixi, xarici dil telebi
#     ('iOS developer', 'A2Z Technologies', 3500, '2022-07-18', True),
#     ('Tender üzrə mütəxəssis', 'A2Z Technologies', 1500, '2022-06-11', False),
#     ('Məlumat bazası üzrə inzibatçı', 'ABB ASC', 1500, '2022-07-12', True),
#     ('Database Administrator', 'A2Z Technologies', 2500, '2022-07-14', True),
#     ('Front-End Developer', 'AzəriMed QSC', 1500, '2022-07-23', False),
#     ('Proqram təminatının testləşdirilməsi üzrə mühəndis',
#      'ABB ASC', 1500, '2022-08-10', False),
#     ('Back-end üzrə proqramçı', 'ABB ASC', 4100, '2022-07-11', True),
#     ('Biznes analitika üzrə Baş mütəxəssis ', 'ABB ASC', 2200, '2022-07-03', True),
#     ('Android proqramçı', 'ABB ASC', 1300, '2022-07-22', True),
#     ('Front-end üzrə proqramçı', 'ABB ASC', 3200, '2022-07-06', True),
#     ('Full stack PHP proqramçı', 'AzəriMed QSC', 2400, '2022-07-17', False),
#     ('Avtomatlaşdırılmış əməliyyat sistemi üzrə proqramçı',
#      'ABB ASC', 2700, '2022-07-15', True),
#     ('Proqram təminatı üzrə mühəndis', 'Kontakt Home', 2700, '2022-07-13', False),
#     ('Hüquqşünas', 'Kontakt Home', 1500, '2022-07-03', False),
#     ('Çatdırılma xidmətləri üzrə fəhlə', 'Kontakt Home', 500, '2022-07-15', True),
#     ('PHP developer', 'ARIS', 1500, '2022-07-11', True),
#     ('Məhsul üzrə menecer', 'Kontakt Home', 2800, '2022-07-05', True),
#     ('Proqram təminatı üzrə aparıcı mühəndis',
#      'Kontakt Home', 2500, '2022-07-02', False),
#     ('İT sənədləşməsi üzrə mütəxəssis', 'Azericard', 1500, '2022-07-25', True),
#     ('Information Security Specialist', 'DEFSCOPE LLC', 2500, '2022-07-03', False),
#     ('IT Helpdesk', 'Azericard', 1500, '2022-07-30', True),
#     ('Cybersecurity Business Development Internship',
#      'DEFSCOPE LLC', 2900, '2022-07-19', False),
#     ('Vue.js developer', 'ARIS', 1500, '2022-07-29', True),
# ]



# query = '''
# INSERT INTO jobs (title, company, salary, expiration_date, lang) VALUES(%s, %s, %s, %s, %s)
# '''
# for row in info_list:
#     cursor.execute(query, row)


# query = '''
# SELECT * FROM jobs WHERE
# '''

# query = '''
# SELECT * FROM jobs WHERE company= 'ABB ASC';
# '''
# query = '''
# SELECT * FROM jobs WHERE company= 'ABB ASC' AND salary<2000;
# '''
# query = '''
# SELECT * FROM jobs WHERE company= 'Kontakt Home' AND expiration_date < '2022-07-10';
# '''
# query = '''
# SELECT * FROM jobs WHERE lang = false AND salary >= 2500;
# '''
# query = '''
# SELECT * FROM jobs WHERE title ~ 'proqramçı$';
# '''
# query = '''
# SELECT * FROM jobs WHERE title NOT LIKE '%end%' AND title NOT LIKE '%End%'
# '''
# query = '''
# SELECT * FROM jobs WHERE title LIKE 'IT%' OR title LIKE 'İT%'
# '''
# query = '''
# SELECT * FROM jobs WHERE lang = True ORDER BY salary
# '''
# query = '''
# SELECT MAX(salary) AS Highest_Salary FROM jobs 
# '''
# query = '''
# SELECT * FROM jobs WHERE expiration_date < '2022-07-10' ORDER BY expiration_date LIMIT 3 OFFSET 2
# '''
# query = '''
# SELECT * FROM jobs WHERE lang = False and title LIKE '%developer%' OR title LIKE '%proqramçı%'
# '''
# query = '''
# SELECT * FROM jobs WHERE company = 'Kontakt Home' OR company = 'AzəriMed QSC' OR company = 'A2Z Technologies' AND salary BETWEEN 2500 AND 3000
# '''
# query = '''
# SELECT COUNT(*) FROM jobs WHERE company = 'ABB ASC' and expiration_date < '2022-07-10'
# '''
# query = '''
# SELECT MAX(salary) FROM jobs WHERE lang = False
# '''
# query = '''
# SELECT MIN(salary) FROM jobs WHERE lang = True
# '''
# query = '''
# SELECT AVG(salary) FROM jobs WHERE title LIKE '%developer%' OR title LIKE '%proqramçı%'
# '''
# query = '''
# SELECT SUM(salary) FROM jobs WHERE company = 'Kontakt Home' OR company = 'AzəriMed QSC' OR company = 'A2Z Technologies'
# '''




