-- DDL (Data definition language)

CREATE TABLE student (
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(40),
	last_name VARCHAR(40),
	email VARCHAR(80),
	phone INT
);

CREATE TABLE instructor (
	instructor_id SERIAL PRIMARY KEY,
	first_name VARCHAR(40),
	last_name VARCHAR(40),
	degree VARCHAR(4)
);

CREATE TABLE course(
	course_id SERIAL PRIMARY KEY,
	course_name VARCHAR(50),
	credits INT CHECK (credits > 0),
	instructor_id INT REFERENCES instructor(instructor_id)
);

-- This is our many to many table (AKA junction table)
CREATE TABLE enrollment (
	enrollment_id SERIAL PRIMARY KEY,
	student_id INT REFERENCES student(student_id),
	course_id INT REFERENCES course(course_id),
	grade CHAR(2)
);


-- DML to work with data inside the tables
INSERT INTO student (first_name, last_name, email, phone) 
VALUES ('Mary', 'Dolittle', 'marydo@email.com', 2223333),
	('Jane', 'Doe', 'jdoe@email.com', 1231234),
	('Peter', 'Parker', 'spidey@email.com', 7897894),
	('Tony', 'Stark', 'ironman@email.com', 7537894);

INSERT INTO instructor (first_name, last_name, degree)
VALUES ('Sarah', 'Dolette', 'CS'),
	('Cave', 'Johnson', 'MS'),
	('John', 'Doe', 'BB'),
	('Amanda', 'Dixie', 'ME');

INSERT INTO course (course_name, credits, instructor_id)
VALUES ('Algebra', 3, 3),
	('International Foods', 2, 4),
	('Biology', 4, 2),
	('Database Systems', 3, 1);

INSERT INTO enrollment (student_id, course_id, grade) 
VALUES (2, 3, 'A'),
	(3, 1, 'C'),
	(1, 1, 'A-'),
	(1, 2, 'B'),
	(2, 1, 'C');

-- Data Query Language:
SELECT * from enrollment;

-- Still using DML, but to change data in the enrollment table
UPDATE enrollment
SET grade = 'B'
WHERE student_id = 1 AND course_id = 1;

DELETE FROM  enrollment
WHERE grade = 'C'; -- Will delete ALL RECORDS that have a grade C!

-- DDL (Data definition language) changes structure NOT data
ALTER TABLE student
ADD COLUMN major VARCHAR(50);

SELECT * FROM student;

UPDATE student
SET major = 'Computer Science'
WHERE student_id = 1;

UPDATE student
SET major = 'Marine Biology'
WHERE student_id = 2;

UPDATE student
SET major = 'Computer Science'
WHERE student_id = 3;

UPDATE student
SET major = 'Computer Science'
WHERE student_id = 4;

-- DQL
SELECT first_name, last_name, major FROM student
WHERE major = 'Computer Science'
AND last_name LIKE 'D%'
ORDER BY last_name ASC; -- search for names starting with D

-- Scalar functions
SELECT student_id,
	UPPER(last_name) AS last_name_upper,
	LOWER(first_name) AS first_name_lower,
	LENGTH(email) AS email_length
FROM student;

-- Aggregate functions
SELECT major,
	COUNT(*) AS total_students
FROM student GROUP BY major;



