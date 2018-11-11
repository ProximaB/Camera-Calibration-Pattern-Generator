import numpy as np
import argparse
import sys

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--rows-grid-num", required=True,
                help="Number of grid for width")
ap.add_argument("-c", "--columns-grid-num", required=True,
                help="Number of grid for height")
ap.add_argument("-g", "--grid-size", required=True,
                help="Size of grid element in mm")
#args = vars(ap.parse_args())

if __name__=='__main__':
    args = vars(ap.parse_args())
else:
    print("ChekcerboardCreator.py is being imported into another module")

print(args)

#soup = BeautifulSoup(open(args["pokemon_list"]).read())
#pts = np.array(eval(args["coords"]), dtype="float32")
