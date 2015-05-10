class engine(object):
	def __init__(self, room_name):
		self.room = room_name

	def play(self):
		current_room = self.room.enter()
		next_room = mapper.rooms.get(current_room)
		next_room.enter()
			
class room(object):
	pass

class entrance(room):
	def enter(self):
		print "Room 1"
		action = raw_input("> ")
		
		if action == "change":
			return "rat_room"
		else:
			return "entrance"
	
class rat_room(room):
	def enter(self):
		print "You did it!"

class mapper(object):
	rooms = {"rat_room" : rat_room(), "entrance":  entrance()}

	def next_room(self, room):
		self.room = next_room
		mapper.rooms.get(next_room)


first_room = entrance()
game = engine(first_room)
game.play()