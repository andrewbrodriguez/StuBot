import cv2
from deepface import DeepFace
import json
import pandas as pd
import numpy as np

to_analyze = cv2.imread("Test.png")

analysis = DeepFace.analyze(to_analyze, enforce_detection = False)

def EMAUpdate(vector):
    return new_vector


json_object = json.dumps(analysis['emotion'], indent=4)

with open("output.json", "w") as file:
    file.write(json_object)