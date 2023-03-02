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
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[voltage source,l_=v$_I$(t)] (0,0)
(0,3) to[R,lx={R and 1~k$\Omega$}] (3,3)
(3,3) to[L,lx={L and 100~mH},v=v$_O$(t)] (3,0)
(0,0) -- (3,0)
;
\end{circuitikz}
\end{center}
Find v$_O$(t) given that v$_I$(t)=4~cos(10000t+45$^\circ$)~V
\end{example}

### Current Divider

\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[current source,l^=i$_I$(t)] (0,3)
(3,0) to[R,lx={R and 500~$\Omega$}] (3,3)
(6,0) to[C,lx={C and 1~$\mu$F},i<=i$_O$(t)] (6,3)
(0,0) -- (6,0)
(0,3) -- (6,3)
;
\end{circuitikz}
\end{center}
Find i$_O$(t) given that i$_I$(t)=400~cos(1000t-30$^\circ$)~mA
\end{example}

### Mesh Analysis

\index{Mesh Analysis}
\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,5) to[voltage source,lx_={V$_S$ and 12$\angle$0$^\circ$~V}] (0,0)
(0,5) to[R,lx={R$_1$ and 4~$\Omega$}] (3,5)
(3,5) to[L,lx={L and j2~$\Omega$}] (6,5)
(6,0) to[current source,lx_={I$_S$ and 4$\angle$90$^\circ$~A}] (6,5)
(3,5) to[C,lx={C and -j4~$\Omega$}] (3,2.5)
(3,2.5) to[R,lx={R$_2$ and 2~$\Omega$},v=V$_O$] (3,0)
(0,0) -- (6,0)
;
\end{circuitikz}
\end{center}
\end{example}

### Nodal Analysis

\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[voltage source,lx_={V$_S$ and 6$\angle$0$^\circ$~V}] (0,0)
(0,3) to[L,lx={L and j2~$\Omega$}] (3,3)
(3,3) to[current source,lx_={I$_S$ and 4$\angle$45$^\circ$~A}] (3,0)
(3,3) to[C,lx={C and -j1~$\Omega$}] (6,3)
(6,3) to[R,lx={R$_2$ and 2~$\Omega$},v=V$_O$] (6,0)
(0,0) -- (6,0)
(3,0) node[sground,scale=0.5]{}
;
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) -- (0,3)
(0,3) to[R,lx={R$_1$ and 2~$\Omega$}] (3,3)
(3,0) to[R,lx={R$_2$ and 2~$\Omega$},i>=I$_O$] (3,3)
(6,0) to[R,lx={R$_3$ and 2~$\Omega$}] (6,3)
(3,0) to[L,lx={L and j2~$\Omega$}] (6,0)
(3,3) to[C,lx={C and -j2~$\Omega$}] (6,3)
(0,3) -- (0,5) to[voltage source,lx={V$_S$ and 12$\angle$0$^\circ$~V}] (6,5) -- (6,3)
(0,0) -- (3,0)
(3,0) node[sground,scale=0.5]{}
;
\end{circuitikz}
\end{center}
\end{example}

### Superposition

### Thevenin's Theorem

\index{Thevenin's Theorem}
\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[voltage source,lx_={V$_S$ and 50$\angle$30$^\circ$~V}] (0,0)
(0,3) to[L,lx={L and j20~$\Omega$}] (3,3)
(3,3) to[C,lx_={C and -j10~$\Omega$}] (3,0)
(3,3) to[R,lx={R and 10~$\Omega$},-o] (6,3) node[below]{A}
(0,0) to[short,-o] (6,0) node[above]{B}
;
\end{circuitikz}
\end{center}
Find the Thevenin equivalent of the circuit above.

\Solution
Find V\tss{OC} first. The load is already removed in this example so there is already an open circuit where the load will connect. Find the voltage across that open.
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[voltage source,lx_={V$_S$ and 50$\angle$30$^\circ$~V}] (0,0)
(0,3) to[L,lx={L and j20~$\Omega$},v=~] (3,3)
(3,3) to[C,lx={C and -j10~$\Omega$},v=~] (3,0)
(3,3) to[R,lx={R and 10~$\Omega$},-o] (6,3) node[below]{A}
(0,0) to[short,-o] (6,0) node[above]{B}
(6,2.7) to[open,v_=V\tss{OC}] (6,.3)
(1.5,1.5) node[red]{I}
;
\centerarc[red,->,thick](1.5,1.5)(225:-45:5mm)
\end{circuitikz}
\end{center}
We can find I using mesh analysis on the single mesh.  
 \[(50\angle{30^\circ}~V)-(j20~\Omega)I-(-j10~\Omega)I=0\]
so
\[I=\frac{(50\angle{30^\circ}~V)}{(j10~\Omega)}=(5\angle{-60^\circ}~A)\]
Using $I$ we can find the voltage across the inductor and capacitor
\[V*L=(5\angle{-60^\circ}~A)(j20~\Omega)=(100\angle{30^\circ}~V)\text{~and~}V_C=(5\angle{-60^\circ}~A)(-j10~\Omega)=(50\angle{-150^\circ}~V)\]
There is no current through the resistor since it is not part of a closed path. Therefore there is no voltage across it. We can label all of these voltage on the schematic
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[voltage source,lx*={V$_S$ and 50$\angle$30$^\circ$~V}] (0,0)
		(0,3) to[L,lx={L and j20~$\Omega$},v=100$\angle$30$^\circ$~V] (3,3)
		(3,3) to[C,lx={C and -j10~$\Omega$},v=50$\angle$-150$^\circ$~V] (3,0)
		(3,3) to[R,lx={R and 10~$\Omega$},v=0~V,-o] (6,3) node[below]{A}
		(0,0) to[short,-o] (6,0) node[above]{B}
		(6,2.7) to[open,v_=V\tss{OC}] (6,.3)
		;
		\end{circuitikz}
	\end{center}
	Now we can write a KVL that includes the unknown $V_{OC}$. I chose to move over the capacitor, resistor, and open since it is the shortest loop that included $V_{OC}$.
\[(50\angle{-150^\circ}~V)-(0~V)-V*{OC}=0\]
which reduces to
\[V*{OC}=50\angle{-150^\circ}~V=V*{TH}\]
which is the Thevenin voltage.
Next, we find Z\tss{TH}. There are no dependent supplies in this circuit so we can treat it as an equivalent impedance problem. This is method \#1 presented in the Thevenin section. Replace the voltage supply with its ideal impedance, a short.
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[short] (0,3)
(0,3) to[L,lx={L and j20~$\Omega$}] (3,3)
(3,3) to[C,lx={C and -j10~$\Omega$}] (3,0)
(3,3) to[R,lx={R and 10~$\Omega$},-o] (6,3) node[below]{A}
(0,0) to[short,-o] (6,0) node[above]{B}
(6,2.7) to[open,l=Z\tss{TH}] (6,.3)
;
\draw[-latex] (6,1.5) -- (5.5,1.5) ;
\end{circuitikz}
\end{center}
For this circuit
\[Z*{TH}=R+(L||C)=10-j20~\Omega\]
We can now draw the Thevenin equivalent circuit since we have both V\tss{TH} and Z\tss{TH}.
\begin{center}
\begin{circuitikz}[american]\draw
(2,3) to[voltage source,lx_={V\tss{TH} and 50$\angle${210$^\circ$}~V}] (2,0)
(2,3) to[european resistor,l=$10-j20~\Omega$,-o] (6,3) node[below]{A}
(2,0) to[short,-o] (6,0) node[above]{B}
(4,3.7) node[above]{Z\tss{TH}}
;
\end{circuitikz}
\end{center}

\end{example}

### Norton's Theorem

\index{Norton's Theorem}

### Source Conversions

\index{Source Conversions}
\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[voltage source,l=2+j2~V] (0,3)
(0,3) to[R,l=1~$\Omega$] (2,3)
(2,3) to[L,l=j1~$\Omega$] (4,3)
(4,3) to[voltage source,l=6$\angle$0$^\circ$~V] (6,3)
(9,3) to[C,l=-j1~$\Omega$] (9,0)
(6,3) to[R,l=1~$\Omega$,i=I$_O$] (6,0)
(6,3) to[R,l=1~$\Omega$] (9,3)
(0,0) -- (9,0)
;
\end{circuitikz}
\end{center}
Find $I_O$

\Solution
First, look for any impedances that are in series/parallel. The $1~\Omega$ resistor on the left and the $j1~\Omega$ inductor are in series. Also, the $1~\Omega$ resistor on the right and the $-j1~\Omega$ capacitor are in series. Both combinations are shown in the schematic below as a generic impedance. They appear as a box with an impedance label.

Second look for, voltage supplies in series or current supplies in parallel. In this case the two voltage supplies are in series. Their polarities match so they add together. Take a moment to practice these calculations either on your calculator or by hand.
\begin{center}
\begin{circuitikz}[american]\draw
(3,0) to[voltage source,l=8+j2~V] (3,3)
(3,3) to[european resistor,l=1+j1~\Om] (6,3)
(9,3) to[european resistor,l=1-j1~$\Omega$] (9,0)
(6,3) to[R,l=1~$\Omega$,i=I$_O$] (6,0)
(6,3) to[short] (9,3)
(3,0) -- (9,0)
;
\end{circuitikz}
\end{center}

No more impedances or sources can be comined yet. Now we consider if we can perform any source transformations. There are no current sources so there are no Norton equivalents to consider. There is a voltage source so we can consider whether it is a Thevenin equivalent. Does it have an impedance in series? Yes, the $1+j1~\Omega$ impdeance. Those two components can be transformed into a Norton equivalent and reconnected to the rest of the circuit as the load.
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[current source,l=5-j3~V] (0,3)
(3,0) to[european resistor,l=1+j1~\Om] (3,3)
(9,3) to[european resistor,l=1-j1~$\Omega$] (9,0)
(6,3) to[R,l=1~$\Omega$,i=I$_O$] (6,0)
(0,3) to[short] (9,3)
(0,0) -- (9,0)
;
\end{circuitikz}
\end{center}
Note that the current of the Norton equivalent is $(8+j2~V)/(1+j1~\Omega)$=$(5-j3~A)$

After the transformation we can again look for impedances in series/parallel, voltage sources in series, or current supplies in parallel. The $1+j1~\Omega$ and $1-j1~\Omega$ impedances are in parallel. They are not next to each other but they are connected to the same two nodes.
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[current source,l=5-j3~V] (0,3)
(3,0) to[european resistor,l=1~\Om] (3,3)
(6,3) to[R,l=1~$\Omega$,i=I$_O$] (6,0)
(0,3) to[short] (6,3)
(0,0) -- (6,0)
;
\end{circuitikz}
\end{center}
Those two impedances combine to a $1~\Omega$ impedance.

From this point we can use a simple current divider to find $I_O$.
\[I_O=(5-j3~A)\left[\frac{1}{1+1}\right]=2.5-j1.5~A=2.915\angle{-30.96^\circ}~A\]

\end{example}
