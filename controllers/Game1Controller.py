
# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core

from config import APP_PATH

from scanner.SaveFoto import save_frame_camera_key
from AIs.IA import *




class Game1Controller(Controller):

    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
   
    def __init__(self):
        self.tamaño_resultados = Core.recuperar_data_json()["tamaño_resultados"]
        self.homeView = self.loadView("game1")

    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------

    def ScannerDoodle(self):
        scanner_dir_image = save_frame_camera_key("rtsp://admin:Piedras3980@10.128.10.250:554",0, 'data', 'screen',10,35,600,400,700,10)
        return scanner_dir_image
    
    def AnalyzeImage(self, path_image):
        path_image = f"{APP_PATH}/data/{path_image}" 
        resultados = PredictDrawingPhoto(path_image, self.tamaño_resultados)
        return resultados

    def GamePart2(self): 
        pass

    def main(self):
        self.homeView.main()