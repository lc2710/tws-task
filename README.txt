# Overview
	Python app to simulate the operation of a squad of Mars rovers moving around a plateau. I have assumed that rovers initialised outside the plateau or on top of another rover are to be ignored. Also commands for rovers to move into a space occupied by another rover or outside of the plateau range are also ignored by the rovers.

# Running
	The program reads instructions from a txt file and is run with the command:
	python run.py FILENAME.txt

# Results
	The output is written to output.txt

# Testing
	Unittests are included and can be run with:
	python test.py