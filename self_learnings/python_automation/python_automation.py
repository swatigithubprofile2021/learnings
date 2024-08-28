import requests
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt",help = "The prompt to dent to the")
parser.add_argument("file_name",help = "name of the file to save in python script")


args  = parser.parse_args()


api_endpoint = "https://api.openai.com/v1/completions"
API_KEY = os.getenv("OPENAI_API_KEY")
# print(API_KEY)

request_headers = { 
    "Content-Type" : "application/json",
    "Authorization" : "Bearer " + API_KEY


}

request_data = {
  "model": "text-davinci-003",
  "prompt": f"write python script for {args.prompt} ",
  "max_tokens": 800,
  "temperature": 0.5,
}

response = requests.post(api_endpoint,headers =request_headers,json = request_data )
print(response.text)

if response.status_code ==200:
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name,"w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")    
    


