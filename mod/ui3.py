# coding=utf-8
import customtkinter as ctk
from .groceries import dev_clear,rini
import os


path=os.getcwd()

class Ui3(ctk.CTk):
        def __init__(self,var,app):
            super().__init__()
            self.geometry(f"300x600")
            self.attributes('-topmost', 'true')
            self.title(f"生骸{var}")
            ctk.set_appearance_mode("System")
            ctk.set_default_color_theme("blue")
            self.app=app
            self.valueslist=['暴擊%','暴傷%','攻擊傷害%','攻擊點傷','共鳴技能加成%','共鳴解放加成%','普通攻擊傷害%','重擊傷害%','生命','生命%','防禦','防禦%','共鳴效率']
            self.valuesdict={}

            self.op(var)

        def op(self,var):

            config = rini(f'{path}/calculate/dev{var}.ini')

            label = ctk.CTkLabel(self,text=f"生骸{var}",font=("Arial", 16))
            label.pack()

            self.topatt = ctk.CTkComboBox(self,font=("Arial", 16),width=160,
                                               values=['4c:暴擊22%','4c:暴傷44%','4c:攻擊傷害33%','4c:生命33%','4c:防禦41.8%',
                                                       '3c:屬性加成30%','3c:攻擊傷害30%','3c:生命30%','3c:防禦38%','3c:共鳴效率32%',
                                                       '1c:攻擊傷害18%','1c:生命22.8%','1c:防禦18%'])
            self.topatt.set(f"{config['var'][f'fixed']}")
            self.topatt.pack(pady=5)

            self.varatt1,self.varatt2,self.varatt3,self.varatt4,self.varatt5=[None,None,None,None,None]
            varattlist=[self.varatt1,self.varatt2,self.varatt3,self.varatt4,self.varatt5]

            for loc,i in enumerate(varattlist):
                i=ctk.CTkComboBox(self,font=("Arial", 16),values=self.valueslist,width=160)
                self.valuesdict[i]=ctk.CTkEntry(self,width=20*4)
                i.set(f"{config['var'][f'top{loc+1}']}")
                i.pack(pady=5)

                self.valuesdict[i].insert(0, f"{config['var'][f'ent{loc+1}']}")
                self.valuesdict[i].pack()

                _ = ctk.CTkLabel(self,text='',font=("Arial", 10))
                _.pack(pady=0)


            step1_label = ctk.CTkButton( self,text=f"確定",command=lambda:self.check_ok(var,config),font=("Arial", 16))
            step1_label.pack(pady=10)

        def check_ok(self,var,config):

            dev_clear(var)

            config.set('var','fixed',f'{self.topatt.get()}%')

            for loc,i in enumerate(self.valuesdict):
                if '%' in i.get():
                    i.set(f'{i.get()}%')

                config.set('var',f'top{loc+1}',f'{i.get()}')
                config.set('var',f'ent{loc+1}',f'{self.valuesdict[i].get()}')


            with open(f'{path}/calculate/dev{var}.ini', 'w',encoding="utf-8") as configfile:
                config.write(configfile)

            self.app.show()
            self.destroy()

        def loop(self):
            self.mainloop()

