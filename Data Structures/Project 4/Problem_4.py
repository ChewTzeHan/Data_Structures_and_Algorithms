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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True
    
    if group.get_groups():

        for i in group.get_groups():
            if is_user_in_group(user, i) == True:
                return True
            
    
    return False


user = 'sub_child_user'
group = parent
print("Is '{a}' in Group '{b}'? {c} ".format(a = user, b = group.get_name(), c = is_user_in_group(user, group)))

print('--------------------')
## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values


## Test Case 1

Firene = Group('Firene')
Brodia = Group('Brodia')
Elusia = Group('Elusia')
Solm = Group('Solm')
Continents = [Firene, Brodia, Elusia, Solm]

Elyos = Group('Elyos')


for i in Continents:
    Elyos.add_group(i)

Firenese_residents = ['Alfred', 'Celine', 'Louis', 'Chloe', 'Boucheron', 'Etie']
Brodian_residents = ['Diamant', 'Alcryst', 'Lapis', 'Citrinne', 'Amber', 'Jade']
Elusian_residents = ['Ivy', 'Hortensia', 'Kagetsu', 'Zelkov', 'Rosado', 'Goldmary']
Solm_residents = ['TImerra', 'Fogado', 'Merin', 'Panette', 'Pandreo', 'Bunet']

Elyos_residents = [Firenese_residents, Brodian_residents, Elusian_residents, Solm_residents]

for i in range(len(Continents)):
    for person in Elyos_residents[i-1]:
        Elyos.get_groups()[i-1].add_user(person)

user_1 , user_2 , user_3 , user_4 = 'Celine' , 'Ivy' , 'Lapis' , 'Merin'
group_1 , group_2 , group_3 , group_4 = Firene , Elusia , Solm, Elyos

print("Is '{a}' in Group '{b}'? {c} ".format(a = user_1, b = group_1.get_name(), c = is_user_in_group(user_1, group_1)))
print("Is '{a}' in Group '{b}'? {c} ".format(a = user_2, b = group_2.get_name(), c = is_user_in_group(user_2, group_2)))
print("Is '{a}' in Group '{b}'? {c} ".format(a = user_3, b = group_3.get_name(), c = is_user_in_group(user_3, group_3)))
print("Is '{a}' in Group '{b}'? {c} ".format(a = user_4, b = group_4.get_name(), c = is_user_in_group(user_4, group_4)))

'''
Expected output:
    Is 'Celine' in Group 'Firene'? True 
    Is 'Ivy' in Group 'Elusia'? True 
    Is 'Lapis' in Group 'Solm'? False 
    Is 'Merin' in Group 'Elyos'? True 
'''
print('--------------------')
## Test Case 2 EDGE CASE: Many subgroups

Terakomari = Group('Terakomari')

T = Group('T'); Terakomari.add_group(T); E = Group('E'); T.add_group(E); R_1 = Group('R'); E.add_group(R_1)
A_1 = Group('A'); R_1.add_group(A_1); K = Group('K'); A_1.add_group(K); O = Group('O'); K.add_group(O)
M = Group('M'); O.add_group(M); A_2 = Group('A'); M.add_group(A_2); R_2 = Group('R'); A_2.add_group(R_2)
I = Group('I'); R_2.add_group(I); 

I.add_user('Sakuna')
Terakomari.add_user('Vill')

print("Is '{a}' in Group '{b}'? {c} ".format(a = 'Sakuna', b = Terakomari.get_name(), c = is_user_in_group('Sakuna', Terakomari)))
print("Is '{a}' in Group '{b}'? {c} ".format(a = 'Vill', b = Terakomari.get_name(), c = is_user_in_group('Vill', Terakomari)))
print("Is '{a}' in Group '{b}'? {c} ".format(a = 'Vill', b = K.get_name(), c = is_user_in_group('Vill', K)))
print("Is '{a}' in Group '{b}'? {c} ".format(a = 'Sakuna', b = K.get_name(), c = is_user_in_group('Sakuna', K)))

'''
Expected output:
    Is 'Sakuna' in Group 'Terakomari'? True 
    Is 'Vill' in Group 'Terakomari'? True 
    Is 'Vill' in Group 'K'? False 
    Is 'Sakuna' in Group 'K'? True 
'''

print('--------------------')

## Test Case 3 EDGE CASE: Empty values

Claire = Group(None)
Rae = Group('Lene')
Misha = Group('None')

Claire.add_group(Rae)
Rae.add_group(Misha)

Misha.add_user('Manaria')
Rae.add_user(None)

print("Is '{a}' in Group '{b}'? {c} ".format(a = None, b = Rae.get_name(), c = is_user_in_group(None, Rae)))
print("Is '{a}' in Group '{b}'? {c} ".format(a = 'Manaria', b = Misha.get_name(), c = is_user_in_group('Manaria', Misha)))
print("Is '{a}' in Group '{b}'? {c} ".format(a = None, b = Misha.get_name(), c = is_user_in_group(None, Misha)))

'''
Expected output:
    Is 'None' in Group 'Lene'? True 
    Is 'Manaria' in Group 'None'? True 
    Is 'None' in Group 'None'? False 
'''