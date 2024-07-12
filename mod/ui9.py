# coding=utf-8
import customtkinter as ctk
from .groceries import rini
import os


path=os.getcwd()

class Ui9(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.geometry(f"900x320")
            self.attributes('-topmost', 'true')
            self.title(f"聲骸詳細面板")
            ctk.set_appearance_mode("System")
            ctk.set_default_color_theme("blue")

            self.op()


        def op(self):
            
            for i in range(1,6):
                txt=''
                txt+=f'聲骸{i}\n\n'
                
                devini=rini(f'{path}/calculate/dev{i}.ini')
                txt+=f"{devini['var'][f'fixed']}\n\n"
                for i2 in range(1,6):
                    txt+=f"{devini['var'][f'top{i2}']}:{devini['var'][f'ent{i2}']}\n\n"

                label = ctk.CTkLabel(self, text=txt,font=("Arial", 16),justify=ctk.LEFT)
                label.place(x=20+(i-1)*180,y=20)

            step1_label = ctk.CTkButton( self,text=f"確定",command=self.check_ok,font=("Arial", 16))
            step1_label.place(x=450-70,y=275)

        def check_ok(self):
            self.destroy()

        def loop(self):
            self.mainloop()



