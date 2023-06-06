# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core



class InputController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.homeView = self.loadView("input")
    
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------

    def GamePart1(self, rondas, segundos, minutos, validacion):

        if validacion:
            data = {"segundos" : int(segundos), "minutos" : int(minutos), "numero_rondas" : int(rondas)}
            Core.guardar_data_json(data)

            c = Core.openController("countdownTimer")
            c.main()



    def main(self):
        self.homeView.main()