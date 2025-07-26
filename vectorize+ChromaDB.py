from transformers import AutoTokenizer, AutoModel
import torch
import chromadb
from chromadb.config import Settings
import faiss
import numpy as np
import pickle

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings[0].numpy()


#chromaDB
client = chromadb.PersistentClient(path="./code_index")  # ✅ NEW
collection = client.get_or_create_collection("code_snippets")


#ast of all languages
from extract_code import Extract
base_dir = r"C:\Users\FASI OWAIZ AHMED\Desktop\Code_gen\Data"
extracted=Extract.extract_all_functions(base_dir)


# vectorizing and storing in chromaDB
faiss_embeddings = []
faiss_metadata = []

for idx, item in enumerate(extracted):
    text_for_embedding = item["function_name"] + " "+ item["code"] + " " + item["docstring"]
    vector = get_embedding(text_for_embedding)

    collection.add(
        documents=[text_for_embedding],
        embeddings=[vector],
        metadatas=[{
            "function_name": item["function_name"],
            "file_path": item["file_path"],
            "language": item["language"],
            "docstring": item["docstring"]
        }],
        ids=[str(idx)]
    )
    faiss_embeddings.append(vector)
    faiss_metadata.append(item)
embedding_matrix = np.vstack(faiss_embeddings).astype("float32")
index = faiss.IndexFlatL2(embedding_matrix.shape[1])
index.add(embedding_matrix)

# Save FAISS index and metadata
faiss.write_index(index, "code_index.faiss")
with open("faiss_metadata.pkl", "wb") as f:
    pickle.dump(faiss_metadata, f)

