from flask import Flask, render_template, request, redirect, url_for, send_file
from models.feedback import db, Feedback, Service
from config import Config
import pandas as pd

app = Flask(__name__)
app.config.from_object(Config)

# 데이터베이스 초기화
db.init_app(app)

@app.route('/')
def index():
    services = Service.query.all()
    return render_template('feedback_form.html', services=services)

@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    service_id = request.form['service_id']
    feedback_type = request.form['feedback_type']
    feedback_content = request.form['feedback_content']
    
    new_feedback = Feedback(name=name, email=email, service_id=service_id,
                            feedback_type=feedback_type, feedback_content=feedback_content)
    db.session.add(new_feedback)
    db.session.commit()
    
    return redirect(url_for('feedback_list'))

@app.route('/feedbacks')
def feedback_list():
    feedbacks = Feedback.query.all()
    services = Service.query.all()
    return render_template('feedback_list.html', feedbacks=feedbacks, services=services)

@app.route('/statistics')
def statistics():
    service_stats = {}
    services = Service.query.all()
    
    for service in services:
        total_feedback = Feedback.query.filter_by(service_id=service.id).count()
        positive_feedback = Feedback.query.filter_by(service_id=service.id, feedback_type='긍정적').count()
        negative_feedback = Feedback.query.filter_by(service_id=service.id, feedback_type='부정적').count()
        
        service_stats[service.name] = {
            'total': total_feedback,
            'positive': positive_feedback,
            'negative': negative_feedback,
        }
    return render_template('statistics.html', service_stats=service_stats)
    
@app.route('/download_statistics')
def download_statistics():
    service_stats = {}
    services = Service.query.all()
    
    for service in services:
        total_feedback = Feedback.query.filter_by(service_id=service.id).count()
        positive_feedback = Feedback.query.filter_by(service_id=service.id, feedback_type='긍정적').count()
        negative_feedback = Feedback.query.filter_by(service_id=service.id, feedback_type='부정적').count()
        
        service_stats[service.name] = {
            '총 피드백': total_feedback,
            '긍정적 피드백': positive_feedback,
            '부정적 피드백': negative_feedback,
        }

    df = pd.DataFrame.from_dict(service_stats, orient='index') 
    df.reset_index(inplace=True) 
    df.rename(columns={'index': '서비스'}, inplace=True)  

    file_path = 'service_statistics.xlsx'
    df.to_excel(file_path, index=False, engine='openpyxl')  

    return send_file(file_path, as_attachment=True)  

if __name__ == '__main__':
    app.run(debug=True)
