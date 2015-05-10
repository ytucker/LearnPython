class player(object):
	def __init__(self, name, hitpoints):
		self.name = name
		self.hitpoints = hitpoints

class fighter(player):
	def damaged(self, damage):
		print "Player takes %d damage." % damage
		self.hitpoints = self.hitpoints - damage
		print "Player has %d hitpoints left" % self.hitpoints


player1 = fighter("Karunes", 20)

print player1.name
print player1.hitpoints

player1.damaged(5)
print player1.hitpoints
