import sys
import halafia
import os

os.environ["OPENAI_API_KEY"] = halafia.API_KEY

from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI


query = input('user: ')


#loader = TextLoader('custom_data.txt')
loader = DirectoryLoader(path="./Data", glob = "*.txt")

index = VectorstoreIndexCreator().from_loaders([loader])
print(index.query(query, llm=ChatOpenAI()))

