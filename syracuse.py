def longueur_vol(n):
	'''retourne le nombre d'étapes avant d'arriver à 1 dans la suite de syracuse'''
	assert type(n) == int and n >= 1
	compteur = 0
	while n > 1:
		#print(n)
		if n % 2 == 0 : #si n est pair
			n = n // 2
		else :
			n = 3 * n + 1
		compteur += 1
	#print(n)
	return compteur


############
def syracuse(n):
        '''retourne une liste avec les termes de la suite de syracuse'''
        assert type(n) == int and n >= 1
        reponse = []
        while n > 1:
                reponse.append(n)
                if n % 2 == 0 : #si n est pair
                        n = n // 2
                else :
                        n = 3 * n + 1
                compteur += 1
        reponse.append(n)
        return reponse
# Tests
assert longueur_vol(3) == 7
assert longueur_vol(7) == 16
assert longueur_vol(1) == 0
assert syracuse(3) == [3, 10, 5, 16, 8, 4, 2, 1]
assert syracuse(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert syracuse(1) == [1]
print("BRAVO!")
