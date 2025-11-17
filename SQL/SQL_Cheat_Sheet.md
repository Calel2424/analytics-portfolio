# SQL Cheat Sheet

Quick reference for common SQL patterns used in data analysis.

---

## Basic SELECT

```sql
SELECT column1, column2
FROM table_name;

SELECT *
FROM table_name
WHERE price > 10;

SELECT *
FROM table_name
WHERE city = 'Paris';

SELECT *
FROM table_name
WHERE name LIKE 'A%';

SELECT *
FROM table_name
ORDER BY amount DESC;

SELECT *
FROM table_name
ORDER BY city ASC, amount DESC;

SELECT
  COUNT(*)        AS row_count,
  SUM(amount)     AS total_amount,
  AVG(amount)     AS avg_amount,
  MIN(amount)     AS min_amount,
  MAX(amount)     AS max_amount
FROM table_name;

SELECT region, SUM(amount) AS total_sales
FROM sales
GROUP BY region;

SELECT region, SUM(amount) AS total_sales
FROM sales
GROUP BY region
HAVING SUM(amount) > 10000;

-- Inner join
SELECT *
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id;

-- Left join
SELECT *
FROM customers c
LEFT JOIN orders o
  ON c.customer_id = o.customer_id;

SELECT *
FROM orders
WHERE amount > (
  SELECT AVG(amount) FROM orders
);

SELECT
  TRIM(name)              AS name_trimmed,
  LOWER(email)            AS email_lower,
  COALESCE(country,'N/A') AS country_clean
FROM customers;

