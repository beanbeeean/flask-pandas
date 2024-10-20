from app import app
from models.feedback import db, Service

# 데이터베이스 초기화 및 기본 데이터 추가
def init_db():
    with app.app_context():
        db.create_all()  # 테이블 생성

        # 기본 서비스 데이터 추가
        if Service.query.count() == 0:
            services = ['서비스 A', '서비스 B', '서비스 C']
            for service_name in services:
                service = Service(name=service_name)
                db.session.add(service)
            db.session.commit()

if __name__ == '__main__':
    init_db()  # 데이터베이스 초기화
    app.run()
