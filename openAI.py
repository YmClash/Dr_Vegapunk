import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
print(f'Dr Vegapunk  dev by YmC , Powered  By Open AI  model :')



while True :
    user_input = input(f'YMC: ')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role" : "system", "content" : "Franki"},
            {"role" : "user", "content" : user_input}
        ],
        max_tokens=500,
        temperature=0.75,
        # top_p=1.0,
        # stop =4,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )

    message = response.choices[0].message.content.strip()
    print(message)
