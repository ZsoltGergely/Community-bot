
class Error(Exception):
    pass

class UserNameAlreadyUsed(Error):
    def __init__(self, message):
        self.message = message

class NoCommunityWithName(Error):
    def __init__(self, message):
        self.message = message

class Comm_Guild_class:
    def __init__(self, id, emotes, invite_channel_id):
        self.id = id
        self.emotes = emotes
        self.invite_channel_id = invite_channel_id
        # self.communities = communities

    def create_comm(self, name, leader, role):
        record = db_get_community_name(name)
        if record:
            raise UserNameAlreadyUsed("username already used")

        new_community = Community_class(self, name, leader, role, [])
        return new_community

    def edit(self, emotes, invite_channel_id ):
        self.emotes = emotes
        self.invite_channel_id = invite_channel_id

    def get_community_name(self, name):
        record = db_get_community_name(name)
        if record:
            # leader = get from dc int(record[3])
            # role = get from dc int(record[2])
            members = []
            db_members = db_get_members_id(record[0])
            # for db_member in db_members:
            #     member = dicord get member (db_get_members_id[0])
            #     members.append(member)
            community = Community_class(self, name, leader, role, members)
            return community
        else:
            raise NoCommunityWithName("There is no community with that name")

    def get_invite_channel(self, invite_channel_id):
        print("Getting channel from DC")

    def get_community_id(self, id):
        record = db_get_community_id(id)
        if record:
            # leader = get from dc int(record[3])
            # role = get from dc int(record[2])
            members = []
            db_members = db_get_members_id(record[0])
            # for db_member in db_members:
            #     member = dicord get member (db_get_members_id[0])
            #     members.append(member)
            community = Community_class(self, name, leader, role, members)
            return community
        else:
            raise NoCommunityWithName("There is no community with that id")

    def get_invite_channel(self, invite_channel_id):
        print("Getting channel from DC")

        # return channel

class Community_class:
    def __init__(self, Comm_Guild, name, leader, role, members):
        self.Comm_Guild = Comm_Guild
        self.name = name
        self.leader = leader
        self.role = role
        self.memmbers = members

    def invite_member(self, member):
        print("inviting member")

    def remove_member(self, member):
        print("removing member")

    def get_community_roles(self):
        print("get roles created in community")

    def delete(self):
        db_delete_community_name(self.name)


class Community_Member_class:
    def __init__(self, member, communities, name, leader_id, members):
        self.member = member
        self.communities = communities
        self.name = name
        self.leader_id = leader_id
        self.memmbers = members

    def kick(self):
        print("kicking member")

    def ban(self):
        print("baning member")

    def unban(self):
        print("unbaning member")
