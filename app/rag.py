import json
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "incidents.json"

def load_vector_db():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        incidents = json.load(f)

    texts = [i["incident"] for i in incidents]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.from_texts(texts, embeddings)
