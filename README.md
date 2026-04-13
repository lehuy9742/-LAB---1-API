# 🚀 AI Text Summarizer API (FastAPI + BART)

Dự án này là một hệ thống tóm tắt văn bản tiếng Anh tự động dựa trên trí tuệ nhân tạo (AI), được thực hiện cho môn học **Tư duy tính toán**.

---

## 👤 Thông tin sinh viên
* **Họ và tên:** Lê Nguyễn Gia Huy
* **Mã số sinh viên (MSSV):** 24120061
* **Trường:** Đại học Khoa học Tự nhiên TP.HCM (VNU-HCMUS)
* **Khoa:** Công nghệ Thông tin
* **Môn học:** Tư duy tính toán
---

## 🤖 Mô hình AI
* **Tên mô hình:** `facebook/bart-large-cnn`
* **Liên kết trên Hugging Face:** [https://huggingface.co/facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)
* **Mô tả:** Mô hình BART (Bidirectional and Auto-Regressive Transformers) được huấn luyện chuyên biệt trên tập dữ liệu CNN/Daily Mail để thực hiện tóm tắt văn bản theo dạng trích xuất ý chính (Abstractive Summarization).

---

## 📝 Mô tả chức năng
Hệ thống cung cấp một giao diện API cho phép:
1. **Kiểm tra trạng thái:** Đảm bảo máy chủ và mô hình đã sẵn sàng hoạt động.
2. **Tóm tắt văn bản:** Tự động thu gọn các đoạn văn bản dài thành một đoạn văn ngắn súc tích mà vẫn giữ nguyên được nội dung cốt lõi của thông tin.

---

## ⚙️ Hướng dẫn cài đặt thư viện

Yêu cầu máy tính đã cài đặt Python 3.9+. Sau khi tạo và kích hoạt môi trường ảo (`venv`), hãy chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install fastapi uvicorn transformers torch requests
```

---

## 🚀 Hướng dẫn chạy chương trình

### 1. Khởi chạy Server cục bộ (Local)
Mở Terminal và gõ lệnh khởi động máy chủ FastAPI:
```bash
python -m uvicorn main:app --reload
```
Sau đó, bạn có thể truy cập vào giao diện thử nghiệm trực quan tại: `http://127.0.0.1:8000/docs`

### 2. Tạo đường link Public (Truy cập từ xa)
Để người khác có thể truy cập API của bạn qua Internet (dành cho demo), mở Terminal thứ hai và chạy:
```bash
ssh -p 443 -R0:127.0.0.1:8000 pinggy@a.pinggy.io
```

---

## 📡 Hướng dẫn gọi API và Ví dụ

### Endpoint 1: Kiểm tra trạng thái
* **URL:** `/health`
* **Method:** `GET`
* **Ví dụ Response:**
  ```json
  { "status": "ok", "message": "Server is running perfectly!" }
  ```

### Endpoint 2: Tóm tắt văn bản
* **URL:** `/generate`
* **Method:** `POST`
* **Ví dụ Request (JSON):**
  ```json
  {
    "text": "Artificial intelligence is a field of computer science that focuses on creating systems capable of performing tasks that typically require human intelligence..."
  }
  ```
* **Ví dụ Response:**
  ```json
  {
    "original_length": 1500,
    "summary_text": "AI focuses on creating systems that mimic human intelligence tasks."
  }
  ```

---

## 🎥 Video Demo
Dưới đây là video hướng dẫn sử dụng và kết quả thực tế của hệ thống:



https://github.com/user-attachments/assets/1e97d117-3be7-4b06-bd98-005e95233918






