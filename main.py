import discord
import quotes
import openai
import os
import dr_vegapunk
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('DR_VEGAPUNK_API_KEY')


if __name__ == '__main__':
    dr_vegapunk.bot.run()



# Dev  by Y_mC
