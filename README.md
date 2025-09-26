# QRCode Maker

[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

👉 바로 사용하기: [https://qrcode-maker-dnp4.onrender.com/](https://qrcode-maker-dnp4.onrender.com/)

간단한 URL 입력만으로 QR 코드를 생성하고 **미리보기 및 다운로드**할 수 있는 웹 서비스입니다.  
Django + Render 배포 환경을 기반으로 제작되었습니다.

---

## 🚀 Features
- ✅ URL 입력 시 QR 코드 자동 생성
- ✅ **미리보기 기능**: 생성된 QR 코드를 브라우저에서 바로 확인
- ✅ **다운로드 기능**: PNG 이미지로 저장
- ✅ Render 무료 플랜 기반 배포

---

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: [Django 5.x](https://www.djangoproject.com/)
- **Database**: PostgreSQL (Render)
- **Deployment**: [Render](https://render.com/)
- **Libraries**:
  - [`qrcode`](https://pypi.org/project/qrcode/) – QR 코드 생성
  - [`Pillow`](https://pypi.org/project/Pillow/) – 이미지 처리
  - [`gunicorn`](https://pypi.org/project/gunicorn/) – WSGI 서버
  - [`dj-database-url`](https://pypi.org/project/dj-database-url/) – Render PostgreSQL 연동

---

## 📂 Project Structure
QRCode_maker/ # GitHub Repo Root
│
├── qr_maker/ # Django 프로젝트 루트
│ ├── qr_maker/ # Django 설정 (settings.py, urls.py, wsgi.py)
│ ├── qrapp/ # QR 코드 생성 앱
│ ├── manage.py
│ ├── requirements.txt
│ └── Procfile
│
├── .env # 로컬 개발용 환경변수 (Render에선 대시보드에서 관리)
├── .gitignore
└── README.md


DEBUG=False

📸 Screenshot


📝 License
MIT License

<img width="1426" height="1085" alt="image" src="https://github.com/user-attachments/assets/01b0caf8-cdee-4b18-9eef-eb521bba55e3" />
