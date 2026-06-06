from flask import Blueprint, request, jsonify
from model import db, Ticket, Note
import uuid
from sqlalchemy import case 

bp = Blueprint('api', __name__)

@bp.route('/api/tickets', methods=['POST'])
def create_ticket():
    data = request.json
    if not data or 'customer_name' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_id = f"TKT-{uuid.uuid4().hex[:6].upper()}"
    new_ticket = Ticket(
        ticket_id=new_id,
        customer_name=data.get('customer_name'),
        customer_email=data.get('customer_email'),
        subject=data.get('subject'),
        description=data.get('description'),
        status='Open'
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({"ticket_id": new_ticket.ticket_id}), 201

@bp.route('/api/tickets', methods=['GET'])
def get_tickets():
    search_term   = request.args.get('search', '').strip()
    status_filter = request.args.get('status', '').strip()

    query = Ticket.query

    if search_term:
        search_pattern = f"%{search_term}%"
        query = query.filter(
            (Ticket.customer_name.ilike(search_pattern)) |
            (Ticket.ticket_id.ilike(search_pattern))
        )

    if status_filter and status_filter != 'All':
        query = query.filter(Ticket.status == status_filter)

    tickets = query.order_by(Ticket.created_at.desc()).all()

    return jsonify([{
        "ticket_id":     t.ticket_id,
        "customer_name": t.customer_name,
        "subject":       t.subject,
        "status":        t.status
    } for t in tickets]), 200