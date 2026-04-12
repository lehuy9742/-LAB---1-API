from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
# Import các công cụ lõi 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# 1. KHỞI TẠO FASTAPI
app = FastAPI(
    title="Hệ thống Tóm tắt Văn bản AI",
    description="API này sử dụng mô hình Hugging Face (BART) viết bằng code thủ công.",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# 2. KHỞI TẠO MÔ HÌNH AI 
MODEL_NAME = "facebook/bart-large-cnn"
print(f"Đang tải Tokenizer và Model {MODEL_NAME}... Vui lòng đợi...")

try:
    # Tải phễu băm chữ
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    # Tải não bộ AI
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    print("Tải mô hình thành công! Máy chủ đã sẵn sàng.")
except Exception as e:
    tokenizer = None
    model = None
    print(f"Lỗi khi tải mô hình: {e}")

# 3. KHUÔN MẪU DỮ LIỆU ĐẦU VÀO
class GenerateRequest(BaseModel):
    text: str = Field(..., min_length=20, description="Đoạn văn bản tiếng Anh cần tóm tắt")

# ==========================================
# CÁC ENDPOINT (API ROUTER)
# ==========================================

@app.get("/")
def read_root():
    return {
        "thong_bao": "Chào mừng đến với API Tóm tắt Văn bản (Manual Mode)",
        "chuc_nang": "Sử dụng AutoModelForSeq2SeqLM để tóm tắt văn bản",
        "huong_dan": "Gửi POST request tới /generate kèm theo dữ liệu JSON {'text': 'nội dung'}"
    }

@app.get("/health")
def health_check():
    # Kiểm tra xem cả tokenizer và model đã được tải lên chưa
    if tokenizer is not None and model is not None:
        return {"status": "ok", "model_loaded": True, "model_name": MODEL_NAME}
    else:
        raise HTTPException(status_code=503, detail="Mô hình AI chưa sẵn sàng hoạt động")

@app.post("/generate")
def generate_summary(request: GenerateRequest):
    try:
        input_text = request.text
        
        # --- BƯỚC 1: BĂM CHỮ (Tokenization) ---
        # truncation=True để cắt bỏ bớt nếu người dùng nhập bài báo quá dài (quá sức chịu đựng của AI)
        inputs = tokenizer(
            [input_text], 
            max_length=1024, 
            return_tensors="pt", 
            truncation=True
        )
        
        # --- BƯỚC 2: ĐÚT VÀO NÃO VÀ ÉP SINH CHỮ (Generation) ---
        # Áp dụng đầy đủ các kỹ năng thực chiến: giới hạn độ dài, cấm lặp từ (no_repeat_ngram_size)
        summary_ids = model.generate(
            inputs["input_ids"], 
            num_beams=4, 
            min_length=30, 
            max_length=130,
            no_repeat_ngram_size=3 
        )
        
        # --- BƯỚC 3: DỊCH NGƯỢC RA CHỮ (Decoding) ---
        summary = tokenizer.batch_decode(
            summary_ids, 
            skip_special_tokens=True, 
            clean_up_tokenization_spaces=False
        )[0]
        
        # Trả kết quả
        return {
            "status": "success",
            "original_length": len(input_text),
            "summary_text": summary
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi trong quá trình suy luận AI: {str(e)}")