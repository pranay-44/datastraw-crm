document.addEventListener('DOMContentLoaded', function () {
    const tbody        = document.getElementById('ticketBody');
    const searchInput  = document.getElementById('searchInput');
    const statusFilter = document.getElementById('statusFilter');
    const ticketForm   = document.getElementById('ticketForm');
 
    
    function statusBadge(status) {
        const cls = status === 'Open' ? 'badge-open'
                  : status === 'In Progress' ? 'badge-progress'
                  : 'badge-closed';
        return `<span class="badge ${cls}">${status}</span>`;
    }
 
    async function fetchTickets() {
        const status = statusFilter.value;
        const search = searchInput.value.trim();
        const url = `/api/tickets?status=${encodeURIComponent(status)}&search=${encodeURIComponent(search)}`;
        const res  = await fetch(url);
        const data = await res.json();
 
        if (data.length === 0) {
            tbody.innerHTML = '<tr><td colspan="4" style="text-align:center;padding:20px;color:#999">No tickets found.</td></tr>';
            return;
        }
 
        tbody.innerHTML = data.map(t => `
            <tr>
                <td>${t.ticket_id}</td>
                <td>${t.customer_name}</td>
                <td>${t.subject}</td>
                <td>${statusBadge(t.status)}</td>
            </tr>
        `).join('');
    }
 
    async function handleCreateTicket(event) {
        event.preventDefault();
        const res = await fetch('/api/tickets', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                customer_name:  document.getElementById('name').value.trim(),
                customer_email: document.getElementById('email').value.trim(),
                subject:        document.getElementById('subject').value.trim(),
                description:    document.getElementById('description').value.trim()
            })
        });
        const data = await res.json();
        alert('Ticket ' + data.ticket_id + ' created!');
        ticketForm.reset();
        fetchTickets();
    }
 
    ticketForm.addEventListener('submit', handleCreateTicket);
    searchInput.addEventListener('input', fetchTickets);
    statusFilter.addEventListener('change', fetchTickets);
    fetchTickets();
});