# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core


"""
    Main controller. It will be responsible for program's main screen behavior.
"""
class HomeController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.homeView = self.loadView("home")
    
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Opens controller according to the option chosen
    """
    def btnClicked(self, title):
        if title == "Iniciar el Juego":
            c = Core.openController("input")
            c.main()
        elif title == "Configuración":
            c = Core.openController("setting")
            c.main()

            
    """
        @Override
    """
    def main(self):
        self.homeView.main()