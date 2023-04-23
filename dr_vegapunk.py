import discord
import openai
import os
import quotes
import random
import logging
from dotenv import load_dotenv


load_dotenv()

key = os.getenv('DR_VEGAPUNK_API_KEY')


intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)




@bot.event
async def on_ready() :
    print(f'We have logged in #momo-jam-cava as : {bot.user} , SUPER!!!!!!!!!!!!!!!!!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('roll 10'):
        roll = [random.randint(1,100) for i in range(10)]
        await message.channel.send(f'{roll}')

    if message.content.startswith('quote'):
        quote = random.choice(quotes.quotes)
        await message.channel.send(f'{quote}')

    # dr_vegapunk_channel : discord.TextChannel = bot.get_channel(1099103151572926477)
    # # if message.content.startswith("!"):
    #





bot.run(key,log_level=logging.INFO)

# generator = pipeline('text-generation', model='gpt2-xl')
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2-xl')
# tokenizer.pad_token = tokenizer.eos_token
# dr_vegapunk = GPT2LMHeadModel.from_pretrained('gpt2-xl')
#
#
# def generate_response(prompt, model, tokenizer, max_length=50) :
#     inputs = tokenizer(prompt,
#                        return_tensors="pt",
#                        padding=True,
#                        truncation=True,
#                        max_length=max_length)
#     input_ids = inputs["input_ids"]
#     attention_mask = inputs["attention_mask"]
#     output = model.generate(input_ids,
#                             max_length=max_length,
#                             num_return_sequences=1,
#                             no_repeat_ngram_size=2,
#                             do_sample=True,
#                             temperature=0.1,
#                             attention_mask=attention_mask,
#                             pad_token_id=tokenizer.eos_token_id)
#     response = tokenizer.decode(output[0], skip_special_tokens=True)
#     print(response)
#
#     # return response
#
#
# while True :
#     prompt = input(f'YMC: ')
#     generate_response(prompt, dr_vegapunk, tokenizer)
