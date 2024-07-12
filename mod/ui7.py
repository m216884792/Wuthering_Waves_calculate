# coding=utf-8
import customtkinter as ctk
from .groceries import skill_clear,rini
import os


path=os.getcwd()

class Ui7(ctk.CTk):
        def __init__(self,app):
            super().__init__()
            self.geometry(f"300x600")
            self.title(f"招式傷害%")
            self.attributes('-topmost', 'true')
            ctk.set_appearance_mode("System")
            ctk.set_default_color_theme("blue")
            self.app=app
            self.valuesdict={}

            self.valueslist=['招式傷害%','重擊招式傷害%','共鳴招式傷害%','共鳴解放招式傷害%']
            self.op()


        def op(self):

            config=rini(f'{path}/calculate/skill.ini')

            for i in self.valueslist:
                label = ctk.CTkLabel(self, text=f'{i}',font=("Arial", 16))
                label.pack()

                self.valuesdict[f'{i}']=ctk.CTkEntry(self,width=20*4)
                self.valuesdict[f'{i}'].insert(0, f"{config['var'][f'{i}']}")
                self.valuesdict[f'{i}'].pack()

                _ = ctk.CTkLabel(self,text='',font=("Arial", 10))
                _.pack(pady=0)


            step1_label = ctk.CTkButton( self,text=f"確定",command=lambda:self.check_ok(config),font=("Arial", 16))
            step1_label.pack(pady=10)


        def check_ok(self,config):

            skill_clear()

            for loc,i in enumerate(self.valuesdict):
                config.set('var',f'{self.valueslist[loc]}',f'{self.valuesdict[self.valueslist[loc]].get()}')

            with open(f'{path}/calculate/skill.ini', 'w',encoding="utf-8") as configfile:
                config.write(configfile)
            self.app.show()
            self.destroy()


        def loop(self):
            self.mainloop()

