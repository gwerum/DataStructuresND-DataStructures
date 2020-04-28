import unittest
import pandas as pd

class Group():
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.members = []

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.name)+"\n"
        for group in self.groups:
            ret += group.__repr__(level+1)
        return ret

    def add_group(self, group):
        self.groups.append(group)

    def add_member(self, member):
        self.members.append(member)

    def get_groups(self):
        return self.groups

    def get_members(self):
        return self.members

    def get_name(self):
        return self.name

def is_member_in_group(member, group):
    """
    Return True if member is in the group, False otherwise.

    Args:
      member(str): member name/id
      group(class:Group): group to check member membership against
    """
    if member in group.get_members():
        return True
    for sub_group in group.get_groups():
        if is_member_in_group(member, sub_group):
            return True
    return False


class TestActiveDirectory(unittest.TestCase):
    """docstring for TestActiveDirectory"""
    def test_family_directory(self):
        print("\n ############# Test case 1: Test family memberships ########### ")
        print("Input dictionary:")
        dictionary = {}
        dictionary['Parents'] = \
            {'Members': ['Grandpa','Grandma'], 'Groups': ['Children']}
        dictionary['Children'] = \
            {'Members': ['Father', 'Mother', 'Uncle_1', 'Aunt_1', 'Uncle_2','Aunt_2'],\
             'Groups': ['Childrens_Children']}
        dictionary['Childrens_Children'] = \
            {'Members': ['Son_1', 'Son_2', 'Daugther_1', 'Daugther_2', 'Cousin_male','Cousin_female'],\
             'Groups': [] }
        print(dictionary)

        directory = self.create_directory_from(dictionary, 'Parents')
        self.run_test(dictionary, directory, 'Family')
        del directory
        pass

    def test_number_directory(self):
        print("\n ############# Test case 2: Test number memberships ########### ")
        print("Input dictionary:")
        dictionary = {}
        dictionary['Is smaller 1000'] = \
            {'Members': [349, 874, 652, 492, 568], 'Groups': ['Is smaller 100', 'Is smaller 300']}
        dictionary['Is smaller 300'] = \
            {'Members': [100, 178, 287, 198, 234],\
             'Groups': ['Is smaller 10', 'Is smaller 100']}
        dictionary['Is smaller 100'] = \
            {'Members': [10, 17, 45, 67, 23, 50, 93, 71, 85],\
             'Groups': ['Is smaller 10']}
        dictionary['Is smaller 10'] = \
            {'Members': [2, 5, 6, 7, 8, 9],\
             'Groups': [] }
        print(dictionary)

        directory = self.create_directory_from(dictionary, 'Is smaller 1000')
        self.run_test(dictionary, directory, 'Numbers')
        del directory
        pass

    def create_directory_from(self, dictionary, parent_name):
        directory = Group(parent_name)
        for member in dictionary[parent_name]['Members']:
            directory.add_member(member)
        for group_name in dictionary[parent_name]['Groups']:
            directory.add_group(self.create_directory_from(dictionary, group_name))
        return directory
        
    def run_test(self, dictionary, directory, directory_name):
        members = self.get_all_members_from(directory)
        groups = self.get_all_groups_from(directory)
        print("\nThe '"+directory_name+"' directory has the following members: ")
        print(members)
        print("\nThe '"+directory_name+"' directory has the following group hierarchy: ")
        print(directory)
        # Run test an check if memberships are correctly returned
        memberships = {'Members': members}
        for group in groups.keys():
            group_membership = []
            for member in members:
                is_member = is_member_in_group(member, groups[group])
                self.assertEqual(is_member, self.expected_membership(member, group, dictionary))
                group_membership.append(is_member)
            memberships[group] = group_membership
        df = pd.DataFrame(memberships)
        df.set_index('Members', inplace=True, drop=True)
        print("\nThe members of the '"+directory_name+"' directory have the following memberships:")
        print(df)

    def expected_membership(self, member, group, dictionary):
        member_in_group = self.is_in_group(member, group, dictionary)
        is_member_in_subgroup = self.is_in_subgroup(member, group, dictionary)
        return (member_in_group or is_member_in_subgroup)

    def is_in_group(self, member, group, dictionary):
        members = dictionary[group]['Members']
        if member in members:
            return True
        return False

    def is_in_subgroup(self, member, group, dictionary):
        if self.is_in_group(member, group, dictionary):
            return True
        is_member = 0
        for sub_group in dictionary[group]['Groups']:
            if self.is_in_subgroup(member, sub_group, dictionary):
                is_member += 1
        if is_member > 0:
            return True
        return False

    def get_all_members_from(self, group):
        member_list = []
        for member in group.get_members():
            member_list.append(member)
        for group in group.get_groups():
            member_list += self.get_all_members_from(group)
        return member_list

    def get_all_groups_from(self, group):
        group_dict = {group.name: group}
        for sub_group in group.get_groups():
            group_dict.update(self.get_all_groups_from(sub_group))
        return group_dict




