CREATE TABLE residents (
	resident_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	apartment_id INT REFERENCES apartments(apartment_id)
);

CREATE TABLE cars (
	car_id SERIAL PRIMARY KEY,
	make VARCHAR(25),
	model VARCHAR(25),
	year INT,
	license_plate VARCHAR(10),
	owner_id INT REFERENCES residents(resident_id)
);


CREATE TABLE apartments (
	apartment_id SERIAL PRIMARY KEY,
	building_letter VARCHAR(2),
	room_number INT,
	monthly_rent DECIMAL(5, 2)
);

ALTER TABLE apartments
ALTER COLUMN monthly_rent TYPE DECIMAL(6, 2);

CREATE TABLE pets (
	pet_id SERIAL PRIMARY KEY,
	breed VARCHAR(50),
	name VARCHAR(50),
	apartment_id INT,
	is_service_animal BOOL
);

INSERT INTO apartments (building_letter, room_number, monthly_rent)
VALUES ('B', 101, 600.00),
	('B', 102, 750.00),
	('A', 500, 1250.00),
	('A', 404, 1050.00),
	('C', 202, 750.00),
	('C', 204, 750.00);

SELECT * FROM apartments;

INSERT INTO residents (first_name, last_name, apartment_id)
VALUES ('Jon', 'Smith', 3),
	('Sally', 'Sitwell', 5),
	('Terry', 'Spoon', 1),
	('Trevor', 'Goodchild', 4),
	('Aeon', 'Flux', 6),
	('Adam', 'Apple', 2);

INSERT INTO cars (make, model, year, license_plate, owner_id) 
VALUES ('Hyundai', 'Elantra', 2016, 'THX-5838', 1),
	('Ford', 'Mustang', 1960, 'BTY-3944', 3),
	('Subaru', 'Forester', 2020, '637-YRTR', 6);

INSERT INTO pets (breed, name, apartment_id, is_service_animal)
VALUES ('Longhair cat', 'Mr. Wiskers', 1, False),
	('Shorthair tabby cat', 'Olivia', 6, False),
	('Maine Coon', 'Benson', 2, True);

SELECT * 
FROM residents;

SELECT residents.first_name, residents.last_name
FROM residents
JOIN apartments ON residents.apartment_id=apartments.apartment_id
WHERE building_letter = 'B'

SELECT AVG(monthly_rent) AS average_monthly_rent
FROM apartments
WHERE building_letter = 'C'

SELECT COUNT(pet_id) as total_number_of_pets
FROM pets;
