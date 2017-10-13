select f.title, c.name from film f, category c,film_category g where f.film_id=g.film_id and g.category_id=c.category_id order by f.title;
