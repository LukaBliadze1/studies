SELECT students.*, courses.course_name
FROM students
INNER JOIN enrollments ON students.student_id = enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.course_id;

-- 

SELECT courses.course_name, students.first_name, students.last_name
FROM courses
LEFT JOIN enrollments ON courses.course_id = enrollments.course_id
LEFT JOIN students ON enrollments.student_id = students.student_id;

-- 

SELECT students.first_name, students.last_name, courses.course_name
FROM students
RIGHT JOIN enrollments ON students.student_id = enrollments.student_id
RIGHT JOIN courses ON enrollments.course_id = courses.course_id;

-- 

SELECT students.first_name, students.last_name, courses.course_name
FROM students
FULL JOIN enrollments ON students.student_id = enrollments.student_id
FULL JOIN courses ON enrollments.course_id = courses.course_id;
