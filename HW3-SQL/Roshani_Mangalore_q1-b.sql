select count(f.film_id) as count , c.name as category_name from film f, category c,film_category g where f.film_id=g.film_id and g.category_id=c.category_id group by c.name order by c.name;
