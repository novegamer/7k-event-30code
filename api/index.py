from flask import Flask, request, jsonify
import requests

# ประกาศ app ไว้ที่ระดับนอกสุดเพื่อให้ Vercel ตรวจพบได้ทันที
app = Flask(__name__)

# รายการโค้ดที่บันทึกไว้หลังบ้าน
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

        # ใช้ URL และโครงสร้างตามภาพ image_57ad69.png เป๊ะๆ
        url = "https://coupon.netmarble.com/api/coupon/reward"
        params = {
            "gameCode": "tskgb",
            "couponCode": code.strip(),
            "langCd": "TH_TH",
            "pid": pid
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://coupon.netmarble.com/tskgb",
            "Accept": "application/json"
        }

        # ส่งแบบ GET ตามหลักฐานใน Network Tab
        response = requests.get(url, params=params, headers=headers, timeout=10)
        return jsonify(response.json())
    
    except Exception as e:
        return jsonify({"errorCode": 500, "errorMessage": str(e)}), 200

# ห้ามใส่ def handler หรือ if __name__ == "__main__"
