from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# ========== YOUR PERSONAL INFORMATION ==========
PORTFOLIO_DATA = {
    'name': 'Salman Saifee',
    'title': 'Senior Data Analyst',
    'email': 'salmansaifee77@gmail.com',
    'location': 'India',
    'phone': '+91-8655512366',
    'experience_years': 3,
    'bio': 'Data Analyst with 3 years of expertise transforming data into actionable insights.',
    
    'projects': [
        {
            'id': 1,
            'title': 'Sales Performance Dashboard',
            'description': 'Interactive Power BI dashboard for sales analytics',
            'tools': ['Power BI', 'SQL', 'Excel'],
            'impact': '15% Revenue Increase',
            'details': 'Created dashboard analyzing 5000+ transactions resulting in 15% revenue increase'
        },
        {
            'id': 2,
            'title': 'Customer Churn Prediction Model',
            'description': 'ML model to predict customer churn',
            'tools': ['Python', 'SQL', 'Tableau'],
            'impact': '3.2% Churn Reduction',
            'details': 'Built ML model with 87% accuracy to identify at-risk customers'
        },
        {
            'id': 3,
            'title': 'Inventory Optimization Analysis',
            'description': 'SQL-based warehouse optimization',
            'tools': ['SQL', 'Excel', 'Power BI'],
            'impact': '12% Cost Savings',
            'details': 'Optimized stock levels for 500+ SKUs saving 12% operational costs'
        }
    ],
    
    'skills': {
        'Data Tools': [
            {'name': 'Power BI', 'level': 95},
            {'name': 'Tableau', 'level': 60},
            {'name': 'Excel', 'level': 95}
        ],
        'Programming': [
            {'name': 'Python', 'level': 50},
            {'name': 'SQL', 'level': 60}
        ]
    },
    
    'experience': [
        {
            'company': 'DataAstraa LLP',
            'role': 'Senior Data Analyst',
            'duration': 'Sept 2022 - Present',
            'achievements': [
                'Led team of 3 analysts',
                'Developed 25+ dashboards',
                'Implemented data governance'
            ]
        },
        {
            'company': 'Accenture',
            'role': 'Analyst',
            'duration': 'Mar 2022 - Mar 2022',
            'achievements': [
                'Preparation of Teams Performance Report in Excel',
                'Performed Excel analysis',
                'Improved efficiency by 30%'
            ]
        }
    ]
}

# ========== API ENDPOINTS ==========

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'Server is running!'}), 200

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    return jsonify(PORTFOLIO_DATA), 200

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify(PORTFOLIO_DATA['projects']), 200

@app.route('/api/skills', methods=['GET'])
def get_skills():
    return jsonify(PORTFOLIO_DATA['skills']), 200


@app.route('/api/experience', methods=['GET'])
def get_experience():
    return jsonify(PORTFOLIO_DATA['experience']), 200

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        print(f"Message from {name} ({email}): {message}")
        
        return jsonify({
            'status': 'success',
            'message': 'Message received!'
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
