# 🚀 AI Text Summarizer API (FastAPI + BART)

Dự án này là một hệ thống tóm tắt văn bản tiếng Anh tự động dựa trên trí tuệ nhân tạo (AI). Hệ thống sử dụng mô hình ngôn ngữ lớn để trích xuất những ý chính từ các đoạn văn bản dài, giúp tiết kiệm thời gian đọc và nắm bắt thông tin.

---

## 🌟 Tính năng chính
* **Tóm tắt thông minh:** Sử dụng mô hình `facebook/bart-large-cnn` chuyên dụng cho tóm tắt tin tức.
* **API Hiệu năng cao:** Xây dựng trên nền tảng FastAPI giúp xử lý yêu cầu nhanh chóng.
* **Giao diện Swagger UI:** Cho phép thử nghiệm API trực tiếp tại đường dẫn `/docs`.
* **Public Access:** Tích hợp hướng dẫn sử dụng Pinggy/Localhost.run để chia sẻ link qua Internet.

---

## 🛠️ Công nghệ sử dụng
* **Ngôn ngữ:** Python 3.9+
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **AI Engine:** [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
* **Model:** BART Large CNN
* **Tunneling:** Pinggy / Localhost.run

---

## ⚙️ Cài đặt & Cấu hình

Để dự án hoạt động ổn định, vui lòng tuân thủ các bước thiết lập môi trường ảo dưới đây:

### 1. Khởi tạo môi trường ảo (venv)
```bash
python -m venv venv
```

### 2. Kích hoạt môi trường
* **Windows:**
  ```powershell
  .\venv\Scripts\activate
  ```
* **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 3. Cài đặt thư viện
```bash
pip install fastapi uvicorn transformers torch requests
```

---

## 🚀 Hướng dẫn vận hành

Hệ thống cần chạy song song hai tiến trình (Terminal) để có thể truy cập từ xa.

### Bước 1: Khởi động Server (Terminal 1)
```bash
python -m uvicorn main:app --reload
```
* Sau khi chạy, API sẽ sẵn sàng tại: `http://127.0.0.1:8000`

### Bước 2: Tạo đường hầm Public (Terminal 2)
Mở một cửa sổ mới và gõ lệnh sau để lấy link truy cập từ Internet:
```bash
ssh -p 443 -R0:127.0.0.1:8000 pinggy@a.pinggy.io
```
* Copy link `https://...` hiện ra và thêm `/docs` vào cuối để sử dụng giao diện web.

---

## 🎥 Video Demo (60s)

[Kéo thả video demo của bạn vào đây để GitHub tự tạo link]

---

## 📂 Cấu trúc dự án
```text
API_PROJECT/
├── main.py            # Code xử lý chính (FastAPI & AI Model)
├── test_API.py        # Script kiểm tra API từ Client
├── requirements.txt   # Danh sách thư viện (nếu có)
├── README.md          # Tài liệu hướng dẫn này
└── venv/              # Môi trường ảo (đã được loại bỏ khỏi Git)
```

---

## 👤 Tác giả
* **Họ và tên:** [Tên của bạn]
* **MSSV:** [Mã số sinh viên của bạn]
* **Đơn vị:** Khoa Công nghệ Thông tin - Trường ĐH Khoa học Tự nhiên (VNU-HCM)
* **Môn học:** Tư duy tính toán