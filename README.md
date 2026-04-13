# 🚀 AI Text Summarizer API (FastAPI + BART)

Dự án Xây dựng Hệ thống Tóm tắt Văn bản Tiếng Anh tự động dựa trên Trí tuệ Nhân tạo (AI). Hệ thống cung cấp API hiệu năng cao để trích xuất những ý chính từ các đoạn văn bản tin tức dài chỉ trong vài giây.

Dự án được thực hiện phục vụ cho đồ án môn học **Tư duy tính toán**.

---

## 👨‍🎓 Thông tin sinh viên
* **Họ và tên:** Lê Nguyễn Gia Huy
* **Mã số sinh viên (MSSV):** 24120061
* **Trường:** Đại học Khoa học Tự nhiên TP.HCM (VNU-HCMUS)
* **Khoa:** Công nghệ Thông tin
* **Lớp:**24CTT3

---

## 🤖 Thông tin Mô hình AI
* **Mô hình cốt lõi:** `facebook/bart-large-cnn`
* **Nền tảng:** [Hugging Face](https://huggingface.co/facebook/bart-large-cnn)
* **Mô tả:** Hệ thống sử dụng mô hình ngôn ngữ lớn BART (Bidirectional and Auto-Regressive Transformers) đã được tinh chỉnh (fine-tuned) trên bộ dữ liệu báo chí CNN/Daily Mail. Mô hình đặc biệt xuất sắc trong việc tóm tắt dạng trích xuất (Abstractive Summarization) cho các văn bản tiếng Anh.

---

## 📂 Cấu trúc Dự án

```text
API_PROJECT/
├── main.py              # File chứa mã nguồn chính của FastAPI và Load Model AI
├── test_API.py          # Script kiểm thử tự động (Auto-test các trường hợp lỗi)
├── requirements.txt     # Danh sách các thư viện cần cài đặt
├── README.md            # Tài liệu hướng dẫn sử dụng (File này)
└── .gitignore           # File cấu hình bỏ qua thư mục venv khi đẩy lên GitHub
```

---

## ⚙️ Hướng dẫn Cài đặt (Step-by-Step)

Vui lòng làm theo trình tự các bước sau để thiết lập môi trường chạy dự án:

### Bước 1: Yêu cầu hệ thống
* Đảm bảo máy tính đã cài đặt **Python 3.9** trở lên.
* Mở Terminal/Command Prompt và di chuyển vào thư mục dự án `API_PROJECT`.

### Bước 2: Khởi tạo và Kích hoạt Môi trường ảo (Virtual Environment)
Việc sử dụng môi trường ảo giúp tránh xung đột thư viện trên máy tính.
* **Tạo môi trường:**
  ```bash
  python -m venv venv
  ```
* **Kích hoạt (Activate):**
  * Trên Windows (PowerShell/CMD):
    ```powershell
    .\venv\Scripts\activate
    ```
  * Trên Mac/Linux (Bash):
    ```bash
    source venv/bin/activate
    ```
*(Lưu ý: Sau khi kích hoạt, bạn sẽ thấy chữ `(venv)` hiện ở đầu dòng lệnh).*

### Bước 3: Cài đặt Thư viện
Chạy lệnh sau để tự động tải và cài đặt toàn bộ công cụ cần thiết (FastAPI, Transformers, PyTorch,...):
```bash
pip install -r requirements.txt
```
*(Nếu chưa có file requirements.txt, hãy chạy: `pip install fastapi uvicorn transformers torch pydantic requests`)*

---

## 🚀 Hướng dẫn Chạy Hệ thống & Swagger UI

### 1. Khởi động Server cục bộ (Local)
Tại Terminal (đang bật venv), gõ lệnh sau để chạy máy chủ:
```bash
python -m uvicorn main:app --reload
```
Khi Terminal báo `Application startup complete`, hệ thống đã sẵn sàng!

### 2. Giao diện Swagger UI (Đóng vai trò Client)
FastAPI tự động sinh ra một giao diện website cực kỳ trực quan để người dùng tương tác với AI mà không cần viết code frontend.
👉 **Truy cập ngay:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Tại trang này, bạn có thể xem toàn bộ cấu trúc API, nhấn nút **"Try it out"**, nhập văn bản và nhấn **"Execute"** để nhận kết quả tóm tắt ngay trên trình duyệt.

### 3. Chia sẻ Public qua Internet (Tùy chọn Demo)
Để giảng viên hoặc bạn bè truy cập được vào Swagger UI của bạn từ xa, mở thêm một Terminal mới và gõ lệnh tạo đường hầm Pinggy:
```bash
ssh -p 443 -R0:127.0.0.1:8000 pinggy@a.pinggy.io
```
Copy đường link kết thúc bằng `.link` và thêm `/docs` vào cuối để gửi cho người khác.

---

## 📡 Tài liệu API (Endpoints)

Hệ thống cung cấp 2 cổng giao tiếp chính:

### 1. Kiểm tra trạng thái (`GET /health`)
* **Chức năng:** Kiểm tra xem máy chủ và mô hình AI đã tải xong chưa.
* **Response (200 OK):**
  ```json
  {
    "status": "ok",
    "message": "Server và Model đang hoạt động tốt!"
  }
  ```

### 2. Tóm tắt Văn bản (`POST /generate`)
* **Chức năng:** Gửi văn bản tiếng Anh để AI tóm tắt.
* **Validation (Ràng buộc):** Dữ liệu phải là chuỗi (string) và dài tối thiểu 20 ký tự.
* **Request Body (JSON):**
  ```json
  {
    "text": "The Amazon rainforest, often referred to as the lungs of the Earth, plays a crucial role in regulating the global climate. It absorbs millions of tons of carbon dioxide emissions every year, helping to slow down global warming. However, deforestation driven by logging, mining, and agriculture threatens this vital ecosystem..."
  }
  ```
* **Response (200 OK):**
  ```json
  {
    "original_length": 345,
    "summary_text": "The Amazon rainforest plays a crucial role in regulating the global climate. However, deforestation threatens this vital ecosystem."
  }
  ```

---

## 🧪 Kiểm thử Tự động (Auto-Testing)

Dự án được tích hợp sẵn kịch bản kiểm thử để đảm bảo tính ổn định và khả năng bắt lỗi (Error Handling) của hệ thống.

Để chạy kiểm thử, mở Terminal mới (đã bật venv) và chạy:
```bash
python test_API.py
```
Kịch bản sẽ tự động chạy 5 bài test:
1. Gửi văn bản hợp lệ (Kỳ vọng: Trả về bản tóm tắt).
2. Kiểm tra `Health Check`.
3. Gửi sai tên trường dữ liệu (Kỳ vọng: Báo lỗi 422).
4. Gửi văn bản quá ngắn dưới 20 ký tự (Kỳ vọng: Báo lỗi 422).
5. Gửi sai kiểu dữ liệu - gửi số thay vì chuỗi (Kỳ vọng: Báo lỗi 422).

---

## 🎥 Video Demo Thực tế

Dưới đây là video quá trình khởi chạy, test bằng Swagger UI và xử lý kết quả:





https://github.com/user-attachments/assets/fbcf07df-26e4-4ab6-92a6-b86fcea3fcc9







