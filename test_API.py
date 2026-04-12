import requests
import json

# URL của API cục bộ
API_URL = "http://127.0.0.1:8000/generate"

# Dữ liệu mẫu để test
payload = {
    "text": (
        "PG&E stated it scheduled the blackouts in response to forecasts for high winds "
        "amid dry conditions. The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were "
        "scheduled to be affected by the shutoffs which were expected to last through at least midday tomorrow."
    )
}

# Gửi yêu cầu POST kèm JSON [cite: 40]
try:
    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        print("--- GỌI API THÀNH CÔNG ---")
        result = response.json()
        print(f"Nội dung gốc: {result['original_length']}...")
        print(f"Bản tóm tắt: {result['summary_text']}")
    else:
        print(f"Lỗi API: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Không thể kết nối tới API: {e}")