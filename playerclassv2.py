class player(object):
	def __init__(self, name, hitpoints):
		self.name = name
		self.hitpoints = hitpoints

class fighter(player):
	def damaged(self, damage):
		print "Player takes %d damage." % damage
		self.hitpoints = self.hitpoints - damage
		print "Player has %d hitpoints left" % self.hitpoints

print "What is your name?"
playername = raw_input("> ")

print "How many hitpoints do you have?"
hitpoints = raw_input("> ")
hitpoints = int(hitpoints)

player1 = fighter(playername, hitpoints)
print "Well met %s!" % player1.name
print "You have %d hitpoints." % player1.hitpoints
