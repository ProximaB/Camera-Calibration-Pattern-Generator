import numpy as np
import argparse
import cv2
import sys
from datetime import datetime

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--rows-grid-num", required=True, type=int,
                help="Number of grid for width.")
ap.add_argument("-c", "--columns-grid-num", required=True, type=int,
                help="Number of grid for height.")
ap.add_argument("-g", "--grid-size-num", required=False, type=int, default=20,
                help="Size of grid element in mm.")
ap.add_argument("-o", "--output-file-name", required=False, type=str, default="Checkedboard_" + f"{datetime.now():%Y%m%d_%H%M%S}",
                help="Name of output pdf file.")
ap.add_argument("-b", "--base-color", required=False, type=str, default="(255,255,255)",
                help="Color of rectangle, background will be set to its inverted color. (rrr,ggg,bbb)")
# args = vars(ap.parse_args())


def main(rows_num, columns_num, grid_size, output_name, base_color):
    block_size = 60
    image_width = block_size * columns_num
    image_height = block_size * rows_num
    base_color = eval(base_color)
    inv_color = tuple(255 - val for val in base_color),

    checker_board = np.zeros((image_height, image_width, 3), np.uint8)

    color_row = 0
    color_column = 0

    for i in range(0, image_width, block_size):
        color_row =not color_row
        color_column = color_row

        for j in range(0, image_height, block_size):
            checker_board[i:i+block_size, j:j+block_size] = base_color if color_column else inv_color
            color_column = not color_column

    cv2.imshow('result', checker_board)
    cv2.waitKey(0)


if __name__ == '__main__':
    args = vars(ap.parse_args())

    rows_num = args['rows_grid_num']
    columns_num = args['columns_grid_num']
    grid_size = args['grid_size_num']
    output_name = args['output_file_name']
    base_color = args['base_color']

    print(args)
    main(rows_num, columns_num, grid_size, output_name, base_color)
else:
    print("ChekcerboardCreator.py is being imported into another module")
