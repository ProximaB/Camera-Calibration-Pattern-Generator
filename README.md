# Checkerboard-creator-for-camera-calibration
Checkerboard creator for camera calibration and saving to pdf.

```
usage: CheckerboardCreator.py [-h] -r ROWS_GRID_NUM -c COLUMNS_GRID_NUM
                              [-s BLOCK_SIZE_MM] [-o OUTPUT_FILE_NAME]
                              [-d OUTPUT_PATH] [-b BASE_COLOR]

optional arguments:
  -h, --help            show this help message and exit
  -r ROWS_GRID_NUM, --rows-grid-num ROWS_GRID_NUM
                        Number of grid for width.
  -c COLUMNS_GRID_NUM, --columns-grid-num COLUMNS_GRID_NUM
                        Number of grid for height.
  -s BLOCK_SIZE_MM, --block-size-mm BLOCK_SIZE_MM
                        Size of block element in mm.
  -o OUTPUT_FILE_NAME, --output-file-name OUTPUT_FILE_NAME
                        Name of output pdf file.
  -d OUTPUT_PATH, --output-path OUTPUT_PATH
                        Path where save the checkerboard. e.g. -d C:/. | -d
                        ./checkerboards
  -b BASE_COLOR, --base-color BASE_COLOR
                        Color of rectangle, background will be set to its
                        inverted color. (rrr,ggg,bbb)
examples:
  py CheckerboardCreator.py -r 2 -c 2
  py CheckerboardCreator.py -r 2 -c 2 -s 30 -o 2x2
  py CheckerboardCreator.py -r 7 -c 8 -s 30 -o A4 -d results -b (20,30,80)
  ```
  
![preview](https://github.com/ProximaB/Checkerboard-creator-for-camera-calibration/blob/master/preview.png?raw=true)
