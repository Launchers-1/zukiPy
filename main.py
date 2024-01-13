import zukiPy
import asyncio

api_key = ""  # Get your API key @ https://discord.gg/zukijourney
api_key_backup = "" # Set this to your backup API key (optional, usually for testing with different LLM APIs)
zukiAI = zukiPy.zukiCall(api_key, api_key_backup, "gpt-3.5-turbo")


async def main():
    chat_response = await zukiAI.zuki_chat.sendMessage("Launchers", "Hello")
    print("Chat Response:", chat_response)

    image_response = await zukiAI.zuki_image.generateImage("Horror version of Garfield the Cat", 1)
    # I'm sorry Jon...
    print("\n Image Response:", image_response)

    # To call from a backup API endpoint use .sendMessageBackup() and .generateImageBackup()


# You also need to run the async function:
asyncio.run(main())

# Hey, 1_aunchers(creator of this) here. This is made by heavily referencing Sabsterrexx. You can find him @ https://github.com/Sabsterrexx
# WARNING: The default backup endpoint is currently WebRaft, which is currently UNSTABLE. Change your backup 
