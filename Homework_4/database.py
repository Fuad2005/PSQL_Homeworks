import psycopg2

connection = psycopg2.connect(
    user = 'postgres',
    password = '0556476163',
    host = 'localhost',
    port = '5432',
    database = 'ecommerce'
)

cursor = connection.cursor()

def show(cursor):
    print(*[desc[0].ljust(15) for desc in cursor.description], sep='')
    print('-'*80)
    print('\n'.join(''.join(str(z).ljust(20) for z in i) for i in cursor.fetchall()))




query = '''
CREATE TABLE tag (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50)
);
CREATE TABLE seller (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
    CREATE TABLE product (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        price FLOAT NOT NULL,
        seller_id INT,
        CONSTRAINT seller_fk
        FOREIGN KEY (seller_id)
        REFERENCES seller(id)
        ON DELETE CASCADE
    );

CREATE TABLE wishlist (
    id SERIAL PRIMARY KEY,
    customer_id INT UNIQUE,
    CONSTRAINT customer_fk
    FOREIGN KEY (customer_id)
    REFERENCES customer(id)
    ON DELETE CASCADE
);
CREATE TABLE review (
    id SERIAL PRIMARY KEY,
    rate INT,
    customer_id INT,
    product_id INT,
    CONSTRAINT customer_review_fk
    FOREIGN KEY (customer_id)
    REFERENCES customer(id)
    ON DELETE SET NULL,
    CONSTRAINT product_review_fk2
    FOREIGN KEY (product_id)
    REFERENCES product(id)
    ON DELETE CASCADE
);
CREATE TABLE product_tags (
    id SERIAL PRIMARY KEY,
    product_id INT,
    tag_id INT,
    CONSTRAINT prod_id_fk
    FOREIGN KEY (product_id)
    REFERENCES product(id),
    CONSTRAINT tag_id_fk
    FOREIGN KEY (tag_id)
    REFERENCES tag(id)
);
'''
data = [
   {
      "title": "M&M Food Market",
      "price": "17.0616609356653"
   },
   {
      "title": "Soprole",
      "price": "11.6234613464323"
   },
   {
      "title": "Kinder",
      "price": "2.62073436454904"
   },
   {
      "title": "Andy Capp's fries",
      "price": "14.6864611770429"
   },
   {
      "title": "Bewley's",
      "price": "7.01804420073426"
   },
   {
      "title": "Vitta Foods",
      "price": "4.5093621385793"
   },
   {
      "title": "Taco Bell",
      "price": "19.1318949810843"
   },
   {
      "title": "Sun-Pat",
      "price": "9.6603184191791"
   },
   {
      "title": "Baskin robbins",
      "price": "16.105171543595"
   },
   {
      "title": "Wendy's",
      "price": "5.43620887838128"
   },
   {
      "title": "Cobblestone",
      "price": "7.22419333514953"
   },
   {
      "title": "Wonder Bread",
      "price": "14.6278888390529"
   },
   {
      "title": "Lavazza",
      "price": "10.305469252777"
   },
   {
      "title": "Kinder",
      "price": "19.4697343713929"
   },
   {
      "title": "Soprole",
      "price": "16.3448767300439"
   },
   {
      "title": "Nabisco",
      "price": "2.48867588838966"
   },
   {
      "title": "Tic Tac",
      "price": "2.60812248457601"
   },
   {
      "title": "Magnum",
      "price": "19.4421954995218"
   },
   {
      "title": "Papadopoulos",
      "price": "19.4472127819654"
   },
   {
      "title": "Wonder Bread",
      "price": "12.7520409541913"
   },
   {
      "title": "Papadopoulos",
      "price": "1.811215852765"
   },
   {
      "title": "Olymel",
      "price": "7.34511601847835"
   },
   {
      "title": "Domino",
      "price": "7.64364533249459"
   },
   {
      "title": "Pizza Hut",
      "price": "12.6648227300797"
   },
   {
      "title": "Red Lobster",
      "price": "10.0007594130005"
   },
   {
      "title": "Andy Capp's fries",
      "price": "18.5981898673802"
   },
   {
      "title": "Secret Recipe",
      "price": "18.6991437984161"
   },
   {
      "title": "Sun-Pat",
      "price": "3.15631274094633"
   },
   {
      "title": "Magnum",
      "price": "10.3542353042188"
   },
   {
      "title": "Heinz",
      "price": "17.7369680049536"
   },
   {
      "title": "Olymel",
      "price": "19.9154627821015"
   },
   {
      "title": "Taco Bell",
      "price": "10.9514749045258"
   },
   {
      "title": "Dunkin' Donuts",
      "price": "11.479457990024"
   },
   {
      "title": "Applebee's",
      "price": "15.7718961763996"
   },
   {
      "title": "Knorr",
      "price": "10.4961827092321"
   },
   {
      "title": "KFC",
      "price": "12.4794360452702"
   },
   {
      "title": "Domino",
      "price": "17.0641279993877"
   },
   {
      "title": "Knorr",
      "price": "2.66790023197788"
   },
   {
      "title": "Kits",
      "price": "18.8862874209351"
   },
   {
      "title": "Dunkin' Donuts",
      "price": "7.84475450163929"
   },
   {
      "title": "Applebee's",
      "price": "13.4456292886499"
   },
   {
      "title": "Nutella",
      "price": "4.63776473637566"
   },
   {
      "title": "Bewley's",
      "price": "13.0057596485157"
   },
   {
      "title": "Kits",
      "price": "1.38640394266062"
   },
   {
      "title": "Nesquik",
      "price": "6.1496629436266"
   },
   {
      "title": "KFC",
      "price": "15.6723103028128"
   },
   {
      "title": "Andy Capp's fries",
      "price": "17.8805946269448"
   },
   {
      "title": "Tic Tac",
      "price": "7.01679017348997"
   },
   {
      "title": "Andy Capp's fries",
      "price": "7.87038087466284"
   },
   {
      "title": "Bel Group",
      "price": "10.6127773935966"
   }
]




# for info in data:

#     cursor.execute("INSERT INTO product (title, price) VALUES (%s, %s)", (info['title'], info['price']))

#     connection.commit()





# cursor.execute(query)

rows = 'SELECT * FROM product'
cursor.execute(rows)
show(cursor)