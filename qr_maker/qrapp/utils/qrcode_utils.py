from io import BytesIO
import qrcode

def generate_qr_png(url: str) -> BytesIO:
    # 간단한 검증(스킴 없는 경우 400 처리용으로 빈 바이트 반환하지 않도록)
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError("URL must start with http(s)://")

    img = qrcode.make(url)  # 기본 설정으로 PNG 생성
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf

