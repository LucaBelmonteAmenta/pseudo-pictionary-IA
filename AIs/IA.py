# import libraries
import base64
from io import BytesIO
import io
import time
import json
from imageio import imread, imwrite
from scipy import ndimage, misc
import data
import math

from fastai import *
from fastai.basic_train import load_learner
import cv2
import torch
import numpy as np
import pandas as pd
from torch.utils.data import Sampler, BatchSampler

from fastai.vision import open_image
from fastai.vision import *

import sys

sys.path.insert(0, "../")

from utils import *

class JSONImageItemList(ImageList):
    def open(self, fn):
        with io.open(fn) as f:
            j = json.load(f)
        drawing = list2drawing(j["drawing"], size=128)
        tensor = drawing2tensor(drawing)
        return Image(tensor.div_(255))


def PredictDrawingPhoto(PATH_imagen, cantidad_resultados):
    
    model = load_learner("../")
    class_labels = data.class_return()

    image = cv2.imread(PATH_imagen ,cv2.IMREAD_COLOR)
    size = 256
    img = cv2.resize(image, (size, size), interpolation=cv2.INTER_LINEAR)
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    rgb = rgb.transpose(2,0,1).astype(np.float32)
    tensor = torch.from_numpy(rgb)
    image = Image(tensor.div_(255))

    # # apply model and print prediction
    _, _, preds = model.predict(image)

    results_index = np.argsort(preds)

    resultados = []

    for X in list(reversed(results_index[-cantidad_resultados:])):
        resultado = {class_labels[X] : math.ceil((preds[X]).item() * 100)}
        resultados.append(resultado)
    
    return resultados


if (__name__ == "__main__"):
    path_image = '/home/tecnicus/Documentos/Repositorios/pseudo-pictionary-IA/images/screen_1686092506400181.jpg'
    prediccion = PredictDrawingPhoto(path_image, 10)
    print(prediccion)


