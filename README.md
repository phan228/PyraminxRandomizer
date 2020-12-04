# Pyraminx Randomizer

Consider a [4-layer pyraminx](https://ruwix.com/twisty-puzzles/pyraminx-triangle-rubiks-cube/master-pyraminx/). 
Four faces of the pyraminx are implemented using four 4x7 matrices (2D arrays). When rotating, the color blocks on each face will switch places for the corresponding blocks' positions on another face depending on the rotations.
The list of moves is stored in the moves[] array as a record for the 2nd project so it won't be printed out in this one.

### How to run: `python randomizer.py`

### Implementation: 
There are 24 moves in total for the pyraminx, with 12 clockwise and 12 counter-clockwise rotations: tip rotations, 2-layer rotations, and 3-layer rotations for 4 sides: Up, Left, Right, Back.

The program takes in the number of moves and randomly picks numbers from 1-24, these numbers are associated with different moves (i.e: 1 is for U1 - rotate 1 layer of the top tip clockwise, and 17 is for L2_inv - rotate 2 layers of the left tip counter-clockwise). Then it will randomize the pyraminx and print the result out to the console.

For example, the initial pyraminx is as below:

	      R		      Y		      G
	    R R R 	    Y Y Y	    G G G
	  R R R R R	  Y Y Y Y Y	  G G G G G
	R R R R R R R	Y Y Y Y Y Y Y	G G G G G G G
			B B B B B B B
		          B B B B B
			    B B B
			      B
  
After U1 - rotating 1 layer of the top tip clockwise, the affected faces are red (R), yellow (Y), green (G). The pyraminx after randomization is:

	      Y		      G		      R
	    R R R 	    Y Y Y	    G G G
	  R R R R R	  Y Y Y Y Y	  G G G G G
	R R R R R R R	Y Y Y Y Y Y Y	G G G G G G G
			B B B B B B B
			  B B B B B
			    B B B
			      B

2020 Intro to Artificial Intelligence
