import os
import argparse


def backUP(path: str):
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            backUP(os.path.join(path, file))

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Copy the files in the csv to the dataset folder")

    parser.add_argument("source", help='Path of the source folder', type=str)
    parser.add_argument("dest", help="Path of the destination folder", type=str)
    