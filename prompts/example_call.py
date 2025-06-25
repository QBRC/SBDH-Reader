import os
import sys
import openai
import time
import pandas as pd
import json
import numpy as np
from openai import AzureOpenAI

import caller
import cats

# Create and Insert credentials in the file: SBDH-LLM/creds/azure_credentials.json
azure_creds_file = "../../creds/azure_credentials.json"
    
with open(azure_creds_file, 'r') as file:
    azure_data = json.load(file)
    api_key = azure_data['API_KEY']
    api_version = azure_data['API_VERSION']
    azure_endpoint = azure_data['AZURE_ENDPOINT']
    azure_deployment_name = azure_data['AZURE_DEPLOYMENT_NAME']

assert api_key != None, ""
assert api_version != None, ""
assert azure_endpoint != None, ""
assert azure_deployment_name != None, ""

azure_client = AzureOpenAI(
    api_key = api_key,
    api_version = api_version,
    azure_endpoint = azure_endpoint
    )

# load and format data

# select categories to extract
# my_cats_step1 = [cats.housing, cats.employment]
my_cats_step2 = [cats.employment, cats.alcohol]


message_text = caller.get_llm_step1_input_message(free_text = 'Patient is homeless but he has got a steady job at a foodtruck', cats = my_cats_step2, print_prompt=True)

print(message_text)

# # call api
# response = azure_client.chat.completions.create(
#     model=azure_deployment_name,
#     response_format={ "type": "json_object" },
#     messages=message_text,
#     temperature=0,
#     max_tokens=50,
#     top_p=0.95,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=None
#     )

# print(response.choices[0].message.content.strip())

#   response = openai.ChatCompletion.create(
#     engine=DEPLOYMENT_NAME,
#     messages = message_text,
#     temperature=0,
#     max_tokens=1500,
#     top_p=0.95,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=None,
#     response_format={ "type": "json_object" }
#   )
#   raw_response = response['choices'][0]['message']['content']
#   # json_response = json.loads(raw_response)
#   # print(json_response)

# post-processing and evaluate results