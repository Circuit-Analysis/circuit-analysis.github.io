from manim import *

import matplotlib
import schemdraw
import schemdraw.elements as elm

import os.path


matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


class Capacitor(SVGMobject):
    def __init__(self):
        if (not os.path.exists('capacitor.svg')):
            with schemdraw.Drawing(file='capacitor.svg', show=False) as d:
                d += elm.Capacitor().label('Capacitor').color('white')

        super().__init__('capacitor.svg')


class Resistor(SVGMobject):
    def __init__(self):
        if (not os.path.exists('resistor.svg')):
            with schemdraw.Drawing(file='resistor.svg', show=False) as d:
                d += elm.Resistor().label('Resistor').color('white')

        super().__init__('resistor.svg')


class Inductor(SVGMobject):
    def __init__(self):
        if (not os.path.exists('inductor.svg')):
            with schemdraw.Drawing(file='inductor.svg', show=False) as d:
                d += elm.Inductor().label('Inductor').color('white')

        super().__init__('inductor.svg')


class VoltageSource(SVGMobject):
    def __init__(self):
        if (not os.path.exists('voltage_source.svg')):
            with schemdraw.Drawing(file='voltage_source.svg', show=False) as d:
                d += elm.SourceV().label('Voltage Source').color('white').right()

        super().__init__('voltage_source.svg')


class DependentVoltageSource(SVGMobject):
    def __init__(self):
        if (not os.path.exists('dependent_voltage_source.svg')):
            with schemdraw.Drawing(file='dependent_voltage_source.svg', show=False) as d:
                d += elm.SourceControlledV().label('Dependent Voltage Source').color('white').right()

        super().__init__('dependent_voltage_source.svg')


class CurrentSource(SVGMobject):
    def __init__(self):
        if (not os.path.exists('current_source.svg')):
            with schemdraw.Drawing(file='current_source.svg', show=False) as d:
                d += elm.SourceI().label('Current Source').color('white').right()

        super().__init__('current_source.svg')


class DependentCurrentSource(SVGMobject):
    def __init__(self):
        if (not os.path.exists('dependent_current_source.svg')):
            with schemdraw.Drawing(file='dependent_current_source.svg', show=False) as d:
                d += elm.SourceControlledI().label('Dependent Current Source').color('white').right()

        super().__init__('dependent_current_source.svg')


class Grounds(SVGMobject):
    def __init__(self):
        if (not os.path.exists('grounds.svg')):
            with schemdraw.Drawing(file='grounds.svg', show=False) as d:
                d += elm.Ground().label('Ground').color('white')
                d.move(4, 0)
                d += elm.GroundSignal().label('Signal Ground').color('white')
                d.move(4, 0)
                d += elm.GroundChassis().label('Chassis Ground').color('white')

        super().__init__('grounds.svg')


class DefaultTemplate(Scene):
    def construct(self):

        resistor = Resistor()
        resistor2 = Resistor()
        resistor2.set_color(DARK_BLUE)

        self.fly_in(resistor, resistor2)

        capacitor = Capacitor()
        capacitor2 = Capacitor()
        capacitor2.set_color(DARK_BLUE)

        self.fly_in(capacitor, capacitor2)

        inductor = Inductor()
        inductor2 = Inductor()
        inductor2.set_color(DARK_BLUE)

        self.fly_in(inductor, inductor2)

        voltage = VoltageSource()
        voltage2 = VoltageSource()
        voltage2.set_color(DARK_BLUE)

        self.fly_in(voltage, voltage2)

        current = CurrentSource()
        current2 = CurrentSource()
        current2.set_color(DARK_BLUE)

        self.fly_in(current, current2)

        dependent_voltage = DependentVoltageSource()
        dependent_voltage2 = DependentVoltageSource()
        dependent_voltage2.set_color(DARK_BLUE)

        self.fly_in(dependent_voltage, dependent_voltage2)

        dependent_current = DependentCurrentSource()
        dependent_current2 = DependentCurrentSource()
        dependent_current2.set_color(DARK_BLUE)

        self.fly_in(dependent_current, dependent_current2)

        grounds = Grounds()
        grounds2 = Grounds()
        grounds2.set_color(DARK_BLUE)

        self.fly_in(grounds, grounds2)

    def fly_in(self, in_object, out_object):
        self.play(FadeIn(in_object, shift=DOWN, scale=0.5), run_time=2)
        self.play(ReplacementTransform(in_object, out_object), run_time=2)
        self.play(FadeOut(out_object, shift=DOWN * 2, scale=2), run_time=2)
