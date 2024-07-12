import customtkinter as ctk
from .groceries import rank_clear,rini
import os


path=os.getcwd()

class Ui4(ctk.CTk):
        def __init__(self,app):
            super().__init__()
            self.geometry(f"300x300")
            self.attributes('-topmost', 'true')
            self.title(f"等級")
            ctk.set_appearance_mode("System")
            ctk.set_default_color_theme("blue")
            self.app=app

            self.op()


        def op(self):
            config = rini(f'{path}/calculate/rank.ini')

            label = ctk.CTkLabel(self, text='人物等級',font=("Arial", 16))
            label.pack(pady=10)

            self.rank1 = ctk.CTkEntry(self,width=16*4,textvariable='')
            self.rank1.insert(0, f"{config['var'][f'rank1']}")
            self.rank1.pack(pady=10)

            label = ctk.CTkLabel(self, text='怪物等級',font=("Arial", 16))
            label.pack(pady=10)

            self.rank2 = ctk.CTkEntry(self,width=16*4,textvariable='')
            self.rank2.insert(0, f"{config['var'][f'rank2']}")
            self.rank2.pack(pady=10)


            step1_label = ctk.CTkButton( self,text=f"確定",command=lambda:self.check_ok(config),font=("Arial", 16))
            step1_label.pack(pady=10)


        def check_ok(self,config):
            rank_clear()

            config.set('var',f'rank1',f'{self.rank1.get()}')
            config.set('var',f'rank2',f'{self.rank2.get()}')

            with open(f'{path}/calculate/rank.ini', 'w',encoding="utf-8") as configfile:
                config.write(configfile)
            self.app.show()
            self.destroy()


        def loop(self):
            self.mainloop()

