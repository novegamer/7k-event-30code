from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OFFICIAL_CODES = [
    "SUNWUKONGNO1", "HAPPYNEWYEAR2026", "7S7E7V7E7N7", "DANCINGPOOKI", 
    "BRANZEBRANSEL", "GRACEOFCHAOS", "SENAHAJASENA", "CHAOSESSENCE", 
    "77EVENT77", "100MILLIONHEARTS", "KEYKEYKEY", "POOKIFIVEKINDS", 
    "LETSGO7K", "GOLDENKINGPEPE", "HALFGOODHALFEVIL", "DELLONSVSKRIS", 
    "TARGETWISH", "OBLIVION", "SENASTARCRYSTAL", "SENA77MEMORY"
]

# ใช้ Headers ที่มีความเป็นบราวเซอร์สูงที่สุดเพื่อเลี่ยงการโดนบล็อก
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://coupon.netmarble.com/tskgb",
    "Origin": "https://coupon.netmarble.com"
}

@app.route('/api/get-codes', methods=['GET'])
def get_codes():
    return jsonify({"codes": OFFICIAL_CODES})

@app.route('/api/check-user', methods=['POST'])
def check_user():
    try:
        pid = request.json.get('pid')
        url = "https://coupon.netmarble.com/api/coupon/inquiry"
        params = {"gameCode": "tskgb", "langCd": "TH_TH", "pid": pid}
        resp = requests.get(url, params=params, headers=HEADERS, timeout=10)
        
        # ตรวจสอบว่าเป็น JSON จริงไหมก่อนประมวลผล
        try:
            return jsonify(resp.json())
        except:
            return jsonify({"errorCode": 403, "errorMessage": "Netmarble บล็อกการเข้าถึงจาก Vercel ชั่วคราว"})
    except Exception as e:
        return jsonify({"errorCode": 500, "errorMessage": str(e)})

@app.route('/api/redeem', methods=['POST'])
def redeem():
    try:
        data = request.json
        url = "https://coupon.netmarble.com/api/coupon/reward"
        params = {
            "gameCode": "tskgb",
            "langCd": "TH_TH",
            "pid": data.get('pid'),
            "couponCode": data.get('code').strip()
        }
        resp = requests.get(url, params=params, headers=HEADERS, timeout=10)
        
        try:
            return jsonify(resp.json())
        except:
            return jsonify({"errorCode": 403, "errorMessage": "เซิร์ฟเวอร์ไม่ตอบกลับข้อมูล JSON"})
    except Exception as e:
        return jsonify({"errorCode": 500, "errorMessage": str(e)})
