import openai

openai.api_key = "sk-<<Your API key here>>"
#messages to store the conversation
messages = [
]

#Append the message to the conversation history 
def add_message(role, message):
    messages.append({"role": role, "content": message})

#Trigger the Open AI APIs
def converse_with_chatGPT():
    """Trigger the OPEN AI APIs with the given inputs """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", #Open AI model name
        messages=messages, # user query
        max_tokens = 1024, # this is the maximum number of tokens that can be used to provide a response.
        n=1, #number of responses expected from the Chat GPT
        stop=None, 
        temperature=0.5 #making responses deterministic or not much imaginative
    )
    # print(response)
    message = response.choices[0].message.content
    messages.clear()
    # add_message("assistant", message)
    return message.strip()

# process user prompt
def process_user_query(prompt):
    user_prompt = (f"{prompt}")
    add_message("user", user_prompt)
    result = converse_with_chatGPT()
    print(result)

#Request user to provide the query
def user_query():
    while True:
        prompt = input("Enter your question: ")
        response = process_user_query(prompt)
        print(response)

user_query()