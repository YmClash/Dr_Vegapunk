from edison import initialize_agent_zero_shot
from pythago import tool_start_playing_song_by_name


agent_name = "Atlas"
tools = [
    tool_start_playing_song_by_name()
]

agent = initialize_agent_zero_shot(tools=tools)
print(f"Hallo  je suis {agent_name}, qu'est que je peux faire pour vous ")

while True:
    # agent.run(input('YMC: '))
    request = input('YMC: ')
    result = agent({"input": request})
    reponse = result["output"]
    print(reponse)



