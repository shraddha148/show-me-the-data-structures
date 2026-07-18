class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
        user (str): User name/id
        group (Group): Group to search
    """

    # Edge case
    if user is None or group is None:
        return False

    # Check current group's users
    if user in group.get_users():
        return True

    # Recursively check child groups
    for child_group in group.get_groups():
        if is_user_in_group(user, child_group):
            return True

    return False

#Test Case 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"

sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent))
# Expected Output: True

#Test Case 2 - User Not Present
print(is_user_in_group("unknown_user", parent))
# Expected Output: False

#Test Case 3 - Null Group
print(is_user_in_group("sub_child_user", None))
# Expected Output: False

#additional edge case - Emplty Group
empty_group = Group("empty")

print(is_user_in_group("user1", empty_group))
# Expected Output: False
