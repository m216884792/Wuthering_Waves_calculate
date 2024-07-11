import os
from configparser import ConfigParser


path=os.getcwd()

def arms_clear():
    wtext=''
    with open(f'{path}/calculate/arms.ini','w',encoding="utf-8") as text:

        wtext+=f'[var]\n'
        
        for i in range(1,6):
            wtext+=f'top{i} = 暴擊%% \n'
            wtext+=f'ent{i} = 0 \n'

        text.write(wtext)

def dev_clear(var):
    wtext=''
    with open(f'{path}/calculate/dev{var}.ini','w',encoding="utf-8") as text:

        wtext+=f'[var]\n'

        wtext+=f'fixed = 4c:暴擊22%% \n'
        for i in range(1,6):
            wtext+=f'top{i} = 暴擊%% \n'
            wtext+=f'ent{i} = 0 \n'

        text.write(wtext)

def rank_clear():
    wtext=''
    with open(f'{path}/calculate/rank.ini','w',encoding="utf-8") as text:

        wtext+=f'[var]\n'

        wtext+=f'rank1 = 0 \n'
        wtext+=f'rank2 = 0 \n'

        text.write(wtext)

def exception_clear():
    wtext=''
    with open(f'{path}/calculate/exception.ini','w',encoding="utf-8") as text:

        wtext+=f'[var]\n'

        for i in ['屬性加成','攻擊傷害%','暴擊%','暴傷%','共鳴技能加成%','共鳴解放加成%','普通攻擊傷害%','重擊傷害%']:
            wtext+=f'{i} = 0 \n'

        text.write(wtext)

def exception2_clear():
    wtext=''
    with open(f'{path}/calculate/exception2.ini','w',encoding="utf-8") as text:

        wtext+=f'[var]\n'

        for i in ['全傷害加深%','屬性傷害加深%','共鳴技能加深%','共鳴解放加深%','普通攻擊加深%','重擊加深%']:
            wtext+=f'{i} = 0 \n'

        text.write(wtext)

def skill_clear():
    wtext=''
    with open(f'{path}/calculate/skill.ini','w',encoding="utf-8") as text:

        wtext+=f'[var]\n'

        for i in ['招式傷害%','重擊招式傷害%','共鳴招式傷害%','共鳴解放招式傷害%']:
            wtext+=f'{i} = 0 \n'

        text.write(wtext)

def rini(path):
    config = ConfigParser()
    config.optionxform = str
    config.read(f'{path}',encoding="utf-8")
    return config
