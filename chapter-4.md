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

# Dividers

Equivalent resistances and Ohm's law allows us to analyze to small, but important, circuits

## Voltage Divider

\index{Voltage Divider}
The voltage divider relates voltage across multiple resistors connected in series to the voltage across an individual resistor.
\begin{example}
\begin{center}\begin{circuitikz}[scale=.75]\draw
(0,6) to[battery,lx_={$V_{S}$ and 15~\text{V}}] (0,0)
(3,6) to[R,lx={$R_1$ and 10~k\Om},v=$V_{R_1}$] (3,3)
(3,3) to[R,lx={$R_2$ and 20~k\Om},v=$V_{R_2}$] (3,0)
(0,0) -- (3,0)
(0,6) to[short,i=$I$] (3,6)
;
\end{circuitikz}\end{center}
Find $V_{R_1}$ and $V_{R_2}$.

\Solution
Right now we are only equipped with Ohm's law and that ability to combine resistors when they are in parallel or series. $R_1$ and $R_2$ are connected in series in this circuit as they share a single node exclusively and carry the same current.
\begin{center}\begin{circuitikz}[scale=.75]\draw
(0,3) to[battery,lx_={$V_{S}$ and 15~\text{V}}] (0,0)
(3,3) to[R,lx={$R_{1+2}$ and 30~k\Om}] (3,0)
(0,0) -- (3,0)
(0,3) to[short,i=$I$] (3,3)
;
\end{circuitikz}\end{center}
With the combination of the resistors depicted above we have lost the node between the two resistors. We can't find the voltages across the two resistors as each of those voltages is measured using the node that disappeared between the resistors. However, we can find the current with a simple application of Ohm's law. Since the resistors were connected in series, the current we find from this redrawn circuit is equivalent to the current in the original circuit. $I$ is calculated as
\[I=\frac{V*S}{R_1+R_2}=\frac{15~\text{V}}{30~\text{k}\Omega}=500~\mu\text{A}\]
Since that current flows through each resistor the voltages can be calculated as
\[V*{R*1}=IR_1=(500~\mu\text{A})(10~\text{k}\Omega)=5~V~~\text{and}~~V*{R*2}=IR_2=(500~\mu\text{A})(20~\text{k}\Omega)=10~\text{V}\]
The voltage divider is typically written as a single equation that we can form by substituting the expression from our work above.
\[V*{R*1}=V_S\frac{R_1}{R_1+R_2}~~\text{and}~~V*{R_2}=V_S\frac{R_2}{R_1+R_2}\]
Notice that the two equations above look similar though the numerators are different. If we are calculating the voltage across $R_1$, then $R_1$ is in the numerator. Conversely, if we are calculating the voltage across $R_2$, then $R_2$ is in the numerator.
\end{example}

### Can I Apply the Voltage Divider?

Before you commit to using the voltage divider formula, ask yourself these questions:
\begin{itemize}
\item Are the two resistors really in series? Do they share a common node, just with each other?
\item Do I really know the voltage across the two series resistors?
\end{itemize}

## Current Divider

\index{Current Divider}
The current divider relates current into multiple branches connected in parallel to the current through an individual branch.
\begin{example}

\begin{center}\begin{circuitikz}[scale=.75]\draw
(0,0) to[current source,lx={$I_S$ and 3~\text{mA}}, v<=V] (0,3)
(3,0) to[R,lx={$R_1$ and 5~k\Om},i<=$I_{R_1}$] (3,3)
(6,0) to[R,lx={$R_2$ and 10~k\Om},i<=$I_{R_2}$] (6,3)
(0,0) -- (6,0)
(0,3) -- (6,3)
;
\end{circuitikz}\end{center}
Find $I_{R_1}$ and $I_{R_2}$.

\Solution
Right now we are only equipped with Ohm's law and that ability to combine resistors when they are in parallel or series. $R_1$ and $R_2$ are connected in parallel in this circuit as they share the same two nodes and have the same voltage, V, across each. We calculate the parallel combination as
\[R*{1\parallel 2}=\frac{R_1R_2}{R_1+R_2}\]
and we redraw the circuit as
\begin{center}\begin{circuitikz}[scale=.75]\draw
(0,0) to[current source,lx={$I_S$ and 3~\text{mA}}, v<=V] (0,3)
(3,0) to[R,lx*={$R_{1\parallel 2}$ and 3.33~k\Om}] (3,3)
(0,0) -- (3,0)
(0,3) -- (3,3)
;
\end{circuitikz}\end{center}
With the combination of the resistors depicted above we have lost the individual branches. We can't find the current through the individual branches. However, we can find the voltage with a simple application of Ohm's law. Since the resistors were connected in parallel the voltage we find from this redrawn circuit is equivalent to the voltage in the original circuit. $V$ is calculated as
\[V=I*SR*{1\parallel 2}=(3~\text{mA})(3.33~\text{k}\Omega)=10~\text{V}\]
Since that voltage is across each resistor the currents can be calculated as
\[I*{R_1}=\frac{V}{R_1}=\frac{10~\text{V}}{5~\text{k}\Omega}=2~\text{mA}~~\text{and}~~I*{R*2}=\frac{V}{R_2}=\frac{10~\text{V}}{10~\text{k}\Omega}=1~\text{mA}\]
The current divider is typically written as a single equation that we can form by substituting the expressions from our work above.
\[I*{R*1}=\frac{I_S}{R_1}\frac{R_1R_2}{R_1+R_2}~~\text{and}~~I*{R*2}=\frac{I_S}{R_2}\frac{R_1R_2}{R_1+R_2}\]
which reduce to
\[I*{R*1}=I_S\frac{R_2}{R_1+R_2}~~\text{and}~~I*{R_2}=I_S\frac{R_1}{R_1+R_2}\]
Notice that the two equations above look similar though the numerators are different. If we are calculating the current through $R_1$, then $R_2$ is in the numerator. Conversely, if we are calculating the voltage across $R_2$, then $R_1$ is in the numerator. This is the opposite of the voltage divider. Take some time to get this straight in your head to prevent making a simple error in the future.
\end{example}

### Can I Apply the Current Divider?

Before you commit to using the current divider formula, ask yourself these questions:
\begin{itemize}
\item Are the two resistors really in parallel? Do they connect the same two nodes electrically?
\item Do I really know the current flowing into the nodes where they connect?
\item Am I really dividing a current, not a voltage?
\end{itemize}

## A Look at Power

## Kirchhoff's Laws

### Kirchhoff's Voltage Law

The algebraic sum of voltages around a loop in a circuit is zero. {\bf Pay attention to the polarities.}
\begin{minipage}{0.5\textwidth}
\begin{center}\begin{circuitikz}[scale=.75]
\draw
(0,0) to[generic,v^>=$V_{AE}$ ] (0,6)
(0,6) node[above,left]{A}
(0,6) to[generic,v^<=$V_{AB}$ ] (6,6)
(6,6) node[above,right]{B}
(6,6) to[generic,v_<=$V_{BC}$ ] (6,3)
(6,3) node[right]{C}
(6,3) to[generic,v_<=$V_{CD}$ ] (6,0)
(6,0) node[below,right]{D}
(6,0) to[generic,v^<=$V_{DE}$ ] (0,0)
(0,0) node[left,below]{E}
(.5,4.5) to[open,v^=$V_{AD}$] (4.5,.5)
;
\end{circuitikz}\end{center}
\end{minipage}
\begin{minipage}{0.5\textwidth}
\vspace{3mm}
If we consider the voltages around the loop starting and ending at node E we can write a KVL equation for the loop:
\[V*{AE}-V*{AB}-V*{BC}-V*{CD}-V*{DE}=0\]
We can also consider voltages across two distant nodes in the circuit (A and D for this example) and write a KVL such as:
\[V*{AD}-V*{AB}-V*{BC}-V*{CD}=0\]
and rearrange it to find $V*{AD}$:
\[V*{AD}=V*{AB}+V*{BC}+V*{CD}\]
\end{minipage}

### Kirchhoff's Current Law

The algebraic sum of currents into a node in a circuit is zero. {\bf Pay attention to the direction of current flow.}

    	\begin{minipage}{0.5\textwidth}
    	\begin{center}\begin{circuitikz}[scale=.75]
    	\draw
    	(3,3) to[generic,i^<=$I_{1}$ ] (0,0)
    	(3,3) node[circle,fill]{}
    	(3,3) to[generic,i^<=$I_{2}$ ] (6,6)
    	(3,3) to[generic,i_<=$I_{3}$ ] (0,6)
    	(3,3) to[generic,i_<=$I_{4}$ ] (6,3)
    	(3,3) to[generic,i^>=$I_{5}$ ] (3,0)
    	;
    \end{circuitikz}\end{center}
    \end{minipage}
    \begin{minipage}{0.5\textwidth}
    \vspace{3mm}
    If we consider the currents flowing {\bf into} the central node we can write a KCL equation for that node:
    \[I_1 + I_2 + I_3 + I_4 - I_5 =0\]
    Note that $I_5$ is flowing {\sl out} of the node, so its sign is negative.
    \end{minipage}
