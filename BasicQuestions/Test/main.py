import openai

openai.api_key = ""

def chatbot(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.5,
        max_tokens=256
    )
    return response.choices[0].text

print(chatbot("Hello, how are you?"))