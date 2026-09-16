USE MohSchoolAPI;

INSERT INTO Teacher VALUES
(1,'James','Carter','jcarter@school.edu','612-555-0101','2015-08-01',72000,'Mathematics','Full-Time'),
(2,'Laura','Mitchell','lmitchell@school.edu','612-555-0102','2017-01-15',68000,'English','Full-Time'),
(3,'David','Nguyen','dnguyen@school.edu','612-555-0103','2019-03-10',65000,'Science','Full-Time'),
(4,'Sandra','Lee','slee@school.edu','612-555-0104','2020-08-20',61000,'History','Full-Time'),
(5,'Robert','Jones','rjones@school.edu','612-555-0105','2016-06-01',70000,'Computer Science','Full-Time'),
(6,'Maria','Garcia','mgarcia@school.edu','612-555-0106','2021-08-15',58000,'Art','Part-Time'),
(7,'Kevin','Brown','kbrown@school.edu','612-555-0107','2018-09-01',66000,'PE','Full-Time'),
(8,'Angela','Wilson','awilson@school.edu','612-555-0108','2022-01-10',55000,'Music','Part-Time');

INSERT INTO Faculty VALUES
(1,'Alice','Johnson','ajohnson@school.edu','612-555-0201','2014-08-01','Science'),
(2,'Brian','Smith','bsmith@school.edu','612-555-0202','2016-01-15','Mathematics'),
(3,'Carol','White','cwhite@school.edu','612-555-0203','2017-03-10','English'),
(4,'Daniel','Taylor','dtaylor@school.edu','612-555-0204','2018-08-20','History'),
(5,'Emily','Anderson','eanderson@school.edu','612-555-0205','2019-06-01','CS'),
(6,'Fred','Thomas','fthomas@school.edu','612-555-0206','2020-08-15','Art'),
(7,'Grace','Jackson','gjackson@school.edu','612-555-0207','2015-09-01','PE'),
(8,'Henry','White','hwhite@school.edu','612-555-0208','2021-01-10','Music');

INSERT INTO Students VALUES
(1,'Liam','Walker',3.85,'2022-09-01','2026-05-15'),
(2,'Olivia','Scott',3.50,'2022-09-01','2026-05-15'),
(3,'Noah','Reed',2.95,'2023-09-01','2027-05-15'),
(4,'Emma','Collins',3.70,'2023-09-01','2027-05-15'),
(5,'Oliver','Morris',2.60,'2024-09-01','2028-05-15'),
(6,'Ava','Rogers',3.90,'2024-09-01','2028-05-15'),
(7,'Elijah','Cook',3.10,'2021-09-01','2025-05-15'),
(8,'Sophia','Murphy',2.80,'2021-09-01','2025-05-15');

INSERT INTO Courses VALUES
(1,'Algebra II','MATH201',1,2,4,'MWF 8','Room 301',30),
(2,'Literature','ENG202',2,3,3,'TTh 9','Room 205',25),
(3,'Biology','SCI101',3,1,4,'MWF 10','Room 401',28),
(4,'History','HIS201',4,4,3,'TTh 11','Room 210',30),
(5,'Intro CS','CS101',5,5,3,'MWF 1','Room 105',25),
(6,'Art','ART101',6,6,2,'TTh 2','Room 502',20);

INSERT INTO Classes (Course_ID, Student_ID, Grade) VALUES
(1,1,'A'),
(1,2,'B'),
(2,3,'A'),
(2,4,'B+'),
(3,5,'C+'),
(3,6,'A'),
(4,7,'B'),
(4,8,'C');


SELECT * FROM Students;

