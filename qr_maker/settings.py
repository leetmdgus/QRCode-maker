# settings.py

import os
DEBUG = False

# Render는 도메인을 환경변수로 넘겨줘요
ALLOWED_HOSTS = [".onrender.com"]

# 정적 파일 경로
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")