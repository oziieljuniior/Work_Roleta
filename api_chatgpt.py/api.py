import openai as ia

ia.api_key = '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'

model_engine = 'text-davinci-003'
prompt = "Diga um olá mundo e fale um pouco o usuário daqui"

completion = ia.Completion.create(engine = model_engine, prompt = prompt, max_tokens = 4000, n = 1, stop=None, temperature = 0.5)

response = completion.choices[0].text

print(response)
