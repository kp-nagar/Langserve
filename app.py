from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
import os
from config import settings


# 1. Create prompt template
system_template = "who is founder of {item}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{item}')
])

os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
model = ChatOpenAI(model=settings.OPENAI_MODEL)

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route
add_routes(
    app,
    chain,
    path="/ask",
)
