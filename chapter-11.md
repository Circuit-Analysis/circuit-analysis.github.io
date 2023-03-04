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

## Capacitors

### Physical Characteristics

\begin{equation}
Q=VC
\end{equation}
Elastance (D=1/C) unit: Daraf $F^{-1}$

### Equivalent Capacitance: Series

Two elements connected in series share one node **exclusively**.

```{figure} logo.png
---
height: 300px
name: LABEL_0
---
```

When two capacitors are in series they can be redrawn as a single capcitor

```{figure} logo.png
---
height: 300px
name: LABEL_1
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

### Equivalent Capacitance: Parallel

Two elements are in parallel when they are connected to the same two nodes.

```{figure} logo.png
---
height: 300px
name: LABEL_2
---
```

When two capacitors are in parallel they can be redrawn as a single capacitor

```{figure} logo.png
---
height: 300px
name: LABEL_3
---
```

### Voltage/Current Relationship

All of circuit analysis can be related back to the three fundamental laws: KVL, KCL, and Ohm's Law. As new passive components are introduced we must reconsider the relationship between voltage and current. The capacitor equation takes the place of Ohm's law.

We can start with the charge equation introduced earlier and restated here as a time-domain function.
\begin{equation}
q(t)=Cv(t)
\end{equation}
taking the derivative of both sides leads to
\begin{equation}
\frac{dq(t)}{dt}=C\frac{dv(t)}{dt}
\end{equation}
Recall from the section on fundamentals the the time derivative of charge is current, $i(t)=\frac{dq(t)}{dt}$, alternatively stated as the flow rate of charge. Therefore the derivative form of the capacitor equation can be stated as
\begin{equation}
i(t)=C\frac{dv(t)}{dt}
\end{equation}
An alternate form of the equation is used often. Taking the integral of each side of the derivative form results in the integral form of the capacitor equation:
\begin{equation}
v(t)=\frac{1}{C}\int\_{t_0}^t i(\tau)d\tau + v(t_0)
\end{equation}

For capacitors, these two forms of the capacitor equation take the place of Ohm's Law in the methods of analysis previously introduced.

### A Realistic Capacitor Model

## Inductors

### Physical Characteristics

Reluctance ($\mathcal{R}$=1/L) unit: Inverse Henry $H^{-1}$

### Equivalent Inductance: Series

Two elements connected in series share one node **exclusively**.

```{figure} logo.png
---
height: 300px
name: LABEL_4
---
```

When two inductors are in series they can be redrawn as a single inductor

```{figure} logo.png
---
height: 300px
name: LABEL_5
---
```

### Equivalent Inductance: Parallel

Two elements are in parallel when they are connected to the same two nodes.

```{figure} logo.png
---
height: 300px
name: LABEL_6
---
```

When two inductors are in parallel they can be redrawn as a single inductor

```{figure} logo.png
---
height: 300px
name: LABEL_7
---
```

The reluctances add. Recall that

$$ \mathcal{R}=\frac{1}{L} $$

so

$$ \frac{1}{L_P}=\frac{1}{L_1}+\frac{1}{L_2} $$

Solving for $L_P$ and adding additional inductors

$$ L_P=\frac{1}{\frac{1}{L_1}+\frac{1}{L_2}+\dots+\frac{1}{L_N}} $$

The value of two inductors in parallel is commonly expressed as

$$ L_P=\frac{L_1L_2}{L_1+L_2} $$

### Voltage/Current Relationship

The derivative form of the inductor equation can be stated as
\begin{equation}
v(t)=L\frac{di(t)}{dt}
\end{equation}
An alternate form of the equation is used often. Taking the integral of each side of the derivative form results in the integral form of the inductor equation:
\begin{equation}
i(t)=\frac{1}{L}\int\_{t_0}^t v(\tau)d\tau + i(t_0)
\end{equation}

For inductors, these two forms of the inductor equation take the place of Ohm's Law in the methods of analysis previously introduced.

### A Realistic Inductor Model

## Next Steps: Analyzing Circuits with Reactive Components

Both the capacitor and inductor equations result in systems of equations that require knowledge of differential equations. We can approach this type of circuit analysis in two ways: 1) head-on by solving the systems of differential equations or 2) restating the equations using something called a phasor and solving it algebraically. Both approaches are presented here. I encourage you to read both sections if you have studied differential equations. You can skip the next section and proceed the section on phasors if you have not .
