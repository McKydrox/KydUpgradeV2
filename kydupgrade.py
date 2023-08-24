from pystyle import Colorate, Colors, System, Center, Anime
from colorama import init, Fore
import os
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1144020820914610356/7neJaNe7J6KMlrahW2bdzK10bE3HjmXwX3OWJE3aaz9KM5Mm_26AhI-1JgOiBUT0Ka2G", username="KydUpgrade", content="@everyone")

embed = DiscordEmbed(
    title="KydUpgrade", description="Un utilisateur viens d'utiliser votre logiciel 'KydUpgrade'", color="03b2f8"
)
embed.set_author(
    name="Kydrox",
    url="https://github.com/McKydrox/KydUpgradeV2",
    icon_url="https://avatars0.githubusercontent.com/u/14542790",
)
embed.set_footer(text="Kydrox inc")
embed.set_timestamp()

webhook.add_embed(embed)
response = webhook.execute()
init(),

logo = '''
        
$$\   $$\                $$\ $$\   $$\                                              $$\           
$$ | $$  |               $$ |$$ |  $$ |                                             $$ |          
$$ |$$  /$$\   $$\  $$$$$$$ |$$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\   $$$$$$$ | $$$$$$\  
$$$$$  / $$ |  $$ |$$  __$$ |$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ \____$$\ $$  __$$ |$$  __$$\ 
$$  $$<  $$ |  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |  \__|$$$$$$$ |$$ /  $$ |$$$$$$$$ |
$$ |\$$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$   ____|
$$ | \$$\\$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$$$$$$  |\$$$$$$$ |$$ |     \$$$$$$$ |\$$$$$$$ |\$$$$$$$\ 
\__|  \__|\____$$ | \_______| \______/ $$  ____/  \____$$ |\__|      \_______| \_______| \_______|
         $$\   $$ |                    $$ |      $$\   $$ |                                       
         \$$$$$$  |                    $$ |      \$$$$$$  |                                       
          \______/                     \__|       \______/                                        

          
          
Please press Enter ...                                            
                                                                                                                                
'''[1:]

System.Size(100, 30)
System.Title('KydroxTools')
Anime.Fade(Center.Center(logo), Colors.blue_to_cyan, Colorate.Vertical, enter=True)

print(Fore.BLUE + "Chargement de la liste des applications ... ")
os.system("winget upgrade --all")


print(Fore.RED + "Les applications on été mis à jours, vous pouvez maintenant fermer l'application.")


    
