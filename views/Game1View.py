import tkinter as tk
from tkinter import ttk
from views.View import View
from datetime import datetime
from core.Core import Core
from AIs.data import class_return_esp, class_return_esp_faciles

import random
import time


"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""
class Game1View(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    
    PAD = 10
    main_counter = True
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------

    def __init__(self, controller):
        super().__init__()
        self.title("Ronda")
        self.homeController = controller

        self._make_mainFrame()
        self._make_word_generate()
        self._make_timer()
        self._make_buttons_game()
        self._make_table_results()

        self.numero_rondas = Core.recuperar_data_json()["numero_rondas"]
        self.time = Core.recuperar_data_json()["segundos"] + (Core.recuperar_data_json()["minutos"] * 60)

        self.counter_time = self.time
        self.running = False

    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    

    def escanear(self):

        self.nombre_imagen = self.homeController.ScannerDoodle()

        if (self.nombre_imagen != "nofile") and (self.nombre_imagen is not None):
            self.bt_analyze['state']='normal'
        else:
            self.bt_analyze['state']='disabled'

    def analizar(self):
        self.analisis_imagen = self.homeController.AnalyzeImage(self.nombre_imagen)
        self.completar_tabla(self.analisis_imagen)
        
    def completar_tabla(self, resultados):
        # Insertar datos en la tabla

        for item in self.table.get_children():
            self.table.delete(item)

        x = 0
        for resultado in resultados:
            x = x + 1
            clase = list(resultado.keys())[0]
            acertividad = str(list(resultado.values())[0]) + " %"
            self.table.insert(parent='', index=x, iid=x, values=(x, clase, acertividad))

        # Ajustar el ancho de las columnas
        for column in self.table["columns"]:
            self.table.column(column, width=100)

        self.table.pack(fill="x", anchor = 'center')

    def counter_label(self, label):
        
        def count_time_1():
            if self.running:
                tt = datetime.fromtimestamp(self.counter_time)

                date_object = tt.strftime('%M:%S.%f')[:-4]

                display=date_object
                label['text']=display
    
                label.after(10, count_time_1) 
                self.counter_time -= 0.01

                if(self.counter_time <= 0):
                    self.Stop()

        count_time_1()

    def clocktime(self, label):
        
        def count_time_2():
            if (self.main_counter == True):
                label['text']=datetime.utcnow().strftime('%M:%S.%f')
                label.after(500, count_time_2) 

        count_time_2()
        
    def Start(self, label):
        self.running=True
        self.main_counter = False
        self.counter_label(label)
        
        self.start['state']='disabled'
        self.start['highlightbackground']='black'
        
        self.stop['state']='normal'
        self.stop['highlightbackground']='red'
        
        self.reset['state']='normal'
        self.reset['highlightbackground']='dark grey'
    
    def Stop(self):
        self.start['state']='normal'
        self.start['highlightbackground']='green'
        
        self.stop['state']='disabled'
        self.stop['highlightbackground']='black'
        
        self.reset['state']='normal'
        self.reset['highlightbackground']='dark grey'
        
        self.running = False
    
    def Reset(self, label):
        self.counter_time=self.time
        if self.running==False:      
            self.reset['state']='disabled'
            self.reset['highlightbackground']='black'
            
            self.main_counter = True
            self.clocktime(label)

    def Word_Generate(self):

        self.roulette_time = 3
        self.roulette = True
        instanteInicial = datetime.now()

        def funcion_recursiva():
            if (self.roulette == True):
                word = random.choice(class_return_esp_faciles())
                self.entry_word.config(state="normal")
                self.entry_word.delete(0, tk.END)
                self.entry_word.insert(0, word)
                self.entry_word.config(state="readonly")

                self.entry_word.after(10, funcion_recursiva) 

                self.roulette_time -= 0.05

                if (self.roulette_time <= 0):
                    self.roulette = False    

        funcion_recursiva()



    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        #self.mainFrame.config(background='#52E65B')
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    def _make_word_generate(self):
        frame_word = tk.Frame(self.mainFrame)
        #frame_word.configure(background="white")
        frame_word.pack(fill="x", anchor = 'center')

        self.entry_word = tk.Entry(frame_word, state="readonly")
        self.entry_word.config(width=15, font=("Arial", 18))
        self.entry_word.grid(column=0, row=0)

        self.bt_word = tk.Button(frame_word, text="Palabra Random", command=self.Word_Generate)
        self.bt_word.grid(column=1, row=0)

    def _make_label_timer(self, frame_timer):
        self.label_timer = tk.Label(frame_timer, text=datetime.utcnow().strftime('%H:%M:%S'), fg="white", font="Geneva 45 bold",bg="#282828")
        self.label_timer.pack()
        self.clocktime(self.label_timer)

    def _make_buttons_timer(self, frame_timer):

        self.start = tk.Button(frame_timer, text='Start', width=7,height=1, command=lambda:self.Start(self.label_timer),font="Geneva 15 bold",highlightbackground="green",activeforeground='black',fg='green')
        self.reset = tk.Button(frame_timer, text='Reset',width=7,height=1, state='disabled', command=lambda:self.Reset(self.label_timer),font="Geneva 15 bold",borderwidth = 0,highlightbackground="black",activeforeground='black',fg='white')
        self.stop = tk.Button(frame_timer, text='Stop',width=7,height=1,state='disabled',command=self.Stop,font="Geneva 15 bold",bg="darkgrey",highlightbackground="black",activeforeground='black',fg='red')

        self.start.pack(side="left")
        self.reset.pack(side="left")
        self.stop.pack(side ="left")

    def _make_timer(self):
        frame_label = tk.Frame(self.mainFrame)
        frame_label.configure(background="black")
        frame_label.pack(fill="x", anchor = 'center')

        frame_buttons = tk.Frame(self.mainFrame)
        frame_buttons.configure(background="black")
        frame_buttons.pack(fill="x", anchor = 'center')
        
        self._make_buttons_timer(frame_buttons)
        self._make_label_timer(frame_label)

    def _make_buttons_game(self):

        frame_bt_game = tk.Frame(self.mainFrame)
        frame_bt_game.configure(background="black")
        frame_bt_game.pack(fill="x", anchor = 'center')

        self.direccion_imagen = ""

        self.bt_scanner = tk.Button(frame_bt_game, text='Escanear Dibujo', width=7,height=1, command=self.escanear ,font="Geneva 15 bold",highlightbackground="black",activeforeground='black',fg='black')
        self.bt_analyze = tk.Button(frame_bt_game, text='Analizar Dibujo',width=7,height=1, state='disabled', command=self.analizar,font="Geneva 15 bold",borderwidth = 0,highlightbackground="black",activeforeground='black',fg='black')
        
        self.bt_scanner.pack(fill="x", anchor = 'center')
        self.bt_analyze.pack(fill="x", anchor = 'center')

    def _make_table_results(self):

        frame_table = tk.Frame(self.mainFrame)
        frame_table.pack(fill="x", anchor = 'center')

        self.table = ttk.Treeview(self.mainFrame)

        self.table['columns']=('ID', 'Clase', 'Asertividad')
        self.table.column('#0', width=0, stretch=tk.NO)
        self.table.column('ID', anchor=tk.CENTER, width=80)
        self.table.column('Clase', anchor=tk.CENTER, width=80)
        self.table.column('Asertividad', anchor=tk.CENTER, width=80)

        self.table.heading('#0', text='', anchor=tk.CENTER)
        self.table.heading('ID', text='ID', anchor=tk.CENTER)
        self.table.heading('Clase', text='Clase Localizada', anchor=tk.CENTER)
        self.table.heading('Asertividad', text='Porcentaje de Asertividad', anchor=tk.CENTER)
        
        self.table.pack(fill="x", anchor = 'center')

    

            
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
    