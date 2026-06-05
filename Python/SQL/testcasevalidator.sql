-- =========================
-- STUDENT TABLE
-- =========================

CREATE TABLE Student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
);

INSERT INTO Student VALUES
(1, 'Rahul', 85),
(2, 'Priya', 72),
(3, 'Amit', 91),
(4, 'Neha', 68),
(5, 'Rohan', 55);

-- =========================
-- TEST CASE MASTER
-- Stores:
-- 1. What to test
-- 2. Query used
-- 3. Expected result
-- =========================

CREATE TABLE TestCaseMaster (
    test_case_id INT AUTO_INCREMENT PRIMARY KEY,
    test_case_title VARCHAR(100),
    test_case_sql TEXT,
    expected_output VARCHAR(100)
);

INSERT INTO TestCaseMaster
(test_case_title, test_case_sql, expected_output)
VALUES
(
    'Minimum 3 students above 70',
    'SELECT COUNT(*) FROM Student WHERE marks > 70',
    'count >= 3'
);

INSERT INTO TestCaseMaster
(test_case_title, test_case_sql, expected_output)
VALUES
(
    'No negative marks',
    'SELECT COUNT(*) FROM Student WHERE marks < 0',
    'count = 0'
);

-- =========================
-- TEST EXECUTION TABLE
-- Stores:
-- Pass/Fail results
-- =========================

CREATE TABLE TestCaseExecution (
    execution_id INT AUTO_INCREMENT PRIMARY KEY,
    test_case_id INT,
    result VARCHAR(20),
    remarks VARCHAR(200)
);

-- =========================
-- EXECUTE TEST CASE 1
-- Minimum 3 students above 70
-- =========================

INSERT INTO TestCaseExecution
(test_case_id, result, remarks)
SELECT
    1,
    CASE
        WHEN COUNT(*) >= 3
        THEN 'Passed'
        ELSE 'Failed'
    END,
    CASE
        WHEN COUNT(*) >= 3
        THEN 'At least 3 students scored above 70'
        ELSE 'Less than 3 students scored above 70'
    END
FROM Student
WHERE marks > 70;

-- =========================
-- EXECUTE TEST CASE 2
-- No negative marks
-- =========================

INSERT INTO TestCaseExecution
(test_case_id, result, remarks)
SELECT
    2,
    CASE
        WHEN COUNT(*) = 0
        THEN 'Passed'
        ELSE 'Failed'
    END,
    CASE
        WHEN COUNT(*) = 0
        THEN 'No negative marks found'
        ELSE 'Negative marks found'
    END
FROM Student
WHERE marks < 0;

-- =========================
-- FINAL REPORT
-- =========================

SELECT
    m.test_case_title,
    e.result,
    e.remarks
FROM TestCaseMaster m
JOIN TestCaseExecution e
ON m.test_case_id = e.test_case_id;