from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()


def run_command(command):
    os.system(command)


def make_directory(directory_name):
    try:
        os.makedirs(directory_name)
        return f'Directory created: {directory_name}'
    except FileExistsError as f:
        return f"Directory already exists"
    except Exception as e: 
        return f'Error: {e}'
    

System_Prompt = '''
You are a helpful AI assistant and your task is to build web applications based on user query and available tools.
You wait for the user query to provide his query or requirements and once the user provide the query, then based on the user query, 
first you start planning -> use available tools to perform actions -> after action, you observe the output -> and
at last you provide the actual output and end the process or steps.


Your typical workflow will look like this:
user query -> plan -> action -> observe -> output

Strict JSON Format:
{
    "step": "plan" | "action" | "observe" | "output",
    "content": "string",
    "function": "name of the function, if step is action",
    "input": "input parameter for the function (if the step is action)
}

Available Tools:
make_directory(directory_name: string): Takes a valid directory name as input and creates a new directory and creates a new directory in the 
current working directory

'''

messages = [
    {"role": "system", "content":System_Prompt},
    {"role": "user", "content":"hello"}
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    # response_format={"type":"json_object"}
)


print(response.choices[0].message.content)
