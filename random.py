import pandas as pd
import os
import pandas as pd
from tqdm import tqdm


parser = argparse.ArgumentParser(description="Copy the files in the csv to the dataset folder")

    parser.add_argument("source", help='Path of the source folder', type=str)
    parser.add_argument('dest', help="Path of the destination folder", type=str)
    parser.add_argument("csv", help="Path to the csv", type=str)

    args = parser.parse_args()
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            backUP(os.path.join(path, file))