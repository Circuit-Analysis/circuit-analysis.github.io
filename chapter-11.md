---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

(content:chapter:otherpassivecomponents)=

```{include} includes/latex_imports.md
```
```{code-cell} ipython3
:tags: [remove-input, remove-output]
:load: includes/python_imports.py
```

# Other Passive Components

So far, we've only looked at resistors as passive components.  Now, we introduce [capacitors](content:section:capacitors) and [inductors](content:section:inductors).

(content:section:capacitors)=
## Capacitors
```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='one-capacitor.svg') as d:
    d += elm.Capacitor().label(['-', 'V', '+']).label('C', loc='bot')
```

A capacitor is a device that stores charge. Supercapacitors are sometimes used as a short-term replacement for batteries ({cite:ts}`supercapacitors_mitre`).

### Physical Characteristics

```{index} Capacitance
```

```{index} Elastance
```

The relationship between the voltage across a capacitor and the charge stored by the capacitor is

$$ Q=VC $$

where $Q$ is the charge measured in coulombs, $V$ is the applied voltage measured in volts, and $C$ is the capacitance of the capacitor measured in Farads.

```{figure} one-capacitor.svg
---
height: 250px
name: one-capacitor
---
Schematic representation of a capacitor. 
```

Just like resistance has an inverse quantity of conductance, capacitance has an inverse quantity of elastance.

```{list-table} Capacitor Units
:name: table-capacitor-units
:header-rows: 1

* - Quantity
  - Unit
  - Abbreviation
  - Variable
* - Charge
  - Coulomb
  - C
  - $Q,q$
* - Voltage
  - Volt
  - V
  - $V,v$
* - Capacitance
  - Farad
  - F
  - $C$
* - Elastance
  - Daraf
  - F$^{-1}$
  - $D$
```



### Equivalent Capacitance: Series

```{code-cell} ipython3
:tags: [remove-input, remove-output]
with schemdraw.Drawing(file='series-capacitors.svg') as d:
    d += elm.Capacitor().label('$C_1$')
    d += elm.Capacitor().label('$C_2$')

with schemdraw.Drawing(file='series-capacitors-equivalent.svg') as d:
    d += elm.Capacitor().label('$D_1 + D_2$')    

with schemdraw.Drawing(file='capacitors-parallel.svg') as d:
    d += elm.Capacitor().label('$C_1$').up()
    d += elm.Line().right()
    d += elm.Capacitor().label('$C_2$').down()
    d += elm.Line().left()        

with schemdraw.Drawing(file='parallel-capacitors-equivalent.svg') as d:
    d += elm.Capacitor().label('$C_1 + C_2$')    

```

Two elements connected in series share one node **exclusively**.

```{figure} series-capacitors.svg
---
height: 300px
name: series-capacitors
---
```

When two capacitors are in series they can be redrawn as a single capacitor.

```{figure} series-capacitors-equivalent.svg
---
height: 300px
name: series-capacitors-equivalent
---
```

The elastances add. Recall that

$$ D=\frac{1}{C} $$

so

$$ \frac{1}{C_S}=\frac{1}{C_1}+\frac{1}{C_2} $$

Solving for $C_S$ and adding additional capacitors

$$ C_S=\frac{1}{\frac{1}{C_1}+\frac{1}{C_2}+\dots+\frac{1}{C_N}} $$

The value of two capacitors in series is commonly expressed as

$$ C_S=\frac{C_1C_2}{C_1+C_2} $$

which is similar to the way the equivalent resistors of resistors in *parallel* is calculated {eq}`resistors-in-parallel`.

### Equivalent Capacitance: Parallel

Two elements are in parallel when they are connected to the same two nodes.

```{figure} capacitors-parallel.svg
---
height: 300px
name: capacitors-parallel
---
```

When two capacitors are in parallel they can be redrawn as a single capacitor

```{figure} parallel-capacitors-equivalent.svg
---
height: 300px
name: parallel-capacitors-equivalent
---
```

### Voltage/Current Relationship

All of circuit analysis can be related back to the three fundamental laws: KVL, KCL, and Ohm's Law. As new passive components are introduced we must reconsider the relationship between voltage and current. The capacitor equation takes the place of Ohm's law.

We can start with the charge equation introduced earlier and restated here as a time-domain function.

$$ q(t)=Cv(t) $$

taking the derivative of both sides leads to

$$ \frac{dq(t)}{dt}=C\frac{dv(t)}{dt} $$

Recall from the section on fundamentals the the time derivative of charge is current, $i(t)=\frac{dq(t)}{dt}$, alternatively stated as the flow rate of charge. Therefore the derivative form of the capacitor equation can be stated as

$$ i(t)=C\frac{dv(t)}{dt}$$

An alternate form of the equation is used often. Taking the integral of each side of the derivative form results in the integral form of the capacitor equation:

$$ v(t)=\frac{1}{C}\int_{t_0}^t i(\tau)d\tau + v(t_0)$$

For capacitors, these two forms of the capacitor equation take the place of Ohm's Law in the methods of analysis previously introduced.

### Capacitor Impedance for Alternating Current Circuits


(content:section:inductors)=
## Inductors

```{index} Inductance
```

```{index} Reluctance
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]
with schemdraw.Drawing(file='one-inductor.svg') as d:
    d += elm.Inductor().label(['-', 'V', '+']).label('L', loc='bot')
with schemdraw.Drawing(file='series-inductors.svg') as d:
    d += elm.Inductor().label('$L_1$')
    d += elm.Inductor().label('$L_2$')
with schemdraw.Drawing(file='series-inductors-equivalent.svg') as d:
    d += elm.Inductor().label(['-', 'V', '+']).label('$L_1 + L_2$', loc='bot')
with schemdraw.Drawing(file='inductors-parallel.svg') as d:
    d += elm.Inductor().label('$L_1$').up()
    d += elm.Line().right()
    d += elm.Inductor().label('$L_2$').down()
    d += elm.Line().left()    
with schemdraw.Drawing(file='parallel-inductors-equivalent.svg') as d:
    d += elm.Inductor().label('$\cal{R}$$_1$ + $\cal{R}$$_2$', loc='bot')
```

An inductor is a device that stores energy in magnetic flux.

### Physical Characteristics

The relationship between the current through an inductor and the magnetic flux in the inductor is

$$ \phi = L I $$

where $\phi$ is the flux measured in webers, $I$ is the current measured in amperes, and $L$ is the inductance of the inductor measured in Henries ({cite:ts}`stackexchange_current_flux`).

```{figure} one-inductor.svg
---
height: 250px
name: one-inductor
---
Schematic representation of an inductor. 
```

Just like resistance has an inverse quantity of conductance, inductance has an inverse quantity of reluctance.

```{list-table} Inductor Units
:name: table-inductor-units
:header-rows: 1

* - Quantity
  - Unit
  - Abbreviation
  - Variable
* - Flux
  - Weber
  - W
  - $\phi$
* - Current
  - Ampere
  - A
  - $I,i$
* - Inductance
  - Henry
  - H
  - $L$
* - Reluctance
  - Inverse Henry
  - H$^{-1}$
  - $\cal{R}$
```


### Equivalent Inductance: Series

Two elements connected in series share one node **exclusively**.

```{figure} series-inductors.svg
---
height: 300px
name: series-inductors
---
```

When two inductors are in series they can be redrawn as a single inductor

```{figure} series-inductors-equivalent.svg
---
height: 300px
name: series-inductors-equivalent
---
```

### Equivalent Inductance: Parallel

Two elements are in parallel when they are connected to the same two nodes.

```{figure} inductors-parallel.svg
---
height: 300px
name: inductors-parallel
---
```

When two inductors are in parallel they can be redrawn as a single inductor

```{figure} parallel-inductors-equivalent.svg
---
height: 300px
name: parallel-inductors-equivalent
---
```

The *reluctances* add. Recall that

$$ \mathcal{R}=\frac{1}{L} $$

so

$$ \frac{1}{L_P}=\frac{1}{L_1}+\frac{1}{L_2} $$

Solving for $L_P$ and adding additional inductors

$$ L_P=\frac{1}{\frac{1}{L_1}+\frac{1}{L_2}+\dots+\frac{1}{L_N}} $$

The value of two inductors in parallel is commonly expressed as

$$ L_P=\frac{L_1L_2}{L_1+L_2} $$

### Voltage/Current Relationship

The derivative form of the inductor equation can be stated as

$$ v(t)=L\frac{di(t)}{dt}$$

An alternate form of the equation is used often. Taking the integral of each side of the derivative form results in the integral form of the inductor equation:

$$ i(t)=\frac{1}{L}\int_{t_0}^t v(\tau)d\tau + i(t_0)$$

For inductors, these two forms of the inductor equation take the place of Ohm's Law in the methods of analysis previously introduced.

### Inductor Impedance for Alternating Current Circuits


## Realistic Models of Passive Components

### A Realistic Resistor Model
### A Realistic Capacitor Model

### A Realistic Inductor Model

## Next Steps: Analyzing Circuits with Reactive Components

Both the capacitor and inductor equations result in systems of equations that require knowledge of differential equations. We can approach this type of circuit analysis in two ways: 1) head-on by solving the systems of differential equations or 2) restating the equations using something called a phasor and solving it algebraically. Both approaches are presented here. I encourage you to read both sections if you have studied differential equations. You can skip the next section and proceed the section on phasors if you have not .

## References

```{bibliography} ./references.bib
:filter: docname in docnames
```
