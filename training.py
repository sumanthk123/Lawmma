from getpass import getpass
import os
from langchain_community.llms import Replicate

REPLICATE_API_TOKEN = getpass()
os.environ["REPLICATE_API_TOKEN"] = "r8_EMyu2j3ijntEI6q6BytU50P025FmKH43hdLqA"


llm1 = Replicate(
    model="meta/meta-llama-3.1-405b-instruct",
    model_kwargs={"temperature": 0.0, "top_p": 1, "max_new_tokens":500}
)

llm2 = Replicate(
    model = "meta/meta-llama-3.1-405b-instruct", 
    model_kwargs={"temperature": 0.0, "top_p": 1, "max_new_tokens":500}
)

question = "who wrote the book Innovator's dilemma?"
answer = llm1.invoke(question)
second_answer = llm2.invoke(answer)
print("first answer:", answer)
print("second answer:",second_answer)