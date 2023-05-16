import os
import openai
import arxiv
import google_serp_api
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools,initialize_agent,AgentType
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from spotipy import SpotifyClientCredentials

load_dotenv()

openai.api_key= os.getenv('OPENAI_API_KEY')
google_serp_api.client = os.getenv('SERPAPI_API_KEY')
my_api_key = os.getenv('CUSTUM_SEARCH_API_KEY')
my_cs_id = os.getenv('CUSTUM_SEARCH_ID')



lili = OpenAI(temperature=0.9)

search = GoogleSearchAPIWrapper


tools = load_tools(["arxiv"],)
recherche = load_tools(["serpapi","llm-math"],llm=lili)
tool = T

goo



agent_chain = initialize_agent(tools,lili,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True,)

while True:

    agent_chain.run(input("YMC: "))