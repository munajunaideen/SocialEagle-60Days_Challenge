
import os
from langchain_openai import OpenAIEmbeddings

# Load API key from environment variable to avoid committing secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_embed = OpenAIEmbeddings(
    api_key=OPENAI_API_KEY,
    model="text-embedding-3-small"
)

text = "Assalamu Alaikum"
emb = openai_embed.embed_query(text)
print(emb[:10])  # print first 10 numbers
