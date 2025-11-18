from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__)

# --- REMOVED FOR VERCEL ---
# Vercel is read-only, so we cannot create folders or write files.
# if not os.path.exists('data'):
#     os.makedirs('data')

# Route for serving HTML pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page>')
def serve_page(page):
    return render_template(f'{page}.html')

# ===== RESERVATION FORM HANDLER =====
@app.route('/submit-reservation', methods=['POST'])
def submit_reservation():
    try:
        # Get form data
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        date = request.form.get('date')
        time = request.form.get('time')
        guests = request.form.get('guests')
        occasion = request.form.get('occasion', 'Not specified')
        special_request = request.form.get('specialRequest', 'None')
        
        # Create timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Create reservation data
        reservation_data = f"""
{'='*50}
RESERVATION SUBMITTED
{'='*50}
Timestamp: {timestamp}
Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Date: {date}
Time: {time}
Number of Guests: {guests}
Occasion: {occasion}
Special Requests: {special_request}
{'='*50}
"""
        
        # --- FILE SAVING REMOVED FOR VERCEL ---
        # with open('data/reservations.txt', 'a', encoding='utf-8') as f:
        #     f.write(reservation_data)
        
        # Print to Vercel Logs (View this in Vercel Dashboard -> Logs)
        print(reservation_data)
        
        # Return success response
        return jsonify({
            'status': 'success',
            'message': f'Thank you, {first_name}! Your reservation has been confirmed.',
            'data': {
                'name': f'{first_name} {last_name}',
                'date': date,
                'time': time,
                'guests': guests
            }
        }), 200
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'There was an error processing your reservation. Please try again.'
        }), 500

# ===== CAREER APPLICATION HANDLER =====
@app.route('/submit-career', methods=['POST'])
def submit_career():
    try:
        # Get form data
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        position = request.form.get('position')
        experience = request.form.get('experience', '0')
        availability = request.form.get('availability')
        message = request.form.get('message')
        
        # Create timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Create application data
        application_data = f"""
{'='*50}
JOB APPLICATION SUBMITTED
{'='*50}
Timestamp: {timestamp}
Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Position: {position}
Years of Experience: {experience}
Availability: {availability}
Why Hot Spot Kitchen: {message}
{'='*50}
"""
        
        # --- FILE SAVING REMOVED FOR VERCEL ---
        # with open('data/applications.txt', 'a', encoding='utf-8') as f:
        #     f.write(application_data)
        
        # Print to Vercel Logs
        print(application_data)
        
        # Return success response
        return jsonify({
            'status': 'success',
            'message': f'Thank you for your application, {first_name}! We will review it and contact you soon.',
            'data': {
                'name': f'{first_name} {last_name}',
                'position': position,
                'email': email
            }
        }), 200
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'There was an error submitting your application. Please try again.'
        }), 500

# ===== CONTACT FORM HANDLER (Optional) =====
@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        contact_data = f"""
{'='*50}
CONTACT FORM SUBMITTED
{'='*50}
Timestamp: {timestamp}
Name: {name}
Email: {email}
Subject: {subject}
Message: {message}
{'='*50}
"""
        # Print to Vercel Logs instead of saving file
        print(contact_data)
        
        return jsonify({
            'status': 'success',
            'message': f'Thank you, {name}! We have received your message and will get back to you soon.'
        }), 200
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'There was an error sending your message. Please try again.'
        }), 500

# ===== ADMIN ROUTES (Modified to not crash) =====
@app.route('/admin/reservations')
def view_reservations():
    return "<h2>File storage is disabled on Vercel. Please check Vercel Dashboard > Logs to see submissions.</h2>"

@app.route('/admin/applications')
def view_applications():
    return "<h2>File storage is disabled on Vercel. Please check Vercel Dashboard > Logs to see submissions.</h2>"

# ===== ERROR HANDLERS =====
@app.errorhandler(404)
def not_found(e):
    return "<h1>404 - Page Not Found</h1><p>The page you're looking for doesn't exist.</p>", 404

@app.errorhandler(500)
def server_error(e):
    return "<h1>500 - Server Error</h1><p>Something went wrong on our end. Please try again later.</p>", 500

# Main block
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
