import discord
import quotes
import openai
import os
import dr_vegapunk as bot
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('DR_VEGAPUNK_API_KEY')


if __name__ == '__main__':
    bot.bot.run()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
