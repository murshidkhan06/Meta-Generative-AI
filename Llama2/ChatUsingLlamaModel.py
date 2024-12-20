
#Build a Local Chatbot in Python with Just 10 Lines of Code! #falconSp

from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
    model_type='llama',config={'max_new_tokens':256,'temperature':0.01})
template="""You are a helpful assistant,answer {input_text} submitted by the user """
prompt=PromptTemplate(input_variables=["input_text"],template=template)
input_text = ' Why engineers are so smart ? '
response=llm(prompt.format(input_text=input_text))
print(response)
