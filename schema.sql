CREATE DATABASE IF NOT EXISTS project_dashboard;
USE project_dashboard;

CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    team_leader VARCHAR(255) NOT NULL,
    team_members INT NOT NULL,
    start_date DATE NOT NULL,
    deadline DATE NOT NULL,
    priority VARCHAR(20) NOT NULL DEFAULT 'Medium',
    progress INT NOT NULL DEFAULT 0,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending'
);

INSERT INTO projects (project_name, team_leader, team_members, start_date, deadline, priority, progress, status) VALUES
('Inventory Tracking System', 'Aditi Rao', 4, '2026-06-01', '2026-08-15', 'High', 65, 'In Progress'),
('Alumni Networking Portal', 'Rohan Deshmukh', 3, '2026-05-15', '2026-07-30', 'Medium', 100, 'Completed'),
('Campus Event Scheduler', 'Sneha Patil', 5, '2026-06-10', '2026-09-01', 'Low', 20, 'Pending');
