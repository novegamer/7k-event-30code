from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/redeem', methods=['POST'])
def redeem():
    try:
        data = request.json
        pid = data.get('pid') #
        code = data.get('code') #

        # URL สำหรับส่ง GET request ตามโครงสร้างที่คุณตรวจพบ
        url = "https://coupon.netmarble.com/api/coupon/reward"
        
        # ตั้งค่า Query String Parameters ตามที่คุณให้มา
        params = {
            "gameCode": "tskgb",
            "langCd": "TH_TH",
            "pid": pid,
            "couponCode": code.strip()
        }
        
        # ตั้งค่า Headers ตามที่คุณตรวจพบ
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", # แนะนำให้ใช้ตัวเต็มเพื่อความปลอดภัย
            "Origin": "https://coupon.netmarble.com",
            "Referer": "https://coupon.netmarble.com/tskgb"
        }

        # ทำการส่งคำขอแบบ GET
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        # ส่งผลลัพธ์กลับไปที่หน้าเว็บ
        return jsonify(response.json())
    
    except Exception as e:
        # หากเกิดข้อผิดพลาด จะส่ง JSON แทนการเกิด Error 500
        return jsonify({"resultCode": "ERROR", "resultMsg": f"Backend Error: {str(e)}"}), 200

def handler(req, res):
    return app(req, res)
