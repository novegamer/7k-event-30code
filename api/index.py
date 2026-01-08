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

# ใช้ User-Agent ที่เหมือนคนใช้งานจริงที่สุด เพื่อเลี่ยงการโดนบล็อก
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://coupon.netmarble.com",
    "Referer": "https://coupon.netmarble.com/tskgb",
    "Accept-Language": "th-TH,th;q=0.9,en-US;q=0.8,en;q=0.7"
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
        
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        
        # ตรวจสอบว่าสิ่งที่ตอบกลับมาใช่ JSON หรือไม่
        try:
            return jsonify(response.json())
        except:
            # หากไม่ใช่ JSON ให้บอกสถานะที่ได้รับมาแทน
            return jsonify({
                "errorCode": 500, 
                "errorMessage": f"เซิร์ฟเวอร์ตอบกลับไม่ถูกต้อง (Status: {response.status_code})"
            })
            
    except Exception as e:
        return jsonify({"errorCode": 500, "errorMessage": str(e)})

@app.route('/api/redeem', methods=['POST'])
def redeem():
    try:
        data = request.json
        url = "https://coupon.netmarble.com/api/coupon/reward"
        params = {
            "gameCode": "tskgb",
            "couponCode": data.get('code').strip(),
            "langCd": "TH_TH",
            "pid": data.get('pid')
        }
        
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        
        try:
            return jsonify(response.json())
        except:
            return jsonify({
                "errorCode": 500, 
                "errorMessage": "Netmarble บล็อกการเชื่อมต่อชั่วคราว"
            })
            
    except Exception as e:
        return jsonify({"errorCode": 500, "errorMessage": str(e)})
