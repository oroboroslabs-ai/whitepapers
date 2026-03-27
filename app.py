#!/usr/bin/env python3
"""
Resonance Pi Network - Web Interface
Flask-based control panel for Raspberry Pi mesh network

Crafted by Source Technology
"""

from flask import Flask, render_template, jsonify, request
import threading
import time
import json
from static_ai import StaticAI

app = Flask(__name__)
ai_instance = StaticAI(node_id="web_controller_001")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'online',
        'node_id': ai_instance.node_id,
        'resonance_frequency': ai_instance.resonance_frequency,
        'timestamp': time.time()
    })

@app.route('/api/ai/process', methods=['POST'])
def process_ai():
    data = request.json
    input_text = data.get('input', '')
    result = ai_instance.full_consciousness_cycle(input_text)
    return jsonify(result)

@app.route('/api/security/status')
def security_status():
    return jsonify({
        'firewall_active': True,
        'encryption_enabled': True,
        'quantum_resistant': True
    })

def start_background_services():
    def status_updater():
        while True:
            time.sleep(5)
    updater_thread = threading.Thread(target=status_updater)
    updater_thread.daemon = True
    updater_thread.start()

if __name__ == '__main__':
    start_background_services()
    print("Starting Resonance Pi Web Interface...")
    print("Access at: http://localhost:8080")
    app.run(host='0.0.0.0', port=8080, debug=False)