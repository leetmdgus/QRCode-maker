from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import quote
from .utils.qrcode_utils import generate_qr_png

def index(request):
    return render(request, "index.html")

def qr_png(request):
    url = request.GET.get("url", "")
    try:
        png = generate_qr_png(url)
    except Exception as e:
        return HttpResponse(str(e), status=400)

    # 미리보기용: inline
    resp = HttpResponse(png, content_type="image/png")
    resp["Content-Disposition"] = 'inline; filename="qrcode.png"'
    return resp

def qr_download(request):
    url = request.GET.get("url", "")
    filename = request.GET.get("filename") or "qrcode.png"
    try:
        png = generate_qr_png(url)
    except Exception as e:
        return HttpResponse(str(e), status=400)

    # 다운로드용: attachment
    resp = HttpResponse(png, content_type="image/png")
    # 파일명 안전 처리
    resp["Content-Disposition"] = f"attachment; filename*=UTF-8''{quote(filename)}"
    return resp

