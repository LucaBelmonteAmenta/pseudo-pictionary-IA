
# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core
from datetime import time


class CountdownTimerController(Controller):



    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        
        self.homeView = self.loadView("countdownTimer")



    
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------


    def GamePart2(self):
        pass



    def main(self):
        self.homeView.main()