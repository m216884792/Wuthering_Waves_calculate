# coding=utf-8
import os
from .groceries import rini


path=os.getcwd()

def allcalculate():
    devstatedict={'攻擊傷害%':0,'攻擊點傷':0,'暴擊%':5,'暴傷%':150,
    '共鳴技能加成%':0,'共鳴解放加成%':0,
    '重擊傷害%':0,'普通攻擊傷害%':0,
    '生命':0,'生命%':100,'防禦':0,'防禦%':100,
    '共鳴效率':0,'屬性加成':0}
    
    exception = rini(f'{path}/calculate/exception.ini') #額外
    
    varlist=exception.options('var')
    for i in devstatedict:
        if i in varlist:
            devstatedict[i]+=float(exception['var'][i])


    arms = rini(f'{path}/calculate/arms.ini') #武器

    for i in range(1,6):
        var1=arms['var'][f'top{i}']
        var2=arms['var'][f'ent{i}']
        devstatedict[var1]+=float(var2)

    for i in range(1,6):
        dev = rini(f'{path}/calculate/dev{i}.ini') #聲骸

        fixed=dev['var']['fixed']
        if '4c' in fixed:
            devstatedict['攻擊點傷']+=150
            if '暴擊' in fixed:
                devstatedict['暴擊%']+=22
            elif '暴傷' in fixed:
                devstatedict['暴傷%']+=44
            elif '攻擊傷害' in fixed:
                devstatedict['攻擊傷害%']+=33
            elif '生命' in fixed:
                devstatedict['生命%']+=33
            elif '防禦' in fixed:
                devstatedict['防禦%']+=41.8

        elif '3c' in fixed:
            devstatedict['攻擊點傷']+=100
            if '屬性加成' in fixed:
                devstatedict['屬性加成']+=30
            elif '攻擊傷害' in fixed:
                devstatedict['攻擊傷害%']+=30
            elif '生命' in fixed:
                devstatedict['生命%']+=30
            elif '防禦' in fixed:
                devstatedict['防禦%']+=38
            elif '共鳴效率' in fixed:
                devstatedict['共鳴效率']+=32

        elif '1c' in fixed:
            devstatedict['生命']+=2280
            if '攻擊傷害' in fixed:
                devstatedict['攻擊傷害%']+=18
            elif '生命' in fixed:
                devstatedict['生命%']+=22.8
            elif '防禦' in fixed:
                devstatedict['防禦%']+=18
            


        for i2 in range(1,6):
            var1=dev['var'][f'top{i2}']
            var2=dev['var'][f'ent{i2}']
            
            devstatedict[var1]+=float(var2)


    exception2 = rini(f'{path}/calculate/exception2.ini') #額外加成

    for i in ['全傷害加深%','屬性傷害加深%','共鳴技能加深%','共鳴解放加深%','普通攻擊加深%','重擊加深%']:
        if float(exception2['var'][i])>0:
            exception2.set('var',i,f"{float(exception2['var'][i])/100}")
        else:
            exception2.set('var',i,"0")


    returntxt=''

    level = rini(f'{path}/calculate/rank.ini')#等差減傷
    base = rini(f'{path}/calculate/base.ini')#基礎
    returntxt+=f"人物等級:{int(level['var']['rank1'])}        怪物等級:{int(level['var']['rank2'])}\n\n"
    returntxt+=f"生命:{int(int(base['var']['ent3'])*devstatedict['生命%']/100+devstatedict['生命'])}"
    returntxt+=" "*9
    returntxt+=f"防禦:{int(int(base['var']['ent4'])*devstatedict['防禦%']/100+devstatedict['防禦'])} \n\n"


    rdamage=(100+int(level['var']['rank1']))/(199+int(level['var']['rank1'])+int(level['var']['rank2']))#等差減傷
    returntxt+=f'等差減傷:{rdamage}\n\n'

    returntxt+=f"怪物抗性:{int(exception['var']['怪物抗性'])}%\n\n"


    watk=int(base['var']['ent1'])#空裝白值
    yatk=int(base['var']['ent2'])#空裝黃值
    baseatk=watk*(1+devstatedict['攻擊傷害%']/100)+devstatedict['攻擊點傷']+yatk
    returntxt+=f'面板攻擊:{int(baseatk)}\n\n'

    returntxt+=f"共鳴效率:{100+devstatedict['共鳴效率']}%\n\n"

    if devstatedict['暴擊%']>100:
        devstatedict['暴擊%']=100

    returntxt+=f"暴擊機率:{devstatedict['暴擊%']}\n\n"
    returntxt+=f"暴擊傷害:{devstatedict['暴傷%']}\n\n"


    templist=['普通攻擊','重擊','e','r']

    skillini = rini(f'{path}/calculate/skill.ini')#招式傷害%'
    skilldcit={'普通攻擊':float(skillini['var']['招式傷害%']),
               '重擊':float(skillini['var']['重擊招式傷害%']),
               'e':float(skillini['var']['共鳴招式傷害%']),
               'r':float(skillini['var']['共鳴解放招式傷害%'])}

    tempdict={'普通攻擊':'普通攻擊傷害%','重擊':'重擊傷害%','e':'共鳴技能加成%','r':'共鳴解放加成%'}
    skillmoredict={'普通攻擊':'普通攻擊加深%','重擊':'重擊加深%','e':'共鳴技能加深%','r':'共鳴解放加深%'}
    baseskillatk={'普通攻擊':0,'重擊':0,'e':0,'r':0}

    returntxt+='無暴擊\n'

    for i in templist:
        morecal=emorecal(float(devstatedict[tempdict[i]]),devstatedict['屬性加成'])
        var1=baseatk*(1+morecal)*rdamage*(1+float(exception2['var']['全傷害加深%'])+float(exception2['var']['屬性傷害加深%'])+float(exception2['var'][skillmoredict[i]]))
        baseskillatk[i]=var1
        returntxt+=etxt(i,var1,skilldcit[i],int(exception['var']['怪物抗性']))


    returntxt2='\n'*(returntxt.count('\n')-11)
    returntxt2+=f"等效傷害:{round(devstatedict['暴傷%']*devstatedict['暴擊%']/100+100*(1-devstatedict['暴擊%']/100), 5)}%\n\n"
    returntxt2+='暴擊\n'

    for i in templist:
        returntxt2+=etxt(i,baseskillatk[i],skilldcit[i],int(exception['var']['怪物抗性']),devstatedict["暴傷%"])

    return  returntxt,returntxt2


def emorecal(var1,var2):
    morecal=var1+var2
    if morecal!=0:
        morecal/=100
    return morecal

def etxt(a,var1,var2,var3,var4=100):
    resi=1-var3/100
    txt=''
    txt+=f'{a}:{int(var1*resi*var2/100*var4/100)}\n'

    return txt


