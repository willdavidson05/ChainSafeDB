-- Create table
DROP TABLE IF EXISTS sensitive_table;

CREATE TABLE sensitive_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    amount REAL NOT NULL,
    timestamp TEXT NOT NULL
);

-- Insert sample data
INSERT INTO sensitive_table (name, email, amount, timestamp) VALUES
('Megan Quinn', 'mq@example.com', 199.99, '2024-04-05T10:15:00Z'),
('Bob Smith', 'bob@example.com', 250.00, '2024-04-05T11:30:00Z'),
('Charlie Kim', 'charlie@example.com', 75.49, '2024-04-05T12:45:00Z');
