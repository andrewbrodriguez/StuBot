
'''
Run facial recognition on a given image (pre-cropped using a bounding box). 
Specify flags for the different operations we want to perform in a loop. 

'''


import cv2
from deepface import DeepFace
import argparse
import json
import pandas as pd
import numpy as np



# TODO(Ryan or Yaman): make this work with the actual formula
def EMAUpdate(vector):
    return new_vector


def main():

    parser = argparse.ArgumentParser(description='Run facial recognition on an image.')
    parser.add_argument('--emotion', action='store_true')
    args = parser.parse_args()

    to_analyze = cv2.imread('assets/Test.jpg')

    # Dictionary
    json_object = {}

    if args.emotion:
        analysis = DeepFace.analyze(to_analyze, enforce_detection = False)[0]
        json_object['emotion'] = analysis['emotion']

    with open('out/output.json', 'w') as file:
        file.write(json.dumps(json_object, indent=4))



if __name__ == "__main__":
    main()


