# Project Ledger — Project Management Dashboard

A lightweight internal dashboard for tracking team projects: status, priority,
progress, and deadlines, with search and filtering.

Built with **Flask**, **MySQL (PyMySQL)**, and a custom design system
(no frontend framework dependency beyond Chart.js for the status chart).

## Features

- Dashboard with live stat cards (Total / Completed / In Progress / Pending)
- Search projects by name, filter by status
- Add / Edit / Delete projects
- Per-project progress ring and priority/status tags
- Status breakdown doughnut chart

## Tech Stack

| Layer     | Tool               |
|-----------|---------------------|
| Backend   | Flask (Python)       |
| Database  | MySQL via PyMySQL    |
| Frontend  | Jinja2 templates, custom CSS, Chart.js |

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create the database:
   ```bash
   mysql -u root -p < schema.sql
   ```

3. Copy `.env.example` to `.env` and fill in your MySQL credentials, then
   export them (or use a tool like `python-dotenv`):
   ```bash
   cp .env.example .env
   export $(cat .env | xargs)
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Visit `http://localhost:5000`

## Project Structure

```
app.py              Flask routes and DB queries
schema.sql           Table schema + sample data
templates/           Jinja2 templates (base, dashboard, add, edit)
static/css/style.css Design system (colors, type, components)
```

## Notes

Database credentials are read from environment variables — never commit a
`.env` file (already covered by `.gitignore`).
