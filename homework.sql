-- 1) List all customers who live in Texas (use JOINs):
SELECT * FROM address;

SELECT CONCAT(first_name, ' ', last_name) AS "Customer", district AS "State"
FROM customer
JOIN address
ON address.address_id = customer.customer_id
WHERE district = 'Texas';

-- 1) Answer = Dorothy Taylor, Thelma Murray, Daniel Cabral, Leonard Schofield, Alfredo Mcadams
-- 5 Customers total that live in Texas



-- 2) Get all payments above $6.99 with the Customer's Full Name:

SELECT amount AS "Payments", CONCAT(first_name, ' ', last_name) AS "Full Name"
FROM payment
JOIN customer
ON customer.customer_id = payment.customer_id
WHERE amount > 6.99
ORDER BY amount ASC;

-- Answer: 1406 entries found; smallest amount = 7.98, largest amount = 11.99

-- 3) Show all customer names who have made payments over $175 (use subqueries):
-- Construct a query to display the names of customers who have made payments exceeding $175. Employ subqueries to achieve this result.

SELECT * FROM payment;

SELECT customer_id
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 175;

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name"
FROM customer
WHERE customer_id IN (
	SELECT customer_id
	FROM payment
	GROUP BY customer_id
	HAVING SUM(amount) > 175
);

-- 3) Answer: There are 6 customers who made payments over $175
-- Rhonda Kennedy, Clara Shaw, Eleanor Hunt, Marion Snyder, Tommy Collazo, Karl Seal

-- 4) List all customers that live in Nepal (use the city table):
-- Formulate a query to list all customers who reside in Nepal. You will need to utilize the city table in your query.
SELECT * FROM city;
SELECT * FROM country;

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name", country
FROM customer
JOIN address
ON customer.address_id = address.address_id
JOIN city
ON address.city_id = city.city_id
JOIN country
ON city.country_id = country.country_id
WHERE country = 'Nepal';

-- 4) Answer: There is one customer from Nepal: Kevin Schuler

-- 5) Which staff member had the most transactions?
-- Write a query to determine the staff member who conducted the highest number of transactions. Consider the appropriate tables for this task.
SELECT CONCAT(first_name, ' ', last_name) AS "Full Name", COUNT(amount)
FROM staff
JOIN payment
ON staff.staff_id = payment.staff_id
GROUP BY first_name, last_name;
-- 5) Answer: Jon Stephens has more transactions: 7304
-- Mike Hillyer has 7292


-- 6) How many movies of each rating are there?
-- Create a query that counts the number of movies for each distinct rating. Your query should display the rating category along with the corresponding count.
SELECT rating, COUNT(title) AS "Total Movies"
FROM film
GROUP BY DISTINCT rating;


-- 6) Answer: 6 distinct ratings w/ total movies: PG-13: 223, NC-17: 210, R: 195, G: 178, PG: 194

-- 7) Show all customers who have made a single payment above $6.99 (Use Subqueries):
-- Construct a query to retrieve the names of customers who have made only one payment, and the payment amount exceeds $6.99.
-- Utilize subqueries to accomplish this task.
SELECT * FROM customer;
SELECT * FROM payment;

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name"
FROM customer
WHERE customer_id IN (
SELECT customer_id
FROM payment
WHERE amount > 6.99
GROUP BY customer_id
HAVING COUNT(amount) = 1
);

-- 7) Answer: There are 130 customers who made a single payment that was above $6.99

-- 8) How many free rentals did our stores give away?
-- Write a query to calculate the total number of free rentals given away by our stores
SELECT amount FROM payment ORDER BY amount ASC;

SELECT COUNT(amount)
FROM payment
WHERE amount = 0;

-- 8) Answer: 24 free rentals were given away