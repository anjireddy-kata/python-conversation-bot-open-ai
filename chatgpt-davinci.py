import openai

openai.api_key = "sk-<<Your API key here>>"
def generate_response(user_prompt):
    model_engine = "text-davinci-003"
    user_prompt = (f"{user_prompt}")
    #Open AI provided API method to get the response from Chat GPT
    completions = openai.Completion.create(
        engine=model_engine, #Open AI model name
        prompt=user_prompt, # user query
        max_tokens=1024, # number tokens can be used to provide the response
        n=1, #number of responses expected from the Chat GPT
        stop=None, 
        temperature=0.5 #making responses deterministic
    )
    # print(completions)
    message = completions.choices[0].text
    return message.strip()

user_prompt = input("Enter your question: ")
response = generate_response(user_prompt)

print(response)