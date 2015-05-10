from sys import exit

class engine(object):
	def play(self, room):
		self.room = room
		print "--------------"
		room.enter()

class room(object):
	pass

class entryway(room):
	def enter(self):
		print "You have stumbled into the foyer of an abandoned castle."
		print "There is a door in front of you."
		print "What do you do?"

game = engine()
first_room = entryway()
game.play(first_room)


# how do I get this code into engine?
#start = entryway()
#start.enter()



