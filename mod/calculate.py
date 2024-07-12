import os
from .groceries import rini

path=os.getcwd()

def allcalculate():
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
    
    exception = rini(f'{path}/calculate/exception.ini') #額外
    
    attri+=float(exception['var']['屬性加成'])
    varlist=exception.options('var')
    for i in devstatedict:
        if i in varlist:
            devstatedict[i]+=float(exception['var'][i])


    base = rini(f'{path}/calculate/base.ini')#基礎

    watk=int(base['var']['ent1'])#空裝白值
    yatk=int(base['var']['ent2'])#空裝黃值

    base = rini(f'{path}/calculate/arms.ini') #武器
    

    for i in range(1,6):
        var1=base['var'][f'top{i}']
        var2=base['var'][f'ent{i}']
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


    returntxt=''

    exception2 = rini(f'{path}/calculate/exception2.ini') #額外加成

    for i in ['全傷害加深%','屬性傷害加深%','共鳴技能加深%','共鳴解放加深%','普通攻擊加深%','重擊加深%']:
        if float(exception2['var'][i])>0:
            exception2.set('var',i,f"{1+float(exception2['var'][i])/100}")
        else:
            exception2.set('var',i,f"{0}")


    level = rini(f'{path}/calculate/rank.ini')#等差減傷

    rdamage=(100+int(level['var']['rank1']))/(199+int(level['var']['rank1'])+int(level['var']['rank2']))#等差減傷
    returntxt+=f"人物等級:{int(level['var']['rank1'])}        怪物等級:{int(level['var']['rank2'])}\n\n"
    returntxt+=f'等差減傷:{rdamage}\n\n'
    returntxt+=f"怪物抗性:{int(exception['var']['怪物抗性'])}%\n\n"
    baseatk=watk*(1+devstatedict['攻擊傷害%']/100)+devstatedict['攻擊點傷']+yatk
    returntxt+=f'面板攻擊:{int(baseatk)}\n\n'
    returntxt+=f"暴擊機率:{devstatedict['暴擊%']}\n\n"
    returntxt+=f"暴擊傷害:{devstatedict['暴傷%']}\n\n"

    config = rini(f'{path}/calculate/skill.ini')

    skillpercent=float(config['var']['招式傷害%'])
    skillpercent2=float(config['var']['重擊招式傷害%'])
    skillpercent3=float(config['var']['共鳴招式傷害%'])
    skillpercent4=float(config['var']['共鳴解放招式傷害%'])

    returntxt+='無暴擊\n'

    morecal=emorecal(float(devstatedict['普通攻擊傷害%']),attri)

    nbaseatk=baseatk*(1+morecal)*rdamage*(1+float(exception2['var']['全傷害加深%'])+float(exception2['var']['屬性傷害加深%'])+float(exception2['var']['普通攻擊加深%']))
    returntxt+=etxt('普通攻擊',nbaseatk,skillpercent,int(exception['var']['怪物抗性']))


    morecal=emorecal(float(devstatedict['重擊傷害%']),attri)

    nbaseatk2=baseatk*(1+morecal)*rdamage*(1+float(exception2['var']['全傷害加深%'])+float(exception2['var']['屬性傷害加深%'])+float(exception2['var']['重擊加深%']))
    returntxt+=etxt('重擊',nbaseatk2,skillpercent2,int(exception['var']['怪物抗性']))


    morecal=emorecal(float(devstatedict['共鳴技能加成%']),attri)

    nbaseatk3=baseatk*(1+morecal)*rdamage*(1+float(exception2['var']['全傷害加深%'])+float(exception2['var']['屬性傷害加深%'])+float(exception2['var']['共鳴技能加深%']))
    returntxt+=etxt('e',nbaseatk3,skillpercent3,int(exception['var']['怪物抗性']))


    morecal=emorecal(float(devstatedict['共鳴解放加成%']),attri)

    nbaseatk4=baseatk*(1+morecal)*rdamage*(1+float(exception2['var']['全傷害加深%'])+float(exception2['var']['屬性傷害加深%'])+float(exception2['var']['共鳴解放加深%']))
    returntxt+=etxt('r',nbaseatk4,skillpercent4,int(exception['var']['怪物抗性']))

    if devstatedict['暴擊%']>100:
        devstatedict['暴擊%']=100

    returntxt2='\n'*8+f"等效傷害:{round(devstatedict['暴傷%']*devstatedict['暴擊%']/100+100*(1-devstatedict['暴擊%']/100), 5)}%\n\n"
    returntxt2+='暴擊\n'

    returntxt2+=eptxt('普通攻擊',nbaseatk,skillpercent,devstatedict["暴傷%"],int(exception['var']['怪物抗性']))
    returntxt2+=eptxt('重擊',nbaseatk2,skillpercent2,devstatedict["暴傷%"],int(exception['var']['怪物抗性']))
    returntxt2+=eptxt('e',nbaseatk3,skillpercent3,devstatedict["暴傷%"],int(exception['var']['怪物抗性']))
    returntxt2+=eptxt('r',nbaseatk4,skillpercent4,devstatedict["暴傷%"],int(exception['var']['怪物抗性']))

    return  returntxt,returntxt2


def emorecal(var1,var2):
    morecal=var1+var2
    if morecal!=0:
        morecal/=100
    return morecal

def etxt(a,var1,var2,var3):
    resi=1-var3/100
    txt=''
    txt+=f'{a}:{int(var1*resi*var2/100)}\n'

    return txt

def eptxt(a,var1,var2,var3,var4):
    resi=1-var4/100
    txt=''
    txt+=f'{a}:{int(var1*resi*var2/100*var3/100)}\n'

    return txt



