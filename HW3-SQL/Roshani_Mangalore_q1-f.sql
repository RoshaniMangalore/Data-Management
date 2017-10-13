select count(distinct(c.customer_id)) as count from rental r join customer c on r.customer_id=c.customer_id join inventory i on r.inventory_id=i.inventory_id join film_category fc on i.film_id=fc.film_id join category ca on fc.category_id=ca.category_id and ca.name="Action" and c.active=1;