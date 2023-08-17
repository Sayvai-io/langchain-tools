""" Using Langchain Going to Generate a Server that can be used to shcedule meetings """
# Importing the required libraries
import os
from langchain.chat_models import ChatOpenAI
from typing import List, Dict, Any
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

with open("OPEN_AI_KEY.txt", "r") as f:
    OPEN_AI_KEY = f.read()

with open("SERP_API_KEY.txt", "r") as f:
    SERP_API_KEY = f.read()

os.environ["OPENAI_API_KEY"] = OPEN_AI_KEY
os.environ["SERPAPI_API_KEY"] = SERP_API_KEY


class CustomError(Exception):
    pass


class LlmServer:
    """LLm server class"""
    def __init__(self) -> None:
        self.llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
        self.tools = None
        self.agent = None
    
    def initialize_agent(self, tools: List, agent: str) -> str:
        """Initialize the server"""
        if self.tools is None:
            self.tools = load_tools(tools, llm=self.llm)
        self.agent = initialize_agent(self.tools, self.llm, agent, verbose=True)
        return "Initialized"
    
    def initialize_llm(self):
    
    def get_response(self, text: str) -> Dict[str, Any]:
        if self.agent is None:
            raise CustomError('Not Initialized error')
        response = self.agent.run(text)
        return response

    