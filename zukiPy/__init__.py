from zukiPy.MainMods.zukiChat import zukiChat
from zukiPy.MainMods.zukiImage import zukiImage


class zukiCall:
    def __init__(self, api_key, model="gpt-3.5-turbo",  systemPrompt="You are a helpful assistant.", temperature=0.7):
        self.api_key = api_key
        self.api_key_backup = ""
        self.model = model
        self.systemPrompt = systemPrompt
        self.temperature = temperature
        self.zuki_chat = zukiChat(
            api_key, self.api_key_backup, model, systemPrompt, temperature)
        self.zuki_image = zukiImage(api_key, self.api_key_backup)

    def change_backup_key(self, key):
        self.api_key_backup = key
