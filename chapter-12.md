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

(content:chapter:differentialequations)=

# Alternating Current: Differential Equation Approach

## Analysis Methods and Theorems with Alternating Current

### Voltage Divider

\index{Voltage Divider}
\begin{example}

```{figure} logo.png
---
height: 300px
name: LABEL_0
---
```

Find v$_O$(t) given that v$_I$(t)=4~cos(10000t+45$^\circ$)~V
\end{example}

### Current Divider

\begin{example}

```{figure} logo.png
---
height: 300px
name: LABEL_1
---
```

Find i$_O$(t) given that i$_I$(t)=400~cos(1000t-30$^\circ$)~mA
\end{example}

### Mesh Analysis

\index{Mesh Analysis}
\begin{example}

```{figure} logo.png
---
height: 300px
name: LABEL_2
---
```

\end{example}

### Nodal Analysis

\begin{example}

```{figure} logo.png
---
height: 300px
name: LABEL_3
---
```

\end{example}

\begin{example}

```{figure} logo.png
---
height: 300px
name: LABEL_4
---
```

\end{example}

### Superposition

### Thevenin's Theorem

\index{Thevenin's Theorem}
\begin{example}

```{figure} logo.png
---
height: 300px
name: LABEL_5
---
```

Find the Thevenin equivalent of the circuit above.

\Solution
Find V\tss{OC} first. The load is already removed in this example so there is already an open circuit where the load will connect. Find the voltage across that open.

```{figure} logo.png
---
height: 300px
name: LABEL_6
---
```

We can find I using mesh analysis on the single mesh.  
 \[(50\angle{30^\circ}~V)-(j20~\Omega)I-(-j10~\Omega)I=0\]
so
\[I=\frac{(50\angle{30^\circ}~V)}{(j10~\Omega)}=(5\angle{-60^\circ}~A)\]
Using $I$ we can find the voltage across the inductor and capacitor
\[V\*L=(5\angle{-60^\circ}~A)(j20~\Omega)=(100\angle{30^\circ}~V)\text{~and~}V_C=(5\angle{-60^\circ}~A)(-j10~\Omega)=(50\angle{-150^\circ}~V)\]
There is no current through the resistor since it is not part of a closed path. Therefore there is no voltage across it. We can label all of these voltage on the schematic

```{figure} logo.png
---
height: 300px
name: LABEL_7
---
```

    Now we can write a KVL that includes the unknown $V_{OC}$. I chose to move over the capacitor, resistor, and open since it is the shortest loop that included $V_{OC}$.

\[(50\angle{-150^\circ}~V)-(0~V)-V*{OC}=0\]
which reduces to
\[V*{OC}=50\angle{-150^\circ}~V=V\*{TH}\]
which is the Thevenin voltage.
Next, we find Z\tss{TH}. There are no dependent supplies in this circuit so we can treat it as an equivalent impedance problem. This is method \#1 presented in the Thevenin section. Replace the voltage supply with its ideal impedance, a short.

```{figure} logo.png
---
height: 300px
name: LABEL_8
---
```

For this circuit
\[Z\*{TH}=R+(L||C)=10-j20~\Omega\]
We can now draw the Thevenin equivalent circuit since we have both V\tss{TH} and Z\tss{TH}.

```{figure} logo.png
---
height: 300px
name: LABEL_9
---
```

\end{example}

### Norton's Theorem

\index{Norton's Theorem}

### Source Conversions

\index{Source Conversions}
\begin{example}

```{figure} logo.png
---
height: 300px
name: LABEL_10
---
```

Find $I_O$

\Solution
First, look for any impedances that are in series/parallel. The $1~\Omega$ resistor on the left and the $j1~\Omega$ inductor are in series. Also, the $1~\Omega$ resistor on the right and the $-j1~\Omega$ capacitor are in series. Both combinations are shown in the schematic below as a generic impedance. They appear as a box with an impedance label.

Second look for, voltage supplies in series or current supplies in parallel. In this case the two voltage supplies are in series. Their polarities match so they add together. Take a moment to practice these calculations either on your calculator or by hand.

```{figure} logo.png
---
height: 300px
name: LABEL_11
---
```

No more impedances or sources can be comined yet. Now we consider if we can perform any source transformations. There are no current sources so there are no Norton equivalents to consider. There is a voltage source so we can consider whether it is a Thevenin equivalent. Does it have an impedance in series? Yes, the $1+j1~\Omega$ impdeance. Those two components can be transformed into a Norton equivalent and reconnected to the rest of the circuit as the load.

```{figure} logo.png
---
height: 300px
name: LABEL_12
---
```

Note that the current of the Norton equivalent is $(8+j2~V)/(1+j1~\Omega)$=$(5-j3~A)$

After the transformation we can again look for impedances in series/parallel, voltage sources in series, or current supplies in parallel. The $1+j1~\Omega$ and $1-j1~\Omega$ impedances are in parallel. They are not next to each other but they are connected to the same two nodes.

```{figure} logo.png
---
height: 300px
name: LABEL_13
---
```

Those two impedances combine to a $1~\Omega$ impedance.

From this point we can use a simple current divider to find $I_O$.
\[I_O=(5-j3~A)\left[\frac{1}{1+1}\right]=2.5-j1.5~A=2.915\angle{-30.96^\circ}~A\]

\end{example}
