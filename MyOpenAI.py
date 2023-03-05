import openai

model_to_use="gpt-3.5-turbo"
#model_to_use="text-davinci-003" # most capable
#model_to_use="text-curie-001"
#model_to_use="text-babbage-001"
#model_to_use="text-ada-001" # lowest token cost

API_KEY = "YOUR_API_KEY" # here paste your API key from 'chat.openai.com'


class MyOpenAI:
    def __init__(self, model, API_key):
        self.model = model
        openai.api_key= API_key
        
    def chatGPT(self, query):
        response = openai.Completion.create(
            model=self.model,
            prompt=query,
            temperature=0,
            max_tokens=250
            )
        return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']

