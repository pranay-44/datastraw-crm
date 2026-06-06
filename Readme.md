Datastraw CRM — Customer Support Ticketing System
A full stack web application for managing customer support tickets, built as part of the Datastraw Technologies internship assessment.
Live Demo

Coming soon (deployment in progress)

Tech Stack
LayerTechnologyBackendPython 3, FlaskDatabaseSQLite via SQLAlchemy ORMFrontendHTML, Vanilla JS, CSSDeploymentRailway.app (in progress)
Features

Create Tickets — Submit tickets with customer name, email, subject, and description. Auto-generates a unique ID (e.g. TKT-4F3344) and timestamp.
List All Tickets — Dashboard table showing ID, customer name, subject, and status.
Search — Real time search across customer name and ticket ID as you type.
Filter by Status — Filter tickets by Open, In Progress, or Closed.
View & Update Tickets — (in progress) Detail page to view full description and update status or add notes.

Project Structure
Datastraw-crm/
├── static/
│   ├── script.js       # Frontend JS — fetch, render, search, filter
│   └── style.css       # Styling
├── templates/
│   └── index.html      # Main dashboard page
├── app.py              # Flask app — config, routes, DB init
├── model.py            # SQLAlchemy models — Ticket, Note
├── routes.py           # REST API endpoints
├── requirements.txt    # Python dependencies
└── .gitignore
API Endpoints
MethodEndpointDescriptionPOST/api/ticketsCreate a new ticketGET/api/ticketsList all tickets (supports ?status= and ?search=)GET/api/tickets/<ticket_id>Get full ticket details with notesPUT/api/tickets/<ticket_id>Update status or add a note
Local Setup
bash# 1. Clone the repository
git clone https://github.com/pranay-44/datastraw-crm.git
cd datastraw-crm

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
Open your browser at http://127.0.0.1:5000
Database
SQLite is used for simplicity and portability. The database file (crm.db) is auto-created on first run — no manual setup required. Two tables:

tickets — stores all ticket data
notes — stores comments linked to tickets

Author
Pranay Bhalerao
Assessment submission for Datastraw Technologies — AI & Tech Intern role