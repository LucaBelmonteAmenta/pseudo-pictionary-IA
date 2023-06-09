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
    rango_resultados = 10  # Tamaño máximo de la lista de palabras que puede devolver la IA como resultado dl analisis
    
    
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
        self._make_input_rondas_results()
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
        condicion4 = (self.resultados.get() is not None) & (self.resultados.get() != "")

        num = 0

        if (condicion2 == False):
            self.segundos.set("0")
        else:
            num += int(self.segundos.get())

        if (condicion3 == False):
            self.minutos.set("0")
        else:
            num += int(self.minutos.get())*60

        condicion5 = num > 0

        return condicion1 & (condicion2 | condicion3) & condicion4 & condicion5

    def continuar(self):
        self.homeController.Continue(self.rondas.get(), self.segundos.get(), self.minutos.get(), self.resultados.get(), self.validacion_para_continuar())



    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="Parametros iniciales", font=("Helvetica bold", 17))
        title.pack(padx=self.PAD, pady=self.PAD)        

    def _make_input_rondas_results(self):

        frame_cb = ttk.Frame(self.mainFrame)
        frame_cb.pack(fill="x")

        lb_rondas = ttk.Label(frame_cb, text="Rondas de la partida: ")
        lb_rondas.grid(row=0, column=0)

        lb_resultados = ttk.Label(frame_cb, text="Palabras por resultado: ")
        lb_resultados.grid(row=1, column=0)
        
        rondas_permitidas = list(map(lambda x: x, range(self.numero_rondas + 1)))
        tamaños_resultados = list(map(lambda x: x, range(1, self.rango_resultados + 1)))

        self.rondas = tk.StringVar(self.mainFrame)
        self.resultados = tk.StringVar(self.mainFrame)

        cb_rondas = ttk.Combobox(frame_cb, values=rondas_permitidas, text="Rondas",state="readonly", textvariable=self.rondas)
        cb_rondas.config(width=3)
        cb_rondas.grid(row=0, column=1)

        cb_resultados = ttk.Combobox(frame_cb, values=tamaños_resultados, text="Palabras por resultado",state="readonly", textvariable=self.resultados)
        cb_resultados.config(width=3)
        cb_resultados.grid(row=1, column=1)

    def _make_input_time_limit(self):

        frame_cb = ttk.Frame(self.mainFrame)
        frame_cb.pack(fill="x")

        validate_numeric_input = frame_cb.register(self.validate_input_time)

        lb = ttk.Label(frame_cb, text="Tiempo para Dibujar: ")
        lb.pack(fill="x")

        self.segundos = tk.StringVar(self.mainFrame)
        self.minutos = tk.StringVar(self.mainFrame)

        entry_minutes = tk.Entry(frame_cb, width=2, font=("Arial", 15), validate="key", validatecommand=(validate_numeric_input, '%P'), textvariable=self.minutos)
        entry_minutes.pack(side=tk.LEFT, padx=10)
        minutes_label = tk.Label(frame_cb, text="Minutos", font=("Arial", 12))
        minutes_label.pack(side=tk.LEFT)

        entry_seconds = tk.Entry(frame_cb, width=2, font=("Arial", 15), validate="key", validatecommand=(validate_numeric_input, '%P'), textvariable=self.segundos)
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
    