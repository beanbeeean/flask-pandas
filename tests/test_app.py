import unittest
from app import app, db, Feedback, Service

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # 테스트용 애플리케이션과 데이터베이스 설정
        self.app = app.test_client()
        self.app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        # 애플리케이션 컨텍스트 설정
        with app.app_context():
            db.create_all()

            # 테스트 데이터 추가
            service = Service(name='Test Service')
            db.session.add(service)
            db.session.commit()

            # 서비스 객체를 다시 쿼리하여 세션에 바인딩
            self.service = Service.query.first()

    def tearDown(self):
        # 데이터베이스 세션 종료
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_submit_feedback(self):
        # 피드백 제출 테스트
        response = self.app.post('/submit_feedback', data={
            'service_id': self.service.id,
            'feedback_type': '긍정적',
            'content': 'Great service!'
        })
        self.assertEqual(response.status_code, 302)  # 리다이렉션 확인

        # 피드백이 데이터베이스에 저장되었는지 확인
        feedback = Feedback.query.first()
        self.assertIsNotNone(feedback)
        self.assertEqual(feedback.content, 'Great service!')

    def test_statistics_page(self):
        # 통계 페이지 테스트
        response = self.app.get('/statistics')
        self.assertEqual(response.status_code, 200)  # 페이지 로드 확인
        self.assertIn('서비스별 피드백 통계', response.data.decode('utf-8'))  # 페이지 내용 확인

    def test_download_statistics(self):
        # 통계 다운로드 테스트
        response = self.app.get('/download_statistics')
        self.assertEqual(response.status_code, 200)  # 파일 다운로드 확인
        self.assertEqual(response.content_type, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  # Excel 파일 형식 확인

if __name__ == '__main__':
    unittest.main()
