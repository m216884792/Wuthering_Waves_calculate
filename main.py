import customtkinter as ctk
from mod.ui2 import Ui2
from mod.ui3 import Ui3
from mod.ui4 import Ui4
from mod.ui5 import Ui5
from mod.ui6 import Ui6
from mod.ui7 import Ui7
from mod.ui8 import Ui8
from mod.ui9 import Ui9
from mod.calculate import allcalculate,rini
import os


path=os.getcwd()

class Ui(ctk.CTk):
    """UI介面"""
    def __init__(self):
        super().__init__()
        self.geometry("320x575")
        self.title(f"www")

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.attributes('-topmost', 'true')
        self.watk = ctk.StringVar()
        self.yatk = ctk.StringVar()
        self.allatk = ctk.StringVar()
        self.allatk2 = ctk.StringVar()
        self.pack_items()

    def pack_items(self):

        self.config=rini(f'{path}/calculate/base.ini')


        step1_label = ctk.CTkLabel(self, text="空裝白值", font=("Arial", 16))
        step1_label.place(x=160-16*6,y=20)

        Entry1 = ctk.CTkEntry(self,width=16*4,textvariable=self.watk)
        Entry1.insert(0, f"{self.config['var'][f'ent1']}")
        Entry1.place(x=160-16*6,y=45)

        step1_label2 = ctk.CTkLabel(self, text="空裝黃值", font=("Arial", 16))
        step1_label2.place(x=160+16*2,y=20)

        Entry2 = ctk.CTkEntry(self,width=16*4,textvariable=self.yatk)
        Entry2.insert(0, f"{self.config['var'][f'ent2']}")
        Entry2.place(x=160+16*2,y=45)


        open_file_button = ctk.CTkButton(self, text="武器", command=self.arms, font=("Arial", 16))
        open_file_button.place(x=160-16*4,y=85)


        yadd=35

        dev1 = ctk.CTkButton(self, text="生骸1", command=lambda:self.dev(1), font=("Arial", 16))
        dev1.place(x=160-16*4,y=85+yadd)

        dev2 = ctk.CTkButton(self, text="生骸2", command=lambda:self.dev(2), font=("Arial", 16))
        dev2.place(x=160-16*4,y=85+yadd*2)

        dev3 = ctk.CTkButton(self, text="生骸3", command=lambda:self.dev(3), font=("Arial", 16))
        dev3.place(x=160-16*4,y=85+yadd*3)

        dev4 = ctk.CTkButton(self, text="生骸4", command=lambda:self.dev(4), font=("Arial", 16))
        dev4.place(x=160-16*4,y=85+yadd*4)

        dev5 = ctk.CTkButton(self, text="生骸5", command=lambda:self.dev(5), font=("Arial", 16))
        dev5.place(x=160-16*4,y=85+yadd*5)

        lv = ctk.CTkButton(self, text='等級設定', command=self.rank,font=("Arial", 16))
        lv.place(x=160-16*4,y=85+yadd*6)

        ex1 = ctk.CTkButton(self, text='傷害加深', command=self.exception2,font=("Arial", 16))
        ex1.place(x=160-16*4,y=85+yadd*7)

        ex2 = ctk.CTkButton(self, text='額外設定', command=self.exception,font=("Arial", 16))
        ex2.place(x=160-16*4,y=85+yadd*8)

        skill = ctk.CTkButton(self, text='招式傷害%', command=self.skill,font=("Arial", 16))
        skill.place(x=160-16*4,y=85+yadd*9)

        btn2 = ctk.CTkButton(self, text='詳細面板', command=self.show2,font=("Arial", 16))
        btn2.place(x=160-16*4,y=85+yadd*10)

        btn3 = ctk.CTkButton(self, text='聲骸面板', command=self.devshow,font=("Arial", 16))
        btn3.place(x=160-16*4,y=85+yadd*11)

        btn1 = ctk.CTkButton(self, text='顯示', command=self.show,font=("Arial", 16))
        btn1.place(x=160-16*4,y=85+yadd*12)

        label = ctk.CTkLabel(self, textvariable=self.allatk,font=("Arial", 16),justify=ctk.LEFT)
        label.place(x=320,y=20)

        label2 = ctk.CTkLabel(self, textvariable=self.allatk2,font=("Arial", 16),justify=ctk.LEFT)
        label2.place(x=500,y=56)

    def loop(self,app):
        self.app=app
        self.mainloop()

    def show(self):
        self.geometry("675x575")
        self.config.set('var',f'ent1',f'{self.watk.get()}')
        self.config.set('var',f'ent2',f'{self.yatk.get()}')

        with open(f'{path}/calculate/base.ini', 'w',encoding="utf-8") as configfile:
            self.config.write(configfile)
        a,b=allcalculate()
        self.allatk.set(a)
        self.allatk2.set(b)

    def arms(self):
        app2 = Ui2(app=self.app)
        app2.loop()

    def dev(self,var):
        app3 = Ui3(var=var,app=self.app)
        app3.loop()

    def rank(self):
        app4 = Ui4(app=self.app)
        app4.loop()
    
    def exception(self):
        app5 = Ui5(app=self.app)
        app5.loop()

    def exception2(self):
        app5 = Ui6(app=self.app)
        app5.loop()

    def skill(self):
        app6 = Ui7(app=self.app)
        app6.loop()

    def show2(self):
        app2 = Ui8()
        app2.loop()

    def devshow(self):
        app2 = Ui9()
        app2.loop()


def main():
    app = Ui()
    app.loop(app=app)


if __name__ == '__main__':
    main()

#python -m nuitka --standalone --show-memory --windows-disable-console --show-progress --mingw64 --output-dir=E:/nuitkaoutput main.py --windows-uac-admin --plugin-enable=upx --upx-binary=D:\vscpy\bdo\output\upx\upx.exe --remove-output --follow-imports --plugin-enable=tk-inter

