from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path="restaurant_reviews.csv", encoding="utf-8")
docs = loader.load()

print(f"문서 수: {len(docs)}")
print(docs[0])
