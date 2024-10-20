# Flask Feedback Statistics Application
**개인 학습용 프로젝트**
이 프로젝트는 Flask를 사용하여 서비스에 대한 피드백 통계를 수집하고 시각화하는 웹 애플리케이션입니다. 사용자는 피드백을 제출하고, 통계 데이터를 확인하며, Excel 파일로 다운로드할 수 있습니다.

## 기능

- 서비스별 피드백 통계 시각화
- 긍정적 및 부정적 피드백의 차트 표시
- 통계 데이터를 Excel 파일로 다운로드

## 기술 스택

- Python
- Flask
- SQLAlchemy
- Pandas
- Chart.js
- HTML/CSS

## 설치 방법

1. **레포지토리 클론**
   ```
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. **가상 환경 생성 및 활성화**
   ```
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. **필요한 패키지 설치**
   ```
   pip install -r requirements.txt
   ```
4. **데이터베이스 초기화**

## 사용법
1. 서버 실행
```
flask run
```
2. 웹 브라우저에서 http://127.0.0.1:5000에 접속하여 애플리케이션을 사용합니다.
3. 피드백을 제출하고, 통계 페이지에서 피드백 통계를 확인합니다.
4. Excel로 다운로드 버튼을 클릭하여 통계 데이터를 Excel 파일로 다운로드합니다.
