import tkinter as tk
from tkinter import ttk
from views.View import View
from datetime import datetime
from core.Core import Core


"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""
class CountdownTimerView(tk.Tk, View):
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
        self._make_timer()

        self.numero_rondas = Core.recuperar_data_json()["numero_rondas"]
        self.time = Core.recuperar_data_json()["segundos"] + (Core.recuperar_data_json()["minutos"] * 60)

        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",self.time)

        self.counter_time = self.time
        self.running = False
        print(self.time)
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    

    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)
        

    def counter_label(self, label):
        
        def count_time_1():
            if self.running:
                x = self.counter_time
                tt = datetime.fromtimestamp(x)

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
    