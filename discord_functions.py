def get_community_embed(name, leader_mention, role_mention, community_id):
    embed = discord.Embed(description=" ", color=0x03d692, title=" ")
    embed.set_author(name="New Community created", icon_url='https://cdn.discordapp.com/attachments/416682974143184907/688363318679044116/gamer_kavezo_logo.png')
    embed.set_footer(text="Community ID: " + str(community_id))
    embed.add_field(name="Details",
          value="Name: `" + name + "\n`Leader: " + leader_mention + "\nRole: " + role_mention + "", inline=False)
    return embed
