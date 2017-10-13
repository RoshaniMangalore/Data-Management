import sys
import mysql.connector
cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='sakila')
cursor = cnx.cursor()
keyword=sys.argv[1].lower();
query = "select count(f.film_id) as count from film f, category c,film_category g where f.film_id=g.film_id and g.category_id=c.category_id and c.name='"+keyword+"'"
cursor.execute(query)
for name in cursor:
    print name[0]
cursor.close()
cnx.close()
