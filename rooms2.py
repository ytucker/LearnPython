class engine(object):
	def __init__(self, room_name):
		self.room = room_name

	def play(self):
		current_room = self.room.enter()
		current_room.enter()
			
class room(object):
	pass

class entrance(room):
	def enter(self):
		print "Test"
		return rat_room()
	
class rat_room(room):
	def enter(self):
		print "You did it!"

first_room = entrance()
game = engine(first_room)
game.play()
