import discord
from discord.ext import commands

# Enable member intent
intents = discord.Intents.default()
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

# CONFIG
WELCOME_CHANNEL_ID =   # Replace with your welcome channel ID
CHANNEL_ID_WHITELIST = 
CHANNEL_ID_RULES = 
CHANNEL_ID_ANNOUNCEMENTS =   # Update this to your actual channel ID
ROLE_NAME = "Members"  # Replace with your role name
WELCOME_BANNER_URL = ""  # Replace with your banner image URL

# Emojis
EMOJI_ARROW = "<:Arrow_arrow:1359762573733531648>"
EMOJI_DIVIDER = "<:divider:1359764010932633721>"

@bot.event
async def on_member_join(user):
    print(f"👤 {user.name} joined the server.")

    # DM the user
    try:
        await user.send("👋 Welcome Feel free to ask for help anytime.")
        print(f"📬 Sent welcome DM to {user.name}")
    except Exception as e:
        print(f"❌ Could not send DM to {user.name}: {e}")

    # Send welcome embed in public channel
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="Ventury City Events",
            description=f"**Welcome to the Server {user.mention}**\n\n{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}\n\n{EMOJI_ARROW} Get Whitelist from here <#{CHANNEL_ID_WHITELIST}>\n{EMOJI_ARROW} Checkout Discord Rules <#{CHANNEL_ID_RULES}>\n{EMOJI_ARROW} Announcements Channel <#{CHANNEL_ID_ANNOUNCEMENTS}>\n\n{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}{EMOJI_DIVIDER}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=user.display_avatar.url)


        embed.set_image(url=WELCOME_BANNER_URL)
        await channel.send(embed=embed)
        print(f"✅ Sent welcome embed to {channel.name}")

    # Assign role to user
    role = discord.utils.get(user.guild.roles, name=ROLE_NAME)
    if role:
        await user.add_roles(role)
        print(f"✅ Assigned role '{role.name}' to {user.name}")
    else:
        print(f"⚠️ Role '{ROLE_NAME}' not found in the server")

    activity = discord.Game(type=discord.ActivityType.watching, name="")  # Change this to your desired status
    await bot.change_presence(activity=activity)  # Update bot's activity

# Run bot
bot.run("")  # Replace with your actual bot token
