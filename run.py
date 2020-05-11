from operator import add
import sys

class Plateau():
	'''
	Class used to represent the plateau and rovers as described 
	in the input text file. 

	Attributes
	----------
	rover_list : list
		List containing the rover objects
	dimensions : list
		2 element list representing the map dimensions (x, y coordinates)

	Methods
	-------

	read_commands(commande_file)
		Read initial conditions and commands from input file. Initialise rovers 
		and add to list
	move_rovers()
		Call the move method for each rover object
	write_output()
		Write the rovers location and direction information into the output file
	'''

	def __init__(self):
		'''
		Parameters
		----------
		rover_list : list
			List containing the rover objects
		dimensions : list
			2 element list representing the map dimensions (x, y coordinates)
		'''
		self.rover_list = []
		self.dimensions = None

	def read_commands(self, command_file):
		'''
		Read initial conditions and commands from input file. Initialise rovers 
		and add to list

		Parameters
		----------
		command_file : file
			Text file containing the initial conditions and rover commands
		'''
		f = open(command_file, 'r')
		i = 0
		for line in f:
			line = line.strip()
			if i == 0:
				self.dimensions = list(map(int, line.split(" ")))

			elif i % 2 == 1:
				init_conditions = line.split(" ")

			else:

				position = list(map(int, init_conditions[0:2]))
				# If 2 rovers initialised in same position, ignore second rover
				if any(rover.position == position for rover in self.rover_list):
					print("Two rovers initialised in same position, ignoring second rover")
				# If rover initialised outside plateau range, ignore rover
				elif (position[0] > self.dimensions[0] or position[1] > self.dimensions[1] or 
					position[0] < 0 or position[1] < 0):
					print("Rover initialised outside of plateau, ignoring rover")
				# Create rover object. Append to rover object list and rover position list
				else:
					rover = Rover(position=position, 
								direction=init_conditions[2], 
								command_list=line
								)
					self.rover_list.append(rover)

			i = i + 1

		f.close()

	def move_rovers(self):
		'''
		Call the move method for each rover object
		'''
		for i in range (0, len(self.rover_list)):
			# Remove the current rover's position from rover_list when passing to move() for crash detection
			position = self.rover_list[i].move(self.dimensions, self.rover_list[:i] + self.rover_list[i+1:])

	def write_output(self):
		'''
		Write the rovers location and direction information into the output file
		'''
		f = open("output.txt", "w")

		for rover in self.rover_list:
			f.write(str(rover.position[0]) + " " + str(rover.position[1]) + " " + rover.direction + "\n")

		f.close()

class Rover():
	'''
	Class used to represent a rover

	Attributes
	----------
	move_dict : dict
		Dictionary containing instructions for translating move commands 
		into direction/position movements
	position : list
		2 element list containing x, y coordinates of rover location
	direction : str
		String representing direction rover is facing
	command_list : str
		String containing the move commands to be operated by the rover object

	Methods
	-------
	move(dimensions)
		Move rover from initial position according to move commands


	'''

	move_dict = {'N': 
			{'L': 'W', 
			 'R': 'E', 
			 'M': [0, 1]
			 },
		 'E': 
			{'L': 'N', 
			 'R': 'S', 
			 'M': [1, 0]
			 },
		 'S': 
			{'L': 'E', 
			 'R': 'W', 
			 'M': [0, -1]
			 },
		 'W': 
			{'L': 'S', 
			 'R': 'N', 
			 'M': [-1, 0]
			 }
		}

	def __init__(self, position, direction, command_list):
		'''
		Parameters
		----------
		position : list
			2 element list containing x, y coordinates of rover location
		direction : str
			String representing direction rover is facing
		command_list : str
			String containing the move commands to be operated by the rover object
		'''
		self.position = position
		self.direction = direction
		self.command_list = command_list
		
	def move(self, dimensions, rover_list):
		'''
		Move rovers according to commands. Rovers have been fitted with instructions 
		to ignore commands which would result them crashing into other rovers or 
		falling off the plateau.

		Parameters
		----------
		dimensions : list
			2 element list containing plateau dimensions
		rover_list : list
			List containing all rover objects
		'''
		for command in self.command_list: 
			if command == 'M':
				new_pos = list(map(add, self.position, self.move_dict[self.direction][command]))
				# Don't want to crash into another rover, ignore move command if rover is present in move_to location
				if any(rover.position == new_pos for rover in rover_list):
					pass

				# Don't want to fall off plateau, ignore move command if move_to is outside plateau dimensions
				elif (new_pos[0] > dimensions[0] or new_pos[1] > dimensions[1] or 
					new_pos[0] < 0 or new_pos[1] < 0):
					pass
				else:
					self.position = new_pos

			else:
				self.direction = self.move_dict[self.direction][command]

		return self.position

if __name__ == '__main__': 

	plateau = Plateau()
	plateau.read_commands(sys.argv[1])
	plateau.move_rovers()
	plateau.write_output()
