class player(object):
	pass

class fighter(player):
	def __init__(self, name, hitpoints):
		self.name = name
		self.hitpoints = hitpoints

player1 = fighter("Karunes", 20)

print player1.name
print player1.hitpoints
