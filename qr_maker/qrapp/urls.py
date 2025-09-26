from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="qr-index"),
    path("qr.png", views.qr_png, name="qr-png"),             # 미리보기
    path("qr/download", views.qr_download, name="qr-download"),  # 다운로드
]

