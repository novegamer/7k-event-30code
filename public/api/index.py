from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/redeem', methods=['POST'])
def redeem():
    data = request.json
    pid = data.get('pid')
    codes = data.get('codes', [])
    
    # URL จากรูป Headers ที่คุณส่งมา
    base_url = "https://coupon.netmarble.com/api/coupon/reward"
    
    results = []
    for code in codes:
        # พารามิเตอร์ตามรูป Payload ที่คุณส่งมา
        params = {
            "gameCode": "tskgb",
            "couponCode": code.strip(),
            "langCd": "TH_TH",
            "pid": pid
        }
        
        try:
            # ใช้ GET ตามที่ระบุใน Request Method ในรูป
            response = requests.get(base_url, params=params, timeout=10)
            res_json = response.json()
            
            # ดึงข้อความตอบกลับจาก Netmarble
            msg = res_json.get("resultMsg", "ไม่ทราบสถานะ")
            results.append({"code": code, "status": msg})
        except Exception as e:
            results.append({"code": code, "status": f"Error: {str(e)}"})
            
    return jsonify(results)

# จำเป็นสำหรับการรันบน Vercel
def handler(event, context):
    return app(event, context)
