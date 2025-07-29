import os

# os.environ is a mapping object that helps user to map environmental variables
# print(os.environ)

from pprint import pprint

# pprint(os.environ)

# Integration of Avalai Openai API and langchain_openai
### Start ###
os.environ["OPENAI_API_BASE"]='https://api.avalai.ir/v1'
os.environ["OPENAI_API_KEY"]='aa-dd55t7AxtRxzSCDzdTCIgAjxz2M9ZAAOxDv2R6xYnGVdWjcI'

from langchain_openai import ChatOpenAI, OpenAI

llm=ChatOpenAI(model='gpt-4o', temperature=0.7)

response= llm.invoke("Hello, who are you?")
print(response.content)
### End ###
