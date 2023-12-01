import os
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = open("API_KEY", "r").read()

def generateResponse(prompt):
    query = prompt


    #loader = TextLoader('custom_data.txt')
    loader = DirectoryLoader(path="./Data", glob = "*.txt")

    index = VectorstoreIndexCreator().from_loaders([loader])

    try:
        response = index.query(query, llm=ChatOpenAI(max_tokens=100, temperature=1)).replace('\n', '<br>')

    except:
        response = 'oops, You beat the AI'

    return response

