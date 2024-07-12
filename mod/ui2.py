import customtkinter as ctk
from .groceries import arms_clear,rini
import os


path=os.getcwd()

class Ui2(ctk.CTk):
        def __init__(self,app):
            super().__init__()
            self.geometry(f"300x650")
            self.title(f"武器")
            ctk.set_appearance_mode("System")
            ctk.set_default_color_theme("blue")
            self.attributes('-topmost', 'true')
            self.app=app
            self.topattdict={}
            self.op()


        def op(self):
            config = rini(f'{path}/calculate/arms.ini')

            self.topatt1,self.topatt2,self.topatt3,self.topatt4,self.topatt5=[None,None,None,None,None]
            topattlist=[self.topatt1,self.topatt2,self.topatt3,self.topatt4,self.topatt5]

            for loc,i in enumerate(topattlist):
                i = ctk.CTkComboBox(self,font=("Arial", 16),values=['暴擊%','暴傷%','攻擊傷害%','重擊傷害%'])
                i.set(f"{config['var'][f'top{loc+1}']}")
                i.pack(pady=5)

                self.topattdict[i]=ctk.CTkEntry(self,width=20*4)
                self.topattdict[i].insert(0, f"{config['var'][f'ent{loc+1}']}")
                self.topattdict[i].pack()

                _ = ctk.CTkLabel(self,text='',font=("Arial", 10))
                _.pack(pady=0)

            step1_label = ctk.CTkButton( self,text=f"確定",command=lambda:self.check_ok(config),font=("Arial", 16))
            step1_label.pack(pady=10)


        def check_ok(self,config):
            arms_clear()

            for loc,i in enumerate(self.topattdict):
                print(i.get(),'/',self.topattdict[i].get())
                if '%' in i.get():
                    i.set(f'{i.get()}%')

                config.set('var',f'top{loc+1}',f'{i.get()}')
                config.set('var',f'ent{loc+1}',f'{self.topattdict[i].get()}')

            with open(f'{path}/calculate/arms.ini', 'w',encoding="utf-8") as configfile:
                config.write(configfile)

            self.app.show()
            self.destroy()


        def loop(self):
            self.mainloop()

