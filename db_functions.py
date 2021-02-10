    # Database Layout
    #
    # communities:
    #    community_id
    #     name
    #     role_id
    #    leader_id
    #    guild_id

    # community_members:
    #
    #     community_id
    #     guild_id
    #     member_id

    # pending_invites:
    #     message_id
    #     leader_id
    #     guild_id



def db_get_community_name(name):
    try:
        sql_search = "SELECT * FROM communities WHERE name = '{}' "
        mycursor.execute(sql_search.format(name))
        record = mycursor.fetchone()

    except mysql.connector.Error as e:
        print("------------------------")
        print ("Error code:", e.errno)        # error number
        print ("SQLSTATE value:", e.sqlstate )# SQLSTATE value
        print ("Error message:", e.msg )      # error message
        print ("Error:", e)                   # errno, sqlstate, msg values
        s = str(e)
        print ("Error:", s)                   # errno, sqlstate, msg values
        print("------------------------")
        print("Reconnecting...")
        mydb.reconnect()
        print("------------------------")
        sql_search = "SELECT * FROM communities WHERE name = '{}' "
        mycursor.execute(sql_search.format(name))
        record = mycursor.fetchone()
    return record

def db_get_community_leader(leader_id):
    try:
        sql_search = "SELECT * FROM communities WHERE leader_id = '{}' "
        mycursor.execute(sql_search.format(str(leader_id)))
        record = mycursor.fetchone()

    except mysql.connector.Error as e:
        print("------------------------")
        print ("Error code:", e.errno)        # error number
        print ("SQLSTATE value:", e.sqlstate )# SQLSTATE value
        print ("Error message:", e.msg )      # error message
        print ("Error:", e)                   # errno, sqlstate, msg values
        s = str(e)
        print ("Error:", s)                   # errno, sqlstate, msg values
        print("------------------------")
        print("Reconnecting...")
        mydb.reconnect()
        print("------------------------")
        sql_search = "SELECT * FROM communities WHERE leader_id = '{}' "
        mycursor.execute(sql_search.format(str(leader_id)))
        record = mycursor.fetchone()
    return record

def db_get_community_id(id):
    try:
        sql_search = "SELECT * FROM communities WHERE id = '{}' "
        mycursor.execute(sql_search.format(id))
        record = mycursor.fetchone()

    except mysql.connector.Error as e:
        print("------------------------")
        print ("Error code:", e.errno)        # error number
        print ("SQLSTATE value:", e.sqlstate )# SQLSTATE value
        print ("Error message:", e.msg )      # error message
        print ("Error:", e)                   # errno, sqlstate, msg values
        s = str(e)
        print ("Error:", s)                   # errno, sqlstate, msg values
        print("------------------------")
        print("Reconnecting...")
        mydb.reconnect()
        print("------------------------")
        sql_search = "SELECT * FROM communities WHERE id = '{}' "
        mycursor.execute(sql_search.format(id))
        record = mycursor.fetchone()
    return record

def db_get_invites():
    try:
        sql_search = "SELECT * FROM pending_invites"
        mycursor.execute(sql_search)
        invites = mycursor.fetchall()

    except mysql.connector.Error as e:
        print("------------------------")
        print ("Error code:", e.errno)        # error number
        print ("SQLSTATE value:", e.sqlstate )# SQLSTATE value
        print ("Error message:", e.msg )      # error message
        print ("Error:", e)                   # errno, sqlstate, msg values
        s = str(e)
        print ("Error:", s)                   # errno, sqlstate, msg values
        print("------------------------")
        print("Reconnecting...")
        mydb.reconnect()
        print("------------------------")
        sql_search = "SELECT * FROM pending_invites"
        mycursor.execute(sql_search)
        invites = mycursor.fetchall()
    return invites

def db_get_members_id(community_id):
    sql_search = "SELECT * FROM community_members WHERE community_id = '{}' "
    mycursor.execute(sql_search.format(community_id))
    community_members = mycursor.fetchall()
    return community_members

def db_get_emoji_id(community_id):
    sql_search = "SELECT * FROM emojis WHERE community_id = '{}' "
    mycursor.execute(sql_search.format(community_id))
    emojis = mycursor.fetchall()
    return emojis

def db_insert_community(name, role_id, leader_id, guild_id):
    try:
        sql_query = "INSERT INTO communities (name, role_id, leader_id, guild_id) VALUES ('{}', '{}', '{}', '{}')"
        mycursor.execute(sql_query.format(name, str(role_id), str(leader_id), str(guild_id)))
        mydb.commit()

    except mysql.connector.Error as e:
        print("------------------------")
        print ("Error code:", e.errno)        # error number
        print ("SQLSTATE value:", e.sqlstate )# SQLSTATE value
        print ("Error message:", e.msg )      # error message
        print ("Error:", e)                   # errno, sqlstate, msg values
        s = str(e)
        print ("Error:", s)                   # errno, sqlstate, msg values
        print("------------------------")
        print("Reconnecting...")
        mydb.reconnect()
        print("------------------------")
        sql_query = "INSERT INTO communities (name, role_id, leader_id, guild_id) VALUES ('{}', '{}', '{}', '{}')"
        mycursor.execute(sql_query.format(name, str(role_id), str(leader_id), str(guild_id)))
        mydb.commit()

def db_insert_invite(pending_invites, message_id, leader_id, community_id, guild_id):
    try:
        sql_query = "INSERT INTO pending_invites (invited_id, message_id, leader_id, community_id, guild_id) VALUES ('{}', '{}', '{}', '{}', '{}')"
        mycursor.execute(sql_query.format(str(invited_id), str(message_id), str(leader_id), community_id, str(guild_id)))
        mydb.commit()

    except mysql.connector.Error as e:
        print("------------------------")
        print ("Error code:", e.errno)        # error number
        print ("SQLSTATE value:", e.sqlstate )# SQLSTATE value
        print ("Error message:", e.msg )      # error message
        print ("Error:", e)                   # errno, sqlstate, msg values
        s = str(e)
        print ("Error:", s)                   # errno, sqlstate, msg values
        print("------------------------")
        print("Reconnecting...")
        mydb.reconnect()
        print("------------------------")
        sql_query = "INSERT INTO pending_invites (invited_id, message_id, leader_id, community_id, guild_id) VALUES ('{}', '{}', '{}', '{}', '{}')"
        mycursor.execute(sql_query.format(str(invited_id), str(message_id), str(leader_id), community_id, str(guild_id)))
        mydb.commit()

def db_insert_members(member_id, community_id, guild_id):
    sql_query = "INSERT INTO community_members (member_id, community_id, guild_id) VALUES ('{}', '{}', '{}')"
    mycursor.execute(sql_query.format(str(member_id), community_id, str(guild_id)))
    mydb.commit()

def db_delete_invites_id(id):
    sql_query = "DELETE FROM pending_invites  WHERE  community_id = '{}'"
    mycursor.execute(sql_query.format(id))
    mydb.commit()

def db_delete_invites_id_inv_comm(guild_id, community_id, invited_id):
    sql_query = "DELETE FROM pending_invites WHERE guild_id = '{}' AND community_id = '{}' AND invited_id = '{}'"
    mycursor.execute(sql_query.format(str(guild_id), community_id, str(invited_id)))
    mydb.commit()

def db_delete_members_id(id):
    sql_query = "DELETE FROM community_members  WHERE  community_id = '{}'"
    mycursor.execute(sql_query.format(id))
    mydb.commit()

def db_delete_members_guild_member_comm(guild_id, member_id, community_id):
    sql_query = "DELETE FROM community_members  WHERE guild_id = '{}' AND member_id = '{}' AND community_id = '{}'"
    mycursor.execute(sql_query.format(str(guild_id), str(member_id), community_id))
    mydb.commit()

def db_delete_community_id(id):
    sql_query = "DELETE FROM communities  WHERE  community_id = '{}'"
    mycursor.execute(sql_query.format(id))
    mydb.commit()

def db_delete_community_name(name):
    sql_query = "DELETE FROM communities  WHERE  name = '{}'"
    mycursor.execute(sql_query.format(name))
    mydb.commit()
