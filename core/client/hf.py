import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# For better security, load environment variables from a .env file
from dotenv import load_dotenv

load_dotenv()

# Make sure your OPENAI_API_KEY is set in the .env file
hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
# print(hf_token)

# Initialize the Language Model (using ChatOpenAI is recommended)
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="conversational",
    huggingfacehub_api_token=hf_token,
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")

print(result)
