-- Join sales, products, and promotions to calculate real margin
SELECT 
    s.sale_id,
    s.sale_date,
    s.total_price AS revenue,
    (s.quantity * p.cost_price) AS total_cost,
    (s.total_price - (s.quantity * p.cost_price)) AS profit,
    -- Margin percentage rounded to 2 decimal places
    ROUND(((s.total_price - (s.quantity * p.cost_price)) / NULLIF(s.total_price, 0)) * 100, 2) AS margin_pct,
    p.product_name,
    p.category,
    pr.promo_name
FROM sales s
LEFT JOIN products p ON s.product_id = p.product_id
LEFT JOIN promotions pr ON s.product_id = pr.product_id;