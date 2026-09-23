# RDS Connectivity

Database: `studentdb`
Engine: MySQL
Port: `3306`
Public access: No

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    course VARCHAR(100) NOT NULL
);

INSERT INTO students (name, email, course)
VALUES
('Siddarth', 'siddarth@example.com', 'Computer Science'),
('Shrusti', 'shrusti@example.com', 'Computer Science');
```

Never publish the database password.
