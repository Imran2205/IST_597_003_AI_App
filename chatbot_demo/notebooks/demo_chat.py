from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.chains import LLMChain
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain import HuggingFaceHub, PromptTemplate
import chainlit as cl
import getpass
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Check available GPUs
if torch.cuda.is_available():
    num_gpus = torch.cuda.device_count()
    print(f"Number of GPUs available: {num_gpus}")
    for i in range(num_gpus):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("CUDA is not available. Using CPU.")
    num_gpus = 0

# Load the model and tokenizer
model_name = "microsoft/Phi-3-mini-128k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, device_map="auto")

# Specify which GPUs to use
gpu_ids = list(range(num_gpus))  # Use all available GPUs

if num_gpus > 0:
    print(f"Using GPUs: {gpu_ids}")
    # Model is already distributed across GPUs due to device_map="auto"
else:
    print("No GPUs available. Using CPU.")

# Create a transformers pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=256,  # Increased due to larger context window
    temperature=0.7,
    top_p=0.9,
    device_map="auto"  # This will use all available GPUs efficiently
)

# Create a HuggingFacePipeline
conv_model = HuggingFacePipeline(pipeline=pipe)

template = """
    You're a very helpful AI assistant who assists users by answering their queries.

    {query}
"""

@cl.on_chat_start
def on_chat_start():
    # model = ChatOpenAI(streaming=True)
    
    # model = ChatHuggingFace(llm=llm)
    # prompt = ChatPromptTemplate.from_messages(
    #     [
    #         (
    #             "system",
    #             "You're a very knowledgeable historian who provides accurate and eloquent answers to historical questions.",
    #         ),
    #         ("human", "{question}"),
    #     ]
    # )
    prompt = PromptTemplate(template=template, input_variables=['query'])
    chain = LLMChain(llm=conv_model, prompt=prompt, verbose=True)

    cl.user_session.set("chain", chain)


@cl.on_message 
async def on_message(message: cl.Message):
    chain = cl.user_session.get("chain")  # type: LLMChain

    res = await chain.acall(
        message.content, callbacks=[cl.AsyncLangchainCallbackHandler()]
    )

    await cl.Message(content=res["text"]).send()