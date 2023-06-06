import tkinter as tk
from tkinter import ttk
from views.View import View


"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""
class InputView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 10

    numero_rondas = 10  # Valor máximo rondas permitidas
    
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """
    def __init__(self, controller):
        super().__init__()
        self.title("Preparación del juego")
        self.homeController = controller
        
        self._make_mainFrame()
        self._make_title()
        self._make_input_rondas()
        self._make_input_time_limit()
        self._make_buttom_continue()
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    
    def validate_input_time(self, input):
        if (input.isdigit() & (len(input) < 3)):
            num = int(input)
            return (0 <= num <= 59)
        elif (input == ""):
            return True
        else:
            return False
 
    def validacion_para_continuar(self):
        condicion1 = (self.rondas.get() is not None) & (self.rondas.get() != "")
        condicion2 = (self.segundos.get() is not None) & (self.segundos.get() != "")
        condicion3 = (self.minutos.get() is not None) & (self.minutos.get() != "")

        return condicion1 & condicion2 & condicion3

    def continuar(self):
        self.homeController.GamePart1(self.rondas.get(), self.segundos.get(), self.minutos.get(), self.validacion_para_continuar())


    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="Parametros iniciales", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)        

    def _make_input_rondas(self):

        frame_cb = ttk.Frame(self.mainFrame)
        frame_cb.pack(fill="x")

        lb = ttk.Label(frame_cb, text="Rondas de la partida: ")
        lb.pack(fill="x")
        
        rondas_permitidas = list(map(lambda x: x, range(self.numero_rondas + 1)))

        self.rondas = tk.StringVar(self.mainFrame)

        cb = ttk.Combobox(frame_cb, values=rondas_permitidas, text="Rondas",state="readonly", textvariable=self.rondas)
        cb.pack(fill="x")

    def _make_input_time_limit(self):

        frame_cb = ttk.Frame(self.mainFrame)
        frame_cb.pack(fill="x")

        validate_numeric_input = frame_cb.register(self.validate_input_time)

        lb = ttk.Label(frame_cb, text="Rondas de la partida: ")
        lb.pack(fill="x")

        self.segundos = tk.StringVar(self.mainFrame)
        self.minutos = tk.StringVar(self.mainFrame)

        entry_minutes = tk.Entry(frame_cb, width=2, font=("Arial", 24), validate="key", validatecommand=(validate_numeric_input, '%P'), textvariable=self.minutos)
        entry_minutes.pack(side=tk.LEFT, padx=10)
        minutes_label = tk.Label(frame_cb, text="Minutos", font=("Arial", 12))
        minutes_label.pack(side=tk.LEFT)

        entry_seconds = tk.Entry(frame_cb, width=2, font=("Arial", 24), validate="key", validatecommand=(validate_numeric_input, '%P'), textvariable=self.segundos)
        entry_seconds.pack(side=tk.LEFT, padx=10)
        seconds_label = tk.Label(frame_cb, text="Segundos", font=("Arial", 12))
        seconds_label.pack(side=tk.LEFT)
        
    def _make_buttom_continue(self):

        frame_bt = ttk.Frame(self.mainFrame)
        frame_bt.pack(fill="x")

        bt = ttk.Button(frame_bt, text="Continuar", width=2, command=self.continuar)

        bt.pack(fill="x")

        



            
    """
    @Overrite
    """
    def main(self):
        self.mainloop()
        
    """
    @Overrite
    """
    def close(self):
        return
    