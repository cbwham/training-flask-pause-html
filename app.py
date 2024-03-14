from flask import Flask, render_template, jsonify
from healthcheck import HealthCheck
from datetime import datetime
import time # noqa: DC007

app = Flask(__name__)
health = HealthCheck()

# Add a flask route to expose information
app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())

# Funktion zur Abrufung der aktuellen Uhrzeit
def get_current_time():
    return datetime.now().strftime('%H:%M:%S')

# Route für die Startseite mit fortlaufender Uhrzeit-Anzeige
@app.route('/') # noqa: DC002
def index():
    return render_template('index.html')

# Route für die aktuelle Uhrzeit im JSON-Format
@app.route('/get_time') # noqa: DC002
def get_time():
    return jsonify({'time': get_current_time()})

# Route für die Pausenzeiten
@app.route('/zeiten') # noqa: DC002
def zeiten():
    current_time = datetime.now()
    montag_freitag_pausen = "09:30-09:45"
    montag_donnerstag_pausen = "11:15-11:30, 12:15-13:15"

    if 9 <= current_time.hour < 10 and 30 <= current_time.minute < 46 and current_time.weekday() in range(0, 5):
        return f"Aktuelle Pause {montag_freitag_pausen} am {current_time.strftime('%A')}. Pausenzeiten: Montags-Freitags: {montag_freitag_pausen}, Montags-Donnerstags: {montag_donnerstag_pausen}."

    if 11 <= current_time.hour < 12 and 15 <= current_time.minute < 31 and current_time.weekday() in range(0, 4):
        return f"Aktuelle Pause {montag_donnerstag_pausen.split(',')[0]} am {current_time.strftime('%A')}. Pausenzeiten: Montags-Freitags: {montag_freitag_pausen}, Montags-Donnerstags: {montag_donnerstag_pausen}."

    if 12 <= current_time.hour < 14 and 15 <= current_time.minute <= 0 and current_time.weekday() in range(0, 4):
        return f"Aktuelle Pause {montag_donnerstag_pausen.split(',')[1]} am {current_time.strftime('%A')}. Pausenzeiten: Montags-Freitags: {montag_freitag_pausen}, Montags-Donnerstags: {montag_donnerstag_pausen}."

    return f"Im Augenblick keine Pause. Pausenzeiten: Montags-Freitags: {montag_freitag_pausen}, Montags-Donnerstags: {montag_donnerstag_pausen}."

if __name__ == '__main__':
    app.run(debug=True)
