#import sys
import openai

model_to_use="text-davinci-003" # most capable
#model_to_use="text-curie-001"
#model_to_use="text-babbage-001"
#model_to_use="text-ada-001" # lowest token cost

API_KEY = "YOUR_API_KEY"


class MyOpenAI:
    def __init__(self, model, API_key):
        self.model = model
        openai.api_key= API_key
        
    def chatGPT(self, query):
        response = openai.Completion.create(
            model=self.model,
            prompt=query,
            temperature=0,
            max_tokens=200
            )
        return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']



#query=sys.argv[1]

#(res, usage) = chatGPT(query)
#print(res)
#print("\n----------------\nTokens used: "+str(usage))