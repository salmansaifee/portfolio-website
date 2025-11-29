# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# from datetime import datetime
# import os
# import pandas as pd

# app = Flask(__name__)
# CORS(app)

# # ========== CONFIGURATION ==========
# EXCEL_FILE = r'C:\Users\Salman Saifee\portfolio-website\backend\portfolio_data.xlsx'
# USE_EXCEL = os.path.exists(EXCEL_FILE)

# # ========== DEFAULT DATA ==========
# DEFAULT_PORTFOLIO_DATA = {
#     'name': 'Salman Saifee',
#     'title': 'Senior Data Analyst',
#     'email': 'salmansaifee77@gmail.com',
#     'location': 'Mumbai, India',
#     'phone': '+91-86555 12366',
#     'experience_years': '3',
#     'bio': 'Data Analyst with 3 years of expertise transforming data into actionable insights.',
#     'projects': [],
#     'skills': {},
#     'experience': [],
#     'certifications': [],
#     'education': []
# }

# # ========== LOAD DATA FROM EXCEL ==========
# def load_portfolio_data():
#     """Load all data from Excel file or return default data"""
#     if not USE_EXCEL:
#         print(f"⚠️ Excel file not found: {EXCEL_FILE}")
#         print("📝 Using default hardcoded data\n")
#         return DEFAULT_PORTFOLIO_DATA
    
#     try:
#         print(f"\n{'='*60}")
#         print(f"📂 Loading data from Excel: {EXCEL_FILE}")
#         print(f"{'='*60}")
        
#         excel_file = pd.ExcelFile(EXCEL_FILE)
#         print(f"📋 Available sheets: {excel_file.sheet_names}\n")
        
#         # ========== Load Personal Info ==========
#         print("📄 Loading Personal_Info...")
#         personal_df = pd.read_excel(excel_file, 'Personal_Info')
#         personal_info = {}
#         for _, row in personal_df.iterrows():
#             field = str(row['Field']).strip()
#             value = row['Value']
#             # Convert to string but keep numbers as strings
#             if pd.notna(value):
#                 personal_info[field] = str(value).strip()
        
#         print(f"   ✅ Loaded fields: {list(personal_info.keys())}")
        
#         # ========== Load Skills ==========
#         print("📄 Loading Skills...")
#         skills_df = pd.read_excel(excel_file, 'Skills')
#         skills = {}
#         for category in skills_df['Category'].unique():
#             if pd.notna(category):
#                 category_skills = skills_df[skills_df['Category'] == category]
#                 skills[category] = [
#                     {'name': str(row['Skill']), 'level': int(row['Level'])}
#                     for _, row in category_skills.iterrows()
#                     if pd.notna(row['Skill'])
#                 ]
#         print(f"   ✅ Loaded {len(skills)} skill categories: {list(skills.keys())}")
        
#         # ========== Load Experience ==========
#         print("📄 Loading Experience...")
#         experience_df = pd.read_excel(excel_file, 'Experience')
#         experience = []
#         for _, row in experience_df.iterrows():
#             achievements = []
#             for i in range(1, 6):
#                 achievement = row.get(f'Achievement{i}', '')
#                 if pd.notna(achievement) and str(achievement).strip():
#                     achievements.append(str(achievement).strip())
            
#             if pd.notna(row['Company']):
#                 experience.append({
#                     'company': str(row['Company']).strip(),
#                     'role': str(row['Role']).strip() if pd.notna(row['Role']) else '',
#                     'duration': str(row['Duration']).strip() if pd.notna(row['Duration']) else '',
#                     'achievements': achievements
#                 })
#         print(f"   ✅ Loaded {len(experience)} experience entries")
        
#         # ========== Load Projects ==========
#         print("📄 Loading Projects...")
#         projects_df = pd.read_excel(excel_file, 'Projects')
#         projects = []
#         for idx, row in projects_df.iterrows():
#             if pd.notna(row['Title']):
#                 tools_str = str(row['Tools']) if pd.notna(row['Tools']) else ''
#                 tools_list = [t.strip() for t in tools_str.split(',') if t.strip()]
                
#                 dashboard_url = ''
#                 if 'Dashboard_URL' in row and pd.notna(row['Dashboard_URL']):
#                     dashboard_url = str(row['Dashboard_URL']).strip()
                
#                 projects.append({
#                     'id': idx + 1,
#                     'title': str(row['Title']).strip(),
#                     'description': str(row['Description']).strip() if pd.notna(row['Description']) else '',
#                     'tools': tools_list,
#                     'impact': str(row['Impact']).strip() if pd.notna(row['Impact']) else '',
#                     'details': str(row['Details']).strip() if pd.notna(row['Details']) else '',
#                     'dashboard_url': dashboard_url
#                 })
#         print(f"   ✅ Loaded {len(projects)} projects")
        
#         # ========== Load Certifications ==========
#         print("📄 Loading Certifications...")
#         certifications_df = pd.read_excel(excel_file, 'Certifications')
#         certifications = []
#         for _, row in certifications_df.iterrows():
#             if pd.notna(row['Certification']):
#                 # Handle date
#                 cert_date = row['Date']
#                 if isinstance(cert_date, pd.Timestamp):
#                     cert_date = cert_date.strftime('%b-%y')
#                 elif pd.notna(cert_date):
#                     cert_date = str(cert_date)
#                 else:
#                     cert_date = ''
                
#                 # Handle credential ID
#                 credential_id = ''
#                 if 'Credential_ID' in row and pd.notna(row['Credential_ID']):
#                     credential_id = str(row['Credential_ID']).strip()
                
#                 certifications.append({
#                     'name': str(row['Certification']).strip(),
#                     'issuer': str(row['Issuer']).strip() if pd.notna(row['Issuer']) else '',
#                     'date': cert_date,
#                     'credential_id': credential_id
#                 })
#         print(f"   ✅ Loaded {len(certifications)} certifications")
        
#         # ========== Load Education ==========
#         print("📄 Loading Education...")
#         education_df = pd.read_excel(excel_file, 'Education')
#         education = []
#         for _, row in education_df.iterrows():
#             if pd.notna(row['Degree']):
#                 education.append({
#                     'degree': str(row['Degree']).strip(),
#                     'institution': str(row['Institution']).strip() if pd.notna(row['Institution']) else '',
#                     'year': str(row['Year']).strip() if pd.notna(row['Year']) else '',
#                     'details': str(row['Details']).strip() if pd.notna(row.get('Details', '')) else ''
#                 })
#         print(f"   ✅ Loaded {len(education)} education entries")
        
#         # ========== Combine all data ==========
#         portfolio_data = {
#             **personal_info,
#             'skills': skills,
#             'experience': experience,
#             'projects': projects,
#             'certifications': certifications,
#             'education': education
#         }
        
#         print(f"\n{'='*60}")
#         print("✅ ALL DATA LOADED SUCCESSFULLY FROM EXCEL!")
#         print(f"{'='*60}\n")
        
#         return portfolio_data
    
#     except Exception as e:
#         print(f"\n❌ ERROR loading Excel file: {str(e)}")
#         print(f"Error type: {type(e).__name__}")
#         import traceback
#         traceback.print_exc()
#         print("\n📝 Falling back to default hardcoded data.\n")
#         return DEFAULT_PORTFOLIO_DATA


# # ========== API ENDPOINTS ==========

# @app.route('/api/health', methods=['GET'])
# def health():
#     return jsonify({'status': 'healthy', 'message': 'Server is running!'}), 200

# @app.route('/api/portfolio', methods=['GET'])
# def get_portfolio():
#     data = load_portfolio_data()
#     return jsonify(data), 200

# @app.route('/api/projects', methods=['GET'])
# def get_projects():
#     data = load_portfolio_data()
#     return jsonify(data.get('projects', [])), 200

# @app.route('/api/skills', methods=['GET'])
# def get_skills():
#     data = load_portfolio_data()
#     return jsonify(data.get('skills', {})), 200

# @app.route('/api/experience', methods=['GET'])
# def get_experience():
#     data = load_portfolio_data()
#     return jsonify(data.get('experience', [])), 200

# @app.route('/api/certifications', methods=['GET'])
# def get_certifications():
#     data = load_portfolio_data()
#     return jsonify(data.get('certifications', [])), 200

# @app.route('/api/education', methods=['GET'])
# def get_education():
#     data = load_portfolio_data()
#     return jsonify(data.get('education', [])), 200

# @app.route('/api/contact', methods=['POST'])
# def contact():
#     try:
#         data = request.json
#         name = data.get('name')
#         email = data.get('email')
#         message = data.get('message')
        
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         print(f"\n📧 [{timestamp}] Contact Form Submission:")
#         print(f"   Name: {name}")
#         print(f"   Email: {email}")
#         print(f"   Message: {message}\n")
        
#         return jsonify({
#             'status': 'success',
#             'message': 'Message received! Thank you for reaching out.'
#         }), 200
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)}), 500

# @app.route('/')
# def home():
#     data = load_portfolio_data()
#     return render_template('index.html', data=data)

# @app.route('/reload')
# def reload_data():
#     """Force reload data from Excel"""
#     data = load_portfolio_data()
#     return jsonify({
#         'success': True,
#         'message': 'Data reloaded successfully',
#         'using_excel': USE_EXCEL,
#         'excel_path': EXCEL_FILE,
#         'data_summary': {
#             'name': data.get('name', 'N/A'),
#             'projects': len(data.get('projects', [])),
#             'skills_categories': len(data.get('skills', {})),
#             'experience': len(data.get('experience', [])),
#             'certifications': len(data.get('certifications', [])),
#             'education': len(data.get('education', []))
#         }
#     })

# if __name__ == '__main__':
#     port = int(os.getenv('PORT', 5000))
    
#     print("\n" + "="*60)
#     print("🚀 PORTFOLIO WEBSITE SERVER STARTING")
#     print("="*60)
    
#     if USE_EXCEL:
#         print(f"✅ Excel file found: {EXCEL_FILE}")
#         print("📊 Portfolio data will load dynamically from Excel")
#     else:
#         print(f"⚠️ Excel file not found: {EXCEL_FILE}")
#         print("📝 Using hardcoded default data")
    
#     print(f"🌐 Server: http://localhost:{port}")
#     print("="*60)
    
#     app.run(debug=True, host='0.0.0.0', port=port)

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os
import pandas as pd

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
CORS(app)

# ========== DYNAMIC PATH DETECTION ==========
# This works on BOTH local machine AND production server (Render)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Try multiple possible paths for Excel file
POSSIBLE_PATHS = [
    os.path.join(BASE_DIR, 'portfolio_data.xlsx'),                    # backend/portfolio_data.xlsx
    os.path.join(os.path.dirname(BASE_DIR), 'portfolio_data.xlsx'),  # root/portfolio_data.xlsx
    os.path.join(BASE_DIR, 'data', 'portfolio_data.xlsx'),           # backend/data/portfolio_data.xlsx
]

EXCEL_FILE = None
for path in POSSIBLE_PATHS:
    if os.path.exists(path):
        EXCEL_FILE = path
        print(f"✅ Excel file found at: {EXCEL_FILE}")
        break

USE_EXCEL = EXCEL_FILE is not None

if not USE_EXCEL:
    print(f"⚠️  Excel file not found. Checked:")
    for path in POSSIBLE_PATHS:
        print(f"   - {path}")
    print(f"📂 Files in {BASE_DIR}:")
    try:
        for item in os.listdir(BASE_DIR):
            print(f"   - {item}")
    except:
        pass
    print("📝 Using default hardcoded data\n")

# ========== DEFAULT DATA ==========
DEFAULT_PORTFOLIO_DATA = {
    'name': 'Salman Saifee',
    'title': 'Senior Data Analyst',
    'email': 'salmansaifee77@gmail.com',
    'location': 'Mumbai, India',
    'phone': '+91-86555 12366',
    'experience_years': '3',
    'bio': 'Data Analyst with 3 years of expertise transforming data into actionable insights.',
    'LinkedIn': 'https://linkedin.com/in/salmansaifee',
    'GitHub': 'https://github.com/salmansaifee',
    'projects': [],
    'skills': {},
    'experience': [],
    'certifications': [],
    'education': []
}

# ========== LOAD DATA FROM EXCEL ==========
def load_portfolio_data():
    """Load all data from Excel file or return default data"""
    if not USE_EXCEL:
        print("📝 Using default hardcoded data")
        return DEFAULT_PORTFOLIO_DATA
    
    try:
        print(f"\n{'='*60}")
        print(f"📂 Loading data from Excel: {EXCEL_FILE}")
        print(f"{'='*60}")
        
        excel_file = pd.ExcelFile(EXCEL_FILE)
        print(f"📋 Available sheets: {excel_file.sheet_names}\n")
        
        # ========== Load Personal Info ==========
        print("📄 Loading Personal_Info...")
        personal_df = pd.read_excel(excel_file, 'Personal_Info')
        personal_info = {}
        
        # Try both column formats
        for _, row in personal_df.iterrows():
            # Check for different column names
            if 'Field' in personal_df.columns and 'Value' in personal_df.columns:
                field = str(row['Field']).strip()
                value = row['Value']
            else:
                # Direct column names
                continue
            
            if pd.notna(value):
                personal_info[field] = str(value).strip()
        
        print(f"   ✅ Loaded fields: {list(personal_info.keys())}")
        
        # ========== Load Skills ==========
        print("📄 Loading Skills...")
        skills_df = pd.read_excel(excel_file, 'Skills')
        skills = {}
        
        # Determine column names
        category_col = 'Category' if 'Category' in skills_df.columns else 'category'
        skill_col = 'Skill' if 'Skill' in skills_df.columns else 'name'
        level_col = 'Level' if 'Level' in skills_df.columns else 'level'
        
        for category in skills_df[category_col].unique():
            if pd.notna(category):
                category_skills = skills_df[skills_df[category_col] == category]
                skills[str(category).strip()] = [
                    {'name': str(row[skill_col]).strip(), 'level': int(row[level_col])}
                    for _, row in category_skills.iterrows()
                    if pd.notna(row[skill_col])
                ]
        print(f"   ✅ Loaded {len(skills)} skill categories: {list(skills.keys())}")
        
        # ========== Load Experience ==========
        print("📄 Loading Experience...")
        experience_df = pd.read_excel(excel_file, 'Experience')
        experience = []
        
        for _, row in experience_df.iterrows():
            if pd.notna(row.get('Company', '')):
                achievements = []
                for i in range(1, 6):
                    achievement = row.get(f'Achievement{i}', '')
                    if pd.notna(achievement) and str(achievement).strip():
                        achievements.append(str(achievement).strip())
                
                experience.append({
                    'company': str(row['Company']).strip(),
                    'role': str(row.get('Role', '')).strip() if pd.notna(row.get('Role')) else '',
                    'duration': str(row.get('Duration', '')).strip() if pd.notna(row.get('Duration')) else '',
                    'achievements': achievements
                })
        print(f"   ✅ Loaded {len(experience)} experience entries")
        
        # ========== Load Projects ==========
        print("📄 Loading Projects...")
        projects_df = pd.read_excel(excel_file, 'Projects')
        projects = []
        
        for idx, row in projects_df.iterrows():
            if pd.notna(row.get('Title', '')):
                tools_str = str(row.get('Tools', '')) if pd.notna(row.get('Tools')) else ''
                tools_list = [t.strip() for t in tools_str.split(',') if t.strip()]
                
                dashboard_url = ''
                if 'Dashboard_URL' in row and pd.notna(row['Dashboard_URL']):
                    dashboard_url = str(row['Dashboard_URL']).strip()
                
                projects.append({
                    'id': idx + 1,
                    'title': str(row['Title']).strip(),
                    'description': str(row.get('Description', '')).strip() if pd.notna(row.get('Description')) else '',
                    'tools': tools_list,
                    'impact': str(row.get('Impact', '')).strip() if pd.notna(row.get('Impact')) else '',
                    'details': str(row.get('Details', '')).strip() if pd.notna(row.get('Details')) else '',
                    'dashboard_url': dashboard_url
                })
        print(f"   ✅ Loaded {len(projects)} projects")
        
        # ========== Load Certifications ==========
        print("📄 Loading Certifications...")
        certifications_df = pd.read_excel(excel_file, 'Certifications')
        certifications = []
        
        for _, row in certifications_df.iterrows():
            if pd.notna(row.get('Certification', '')):
                cert_date = row.get('Date', '')
                if isinstance(cert_date, pd.Timestamp):
                    cert_date = cert_date.strftime('%b-%y')
                elif pd.notna(cert_date):
                    cert_date = str(cert_date)
                else:
                    cert_date = ''
                
                credential_id = ''
                if 'Credential_ID' in row and pd.notna(row['Credential_ID']):
                    credential_id = str(row['Credential_ID']).strip()
                
                certifications.append({
                    'name': str(row['Certification']).strip(),
                    'issuer': str(row.get('Issuer', '')).strip() if pd.notna(row.get('Issuer')) else '',
                    'date': cert_date,
                    'credential_id': credential_id
                })
        print(f"   ✅ Loaded {len(certifications)} certifications")
        
        # ========== Load Education ==========
        print("📄 Loading Education...")
        education_df = pd.read_excel(excel_file, 'Education')
        education = []
        
        for _, row in education_df.iterrows():
            if pd.notna(row.get('Degree', '')):
                education.append({
                    'degree': str(row['Degree']).strip(),
                    'institution': str(row.get('Institution', '')).strip() if pd.notna(row.get('Institution')) else '',
                    'year': str(row.get('Year', '')).strip() if pd.notna(row.get('Year')) else '',
                    'details': str(row.get('Details', '')).strip() if pd.notna(row.get('Details')) else ''
                })
        print(f"   ✅ Loaded {len(education)} education entries")
        
        # ========== Combine all data ==========
        portfolio_data = {
            **DEFAULT_PORTFOLIO_DATA,  # Start with defaults
            **personal_info,           # Override with Excel data
            'skills': skills,
            'experience': experience,
            'projects': projects,
            'certifications': certifications,
            'education': education
        }
        
        print(f"\n{'='*60}")
        print("✅ ALL DATA LOADED SUCCESSFULLY FROM EXCEL!")
        print(f"{'='*60}\n")
        
        return portfolio_data
    
    except Exception as e:
        print(f"\n❌ ERROR loading Excel file: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        print("\n📝 Falling back to default hardcoded data.\n")
        return DEFAULT_PORTFOLIO_DATA

# ========== API ENDPOINTS ==========

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'Server is running!'}), 200

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    data = load_portfolio_data()
    return jsonify(data), 200

@app.route('/api/projects', methods=['GET'])
def get_projects():
    data = load_portfolio_data()
    return jsonify(data.get('projects', [])), 200

@app.route('/api/skills', methods=['GET'])
def get_skills():
    data = load_portfolio_data()
    return jsonify(data.get('skills', {})), 200

@app.route('/api/experience', methods=['GET'])
def get_experience():
    data = load_portfolio_data()
    return jsonify(data.get('experience', [])), 200

@app.route('/api/certifications', methods=['GET'])
def get_certifications():
    data = load_portfolio_data()
    return jsonify(data.get('certifications', [])), 200

@app.route('/api/education', methods=['GET'])
def get_education():
    data = load_portfolio_data()
    return jsonify(data.get('education', [])), 200

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n📧 [{timestamp}] Contact Form Submission:")
        print(f"   Name: {name}")
        print(f"   Email: {email}")
        print(f"   Message: {message}\n")
        
        return jsonify({
            'status': 'success',
            'message': 'Message received! Thank you for reaching out.'
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/')
def home():
    data = load_portfolio_data()
    return render_template('index.html', data=data)

@app.route('/reload')
def reload_data():
    """Force reload data from Excel"""
    data = load_portfolio_data()
    return jsonify({
        'success': True,
        'message': 'Data reloaded successfully',
        'using_excel': USE_EXCEL,
        'excel_path': EXCEL_FILE if EXCEL_FILE else 'Not found',
        'data_summary': {
            'name': data.get('name', 'N/A'),
            'projects': len(data.get('projects', [])),
            'skills_categories': len(data.get('skills', {})),
            'experience': len(data.get('experience', [])),
            'certifications': len(data.get('certifications', [])),
            'education': len(data.get('education', []))
        }
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    
    print("\n" + "="*60)
    print("🚀 PORTFOLIO WEBSITE SERVER STARTING")
    print("="*60)
    print(f"📂 Working Directory: {BASE_DIR}")
    
    if USE_EXCEL:
        print(f"✅ Excel file found: {EXCEL_FILE}")
        print("📊 Portfolio data will load dynamically from Excel")
    else:
        print(f"⚠️  Excel file not found")
        print("📝 Using hardcoded default data")
        print("\n💡 To use Excel data:")
        print("   1. Place portfolio_data.xlsx in backend/ folder")
        print("   2. Commit to Git: git add backend/portfolio_data.xlsx")
        print("   3. Push to GitHub: git push")
        print("   4. Redeploy on Render")
    
    print(f"🌐 Server: http://0.0.0.0:{port}")
    print("="*60 + "\n")
    
    app.run(debug=False, host='0.0.0.0', port=port)
