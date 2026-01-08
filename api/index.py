from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/redeem', methods=['POST'])
def redeem():
    try:
        data = request.json
        playerId = data.get('playerId')
        code = data.get('code')

        # URL และ Parameter ตามรูป image_4bdf67.png และ image_4bdbe2.png
        url = "https://coupon.netmarble.com/api/coupon/reward"
        params = {
            "gameCode": "tskgb",
            "couponCode": code.strip(),
            "langCd": "TH_TH",
            "playerId": playerId
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://coupon.netmarble.com/tskgb"
        }

        # ส่งแบบ GET ตามรูปที่ส่งมา
        response = requests.get(url, params=params, headers=headers, timeout=10)
        return jsonify(response.json())
    
    except Exception as e:
        # ป้องกัน Error 500 โดยการส่งข้อความ Error กลับไปแทน
        return jsonify({"resultCode": "ERROR", "resultMsg": str(e)}), 200

# สำหรับ Vercel Runtime
def handler(req, res):
    return app(req, res)
