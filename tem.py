import requests
import os
import subprocess
import time 

api_token_gpt = "api token for gpt or any other ai"
def requesting(user_input,api_token):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    
    data = {
        "model": "gpt-4.1-mini",
        "messages": [
            {
                "role": "user",
                "content": f"""
    You are TerminalManagerAI, an expert Linux Mint terminal assistant.
    Your job is to help the user perform system tasks, automation, file operations,
    package installs, updates, process management, networking, and system configuration.
    This environment is Linux Mint (Ubuntu-based).

    Your ONLY output must be the exact shell command(s) needed to accomplish the given task — nothing else.
    No explanations. No comments. No markdown. No extra words.
    Only valid Linux bash commands.

    Below is the user's requested operation.
    Interpret it and output ONLY the necessary Linux Mint terminal commands to accomplish it:

    "{user_input}"
    """
            }
        ]
    }

    response = requests.post(url,headers=headers,json=data)
    return response
def parser(data):
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return None
while True:  
    user_input = input("User#> ")
    data = requesting(user_input,api_token_gpt)
    data = data.json()

    parsed_data = parser(data)

    print(f"Ai#> {parsed_data} \n Allow? ")

    usr = input("User#> ")
    if usr == "allow" or usr == "yes" or usr == "y" or usr=="continue":
        os.system(parsed_data)
        print("------------------------")
        print("| Ai#> Task Completed !|")
        print("------------------------")
        print("")
        print("")

    else:
        print("Ai#> Not Running The Following Command !")






