import unittest 
from run import Plateau, Rover

class TestRover(unittest.TestCase): 
	
	def setUp(self): 
		self.rover = Rover([0, 2], "W", "MRMMLRM")

	def test_rover_init(self):
		'''Test rover initialisation'''
		self.assertEqual(self.rover.position, [0, 2])
		self.assertEqual(self.rover.direction, "W")
		self.assertEqual(self.rover.command_list, "MRMMLRM")

	def test_rover_move(self):
		'''Test rover move functionality'''
		self.rover.move([5, 5], [])
		self.assertEqual(self.rover.position, [0, 5])


class TestPlateau(unittest.TestCase): 
	
	def test_plateau_init(self):
		'''Test plateau initialisation'''
		plateau = Plateau()
		plateau.read_commands('./test/test_commands_1.txt')
		self.assertEqual(plateau.dimensions, [5, 5])

	def test_command_file_1(self):
		'''Test full operation'''
		plateau = Plateau()
		plateau.read_commands('./test/test_commands_1.txt')
		plateau.move_rovers()
		plateau.write_output()

		with open('./test/output_test_1.txt', 'r') as myfile:
  			correct_output = myfile.read().strip('\n')
		with open('./output.txt', 'r') as myfile:
  			test_output = myfile.read().strip('\n')

		self.assertEqual(test_output, correct_output)

	def test_init_outside_range(self):
		'''Test rovers initialised outside the plateau range are ignored'''
		plateau = Plateau()
		plateau.read_commands('./test/test_init_outside_range.txt')
		plateau.move_rovers()
		plateau.write_output()

		with open('./test/output_test_outside_range.txt', 'r') as myfile:
  			correct_output = myfile.read().strip('\n')
		with open('./output.txt', 'r') as myfile:
  			test_output = myfile.read().strip('\n')

		self.assertEqual(test_output, correct_output)

	def test_same_location(self):
		'''Test rovers initialised in the same location are ignored'''
		plateau = Plateau()
		plateau.read_commands('./test/test_commands_same_loc.txt')
		plateau.move_rovers()
		plateau.write_output()
		
		with open('./output.txt', 'r') as myfile:
  			plateau_1_output = myfile.read().strip()

		plateau = Plateau()
		plateau.read_commands('./test/test_commands_single_rover.txt')
		plateau.move_rovers()
		plateau.write_output()
		with open('./output.txt', 'r') as myfile:
  			plateau_2_output = myfile.read().strip()

		self.assertEqual(plateau_1_output, plateau_2_output)

if __name__ == '__main__': 
	unittest.main() 
