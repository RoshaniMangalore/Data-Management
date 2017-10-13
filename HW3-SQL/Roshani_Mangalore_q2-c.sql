select a.customer_id from action_view a left join horror_view h on a.customer_id=h.customer_id where h.customer_id is NULL;
