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

label_by_type = { elm.Resistor: "R", elm.Capacitor: "C", elm.Inductor: "L",
                 elm.SourceI: "I", elm.SourceV: "V", elm.SourceControlledI: "I",
                 elm.SourceControlledV: "V"}


number_by_type = { elm.Resistor: 0, elm.Capacitor: 0, elm.Inductor: 0,
                 elm.SourceI: 0, elm.SourceV: 0, elm.SourceControlledI: 0,
                 elm.SourceControlledV: 0}

value_by_type = { elm.Resistor: [100,40000,100, "$\Omega$"], elm.Capacitor: [1,1000,1, "$\mu$ F"], elm.Inductor: [1,1000,1,"mH"],
                 elm.SourceI: [5,500,5,"mA"], elm.SourceV: [4,40,4,"V"], elm.SourceControlledI: [1,10,1,"V$_x$"],
                 elm.SourceControlledV: [1,20,1,"I$_x$"]}


def get_label(component, needs_vx):
    label = label_by_type[type(component)]
    number = number_by_type[type(component)] + 1
    number_by_type[type(component)] = number
    
    label = "$" + label + "_" + str(number) + "$"
    if component == needs_vx:
        label = ["-", label + "\n$V_x$", "+"] 

    return label

def get_value(component):
    data = value_by_type[type(component)]
    return str(random.choice(range(data[0],data[1],data[2]))) + data[3]

def choose_component_that_is_not_a_source(components):
    choice = random.choice(components)
    while (isinstance(choice, elm.SourceControlledV) or isinstance(choice, elm.SourceControlledI)
           or isinstance(choice, elm.SourceV) or isinstance(choice, elm.SourceI)):
        choice = random.choice(components)

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
CMP1 = get_component()
CMP2 = get_component()
CMP3 = get_component()
CMP4 = get_component()
CMP5 = get_component()
CMP6 = get_component()

components = [CMP1, CMP2, CMP3, CMP4, CMP5, CMP6]
vx_component = ""
if any(isinstance(x, elm.SourceControlledI) for x in components):
    vx_component = choose_component_that_is_not_a_source(components)
    

with schemdraw.Drawing(file='three_mesh.svg') as d:
    d.push()
    d += elm.Line().right()
    d.push()
    d += elm.Line().right()
    d += CMP1.up().label(get_label(CMP1, vx_component)).label(get_value(CMP1), loc='bottom')
    d += CMP2.left().label(get_label(CMP2, vx_component)).label(get_value(CMP2), loc='bottom')
    d += CMP3.left().label(get_label(CMP3, vx_component)).label(get_value(CMP3), loc='bottom')
    d += elm.Line().up()
    d += CMP4.right(6).label(get_label(CMP4, vx_component)).label(get_value(CMP4), loc='bottom')
    d += elm.Line().down()
    d.pop()
    d += CMP5.up().label(get_label(CMP5, vx_component)).label(get_value(CMP5), loc='bottom')
    d.pop()
    d += CMP6.up().label(get_label(CMP6, vx_component)).label(get_value(CMP6), loc='bottom')


    if any(isinstance(x, elm.SourceControlledV) for x in components):
        d += elm.CurrentLabelInline(direction='in').at(choose_component_that_is_not_a_source(components)).label('$I_x$')
    

