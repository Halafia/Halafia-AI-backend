import os
import key
#from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import LLMChain
#from langchain.llms import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)



os.environ["OPENAI_API_KEY"] = key.API_KEY

model=ChatOpenAI(max_tokens=1024, temperature=1)
user_input = "Hello Halafia, analyze the risk associated to my health challenge"


def generatie_risk_assessment(prompt, name="Halafia"):
    chat = model
    user = prompt

    system_template = """
    
    Your name is {name}, you are a helpful generative risk assessment assistant that help people in finding out what risk is
    associated with their health challenges, the health challenge to consider {health_challenge}. Your goal is to help the user analyze the risk associated with
    the particular health challege.

    Don't tell the user you don't know, instead of telling the user you don't know you can throw them a piece
    of advice about that health challege presented to you.

    Consider how deadly {health_challenge} is, and the risk involved in keeping {health_challenge} in the body,
    and consider their {allegeries}

    Start your reply with "Hello there this is {name}, here is an analysis for your patient", then give them a response
    strating from a newline.
    
    Make sure to sign the response off with {signature}

    """

    signature = f"Your's truly, \n{name}"
    health_challenge = f"malaria"
    allegeries = f""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    
    user_template = "Hello Halafia, analyze the risk associated to my health challenge: {health_challenge}"
#    user_template = prompt

    human_message_prompt = HumanMessagePromptTemplate.from_template(user_template)

    input_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=input_prompt)
    response = chain.run(signature=signature, name=name, health_challenge=health_challenge, allegeries=allegeries)

    return response


def alternate_risk_assessment(prompt):

    query = prompt
#    query = user_input


    #loader = TextLoader('custom_data.txt')
    loader = DirectoryLoader(path="./Data", glob = "*.txt")

    index = VectorstoreIndexCreator().from_loaders([loader])

    try:
        response = index.query(query, llm=model).replace('\n', '<br>')

    except:
        response = 'OOPS!!! The response system may be down at this moment, you can check back later.'

    return response

print_statement = generatie_risk_assessment()

print(print_statement)