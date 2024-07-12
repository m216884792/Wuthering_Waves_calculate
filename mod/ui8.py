import customtkinter as ctk
from .groceries import rini
import os


path=os.getcwd()

class Ui8(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.geometry(f"300x400")
            self.attributes('-topmost', 'true')
            self.title(f"詳細面板")
            ctk.set_appearance_mode("System")
            ctk.set_default_color_theme("blue")

            self.op()


        def op(self):
            label = ctk.CTkLabel(self, text=self.getval(),font=("Arial", 16),justify=ctk.LEFT)
            label.pack()

            step1_label = ctk.CTkButton( self,text=f"確定",command=self.check_ok,font=("Arial", 16))
            step1_label.pack(pady=10)

        def getval(self):
            returntxt='\n'
            addatk=0    #點傷
            percentatk=0    #%傷
            chit=5  #暴擊%
            cpercent=150  #暴傷%
            wpercent=0  #重擊%
            eskillpercent=0  #e技%
            rskillpercent=0  #r技%
            npercent=0  #普通攻擊%
            attri=0 #屬性加成%

            devstatedict={'攻擊傷害%':percentatk,'攻擊點傷':addatk,'暴擊%':chit,'暴傷%':cpercent,
            '共鳴技能加成%':eskillpercent,'共鳴解放加成%':rskillpercent,
            '重擊傷害%':wpercent,'普通攻擊傷害%':npercent}

            arms=rini(f'{path}/calculate/arms.ini')#武器

            for i in range(1,6):
                var1=arms['var'][f'top{i}']
                var2=arms['var'][f'ent{i}']
                devstatedict[var1]+=float(var2)

            for i in range(1,6):
                dev= rini(f'{path}/calculate/dev{i}.ini')#聲骸

                fixed=dev['var']['fixed']
                if '4c' in fixed:
                    devstatedict['攻擊點傷']+=150
                    if '暴擊' in fixed:
                        devstatedict['暴擊%']+=22
                    elif '暴傷' in fixed:
                        devstatedict['暴傷%']+=44

                elif '3c' in fixed:
                    devstatedict['攻擊點傷']+=100
                    if '屬性加成' in fixed:
                        attri+=30
                    elif '攻擊傷害' in fixed:
                        devstatedict['攻擊傷害%']+=30

                elif '1c' in fixed:
                    devstatedict['攻擊傷害%']+=18


                for i2 in range(1,6):
                    var1=dev['var'][f'top{i2}']
                    var2=dev['var'][f'ent{i2}']
                    
                    devstatedict[var1]+=float(var2)


            exception = rini(f'{path}/calculate/exception.ini')#額外加成
            varlist=exception.options('var')
            for i in devstatedict:
                if i in varlist:
                    devstatedict[i]+=float(exception['var'][i])


            returntxt+=f"暴擊機率:{devstatedict['暴擊%']}\n\n"
            returntxt+=f"暴擊傷害:{devstatedict['暴傷%']}\n\n"


            returntxt+=f"共鳴技能加成:{devstatedict['共鳴技能加成%']}\n\n"
            returntxt+=f"普攻傷害加成:{devstatedict['普通攻擊傷害%']}\n\n"
            returntxt+=f"重擊傷害加成:{devstatedict['重擊傷害%']}\n\n"
            returntxt+=f"共鳴解放傷害加成:{devstatedict['共鳴解放加成%']}\n\n"

            attri+=float(exception['var']['屬性加成'])

            returntxt+=f'屬性加成:{int(attri)}\n\n'

            return returntxt

        def check_ok(self):
            self.destroy()

        def loop(self):
            self.mainloop()



