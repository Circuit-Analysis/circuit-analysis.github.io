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

(content:chapter:equivalentcircuits)=

# Equivalent Circuits

For instance, we may know nothing about the analog input circuit of the microcontroller pictured below on the left. We know we can connect the ground pin to a circuit we want to connect to and the analog input to another node in that circuit at which we want to measure the voltage. Let's use the voltage divider pictured below on the right. Ideally, connecting the output of the voltage divider to the input of the microcontroller will not affect the voltage labeled $V_\text{OUT}$. We would like it to be 6~\text{V} as would be the case if nothing is connected to the voltage divider. Realistically, $V_\text{OUT}$ will be affected, but by how much?

\begin{minipage}{0.49\textwidth}
\begin{center}\begin{circuitikz}[decoration=snake]
\draw[ultra thick,black] (-2,-1) rectangle (2,4.5)
(-2,4.75) node[right]{Microcontroller}
(0,-1) to[short,*-*] (0,-1)
(0,-1) node[above]{GND}
(2,3) to[short,*-*] (2,3)
(2,3) node[left]{Analog Input}
;
\end{circuitikz}\end{center}
\end{minipage}
\begin{minipage}{0.49\textwidth}
\begin{center}\begin{circuitikz}[decoration=snake]
\draw
(0,0) to[R,l^=100~k\Om] (0,3) to[R,l^=100~k\Om] (0,6) to[short,-o] (0,6)
(0,0) node[sground,scale=0.5]{}
(0,6) node[right]{+12~\text{V}}
(0,3) to[short,-o] (1,3)
(1,3) node[right]{$V_\text{OUT}$}
;
\end{circuitikz}\end{center}
\end{minipage}

The two theorems that will help us answer this question, Thevenin's and Norton's theorems, are detailed in this chapter. I'll revisit this example as I introduce Thevenin's theorem in the next section.

## Thevenin's Theorem

\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[battery,l_=$V_{TH}$] (0,0)
(0,3) to[R,l=$R_{TH}$] (3,3)
(4,3) to[R,l=$R_{L}$] (4,0)
(3,3) -- (4,3)
(0,0) -- (4,0);
\draw[dashed,ultra thick,blue] (-2,-1) rectangle (3,4.5)
(-2,4) node[right]{Thevenin Equivalent};
\draw[->,decorate,ultra thick,blue]
(6.1,2.1) node[above]{Load} to[short] (5.1,1.5) ;
\end{circuitikz}\end{center}

### Thevenin Voltage

\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[battery,lx_={$V_S$ and 12~\text{V}}] (0,0)
(0,3) to[R,lx={$R_1$ and 3~\Om}] (3,3)
(3,3) to[R,lx={$R_2$ and 6~\Om}] (3,0)
(3,3) to[R,lx={$R_3$ and 5~\Om}] (6,3)
(7,3) to[R,l=$R_{L}$] (7,0)
(6,3) -- (7,3)
(0,0) -- (7,0);
\draw[dashed,ultra thick,blue] (-2,-1) rectangle (6,4.5)
(-2,4) node[right]{Fixed Circuit};
\draw[->,decorate,ultra thick,blue]
(8.8,2.1) node[above]{Load} to[short] (7.8,1.5) ;
\end{circuitikz}\end{center}

\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[battery,lx_={$V_S$ and 12~\text{V}}] (0,0)
(0,3) to[R,lx={$R_1$ and 3~\Om}] (3,3)
(3,3) to[R,lx={$R_2$ and 6~\Om}] (3,0)
(3,3) to[R,lx={$R_3$ and 5~\Om}] (6,3)
(6,3) to[open,v=$V_{OC}$] (6,0)
%(7,3) to[R,l=$R_{L}$] (7,0)
%(6,3) -- (7,3)
(0,0) -- (6,0);
%\draw[dashed,ultra thick,blue] (-2,-1) rectangle (6,4.5)
(%-2,4) node[right]{Fixed Circuit};
\draw[->,decorate,ultra thick,blue]
(7.8,2.1) node[above]{Load Removed} to[short] (6.8,1.5) ;
\end{circuitikz}\end{center}

### Thevenin Resistance: Three Methods

There are three methods to determine Thevenin resistance. All three will be demonstrated on the toy problem in this section but each has strengths and weaknesses. Careful attention should be paid to the limitations of each method.

\textbf{Method~\#1)~Equivalent Resistance:}\par
\begin{center}\fbox{\begin{minipage}{30em}
\underline{\textbf{Limitations:}}~ Circuit cannot have any \textbf{dependent} supplies.
\end{minipage}}\end{center}
\begin{enumerate}
\item Remove the load if it is not already removed.
\item Replace all supplies (they should all be independent) with their ideal resistances.
\item Find the equivalent resistance between the nodes where the load will be reconnected. That resistance is $R_{TH}$.
\end{enumerate}
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,0) to[short] (0,3)
(0,3) to[R,lx={$R_1$ and 3~\Om}] (3,3)
(3,3) to[R,lx={$R_2$ and 6~\Om}] (3,0)
(3,3) to[R,lx={$R_3$ and 5~\Om}] (6,3)
(6,3) to[open,l=$R_{TH}$] (6,0)
%(7,3) to[R,l=$R_{L}$] (7,0)
%(6,3) -- (7,3)
(0,0) -- (6,0);
%\draw[dashed,ultra thick,blue] (-2,-1) rectangle (6,4.5)
(%-2,4) node[right]{Fixed Circuit};
\draw[->,ultra thick,black]
(6.1,1.5) -- (5.5,1.5);
\draw[->,decorate,ultra thick,blue]
(8.1,2.1) node[above]{Load Removed} to[short] (7.1,1.5) ;

\draw[->,decorate,ultra thick,blue]
(-1.2,2.1) node[above]{$V_S$ Replaced} to[short] (-.2,1.5) ;
\end{circuitikz}\end{center}
\[ R\_{TH}=(R_1||R_2)+R_3=7~\Omega\]

\textbf{Method~\#2)~Open Circuit Voltage/Short Circuit Current:}\par
\begin{center}\fbox{\begin{minipage}{30em}
\underline{\textbf{Limitations:}}~Circuit must have one or more \textbf{independent} supplies.
\end{minipage}}\end{center}
\begin{enumerate}
\item Remove the load if it is not already removed.
\item Find the open circuit voltage ($V_{OC}$) between the nodes where the load will be reconnected.
\item Place a short between the nodes where the load will be reconnected.
\item Find the short circuit current ($I_{SC}$) through that short.
\item $R_{TH}$ is then $\sfrac{V_{OC}}{I_{SC}}$
\end{enumerate}

$V_{OC}$ was calculated in a previous section as 8~\text{V}. The load is then replaced with a short and the short-circuit current is calculated/measured.
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[battery,lx_={$V_S$ and 12~\text{V}}] (0,0)
(0,3) to[R,lx={$R_1$ and 3~\Om}] (3,3)
(3,3) to[R,lx={$R_2$ and 6~\Om}] (3,0)
(3,3) to[R,lx={$R_3$ and 5~\Om}] (6,3)
(6,3) to[short,i=$I_{SC}$] (6,0)
%(7,3) to[R,l=$R_{L}$] (7,0)
%(6,3) -- (7,3)
(0,0) -- (6,0);
%\draw[dashed,ultra thick,blue] (-2,-1) rectangle (6,4.5)
(%-2,4) node[right]{Fixed Circuit};
\draw[->,decorate,ultra thick,blue]
(7.8,2.1) node[above]{Load Replaced} to[short] (6.8,1.5) ;
\end{circuitikz}\end{center}

Use any method of analysis that you are confident in. I used mesh here:
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[battery,lx_={$V_S$ and 12~\text{V}}] (0,0)
(0,3) to[R,lx={$R_1$ and 3~\Om}] (3,3)
(3,3) to[R,lx={$R_2$ and 6~\Om}] (3,0)
(3,3) to[R,lx={$R_3$ and 5~\Om}] (6,3)
(6,3) to[short,i=$I_{SC}$] (6,0)
%(7,3) to[R,l=$R_{L}$] (7,0)
%(6,3) -- (7,3)
(0,0) -- (6,0);
\draw[red,->,thick] (1.2,1) arc (225:-45:4mm);
\draw[red,thick] (1.5,1) node[above]{$I_1$};
\draw[blue,->,thick] (4.4,1) arc (225:-45:4mm);
\draw[blue,thick] (4.7,1) node[above]{$I_2$};
\draw[->,decorate,ultra thick,blue]
(7.8,2.1) node[above]{Load Replaced} to[short] (6.8,1.5) ;
\end{circuitikz}\end{center}
\[ \left[ \begin{array}{cc}
9\Omega&-6\Omega\\
-6\Omega&11\Omega\\
\end{array} \right]^{-1}\left[\begin{array}{c}12V\\0V\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\end{array}\right]=\left[\begin{array}{c}2.095~\text{A}\\1.143~\text{A}\end{array}\right]\]
and $I_{SC}$=$I_2$ in this case leading to \[R*{TH}=\frac{V*{OC}}{I\_{SC}}=\frac{8~\text{V}}{1.143~\text{A}}=7~\Omega\]
First, note that this result is the same as the value calculated with the previous method. Second, note that the units of the formula above follow Ohm's Law.

\textbf{Method~\#3)~Apply a Voltage Source:}\par
\begin{center}\fbox{\begin{minipage}{30em}
\underline{\textbf{Limitations:}}~None
\end{minipage}}\end{center}
\begin{enumerate}
\item Remove the load if it is not already removed.
\item Replace all \textbf{independent} supplies with their ideal resistances.
\item Place a voltage supply ($V_{NEW}$) between the nodes where the load will be reconnected. You get to pick a voltage for this supply. Any number will do.
\item Calculate the current ($I_{NEW}$) through this new supply.
\item $R_{TH}$ is then $\sfrac{V_{NEW}}{I_{NEW}}$
\end{enumerate}
Let's try it. I picked 42~\text{V} for the voltage source.

\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,0) to[short] (0,3)
(0,3) to[R,lx={$R_1$ and 3~\Om}] (3,3)
(3,3) to[R,lx={$R_2$ and 6~\Om}] (3,0)
(3,3) to[R,lx={$R_3$ and 5~\Om}] (6,3)
(6,3) to[voltage source,lx^={42~\text{V} and $V_{NEW}$}] (6,0)
%(7,3) to[R,l=$R_{L}$] (7,0)
%(6,3) -- (7,3)
(0,0) -- (6,0);
\draw[red,<-,thick] (1.2,1) arc (225:-45:4mm);
\draw[red,thick] (1.5,1) node[above]{$I_1$};
\draw[blue,<-,thick] (4.4,1) arc (225:-45:4mm);
\draw[blue,thick] (4.7,1) node[above]{$I_2$};
\draw[->,decorate,ultra thick,blue]
(8.1,2.6) node[above]{Load Replaced} to[short] (7.1,2) ;

\draw[->,decorate,ultra thick,blue]
(-1.2,2.1) node[above]{$V_S$ Replaced} to[short] (-.2,1.5) ;
\end{circuitikz}\end{center}
Again, I chose mesh to find the current through the new supply. You don't need to use mesh. Use a method that you are comfortable with.
\[ \left[ \begin{array}{cc}
9\Omega&-6\Omega\\
-6\Omega&11\Omega\\
\end{array} \right]^{-1}\left[\begin{array}{c}0~\text{V}\\42~\text{V}\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\end{array}\right]=\left[\begin{array}{c}4~\text{A}\\6~\text{A}\end{array}\right]\]
and $I_{NEW}$=$I_2$ in this case leading to \[R*{TH}=\frac{V*{NEW}}{I\_{NEW}}=\frac{42~\text{V}}{6~\text{A}}=7~\Omega\]

All three methods are applicable to this example and all three yield the same result for $R_{TH}$. Some problems may not allow the application of all three methods according to their limitations however, if multiple methods are applicable the results will be equivalent.

Some examples will allow us to consider each of the three cases and their limitations.

\begin{example}
Find the Thevenin equivalent for the circuit shown here around the resistor, $R_{L}$.
\end{example}

\begin{example}
Find the Thevenin equivalent for the circuit shown here between nodes A and B.
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[voltage source,l_=12~\text{V}] (0,0)
(0,3) to[R,l=4~\Om] (2,3)
(2,3) to[controlled voltage source,l=2$I_{x}$] (5,3)
(5,3) to[R,l=6~$\Omega$,i^=$I_{x}$] (5,0)
(5,3) to[R,l=3~\Om] (8,3)
(0,0) to[short,-o] (9,0)
(8,3) to[short,-o] (9,3)
(10,3) node[below]{A}
(10,0) node[above]{B}
;
\end{circuitikz}\end{center}

\Solution
\textbf{Find $V_{OC}$}\par
In this case $V_{OC}$ is across the nodes A and B as labeled below. Mesh analysis was applied in this example to find the open circuit voltage though an method of analysis would suffice.
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[voltage source,l_=12~\text{V}] (0,0)
(0,3) to[R,l=4~\Om] (2,3)
(2,3) to[controlled voltage source,l=2$I_{x}$] (5,3)
(5,3) to[R,l=6~$\Omega$,i^=$I_{x}$] (5,0)
(5,3) to[R,l=3~\Om] (8,3)
(0,0) to[short,-o] (9,0)
(8,3) to[short,-o] (9,3)
(9,3) to[open,v=$V_{OC}$] (9,0)
(10,3) node[below]{A}
(10,0) node[above]{B}
(2,1.5) node[red,thick]{I}
;
\centerarc[red,->,thick](2,1.5)(225:-45:5mm)
\end{circuitikz}\end{center}
The single KVL equation for this circuit is
\[12-4I+2I*x-6I=0\]
where $I*{x}$ is equal to I. Substituting into the KVL and grouping like terms leads to
\[12-8I=0\]
and solving for I gives
\[I=1.5~\text{A}\]
Using the value of I we can find voltages for all of the passive components in the circuit. Note that the 3~\Om ~resistor has no current flowing through it and therefore the voltage across it is 0~\text{V}.
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[voltage source,l_=12~\text{V}] (0,0)
(0,3) to[R,l=4~\Om,v=6~\text{V}] (2,3)
(2,3) to[controlled voltage source,l=2$I_{x}$] (5,3)
(5,3) to[R,l=6~$\Omega$,i^=$I_{x}$,v=9~\text{V}] (5,0)
(5,3) to[R,l=3~\Om,v=0~\text{V}] (8,3)
(0,0) to[short,-o] (9,0)
(8,3) to[short,-o] (9,3)
(9,3) to[open,v=$V_{OC}$] (9,0)
(10,3) node[below]{A}
(10,0) node[above]{B}
(2,1.5) node[red,thick]{I}
;
\centerarc[red,->,thick](2,1.5)(225:-45:5mm)
\end{circuitikz}\end{center}
We can now write a KVL around the right side of the circuit including the drop across $V_{OC}$
\[9-0-V*{OC}=0\]
and solve for $V*{OC}$
\[V\_{OC}=9~\text{V}\]

\textbf{Find $R_{TH}$}
The dependent supply prevents us from applying the equivalent resistance method (method \#1 described above). Either of the other two methods will yield the correct result.

\vspace{8mm}
\textbf{Find $R_{TH}$ (Method \#2)}
Place a short between nodes A and B and find the short circuit current ($I_{SC}$) through that short. The circuit now has two meshes as shown below and $I_{SC}$ is equal to $I_2$ in magnitude and polarity.
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[voltage source,l_=12~\text{V}] (0,0)
(0,3) to[R,l=4~\Om] (2,3)
(2,3) to[controlled voltage source,l=2$I_{x}$] (5,3)
(5,3) to[R,l=6~$\Omega$,i^=$I_{x}$] (5,0)
(5,3) to[R,l=3~\Om] (8,3)
(0,0) to[short,-o] (9,0)
(8,3) to[short,-o] (9,3)
(9,3) to[short,i=$I_{SC}$] (9,0)
(10,3) node[below]{A}
(10,0) node[above]{B}
(2,1.5) node[red,thick]{$I_1$}
(7,1.5) node[blue,thick]{$I_2$}
;
\centerarc[red,->,thick](2,1.5)(225:-45:5mm)
\centerarc[blue,->,thick](7,1.5)(225:-45:5mm)

\end{circuitikz}\end{center}
The two KVL equations for this circuit are developed here
\[12-4I*1+2I_x-6(I_1-I_2)=0\]
where $I*{x}$ is
\[I*x=I_1-I_2\]
leading to
\[8I_1-4I_2=12\]
The KVL for the second mesh is
\[-6(I_2-I_1)-3I_2=0\]
which becomes
\[6I_1-9I_2=0\]
after distributing and grouping like-terms. Solving the system yields
\[ \left[ \begin{array}{cc}
8\Omega&-4\Omega\\
6\Omega&-9\Omega\\
\end{array} \right]^{-1}\left[\begin{array}{c}12~\text{V}\\0~\text{V}\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\end{array}\right]=\left[\begin{array}{c}2.25~\text{A}\\1.5~\text{A}\end{array}\right]\]
and $I*{SC}$=$I*2$ in this case leading to \[R*{TH}=\frac{V*{OC}}{I*{SC}}=\frac{9~\text{V}}{1.5~\text{A}}=6~\Omega\]

\vspace{8mm}
\textbf{Find $R_{TH}$ (Method \#3)}
Place a voltage supply with a value of your choice ($V_{NEW}$) between nodes A and B and find the current ($I_{NEW}$) through that supply. The circuit now has two meshes as shown below and $I_{SC}$ is equal to $I_2$ in magnitude and polarity.
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,0) to[short] (0,3)
(0,3) to[R,l=4~\Om] (2,3)
(2,3) to[controlled voltage source,l=2$I_{x}$] (5,3)
(5,3) to[R,l=6~$\Omega$,i^=$I_{x}$] (5,0)
(5,3) to[R,l=3~\Om] (8,3)
(0,0) to[short,-o] (9,0)
(8,3) to[short,-o] (9,3)
(9,3) to[battery,l^=$V_{NEW}$,i=$I_{NEW}$] (9,0)
(10,3) node[below]{A}
(10,0) node[above]{B}
(2,1.5) node[red,thick]{$I_1$}
(7,1.5) node[blue,thick]{$I_2$}
;
\centerarc[red,->,thick](2,1.5)(225:-45:5mm)
\centerarc[blue,->,thick](7,1.5)(225:-45:5mm)

\end{circuitikz}\end{center}
The two KVL equations for this circuit are developed here
\[12-4I*1+2I_x-6(I_1-I_2)=0\]
where $I*{x}$ is
\[I*x=I_1-I_2\]
leading to
\[8I_1-4I_2=12\]
The KVL for the second mesh is
\[-6(I_2-I_1)-3I_2-V*{NEW}=0\]
which becomes
\[6I*1-9I_2=V*{NEW}\]
Choosing a value of 20~\text{V} for $V_{NEW}$
\[6I*1-9I_2=20~\text{V}\]
after distributing and grouping like-terms. Solving the system yields
\[ \left[ \begin{array}{cc}
8\Omega&-4\Omega\\
6\Omega&-9\Omega\\
\end{array} \right]^{-1}\left[\begin{array}{c}0~\text{V}\\20~\text{V}\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\end{array}\right]=\left[\begin{array}{c}-1.67~\text{A}\\-3.33~\text{A}\end{array}\right]\]
and $I*{NEW}$=-$I*2$ in this case leading to \[R*{TH}=\frac{V*{NEW}}{I*{NEW}}=\frac{20~\text{V}}{3.33~\text{A}}=6~\Omega\]

The Thevenin equivalent circuit can be drawn using the values found above
\begin{center}\begin{circuitikz}[decoration=snake]\draw
% (3,0) -- (0,0) to[battery,lx={$V_{TH}$ and 9~\text{V}}] (0,3)
(0,3) to[battery,lx_={$V_{TH}$ and 9~\text{V}}] (0,0) -- (3,0)
(0,3) to[R,lx={$R_{TH}$ and 6~$\Omega$}] (3,3)
;
\end{circuitikz}\end{center}

A load connected to the original circuit between nodes A and B will see the same voltage, current, and power as a load connected across the output of the Thevenin equivalent.
\end{example}

\begin{example}
Find the Thevenin equivalent for the circuit shown here between nodes A and B.
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,0) to[controlled current source,lx={$I_S$ and 6$I_{x}$}] (0,4)
(3,0) to[R,lx={$R_1$ and 30~\Om}] (3,4)
(3,4) to[R,lx={$R_2$ and 8~\Om}] (6,4)
(6,0) to[R,lx={$R_3$ and 25~\Om},i<=$I_{x}$] (6,4)
(9,0) to[controlled current source,lx_={$I_S$ and 10$I_{x}$}] (9,2)
(9,2) to[R,lx_={$R_5$ and 6~\Om}] (9,4)
%(7,3) to[R,l=$R_{L}$] (7,0)
%(6,3) -- (7,3)z
(0,4) to[short] (3,4)
(6,4) to[R,lx={$R_4$ and 10~\Om}] (9,4)
(9,4) to[R,lx={$R_6$ and 4~\Om}] (12,4)
(12,4) node[below]{A}
(12,0) node[above]{B}
(0,0) to[short,-o] (12,0)
(12,4) to[short,-o] (12,4)
;
\end{circuitikz}\end{center}
This circuit has no independent supplies leading us to apply a voltage source where the load will be connected (method \#3 described above). The other two methods will not work according to their limitations.

\end{example}

We often use Thevenin equivalent circuits to characterize sub-circuits without having to know the details of each sub-circuit. In this way we can determine what is happening at the nodes where the sub-circuits connect together. Examples of sub-circuits include stages of amplifiers, sections of a power distribution layout, sensors, and microcontrollers.

\begin{example}
\begin{center}\begin{circuitikz}[scale=0.75]\draw
(0,0) to[R,l=10~\Om ](0,3)
(3,0) to[current source,l=2.2~\text{A}] (3,3)
(8,0) -- (6,0) to[voltage source,l=32~\text{V}] (3,0)
(8,3) to[short,i<=$I_O$] (5.8,3) to[R,l=18~\Om] (3,3)
(6,0) to[open,v<=$V_O$](6,3)
(8,0) to[R,l\_=9~\Om ](8,3)
(11,0) to[current source,l\_=2.5~\text{A}](11,3)
% (6.5,0) node[sground,scale=0.5]{}
(14,3) to[voltage source,l=36~\text{V}](14,0)
(11,3) to[R,l=18~\Om] (14,3)
(0,0) to[short] (3,0)
(0,3) to[short] (3,3)
(8,0) to[short] (14,0)
(8,3) to[short] (11,3)
;
\draw[dashed,ultra thick,blue] (-1.5,-1.5) rectangle (5.5,4);
\draw[dashed,ultra thick,red] (7.25,-1.5) rectangle (16,4);
\end{circuitikz}\end{center}

\paragraph{Analyzing the whole circuit}~
\[ \left[ \begin{array}{cccc}
-1&1&0&0\\
0&0&-1&1\\
10&27&-9&0\\
0&-9&9&18
\end{array} \right]^{-1}\left[\begin{array}{c}2.2~\text{A}\\2.5~\text{A}\\-32~\text{V}\\-36~\text{V}\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\\I_3\\I_4\end{array}\right]=\left[\begin{array}{c}-3.288~\text{A}\\-1.088~\text{A}\\-3.363~\text{A}\\-862.7~\text{mA}\end{array}\right]\]
\[I_O=I_2=-1.088~\text{A}\]
\[V_O=9*(I_2-I_3)=9*(-1.088+3.363)=20.47~\text{V}\]

\paragraph{Find the equivalent for the blue circuit}~
\begin{center}\begin{circuitikz}[scale=0.75]\draw
(0,0) to[R,l=10~\Om ](0,3)
(3,0) to[current source,l=2.2~\text{A}] (3,3)
(7,0) to[short,o-] (6,0) to[voltage source,l=32~\text{V}] (3,0)
(7,3) to[short,o-] (5.8,3) to[R,l=18~\Om] (3,3)
(6,0) to[open](6,3)
(0,0) to[short] (3,0)
(0,3) to[short] (3,3)
(7,0) node[below]{B}
(7,3) node[above]{A}
(11,3) to[voltage source,l^=-10~\text{V}] (11,0)
(11,3) to[R,l=28~\Om,-o] (14,3)
(6,0) to[open,v<=$V_O$](6,3)
(11,0) to[short,-o] (14,0)
(14,0) node[below]{B}
(14,3) node[above]{A}
;
\draw [-latex, line width=5pt, cyan] (8,1.5) -- (10,1.5);
\end{circuitikz}\end{center}

\paragraph{Find the equivalent for the red circuit}~
\begin{center}\begin{circuitikz}[scale=0.75]\draw
(8,0) to[R,l\_=9~\Om ](8,3)
(11,0) to[current source,l\_=2.5~\text{A}](11,3)
(14,3) to[voltage source,l=36~\text{V}](14,0)
(11,3) to[R,l=18~\Om] (14,3)
(7,0) to[short,o-] (14,0)
(7,3) to[short,o-] (11,3)
(7,0) node[below]{B}
(7,3) node[above]{A}
(18.5,3) to[R,l\_=6~\Om,o-](21.5,3)
(21.5,3) to[voltage source,l^=27~\text{V}](21.5,0)
(18.5,0) to[short,o-] (21.5,0)
(18.5,0) node[below]{B}
(18.5,3) node[above]{A}
;
\draw [-latex, line width=5pt, cyan] (16,1.5) -- (18,1.5);
\end{circuitikz}\end{center}

\paragraph{Working with the equivalent circuits}~

\begin{center}\begin{circuitikz}[scale=0.75]\draw
(3,3) to[voltage source,l_=-10~\text{V}] (3,0)
%(3,0) node[sground,scale=0.5]{}
(8,0) -- (6,0) to[short] (3,0)
(8,3) to[short,i<=$I_O$] (5.8,3) to[R,l=28~\Om] (3,3)
(6,0) to[open,v<=$V_O$](6,3)
(8,3) to[R,l\_=6~\Om ](11,3)
(11,3) to[voltage source,l^=27~\text{V}](11,0)
%(11,0) node[sground,scale=0.5]{}
(8,0) to[short] (11,0)
;
\draw[dashed,ultra thick,blue] (0.25,-1.5) rectangle (5.5,4);
\draw[dashed,ultra thick,red] (7.25,-1.5) rectangle (13,4);
\end{circuitikz}\end{center}

\end{example}

## Norton's Theorem

\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[battery,l_=$V_{TH}$] (0,0)
(0,3) to[R,l=$R_{TH}$] (3,3)
(4,3) to[R,l=$R_{L}$] (4,0)
(3,3) -- (4,3)
(0,0) -- (4,0);
\draw[dashed,ultra thick,blue] (-2,-1) rectangle (3,4.5)
(-2,4) node[right]{Thevenin Equivalent};
\draw[->,decorate,ultra thick,blue]
(6.1,2.1) node[above]{Load} to[short] (5.1,1.5) ;
\end{circuitikz}\end{center}

\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[battery,lx_={$V_S$ and 12~\text{V}}] (0,0)
(0,3) to[R,lx={$R_1$ and 3~\Om}] (3,3)
(3,3) to[R,lx={$R_2$ and 6~\Om}] (3,0)
(3,3) to[R,lx={$R_3$ and 5~\Om}] (6,3)
(7,3) to[R,l=$R_{L}$] (7,0)
(6,3) -- (7,3)
(0,0) -- (7,0);
\draw[dashed,ultra thick,blue] (-2,-1) rectangle (6,4.5)
(-2,4) node[right]{Fixed Circuit};
\draw[->,decorate,ultra thick,blue]
(8.8,2.1) node[above]{Load} to[short] (7.8,1.5) ;
\end{circuitikz}\end{center}

\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[battery,lx_={$V_S$ and 12~\text{V}}] (0,0)
(0,3) to[R,lx={$R_1$ and 3~\Om}] (3,3)
(3,3) to[R,lx={$R_2$ and 6~\Om}] (3,0)
(3,3) to[R,lx={$R_3$ and 5~\Om}] (6,3)
(7,3) to[R,l=$R_{L}$] (7,0)
(6,3) -- (7,3)
(0,0) -- (7,0);
\draw[dashed,ultra thick,blue] (-2,-1) rectangle (6,4.5)
(-2,4) node[right]{Fixed Circuit};
\draw[->,decorate,ultra thick,blue]
(8.8,2.1) node[above]{Load} to[short] (7.8,1.5) ;
\end{circuitikz}\end{center}

## Maximum Power Transfer

Often we must ensure that the power delivered to a load is as much as possible. This is true when:
\begin{enumerate}
\item Stereo to speaker connection
\item Power transmission
\item Data transmission
\item and many more...
\end{enumerate}
The circuit transmitting can be thought of as its Thevenin equivalent with a load connected as shown here
\begin{center}\begin{circuitikz}[decoration=snake]\draw
(0,3) to[battery,l_=$V_{TH}$] (0,0)
(0,3) to[R,l=$R_{TH}$] (3,3)
(4,3) to[R,l=$R_{L}$,v=$V_{RL}$,i=$I_{RL}$] (4,0)
(3,3) -- (4,3)
(0,0) -- (4,0);
\draw[dashed,ultra thick,blue] (-2,-1) rectangle (3,4.5)
(-2,4) node[right]{Thevenin Equivalent};
\draw[->,decorate,ultra thick,blue]
(6.1,2.1) node[above]{Load} to[short] (5.1,1.5) ;
\end{circuitikz}\end{center}
We want to select the value of $R_{L}$ in order to maximize the power dissipate by that same resistor, $P_{RL}$. In order to find the relationship between the power and the value. This relationship can be stated mathematically using the function $P_{RL}(R_L)$. Don't confuse this notation with multiplication. One variable is a function of the other. Before we develop this function, let's play some mind games and look at some common answers that I get from students.

Use your intuition and guess what value of $R_{L}$ maximizes $P_{RL}$. When I ask for responses in class I usually get one of two answers. First, students will guess $R_{L}$ is 0~\Om (a short) reasoning that value will cause the maximum current to flow. While the current will be maximized, the voltage across a short is 0~\text{V}. Therefore, the power dissipated by the shorted load will be 0~\text{W}.

Second, a student will usually guess that $R_{L}$ is infinite (an open) reasoning that if 0~\text{V} gives us 0~\text{W} we should maximize voltage across the load. This, of course, causes the current to drop to 0~\text{A}. Once again this results in the load resistor dissipating 0~\text{W}. So the extreme limits of the load resistance won't dissipate any power. The answer lies somewhere in between those extremes. But where? Let's do some calculus.

We start by developing the function (relationship) between the load resistance and the power that load resistance dissipates. We start with the definition of power
\[P*{RL}=V*{RL}I*{RL}\]
where the load voltage as pictured in the circuit above can be written with a simple voltage divider
\[V*{RL}=V*{TH}\left[\frac{R_L}{R*{TH}+R*L}\right]\]
and the load current is an application of equivalent resistances and Ohm's law.
\[I*{RL}=\frac{V*{TH}}{R*{TH}+R*L}\]
We can rewrite the load power by substituting the previous two expressions into the first.
\[P*{RL}=V*{TH}\left[\frac{R_L}{R*{TH}+R*L}\right]\frac{V*{TH}}{R*{TH}+R_L}\]
or in a reduced form
\[P*{RL}=\frac{V*{TH}^2R_L}{(R*{TH}+R*L)^2}\]
We can calculate the load power for a given load resistance. Alternatively, to find the maximum power we can set its derivative equal to zero and solve for $R*{L}$.  The derivative with respect to $R_{L}$ is
\[\frac{dP*{RL}}{dR_L}=\frac{V*{TH}^2(R*{TH}-R_L)}{(R*{TH}+R*L)^3}\]
The derivative will be 0 when the numerator is 0 leading to
\[V*{TH}^2(R*{TH}-R_L)=0\]
where $V*{TH}$ and $R_{TH}$ are fixed values so we solve for $R_{L}$. The only value of $R_{L}$ that makes this equation true is
\[R*L=R*{TH}\]
This is it. This is the condition that guarantees the maximum power will be dissipated by/delivered to the load. Let's consider two applications of this theorem.

\begin{example}
Let's take a look at an example with values that supports the theory introduced above. Consider a circuit that has a Thevenin voltage of 10~\text{V} and a Thevenin resistance of 2~\Om. The equivalent circuit can be drawn with a load connected as shown here:
\begin{center}\begin{circuitikz}\draw
(0,3) to[battery,lx_={$V_{TH}$ and 10~\text{V}}] (0,0)
(0,3) to[R,lx={$R_{TH}$ and 2~\Om}] (3,3)
(4,3) to[R,l=$R_{L}$,v=$V_{RL}$,i=$I_{RL}$] (4,0)
(3,3) -- (4,3)
(0,0) -- (4,0);
\end{circuitikz}\end{center}
We'll vary the value of $R_{L}$ along the horizontal of a plot to demonstrate how the other values of interest are affected.
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={0,2,4,6,8,10,12,14},
xtick={0,2,4,6,8,10,12,14,16,18,20,22,24,26},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$R_L (\Omega)$,
ymin=0,
ymax=+14,
xmin=-0,
xmax=+26,
width=13cm,
height=6cm,
legend pos=outer north east
]
\addplot+[blue,mark=none,ultra thick,smooth,domain=0:26,samples=400] (\x,{10*(\x/(\x+2))});
\addplot+[red,mark=none,ultra thick,smooth,domain=0:26,samples=400] (\x,{10/(\x+2))});
\addplot+[green,mark=none,ultra thick,smooth,domain=0:26,samples=400] (\x,{(10/(\x+2)))*(10\*(\x/(\x+2)))});
\legend{$V_{RL}$ (V),$I_{RL}$ (A),$P_{RL}$ (W)}
\end{axis}
\end{tikzpicture}
\end{center}
Now we can graphically look at the values of $R_{L}$ and see how they affect the power dissipated by the load, the green plot above. When $R_{L}$ is 0~\Om, the left extreme of the graph, we see the greatest amount of current flowing, 5~\text{A} for this circuit. However, at that same value of $R_{L}$ we see that $V_{RL}$ is 0~\text{V}. Thus the $P_{RL}$ is 0~\text{W} as shown by the green line in the plot above.

At the other extreme of the domain of $R_{L}$ we can consider, $R_{L}$ is $\infty~\Omega$. Since the paper is not wide enough we'll have to use 26~\Om ~as an approximation of infinity. Notice $P_{RL}$ is asymptotically approaching 0~\text{W} as $I_{RL}$ is asymptotically approaching 0~\text{A}.

The maximum power is dissipated when $R_{L}$=$R_{TH}$, 2~\Om~for this example. This is evident in the plot above as the green line reaches its maximum value of 12.5~\text{W} when $R_{L}$ is 2~\Om.

\end{example}

\begin{example}
Can $R_{L}$ dissipate 50~\text{W} in this circuit?
\begin{center}\begin{circuitikz}\draw
(0,3) to[battery,lx_={$V_S$ and 32~\text{V}}] (0,0)
(0,3) to[R,lx={$R_1$ and 4~\Om}] (3,3)
(3,3) to[R,lx={$R_2$ and 12~\Om}] (3,0)
(6,3) to[R,l=$R_{L}$] (6,0)
(3,3) to[short] (6,3)
(0,0) -- (6,0);
\end{circuitikz}\end{center}
To answer this we can redraw the circuit the circuit as its Thevenin equivalent. Thevenizing around $R_{L}$ give us a Thevenin voltage of 24~\text{V} and Thevenin resistance of 3~\Om. Take a moment to confirm these values. You're an expert now. You've read the first part of this chapter. The equivalent circuit looks like
\begin{center}\begin{circuitikz}\draw
(0,3) to[battery,lx_={$V_{TH}$ and 24~\text{V}}] (0,0)
(0,3) to[R,lx={$R_{TH}$ and 3~\Om}] (3,3)
(3,3) to[R,lx={$R_{L}$ and 3~\Om},v=$V_{RL}$] (3,0)
(0,0) -- (3,0);
\end{circuitikz}\end{center}
I've specified the value of $R_{L}$ that we know will result in the maximum power dissipated by that resistor, 3~\Om. In this case we can find $V_{RL}$ as
\[V*{RL}=24~\text{V}\left[\frac{3~\Omega}{3~\Omega+3~\Omega}\right]=12~\text{V}\]
and therefore the maximum power that $R*{L}$ can dissipate will be
\[P*{RL}=\frac{(12~\text{V})^2}{3~\Omega}=48~\text{W}\]
Any departure from $R*{L}$ being 3~\Om ~will lower the power dissipated by the load. Therefore, there is no value of $R_{L}$ that can dissipate 50~\text{W} in this circuit.
\end{example}

One final note. While the $R_{TH}$=$R_{L}$ condition guarantees maximum power transferred to the load it makes no guarantee about the efficiency. This misconception is common but misguided. When maximum power is dissipated by the load the efficiency will be 50\%. $R_{L}$ and $R_{TH}$ will dissipate the same power. The power dissipated by $R_{TH}$ is considered wasted energy dissipated by the transmitting circuit.

For now I'll leave this as an exercise for you. What value of $R_{L}$ gives maximum efficiency? What if we could vary $R_{TH}$? What value of $R_{TH}$ would lead to maximum efficiency?

## Source Conversions

Converting sources is a bit of an oddity that turns out to be useful. It is possible to solve for some circuit values in some circuits using this technique. However, not all circuits and values will yield to it. It is much more useful as a method of reducing the complexity of a circuit under analysis. Converting equivalent sources is useful to reduce the number of mesh currents or node voltages in a circuit.

\paragraph{Norton Equivalent of a Thevenin Equivalent}
To begin, we will find the Norton equivalent of a Thevenin equivalent circuit. The short circuit current is labeled in the schematic below.
\begin{center}\begin{circuitikz}\draw
(0,3) to[battery,l_=$V_{TH}$] (0,0)
(0,3) to[R,l=$R_{TH}$,-o] (3,3)
(0,0) to[short,-o] (3,0)
(3,3) to[short,i=$I_{SC}$] (3,0)
;
\end{circuitikz}\end{center}
Calculating the short circuit current is a simple application of Ohm's law
\[I*N=I*{SC}=\frac{V*{TH}}{R*{TH}}\]
Finding $R_{N}$ is similarly straight forward. The voltage supply is replaced by a short as shown here
\begin{center}\begin{circuitikz}\draw
(0,3) to[short](0,0)
(0,3) to[R,l=$R_{TH}$,-o] (3,3)
(0,0) to[short,-o] (3,0)
(3.5,1.5) node[right]{$R_{N}$}
;
\draw [-latex, line width=2pt, black] (3.5,1.5) -- (2.5,1.5);
\end{circuitikz}\end{center}
The relationship between $R_{N}$ and $R_{TH}$ is simple given there is only a single resistor to consider.
\[R*N=R*{TH}\]
While the value is the same the location of the resistance is different in the two equivalent circuits. In series with the supply in the Thevenin equivalent and in parallel with the supply in the Norton equivalent.

\paragraph{Thevenin Equivalent of a Norton Equivalent} Now let's turn it around the other way. Starting with a Norton equivalent circuit let's find its Thevenin equivalent.
\begin{center}\begin{circuitikz}\draw
(0,0) to[current source,l*=$I*{N}$](0,3)
(2,0) to[R,l_=$R_{N}$] (2,3)
(0,3) to[short,-o] (4,3)
(0,0) to[short,-o] (4,0)
(4.25,3) to[open,v=$V_{OC}$] (4.25,0)
;
\end{circuitikz}\end{center}
Finding $V_{OC}$ is once again is a simple application of Ohm's Law.
\[V*{TH}=V*{OC}=I_NR_N\]

Finding $R_{TH}$ is similarly straight forward. The current supply is replaced by an open as shown here
\begin{center}\begin{circuitikz}\draw
(0,0) to[open](0,3)
(2,0) to[R,l_=$R_{N}$] (2,3)
(0,3) to[short,-o] (4,3)
(0,0) to[short,-o] (4,0)
(4.5,1.5) node[right]{$R_{N}$}
;
\draw [-latex, line width=2pt, black] (4.5,1.5) -- (3.5,1.5);
\end{circuitikz}\end{center}
The relationship between $R_{TH}$ and $R_{N}$ is again simple given there is only a single resistor to consider.
\[R*{TH}=R*{N}\]

\paragraph{Summary of Conversions}
These conversion allow us to move quickly between Thevenin and Norton equivalents. In doing so the goal is to combine resistors and sources in such a way that reduces the complexity of the circuit. Let's keep the conversion shown below in our heads as we further develop this technique.
\begin{center}\begin{circuitikz}\draw
(0,3) to[battery,l_=$V_{TH}$] (0,0)
(0,3) to[R,l=$R_{TH}$,-o] (3,3)
(0,0) to[short,-o] (3,0)

    (7,0) to[current source,l_=$\frac{V_{TH}}{R_{TH}}$] (7,3)
    (10,0) to[R,l_=$R_{TH}$] (10,3)
    (7,3) to[short,-o] (11,3)
    (7,0) to[short,-o] (11,0)
    (4.85,1.65) node[above]{converts to}
    ;
    \draw [-latex, line width=5pt, cyan] (4,1.5) -- (6,1.5);

\end{circuitikz}\end{center}

\begin{center}\begin{circuitikz}\draw
(0,0) to[current source,l_=$I_{N}$] (0,3)
(3,0) to[R,l_=$R_{N}$] (3,3)
(0,3) to[short,-o] (4,3)
(0,0) to[short,-o] (4,0)

    (8,3) to[battery,l_=$I_{N}$$R_{N}$] (8,0)
    (8,3) to[R,l=$R_{N}$,-o] (11,3)
    (8,0) to[short,-o] (11,0)
    (5.1,1.65) node[above]{converts to}
    ;
    \draw [-latex, line width=5pt, cyan] (4.25,1.5) -- (6.25,1.5);

\end{circuitikz}\end{center}

\paragraph{Circuit Analysis and Reduction of Complexity with Source Conversions} derp

\begin{example}
\begin{center}\begin{circuitikz}\draw
(0,3) to[battery,l_=$V_{TH}$] (0,0)
(0,3) to[R,l=$R_1$] (3,3)
(3,3) to[R,l=$R_2$] (3,0)
(6,3) to[R,l=$R_3$] (6,0)
(3,3) to[short] (6,3)
(0,0) -- (6,0);
\end{circuitikz}\end{center}
\end{example}

\begin{example}
\begin{center}\begin{circuitikz}[scale=0.9]\draw
(0,3) to[R,l_=6~\Om] (0,0)
(3,0) to[current source,l=5~\text{A}] (3,3)
(6,3) to[R,l=3~\Om] (6,0)
(9,3) to[battery,l=5~\text{V}] (6,3)
(9,3) to[R,l=7~\Om,i>=$i_{O}$] (9,0)
(12,0) to[current source,l=3~\text{A}] (12,3)
(0,3) to[short] (6,3)
(12,3) to[R,l=1~\Om] (15,3)
(15,3) to[R,l=4~\Om] (15,0)
(9,3) to[short] (12,3)
(0,0) -- (15,0);
\end{circuitikz}\end{center}
\end{example}

\begin{example}
\begin{center}\begin{circuitikz}\draw
(0,0) to[battery,l_=12~\text{V}] (0,3)
(0,3) to[R,l=4~\Om] (2,3)
(2,3) to[R,l=2~\Om] (4,3)
(4,0) to[R,l=8~\Om,v<=$V_O$] (4,3)
(7,0) to[R,l=3~\Om] (7,3)
(10,0) to[current source,l=4~\text{A}] (10,3)
(4,3) to[short] (10,3)
(0,0) to[short] (10,0)
;
\end{circuitikz}\end{center}
\end{example}

Highlight reduction in complexity
Add Dependent supply example

### Strategy for Source Conversions
