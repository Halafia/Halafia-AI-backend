import os
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI
import key


os.environ["OPENAI_API_KEY"] = key.API_KEY

def generateResponse(prompt):
    query = prompt


    #loader = TextLoader('custom_data.txt')
    loader = DirectoryLoader(path="./Data", glob = "*.txt")

    index = VectorstoreIndexCreator().from_loaders([loader])

    try:
        response = index.query(query).replace('\n', '<br>')

    except:
        response = index.query(query, llm=ChatOpenAI(max_tokens=100, temperature=1)).replace('\n', '<br>')

    return response

