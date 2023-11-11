import schemdraw.elements as elm
import schemdraw
import matplotlib
import random


matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

resistors_only = False

def choose_active():
    return random.choice([elm.SourceV(), elm.SourceI(), elm.SourceControlledI(), elm.SourceControlledV()])

def choose_passive():
    if resistors_only:
        return elm.Resistor()
    else:
        return random.choice([elm.Resistor(), elm.Capacitor(), elm.Inductor()])

def choose_component():

    choice = random.choice(['A','P','P','P'])

    if choice == 'A':
        return choose_active()
    else:
        return choose_passive()
    
components_to_choose = [choose_active(), choose_component(), choose_component(), choose_component(), choose_component(), choose_component() ]

def get_component():
    choice = random.choice(components_to_choose)
    components_to_choose.remove(choice)
    return choice

def get_label(component):
    label_by_type = { elm.Resistor: "R", elm.Capacitor: "C", elm.Inductor: "L",
                 elm.SourceI: "I", elm.SourceV: "V", elm.SourceControlledI: "I",
                 elm.SourceControlledV: "V"}
    return label_by_type[type(component)]

# 
#  *---------[COMPONENT]-----------*
#  |                               |
#  |                               |
#  *--[COMPONENT]--*--[COMPONENT]--*
#  |               |               |
#  ^               ^               ^
# CMP             CMP             CMP
#  v               v               v
#  |               |               |
#  0---------------*---------------*
#

with schemdraw.Drawing(file='three_mesh.svg') as d:
    d.push()
    d += elm.Line().right()
    d.push()
    d += elm.Line().right()
    CMP1 = get_component()
    d += CMP1.up().label(get_label(CMP1) + "1")
    CMP2 = get_component()
    d += CMP2.left().label(get_label(CMP2) + "2")
    CMP3 = get_component()
    d += CMP3.left().label(get_label(CMP3) + "3")
    d += elm.Line().up()
    CMP4 = get_component()
    d += CMP4.right(6).label(get_label(CMP4) + "4")
    d += elm.Line().down()
    d.pop()
    CMP5 = get_component()
    d += CMP5.up().label(get_label(CMP5) + "5")
    d.pop()
    CMP6 = get_component()
    d += CMP6.up().label(get_label(CMP6) + "6")
        



    #for i in range(1,6):
