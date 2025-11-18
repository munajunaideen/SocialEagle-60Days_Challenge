from langchain_huggingface import HuggingFaceEmbeddings
huggingface_embed = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
text = "This is the one of most powerful embedding model."
emb = huggingface_embed.embed_query(text)
print(emb[:10])  # print first 10 numbers