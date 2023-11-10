import schemdraw.elements as elm
import schemdraw
import matplotlib
import random


matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

resistors_only = True

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
    d += get_component().up()
    d += get_component().left()
    d += get_component().left()
    d += elm.Line().up()
    d += get_component().right(6)
    d += elm.Line().down()
    d.pop()
    d += get_component().up()
    d.pop()
    d += get_component().up()
        



    #for i in range(1,6):
