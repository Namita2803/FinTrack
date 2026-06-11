# FinTrack - Expense Management API

FinTrack is a backend application developed using FastAPI and PostgreSQL for managing personal expenses. The system provides RESTful APIs that allow users to create, retrieve, update, and delete expense records with persistent database storage.

## Features

- Create new expense records
- Retrieve all expenses
- Update existing expenses
- Delete expense records
- PostgreSQL database integration
- SQLAlchemy ORM for database operations
- Automatic API documentation using Swagger UI

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- PostgreSQL

### Tools
- pgAdmin
- Git
- GitHub
- Swagger UI

## Project Structure

```bash
FinTrack/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   └── expenses.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── README.md
└── .gitignore
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check server status |
| POST | `/expenses` | Create a new expense |
| GET | `/expenses` | Retrieve all expenses |
| PUT | `/expenses/{expense_id}` | Update an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

## Database

The project uses PostgreSQL as the database system.

Expense table structure:

| Column | Type |
|---|---|
| id | Integer |
| title | String |
| amount | Float |
| category | String |

## Setup Instructions

Clone the repository:

```bash
git clone <repository-url>
```

Move into backend:

```bash
cd FinTrack/backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
DATABASE_URL=your_postgresql_connection_url
```

Run FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Current Status

Implemented:
- Backend API architecture
- PostgreSQL connection
- Expense CRUD operations
- Database persistence

## Future Enhancements

- User authentication and authorization
- Expense filtering by date/category
- Monthly expense analytics
- Budget tracking system
- Frontend/mobile application integration

## Author

Namita Devi  
B.Tech Electronics and Instrumentation Engineering  
National Institute of Technology Silchar
