def nombre_coureurs(lst):
	"""retourne le nombre de coureurs dans lst"""
	assert type(lst) == list
	assert all([type(obj)== str for obj in lst])
	return len(lst)

###################
def premier(lst):
        """retourne le premier  coureur dans lst"""
        assert type(lst) == list
        assert all([type(obj)== str for obj in lst])
        return lst[0]

#################
def dernier(lst):
        """retourne le dernier  coureur dans lst"""
        assert type(lst) == list
        assert all([type(obj)== str for obj in lst])
        return 

#############################

def coureur_en_position(lst, position):
        """retourne le coureur à l'indice position -1 dans lst"""
	assert type(lst) == list
        assert all([type(obj)== str for obj in lst])
        assert type(position) == int and position >= 1 and position <= len(lst)
	return lst [position -1]

#test
classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert nombre_coureurs(classement) == 5
assert premier(classement) == "Nadia"
assert dernier(classement) == "Laure"
assert coureur_en_position(classement, 1) ==  print("bravo") 
