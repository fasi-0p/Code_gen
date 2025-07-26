from vectorize import get_embedding

import chromadb
from chromadb.config import Settings
#chromaDB
client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./code_index"))
collection = client.get_or_create_collection(name="code_snippets")

#ast of all languages
from extract_code import Extract
base_dir = r"C:\Users\FASI OWAIZ AHMED\Desktop\Code_gen\Data"
extracted=Extract.extract_all_functions(base_dir)

# vectorizing and storing in chromaDB
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
