import requests
import json

# Địa chỉ Server của bạn (đảm bảo main.py đang chạy)
BASE_URL = "http://127.0.0.1:8000"

def print_result(test_name, response):
    """Hàm hỗ trợ in kết quả ra màn hình cho đẹp"""
    print(f"\n{'='*50}")
    print(f"🧪 BÀI TEST: {test_name}")
    print(f"Mã trạng thái (Status Code): {response.status_code}")
    print("Dữ liệu trả về (JSON):")
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except:
        print(response.text)
    print(f"{'='*50}")

def run_all_tests():
    print("🚀 BẮT ĐẦU CHẠY AUTO-TEST API...\n")

    # ---------------------------------------------------------
    # TEST 1: Kiểm tra Health Check (Kỳ vọng: 200 OK)
    # ---------------------------------------------------------
    res = requests.get(f"{BASE_URL}/health")
    print_result("1. Kiểm tra trạng thái máy chủ (/health)", res)

    # ---------------------------------------------------------
    # TEST 2: Gửi dữ liệu ĐÚNG chuẩn (Kỳ vọng: 200 OK)
    # ---------------------------------------------------------
    valid_data = {
        "text": "Artificial intelligence is a field of computer science that focuses on creating systems capable of performing tasks that typically require human intelligence. These tasks include learning, reasoning, problem-solving, perception, and language understanding."
    }
    res = requests.post(f"{BASE_URL}/generate", json=valid_data)
    print_result("2. Chạy AI tóm tắt văn bản thành công (Happy Path)", res)

    # ---------------------------------------------------------
    # TEST 3: Gửi SAI tên biến (Kỳ vọng: Lỗi 422)
    # ---------------------------------------------------------
    wrong_key_data = {
        "noidung": "This text should be summarizer but the key is wrong."
    }
    res = requests.post(f"{BASE_URL}/generate", json=wrong_key_data)
    print_result("3. Gửi sai tên biến (Dùng 'noidung' thay vì 'text')", res)

    # ---------------------------------------------------------
    # TEST 4: Gửi dữ liệu QUÁ NGẮN (Kỳ vọng: Lỗi 422)
    # ---------------------------------------------------------
    # Nhớ lại trong main.py ta đã cài min_length=20
    short_text_data = {
        "text": "Too short!"
    }
    res = requests.post(f"{BASE_URL}/generate", json=short_text_data)
    print_result("4. Gửi văn bản quá ngắn (< 20 ký tự)", res)

    # ---------------------------------------------------------
    # TEST 5: Gửi SAI kiểu dữ liệu (Kỳ vọng: Lỗi 422)
    # ---------------------------------------------------------
    wrong_type_data = {
        "text": 1234567890987654321  # Gửi số thay vì chuỗi
    }
    res = requests.post(f"{BASE_URL}/generate", json=wrong_type_data)
    print_result("5. Gửi sai kiểu dữ liệu (Số nguyên thay vì Chuỗi)", res)

if __name__ == "__main__":
    try:
        run_all_tests()
    except requests.exceptions.ConnectionError:
        print("\n❌ LỖI KẾT NỐI: Không tìm thấy Server. Bạn đã bật uvicorn main:app --reload chưa?")