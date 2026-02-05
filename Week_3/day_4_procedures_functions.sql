-- Subqueries
SELECT * FROM enrollment

-- Students enfrolled in more than one course
SELECT * FROM student
WHERE student_id IN (
	SELECT student_id
	FROM enrollment
	GROUP BY student_id
	HAVING COUNT(enrollment.course_id)> 1
);

-- Courses that no student enrolled in
SELECT * FROM course
WHERE course_id NOT IN (
	SELECT course_id FROM enrollment
);

-- Students who are not enrolled in any course
SELECT * FROM student 
WHERE student_id NOT IN (
	SELECT student_id FROM enrollment
);

-- Stored Procedures
-- are prepared SQL code that you can save and reuse
-- good for if you have a SQL query that gets used over and over again

CREATE PROCEDURE selectAllStudents()
LANGUAGE plpgsql
AS $$
BEGIN
SELECT * FROM student;
END;
$$

CALL selectAllStudents();

-- We can also give our stored procedures parameters

CREATE PROCEDURE selectCSStudents(p_major VARCHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
SELECT * FROM student WHERE major = p_major;
END $$;

CALL selectCSStudents('Computer Science');


-- Functions return a value, while stored procedures do not
CREATE OR REPLACE FUNCTION get_course_count(p_student_id INT)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
	total_courses INT;
BEGIN
	SELECT COUNT(*)
	INTO total_courses
	FROM enrollment
	WHERE student_id = p_student_id;
	RETURN total_courses;
END;
$$;

SELECT 
	first_name,
	last_name,
	get_course_count(student_id) AS course_count
FROM student;

SELECT * FROM student
