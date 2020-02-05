import wx
import serial

class panel_eslave_1(wx.Panel):
    def __init__(self, parent,ID , label, initval):
        wx.Panel.__init__(self,parent,ID, pos= (0,0))
        #se almacena el valor recibido
        self.value = initval
        #se crea el box sizer principal
        box = wx.StaticBox(self,-1,label)
        sizer = wx.StaticBoxSizer(box,wx.VERTICAL)
        #se crean los controles
        texto1 = wx.StaticText(self,-1,label="Luz Actual: ")

        self.button_off = wx.Button(self,-1,label="OFF", style = wx.RB_GROUP)
        self.Bind(wx.EVT_BUTTON,self.on_button_off,self.button_off)
        
        self.button_on = wx.Button(self,-1,label ="ON")
        self.Bind(wx.EVT_BUTTON,self.on_button_on,self.button_on)
        
        self.text_ctrl_luz = wx.TextCtrl(self,-1,value = str(initval))
        #se crea el box sizer superior
        text_box_luz = wx.BoxSizer(wx.HORIZONTAL)
        text_box_luz.Add(texto1, flag = wx.ALIGN_CENTRE_VERTICAL)
        text_box_luz.Add(self.text_ctrl_luz, flag = wx.ALIGN_CENTER_VERTICAL)
        #se crea el box sizer inferior
        button_luz_box = wx.BoxSizer(wx.HORIZONTAL)
        button_luz_box.Add(self.button_on, flag = wx.ALIGN_LEFT)
        button_luz_box.Add(self.button_off, flag = wx.ALIGN_RIGHT)
        
        sizer.Add(text_box_luz,0,wx.ALL,10)
        sizer.Add(button_luz_box,0,wx.ALL,10)
        
        self.SetSizer(sizer)
        sizer.Fit(self)
    def on_button_on(self, event):
        print("button on")

    def on_button_off(self, event):
        print("button off")

class panel_eslave_2(wx.Panel):
    def __init__(self, parent, ID, label, initval):
        wx.Panel.__init__(self,parent,ID, pos = (0,200))
        
        self.value = initval
        
        box = wx.StaticBox(self,-1,label)
        sizer = wx.StaticBoxSizer(box,wx.VERTICAL)


        self.text_ctrl_bout = wx.TextCtrl(self,-1,value = str(initval))
        self.button_up = wx.Button(self,-1,label="UP")
        self.Bind(wx.EVT_BUTTON,self.on_button_up,self.button_up)
        self.button_down = wx.Button(self,-1,label="DOWN")
        self.Bind(wx.EVT_BUTTON,self.on_button_down,self.button_down)
        self.button_stop = wx.Button(self,-1,label="STOP")
        self.Bind(wx.EVT_BUTTON,self.on_button_stop,self.button_stop)

        box_buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        box_buttons_sizer.Add(self.button_up, flag = wx.ALIGN_CENTRE_VERTICAL)
        box_buttons_sizer.Add(self.button_stop, flag = wx.ALIGN_CENTER_VERTICAL)
        box_buttons_sizer.Add(self.button_down, flag = wx.ALIGN_CENTER_VERTICAL)

        sizer.Add(self.text_ctrl_bout,0,wx.ALIGN_CENTER_HORIZONTAL,10)
        sizer.Add(box_buttons_sizer,0,wx.ALL,10)
        self.SetSizer(sizer)
        sizer.Fit(self)

    def on_button_up(self,event):
        print("button up")

    def on_button_down(self,event):
        print("button down")

    def on_button_stop(self,event):
        print("button stop")


class panel_eslave_3(wx.Panel):
    def __init__(self, parent, ID, label, initval):
        wx.Panel.__init__(self,parent,ID, pos = (0,300))
        
        self.value = initval

        box = wx.StaticBox(self,-1,label)
        sizer = wx.StaticBoxSizer(box,wx.VERTICAL)

        self.button_add = wx.Button(self,-1,label="Cambiar")
        self.Bind(wx.EVT_BUTTON,self.on_button_add,self.button_add)
        self.button_see = wx.Button(self,-1,label="Ver")
        self.Bind(wx.EVT_BUTTON,self.on_button_see,self.button_see)
        self.text_ctrl_pasw = wx.TextCtrl(self,-1, value = str(initval))

        box_button = wx.BoxSizer(wx.HORIZONTAL)
        box_button.Add(self.button_add, flag= wx.ALIGN_CENTER_HORIZONTAL)
        box_button.Add(self.button_see, flag= wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.text_ctrl_pasw,0,wx.ALL,10)
        sizer.Add(box_button,0,wx.ALL,10)
        self.SetSizer(sizer)
        sizer.Fit(self)

    def on_button_add(self,event):
        print("button cambiar")

    def on_button_see(self,event):
        print("button ver")


class panel_eslave_4(wx.Panel):
    def __init__(self, parent, ID, label, initval):
        wx.Panel.__init__(self,parent,ID, pos = (0,400))
        
        self.value = initval

        box = wx.StaticBox(self,-1,label)
        sizer = wx.StaticBoxSizer(box,wx.VERTICAL)

        self.text_temp = wx.TextCtrl(self,-1,value=str(initval))
        self.button_cool = wx.Button(self,-1,label="Cool")
        self.Bind(wx.EVT_BUTTON,self.on_button_cool,self.button_cool)

        box_cont = wx.BoxSizer(wx.HORIZONTAL)
        box_cont.Add(self.button_cool, flag= wx.ALIGN_CENTER_HORIZONTAL)
        box_cont.Add(self.text_temp, flag= wx.ALIGN_CENTER_HORIZONTAL)

        sizer.Add(box_cont,0,wx.ALL,10)
        self.SetSizer(sizer)
        sizer.Fit(self)

    def on_button_cool(self,event):
        print("button cooling")
        
#clase principal, clase del frame
class class_frame(wx.Frame):
    #constructor
    def __init__(self):
        #valores iniciales del frame    
        wx.Frame.__init__(self,None,-1,title = "Home Control", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        #icono
        self.SetIcon(wx.Icon('C:\\Users\\Felipe Diaz\\Documents\\GitHub\\Programas_python\\home.ico', wx.BITMAP_TYPE_ICO))
        
        # llamado metodos de los paneles, y barras de menu
        self.create_menu()
        self.create_main_panel()

        # actualizacion de la interfaz grafica con timer
        self.redraw_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_refresh, self.redraw_timer)
        self.redraw_timer.Start(10)

    def create_menu(self):
        self.menubar = wx.MenuBar()
        menu_file = wx.Menu()

        menu_black = menu_file.Append(-1,"Black")
        self.Bind(wx.EVT_MENU, self.on_black, menu_black)

        menu_file.AppendSeparator()
        m_white = menu_file.Append(-1,"white")
        #asdg
        menu_file.AppendSeparator()
        m_exit = menu_file.Append(-1, "E&xit\tCtrl-X", "Exit")
        #self.Bind(wx.EVT_MENU, self.on_exit, m_exit)
        
                
        self.menubar.Append(menu_file, "&Theme")
        self.SetMenuBar(self.menubar)

    def on_black(self,event):
        self.panel.SetBackgroundColour(wx.BLACK)

    def on_white(self,event):
        self.panel.SetBackgroundColour(wx.BLACK)

    def on_refresh(self,event):
        print("sss")

    def create_main_panel(self):
        #se crea panel principal
        self.panel = wx.Panel(self)

        self.box = wx.BoxSizer(wx.VERTICAL)
        
        self.esclavo1_control = panel_eslave_1(self.panel,-1,"Control de luz",0)
        self.esclavo2_control = panel_eslave_2(self.panel,-1,"Control de Blackout",0)
        self.esclavo3_control = panel_eslave_3(self.panel,-1,"Control de Seguridad",0)
        self.esclavo4_control = panel_eslave_4(self.panel,-1,"Control de temperatura",0)
        
        self.box.Add(self.esclavo1_control,border = 5, flag=wx.EXPAND)
        self.box.Add(self.esclavo2_control,border = 5, flag=wx.EXPAND)
        self.box.Add(self.esclavo3_control,border = 5, flag=wx.EXPAND)
        self.box.Add(self.esclavo4_control,border = 5, flag=wx.EXPAND)
      
        self.panel.SetSizer(self.box)
        self.box.Fit(self)


if __name__ == '__main__':
    app = wx.App()
    app.frame = class_frame()
    app.frame.Show()    
    app.MainLoop()