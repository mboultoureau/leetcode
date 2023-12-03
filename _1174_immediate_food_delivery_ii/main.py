SELECT ROUND(AVG(order_date=customer_pref_delivery_date) * 100, 2) as immediate_percentage
FROM Delivery AS d2
WHERE EXISTS (
    SELECT customer_id
    FROM Delivery AS d1
    GROUP BY customer_id
    HAVING MIN(d1.order_date) = d2.order_date AND d1.customer_id = d2.customer_id
)
