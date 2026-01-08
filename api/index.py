from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# รายการโค้ด Official ที่คุณต้องการ
OFFICIAL_CODES = [
    "SUNWUKONGNO1", "HAPPYNEWYEAR2026", "7S7E7V7E7N7", "DANCINGPOOKI", 
    "BRANZEBRANSEL", "GRACEOFCHAOS", "SENAHAJASENA", "CHAOSESSENCE", 
    "77EVENT77", "100MILLIONHEARTS", "KEYKEYKEY", "POOKIFIVEKINDS", 
    "LETSGO7K", "GOLDENKINGPEPE", "HALFGOODHALFEVIL", "DELLONSVSKRIS", 
    "TARGETWISH", "OBLIVION", "SENASTARCRYSTAL", "SENA77MEMORY"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://coupon.netmarble.com/tskgb",
    "Accept": "application/json"
}

@app.route('/api/get-codes', methods=['GET'])
def get_codes():
    return jsonify({"codes": OFFICIAL_CODES})

# ขั้นตอนที่ 1: ตรวจสอบ PID (เหมือนปุ่ม Submit ในเว็บจริง)
@app.route('/api/check-user', methods=['POST'])
def check_user():
    pid = request.json.get('pid')
    url = "https://coupon.netmarble.com/api/coupon/inquiry"
    params = {"gameCode": "tskgb", "langCd": "TH_TH", "pid": pid}
    response = requests.get(url, params=params, headers=HEADERS)
    return jsonify(response.json())

# ขั้นตอนที่ 2: แลกรางวัล (เหมือนปุ่ม Confirm ในเว็บจริง - ตามรูป image_57ad69.png)
@app.route('/api/redeem', methods=['POST'])
def redeem():
    data = request.json
    url = "https://coupon.netmarble.com/api/coupon/reward"
    params = {
        "gameCode": "tskgb",
        "couponCode": data.get('code').strip(),
        "langCd": "TH_TH",
        "pid": data.get('pid')
    }
    # ใช้ GET Method ตามที่ระบบทางการใช้
    response = requests.get(url, params=params, headers=HEADERS)
    return jsonify(response.json())
