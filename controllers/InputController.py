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

    def Continue(self, rondas, segundos, minutos, tamaño_resultados, validacion):

        if validacion:
            if (segundos.isdigit() == False):
                segundos="0"
            if (minutos.isdigit() == False):
                minutos="0"

            data = {"segundos" : int(segundos), "minutos" : int(minutos), "numero_rondas" : int(rondas), "tamaño_resultados": int(tamaño_resultados)}
            Core.guardar_data_json(data)

            c = Core.openController("game1")
            c.main()



    def main(self):
        self.homeView.main()