import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(f"Бот {bot.user} подключился к Discord!")
    
    # Пример: отправка сообщения в конкретный канал
    channel_id = YOUR_CHANNEL_ID  # Замените на ID канала, куда хотите отправить сообщение
    channel = bot.get_channel(channel_id)
    
    if channel is not None:
        await channel.send("Бот успешно запущен!")
    else:
        print("Канал не найден.")

# Не забудьте вставить токен вашего бота
bot.run('YOUR_BOT_TOKEN')