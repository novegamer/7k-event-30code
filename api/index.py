from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# รายการโค้ดทั้งหมดที่เก็บไว้หลังบ้าน
OFFICIAL_CODES = [
    "SUNWUKONGNO1", "HAPPYNEWYEAR2026", "7S7E7V7E7N7", "DANCINGPOOKI", 
    "BRANZEBRANSEL", "GRACEOFCHAOS", "SENAHAJASENA", "CHAOSESSENCE", 
    "77EVENT77", "100MILLIONHEARTS", "KEYKEYKEY", "POOKIFIVEKINDS", 
    "LETSGO7K", "GOLDENKINGPEPE", "HALFGOODHALFEVIL", "DELLONSVSKRIS", 
    "TARGETWISH", "OBLIVION", "SENASTARCRYSTAL", "SENA77MEMORY"
]

@app.route('/api/get-codes', methods=['GET'])
def get_codes():
    return jsonify({"codes": OFFICIAL_CODES})

@app.route('/api/redeem', methods=['POST'])
def redeem():
    try:
        data = request.json
        pid = data.get('pid')
        code = data.get('code')

        # URL และ Headers ตามโครงสร้างที่คุณระบุ
        url = "https://coupon.netmarble.com/api/coupon/reward"
        params = {
            "gameCode": "tskgb",
            "langCd": "TH_TH",
            "pid": pid,
            "couponCode": code.strip()
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Origin": "https://coupon.netmarble.com",
            "Referer": "https://coupon.netmarble.com/tskgb"
        }

        # ส่งแบบ GET ตามภาพ Network
        response = requests.get(url, params=params, headers=headers, timeout=10)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"resultCode": "ERROR", "resultMsg": str(e)}), 200

def handler(req, res):
    return app(req, res)
