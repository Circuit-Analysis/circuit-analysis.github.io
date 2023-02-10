#!/usr/bin/env python
# coding: utf-8

# # Nodal Analysis
# 
# \label{ch:nodal}
# Nodal Analysis is another methodical application of KVL, KCL, and Ohm's law that allow use to analyze any circuit. Nodal Analysis has a key advantage over Mesh Analysis but in general students become comfortable with one method or the other. The advantage Nodal Analysis has is the ease of locating the unknowns. This is true for humans and computers. Most circuit simulation software uses Nodal Analysis since it is easier to see where components connect (nodes) rather than closed paths with no intermediate branches. This becomes particularly true when analyzing circuits with ideal operational amplifiers, as we will do in this chapter.
# 
# ## Locating Non-reference Nodes
# 
# if you don't need to cross a component between two of your labeled nodes than they are, in fact, one node
# 
# ## Relating Circuit Values to Node Voltages
# 
# \begin{minipage}{1.0\textwidth}
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) to[european resistor,v^>=$V_1$] (0,3)
# (0,3) to[european resistor,v=$V_2$,*-*] (3,3)
# (6,3) to[european resistor,v=$V_3$,*-*] (3,3)
# (6,3) to[european resistor,v^>=$V_4$] (6,0)
# (3,3) to[european resistor,v=$V_5$] (3,0)
# (0,5) to[european resistor,v=$V_6$] (6,5)
# (0,0) -- (6,0)
# (0,5) -- (0,3)
# (6,5) -- (6,3)
# (0,0) node[sground,scale=0.5]{}
# (0,3) node[left]{A}
# (3,3) node[above]{B}
# (6,3) node[right]{C}
# ;
# \end{circuitikz}
# 
# \vspace{3mm}
# 
# $V_1$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $V_2$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $V_3$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $V_4$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $V_5$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $V_6$=\underline{~~~~~~~~~~~~~~~~~~}
# \end{center}
# \end{minipage}
# \begin{minipage}{0.5\textwidth}
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) to[european resistor,l_=$R_1$,i=$I_a$] (0,3)
# (0,3) to[european resistor,l_=$R_2$,i_=$I_b$,*-*] (3,3)
# (6,3) to[european resistor,l_=$R_3$,i=$I_c$,*-*] (3,3)
# (6,3) to[european resistor,l_=$R_4$,i=$I_d$] (6,0)
# (3,3) to[european resistor,l_=$R_5$,i=$I_e$] (3,0)
# (0,5) to[european resistor,l_=$R_6$,i=$I_f$] (6,5)
# (0,0) -- (6,0)
# (0,5) -- (0,3)
# (6,5) -- (6,3)
# (0,0) node[sground,scale=0.5]{}
# (0,3) node[left]{A}
# (3,3) node[above]{B}
# (6,3) node[right]{C}
# ;
# \end{circuitikz}
# 
# \vspace{3mm}
# 
# $I_a$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_b$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_c$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_d$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_e$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_f$=\underline{~~~~~~~~~~~~~~~~~~}
# \end{center}
# \end{minipage}
# \begin{minipage}{0.5\textwidth}
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) to[european resistor,l_=$R_1$,i<=$I_a$] (0,3)
# (0,3) to[european resistor,l_=$R_2$,i_=$I_b$,*-*] (3,3)
# (6,3) to[european resistor,l_=$R_3$,i=$I_c$,*-*] (3,3)
# (6,3) to[european resistor,l_=$R_4$,i=$I_d$] (6,0)
# (3,3) to[european resistor,l_=$R_5$,i=$I_e$] (3,0)
# (0,5) to[european resistor,l_=$R_6$,i=$I_f$] (6,5)
# (0,0) -- (6,0)
# (0,5) -- (0,3)
# (6,5) -- (6,3)
# (0,0) node[sground,scale=0.5]{}
# (0,3) node[left]{A}
# (3,3) node[above]{B}
# (6,3) node[right]{C}
# ;
# \end{circuitikz}
# 
# \vspace{3mm}
# 
# $I_a$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_b$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_c$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_d$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_e$=\underline{~~~~~~~~~~~~~~~~~~}
# \vspace{3mm}
# 
# $I_f$=\underline{~~~~~~~~~~~~~~~~~~}
# \end{center}
# \end{minipage}
# 
# ## The Steps
# 
# I'm going to list the steps here as reference. Use these steps as we walk through the next example.
# \begin{framed}
# \Large\textbf{Steps for Nodal Analysis}\normalsize
# \begin{enumerate}
# \item Label the non-reference nodes and a current direction for each passive circuit element.  
#  \item Use KCL on each non-reference node.
# \item Use Ohm's law to express the resistor currents in terms of node voltages.
# \item Distribute and group like terms.
# \item Plug in values and solve the system.
# \end{enumerate}
# \end{framed}
# These steps give us a starting point for the first example. We'll develop what to do with special circumstances in more complex circuits.
# 
# ## Our First Toy Problem
# 
# \begin{example}
# Find $I_O$ using Nodal Analysis.
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[current source,lx={$I_S$ and 6~\text{A}}] (0,3)
# (0,3) to[resistor,lx={$R_1$ and 2~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 4~\Om},i=$I_O$] (3,0)
# (3,3) to[resistor,lx={$R_3$ and 4~\Om}] (6,3)
# (6,3) to[resistor,lx={$R_4$ and 2~\Om}] (6,0)
# (6,0) -- ((0,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# ;
# \end{circuitikz}\end{center}
# 
# \Solution
# Start by labeling the non-reference nodes as shown below. Pick a current direction for each passive component. For this problem that means the resistors. In future problems we'll also label current directions for the other passive elements, the capacitors and inductors. These current arrows will help us keep the signs consistent in the system of equations we're about to develop to find the unknowns.
# 
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[current source,lx={$I_S$ and 6~\text{A}}] (0,3)
# (0,3) to[resistor,lx={$R_1$ and 2~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 4~\Om},i=$I_O$] (3,0)
# (3,3) to[resistor,lx={$R_3$ and 4~\Om}] (6,3)
# (6,3) to[resistor,lx={$R_4$ and 2~\Om}] (6,0)
# (6,0) -- ((0,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# (0,3) node[above]{A}
# (3,3) node[above]{B}
# (6,3) node[above]{C}
# ;
# \draw[blue,-latex] (1,2.5) to[short,thick] (2,2.5);
# \draw[blue,-latex] (4,2.5) to[short,thick] (5,2.5);
# \draw[blue,-latex] (2.5,2) to[short,thick] (2.5,1);
# \draw[blue,-latex] (5.5,2) to[short,thick] (5.5,1);
# \end{circuitikz}\end{center}
# \paragraph{KCL for Node A}
# Each term in a KCL must be a current. In the case of node A there will be two terms since two circuit elements are connected to it. The first term I'll write is the current through $I_S$. This term is a constant current and the simplest term we will encounter in Nodal Analysis.
# 
# The second term takes the form that we practice in the earlier section of this chapter. This term will be the current through $R_1$. And of course, we set it equal to zero and Kirchhoff instructed.
# \[ I*S-I*{R1}=0\]
# 
# Notice the sign of each term. The $I_S$ term is positive since the current is entering node A. This arrow was not our choice. It is simply taken from the direction of the arrow with in the current supply symbol.
# 
# The second term is negative. The arrow we drew for I\tss{R1} is leaving node A leading to the negative sign. This is the term that we will need to rewrite to be in terms of the unknown node voltages. Stop and look at the schematic to figure out which node is at the tail of the arrow. Now find the node connected to the tip of the arrow. I'm hope you identified Node A at the tail and Node B at the tip. Using the voltages at the nodes with respect to ground we can write an expression for the current through $R_1$
# \[I\_{R1}=\frac{V_A-V_B}{R_1}\]
# We then substitute this expression into the KCL we wrote above.
# \[ I_S-\frac{V_A-V_B}{R_1}=0\]
# Notice that the sign front of the second term remains negative. In order to group like terms we will break up the fraction
# \[ I_S-\left[\frac{V_A}{R_1}-\frac{V_B}{R_1}\right]=0\]
# and distribute the sign from the KCL
# \[ I_S-\frac{1}{R_1}V_A+\frac{1}{R_1}V_B=0\]
# Moving the constant to the right hand side gives us
# \[-\frac{1}{R_1}V_A+\frac{1}{R_1}V_B=-I_S\]
# and plugging in values gives us
# \[-\frac{1}{2}V_A+\frac{1}{2}V_B=-6\]
# in a form we can use in the system of equations. We have constants and the unknown node voltages, nothing else. Any other variables will have to be dealt with. This example doesn't have any other variables but will will encounter them in future examples.
# 
# \paragraph{KCL for Node B}
# We follow the same process for node B. Node B has three elements connected to it. Therefore the KCL for this node will have three terms.
# \[I*{R1}-I*{R2}-I\_{R3}=0\]
# I\tss{R1} is the only current out of the three that is entering the node and therefore is the only positive term in this KCL. The other two currents are leaving node B and the corresponding terms are both negative.
# 
# All three currents follow the usual format, voltage at the tail minus voltage at the tip over the resistance. I\tss{R1} and I\tss{R3} will look similar to the term we substituted in the previous KCL equation.
# \[I*{R1}=\frac{V_A-V_B}{R_1}\]
# \[I*{R3}=\frac{V*B-V_C}{R_3}\]
# In fact, the expression for I\tss{R1} is identical to then one we wrote previously. The expression for I\tss{R2} will end up looking a little different. Stop and find the voltages at the tail and tip of the arrow for I\tss{R2}. The voltage at the tail is $V_B$. The voltage at the tip is 0~\text{V}. The tip of this arrow points to the ground node and the difference between this node and itself is 0~\text{V}. We can include this 0~\text{V} in the expression
# \[I*{R2}=\frac{V*B-0}{R_2}\]
# but more often than not we exclude it as it is simply a subtraction by zero
# \[I*{R2}=\frac{V_B}{R_2}\]
# Substituting these expressions into the KCL gives us
# \[\frac{V_A-V_B}{R_1}-\frac{V_B}{R_2}-\frac{V_B-V_C}{R_3}=0\]
# Breaking up the fractions and distributing the signs leads to
# \[\frac{1}{R_1}V_A-\frac{1}{R_1}V_B-\frac{1}{R_2}V_B-\frac{1}{R_3}V_B+\frac{1}{R_3}V_C=0\]
# before grouping like terms
# \[\frac{1}{R_1}V_A+\left[-\frac{1}{R_1}-\frac{1}{R_2}-\frac{1}{R_3}\right]V_B+\frac{1}{R_3}V_C=0\]
# and plugging in values
# \[\frac{1}{2}V_A-V_B+\frac{1}{4}V_C=0\]
# We're finally done with this one. We're left with an equation with constants and the unknown node voltages, nothing more.
# 
# \paragraph{KCL for Node C}
# The last KCL we will write is for node C. Two elements are connected to node C, both resistors in this circuit. I\tss{R3} is entering node C and therefore the term will be positive. I\tss{R4} is leaving node C and therefore the term will be negative.
# \[I*{R3}-I*{R4}=0\]
# The expression for I\tss{R3} matches what we wrote previously. I\tss{R4} again has the tip of the arrow pointing at ground giving us the expression
# \[I\_{R4}=\frac{V_C-0}{R_4}=\frac{V_C}{R_4}\]
# Substituting the two expressions into the KCL gives us
# \[\frac{V_B-V_C}{R_3}-\frac{V_C}{R_4}=0\]
# Breaking up the fractions and distributing the signs leads to
# \[\frac{1}{R_3}V_B-\frac{1}{R_3}V_C-\frac{1}{R_4}V_C=0\]
# before grouping like terms
# \[\frac{1}{R_3}V_B+\left[-\frac{1}{R_3}-\frac{1}{R_4}\right]V_C=0\]
# and plugging in values
# \[\frac{1}{4}V_B-\frac{3}{4}V_C=0\]
# And we're done with this one. Again, we're left with an equation with constants and the unknown node voltages, nothing more.
# 
# \paragraph{Solving the system of equations}
# We have three equations and three unknowns. Let's collect the equations from above here for easy reference.
# \begin{eqnarray}
# -\frac{1}{2}V_A+\frac{1}{2}V_B&=&-6\\
# \frac{1}{2}V_A-V_B+\frac{1}{4}V_C&=&0\\
# \frac{1}{4}V_B-\frac{3}{4}V_C&=&0
# \end{eqnarray}
# Be very careful transferring the coefficients to matrices as some terms have coefficients of zero and do not appear in the equations above.
# \[ \left[ \begin{array}{rrr}
# -\frac{1}{2}&\frac{1}{2}&0\\
# \frac{1}{2}&-1&\frac{1}{4}\\
# 0&\frac{1}{4}&-\frac{3}{4}
# \end{array} \right]^{-1}\left[\begin{array}{r}-6\\0\\0\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\end{array}\right]=\left[\begin{array}{r}26.4~\text{V}\\14.4~\text{V}\\4.8~\text{V}\end{array}\right]\]
# 
# \paragraph{Using the Node Voltages to Find Other Values}
# Once you know the node voltage you can find any other value in the circuit. Let's find $I_O$ for this example. $I_O$ is the current flowing down through $R_2$. The voltage across $R_2$ is the voltage at the tail of the current arrow, $V_B$ for this circuit, minus the voltage at the tip of the current arrow, ground (0~\text{V}) for this circuit. To find the current through the resistor we simply divide this voltage by the resistance.
# \[I_O=\frac{V_B-0}{R_2}=\frac{V_B}{R_2}=\frac{14.4~\text{V}}{4~\Omega}=3.6~\text{A}\]
# 
# \end{example}
# 
# \begin{example}
# Find $V_O$ using Nodal Analysis.
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[current source,lx={$I_{S1}$ and 2~\text{mA}}] (0,3)
# (0,3) to[resistor,lx={$R_1$ and 4~k\Om}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 2~k\Om}] (3,0)
# (3,3) to[resistor,lx={$R_3$ and 4~k\Om},v=$V_O$] (6,3)
# (6,3) to[current source,lx={$I_{S2}$ and 6~\text{mA}}] (6,0)
# (6,0) -- ((0,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# ;
# \end{circuitikz}\end{center}
# 
# \Solution
# Begin by locating the non-reference nodes and labeling the current directions through the passive components.
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[current source,lx={$I_{S1}$ and 2~\text{mA}}] (0,3)
# (0,3) to[resistor,lx={$R_1$ and 4~k\Om}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 2~k\Om}] (3,0)
# (3,3) to[resistor,lx={$R_3$ and 4~k\Om},v=$V_O$] (6,3)
# (6,3) to[current source,lx={$I_{S2}$ and 6~\text{mA}}] (6,0)
# (6,0) -- ((0,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# (0,3) node[above]{A}
# (3,3) node[above]{B}
# (6,3) node[above]{C}
# ;
# \draw[blue,-latex] (1,2.5) to[short,thick] (2,2.5);
# \draw[blue,-latex] (4,2.25) to[short,thick] (5,2.25);
# \draw[blue,-latex] (2.5,2) to[short,thick] (2.5,1);
# \end{circuitikz}\end{center}
# We will now write a KCL equation for each non-reference node.
# \paragraph{KCL for Node A}
# \[I*{S1}-I*{R1}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[I*{S1}-\frac{V_A-V_B}{R_1}=0\]
# A bit of algebra give us an equation with values and unknown know voltages; suitable for inclusion in the system of equations
# \[-\frac{V_A}{R_1}+\frac{V_B}{R_1}=-I*{S1}\]
# or with values
# \[-\frac{1}{4k}V_A+\frac{1}{4k}V_B=-2~\text{mA}\]
# 
# \paragraph{KCL for Node B}
# \[I*{R1}-I*{R2}-I\_{R3}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[\frac{V_A-V_B}{R_1}-\frac{V_B-0}{R_2}-\frac{V_B-V_C}{R_3}=0\]
# breaking up the fractions gives us
# \[\frac{V_A}{R_1}-\frac{V_B}{R_1}-\frac{V_B}{R_2}-\frac{V_B}{R_3}+\frac{V_C}{R_3}=0\]
# Gathering like terms yields
# \[\frac{1}{R_1}V_A+\left[-\frac{1}{R_1}-\frac{1}{R_2}-\frac{1}{R_3}\right]V_B+\frac{1}{R_3}V_C=0\]
# Substituting values leads to an equation suitable for inclusion in the system of equations
# \[\frac{1}{4k}V_A-\frac{1}{1k}V_B+\frac{1}{4k}V_C=0\]
# 
# \paragraph{KCL for Node C}
# \[I*{R3}-I*{S2}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[\frac{V*B-V_C}{R_3}-I*{S2}=0\]
# breaking up the fractions gives us
# \[\frac{V*B}{R_3}-\frac{V_C}{R_3}=I*{S2}\]
# Substituting values leads to an equation suitable for inclusion in the system of equations
# \[\frac{1}{4k}V_B-\frac{1}{4k}V_C=6~\text{mA}\]
# 
# \paragraph{Solve the System of Equations}
# Let's gather the results of the three KCLs written above
# \begin{alignat}{3}
# -\frac{1}{4k}V_A+&\frac{1}{4k}V_B&&=-2~\text{mA}\nonumber\\
# \frac{1}{4k}V_A-&\frac{1}{1k}V_B+\frac{1}{4k}V_C&&=0\nonumber\\
# &\frac{1}{4k}V_B-\frac{1}{4k}V_C&&=6~\text{mA}\nonumber
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrr}
# -\frac{1}{4k}&\frac{1}{4k}&0\\
# \frac{1}{4k}&-\frac{1}{1k}&\frac{1}{4k}\\
# 0&\frac{1}{4k}&-\frac{1}{4k}
# \end{array} \right]^{-1}\left[\begin{array}{r}-2~\text{mA}\\0\\6~\text{mA}\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\end{array}\right]=\left[\begin{array}{r}0~\text{V}\\-8~\text{V}\\-32~\text{V}\end{array}\right]\]
# 
# \paragraph{Find Other Values}
# Using the node voltages we can now find other values in the circuit. In this case $V_O$ is found with
# \[V\_{O}=V_B-V_C=-8-(-32)=24~\text{V}\]
# \end{example}
# 
# ## Nodal with Voltage Sources
# 
# Just as current sources create special cases for mesh analysis, voltage sources create special cases for Nodal analysis. We will write a KVL for each voltage supply in a circuit we are analyzing with nodal analysis. The rest of the equations in the system will be KCLs. These special cases are divided into two categories: 1) a voltage supply connecting a non-reference node and ground and 2) a voltage supply connecting two non-reference nodes. These next sections describe how to analyze circuits in these two categories using nodal analysis.
# 
# ### Voltage Sources Connected to Ground
# 
# \begin{example}
# Find $V_O$ and $I_O$ using Nodal Analysis.
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[current source,lx={$I_S$ and 2/3~\text{A}}] (0,3)
# (0,3) to[resistor,lx={$R_1$ and 6~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 12~\Om},i=$I_O$] (3,0)
# (3,3) to[resistor,lx={$R_3$ and 12~\Om},v=$V_O$] (6,3)
# (6,3) to[voltage source,lx^={8~\text{V} and $V_S$}] (6,0)
# (6,0) -- ((0,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# ;
# \end{circuitikz}\end{center}
# \Solution
# Begin by locating the non-reference nodes and labeling the current directions through the passive components. This step does not change due to the presence of the voltage supply.
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[current source,lx={$I_S$ and 2/3~\text{A}}] (0,3)
# (0,3) to[resistor,lx={$R_1$ and 6~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 12~\Om},i=$I_O$] (3,0)
# (3,3) to[resistor,lx={$R_3$ and 12~\Om},v=$V_O$] (6,3)
# (6,3) to[voltage source,lx_={8~\text{V} and $V_S$}] (6,0)
# (6.5,3) to[open,v^=$V_C$] (6.5,0)
# (6,0) -- ((0,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# (0,3) node[above]{A}
# (3,3) node[above]{B}
# (6,3) node[above]{C}
# ;
# \draw[blue,-latex] (1,2.5) to[short,thick] (2,2.5);
# \draw[blue,-latex] (4,2.25) to[short,thick] (5,2.25);
# \draw[blue,-latex] (2.5,2) to[short,thick] (2.5,1);
# \end{circuitikz}\end{center}
# The three non-reference node voltages are the unknown and require a system of three equations to find the solution. The presence of $V_S$ in the circuit leads us to write a KVL for node C. The other two equations will be KCLs written for nodes A and B.
# 
# I'll start with the KVL since it is the equation receiving special treatment in this example. The other two equations are written in a manner similar to the previous examples.
# 
# \paragraph{KVL for Node C}
# I've labeled $V_C$ on the annotated schematic above. I'll start by writing the KVL as we have in the past. Then I'll demonstrate a fast way to get the KVL right without having to think about the loop for the KVL.
# 
# We start at the ground node and move across $V_S$. Next we move across $V_C$ back to ground. This small loop gives us the KVL equation
# \[8-V_C=0\]
# We rearrange the equation to have the unknowns on the left and constants on the right as we have before
# \[V_C=8\]
# This equation is ready for the system of equations. It contains only constants and the unknowns.
# 
# Now let's look at another way to write the equation that will work for any KVL we write during nodal analysis. Anytime there is a voltage supply we can look for the node connected to the positive side of the supply ($V_C$ in this case) and the node connected to the negative side (ground, or 0~\text{V}, in this case). The node voltages are added together assuming the sign of the voltage polarity is it connected to. The right hand side of the equation is whatever the supply value is labeled as. For this example the equations is
# \[V_C-0=8\]
# which can be easily simplified to
# \[V_C=8\]
# the same result as we got above. I like this approach because it will work for any voltage in the circuit. The voltage supply does not need to be connected to ground. The voltage supply could be a dependent source. It works for any labeled voltage in a circuit even if it's across multiple components.
# 
# \paragraph{KCL for Node A}
# This KCL is straightforward if you are comfortable with the previous examples of nodal analysis.
# \[I*{S}-I*{R1}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[I*{S1}-\frac{V_A-V_B}{R_1}=0\]
# A bit of algebra give us an equation with values and unknown know voltages; suitable for inclusion in the system of equations
# \[-\frac{V_A}{R_1}+\frac{V_B}{R_1}=-I*{S1}\]
# or with values
# \[-\frac{1}{6}V_A+\frac{1}{6}V_B=-\frac{2}{3}~\text{A}\]
# 
# \paragraph{KCL for Node B}
# \[I*{R1}-I*{R2}-I\_{R3}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[\frac{V_A-V_B}{R_1}-\frac{V_B-0}{R_2}-\frac{V_B-V_C}{R_3}=0\]
# breaking up the fractions gives us
# \[\frac{V_A}{R_1}-\frac{V_B}{R_1}-\frac{V_B}{R_2}-\frac{V_B}{R_3}+\frac{V_C}{R_3}=0\]
# Gathering like terms yields
# \[\frac{1}{R_1}V_A+\left[-\frac{1}{R_1}-\frac{1}{R_2}-\frac{1}{R_3}\right]V_B+\frac{1}{R_3}V_C=0\]
# Substituting values leads to an equation suitable for inclusion in the system of equations
# \[\frac{1}{6}V_A-\frac{1}{3}V_B+\frac{1}{12}V_C=0\]
# 
# \paragraph{Solve the System of Equations}
# Let's gather the results of the three equations written above
# \begin{alignat}{3}
# &&V_C&=8~\text{V}\nonumber\\
# -\frac{1}{6}V_A+&\frac{1}{6}V_B&&=-\sfrac{2}{3}~\text{A}\nonumber\\
# \frac{1}{6}V_A-&\frac{1}{3}V_B+&\frac{1}{12}V_C&=0~\text{A}\nonumber
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrr}
# 0&0&1\\
# -\frac{1}{6}&\frac{1}{6}&0\\
# \frac{1}{6}&-\frac{1}{3}&\frac{1}{12}
# \end{array} \right]^{-1}\left[\begin{array}{r}8~\text{V}\\-\sfrac{2}{3}~\text{A}\\0~\text{A}\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\end{array}\right]=\left[\begin{array}{r}12~\text{V}\\8~\text{V}\\8~\text{V}\end{array}\right]\]
# 
# \paragraph{Find Other Values}
# Using the node voltages we can now find other values in the circuit. In this case $V_O$ is found with
# \[V*{O}=V_B-V_C=8-8=0~\text{V}\]
# and $I_O$ is found with
# \[I*{O}=\frac{V_B-0}{12}=\sfrac{2}{3}~\text{A}\]
# \end{example}
# 
# ### Voltage Sources Connected to Two Non-ground Nodes
# 
# When a voltage supply connects two non-reference nodes we call it a `supernode''. We treat the voltage supply in a similar manner as the previous example. We write a KVL that includes that voltage supply. The problem we face is then writing a sufficient number of KCL equations to complete the system. Kirchhoff's Current law can be stated more broadly to address this problem. Rather than stating that the algebraic sum of current entering a \textbf{node} is zero, we say that the algebraic sum of currents entering a \textbf{bounded region} is zero. Therefore, we can draw the bounded region around the voltage supply including the two nodes it connects to and write a KCL for this `super node''. Let's look at an example.
# 
# \begin{example}
# Find $I_O$ using nodal analysis
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 3~\Om}] (0,3)
# (0,3) to[resistor,lx={$R_2$ and 6~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_3$ and 12~\Om}] (3,0)
# (3,3) to[voltage source,lx={$V_S$ and 8~\text{V}},i>=$I_O$] (6,3)
# (6,0) to[R,lx={$R_4$ and 4~\Om}] (6,3)
# (6,3) to[resistor,lx={$R_5$ and 8~\Om}] (9,3)
# (9,3) to[resistor,lx={$R_6$ and 5~\Om}] (9,0)
# 
#     (9,0) -- ((0,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# 
# ;
# \end{circuitikz}\end{center}
# 
# \Solution
# We start by looking for non-reference nodes and labeling current directions as before. I'll also draw the bounded region that forms the super node.
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 3~\Om}] (0,3)
# (0,3) to[resistor,lx={$R_2$ and 6~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_3$ and 12~\Om}] (3,0)
# (3,3) to[voltage source,lx={$V_S$ and 8~\text{V}},i>=$I_O$] (6,3)
# (6,0) to[R,lx={$R_4$ and 4~\Om}] (6,3)
# (6,3) to[resistor,lx={$R_5$ and 8~\Om}] (9,3)
# (9,3) to[resistor,lx={$R_6$ and 5~\Om}] (9,0)
# 
#     (9,0) -- ((0,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
#     (0,3) node[above]{A}
#     (3,3) node[above]{B}
#     (6,3) node[above]{C}
#     (9,3) node[above]{D}
# 
# ;
# \draw[blue,-latex] (1,2.5) to[short,thick] (2,2.5);
# \draw[blue,-latex] (7,2.5) to[short,thick] (8,2.5);
# \draw[blue,-latex] (2.5,2) to[short,thick] (2.5,1);
# \draw[blue,-latex] (.5,2) to[short,thick] (.5,1);
# \draw[blue,-latex] (6.5,2) to[short,thick] (6.5,1);
# \draw[blue,-latex] (8.5,2) to[short,thick] (8.5,1);
# 
# \draw[dashed,ultra thick,orange] (2.5,2.4) rectangle (6.5,4.1)
# (2.5,4.25) node[right]{Super Node};
# 
# \end{circuitikz}\end{center}
# 
# The circuit has four non-reference nodes meaning we will write four equations. We write one KVL since there is one voltage source. The rest of the equations, three in this case, are KCLs. Since there is a super node in this circuit one of the KCLs will be written for that super node.
# 
# \paragraph{KVL for $V_S$}
# Let's start with the KVL equation. We write this KVL in a similar manner to the previous example. Here are the questions I ask myself when writing a KVL in this context:
# \begin{enumerate}
# \item Which node is connected to the \textbf{positive} side of the source? \textbf{Node B}
# \item Which node is connected to the \textbf{negative} side of the source? \textbf{Node C}
# \item What is the voltage source value? \textbf{8~\text{V}}
# \end{enumerate}
# The answers given are specific to this example but the questions are common for all KVLs written during nodal analysis. This leads to the KVL equation
# \[V_B-V_C=8\]
# 
# \paragraph{KCL for Super-node (B and C)}
# This is the equation in the example that is a little different from what we've done previously. Look at the bounded region in the annotated schematic above. How many currents flow in or out of that region? All four currents will be included in the KCL
# \[I*{R2}-I*{R3}-I*{R4}-I*{R5}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[\frac{V_A-V_B}{R_2}-\frac{V_B-0}{R_3}-\frac{V_C-0}{R_4}-\frac{V_C-V_D}{R_5}=0\]
# breaking up the fractions gives us
# \[\frac{V_A}{R_2}-\frac{V_B}{R_2}-\frac{V_B}{R_3}-\frac{V_C}{R_4}-\frac{V_C}{R_5}+\frac{V_D}{R_5}=0\]
# Gathering like terms yields
# \[\frac{1}{R_2}V_A+\left[-\frac{1}{R_2}-\frac{1}{R_3}\right]V_B+\left[-\frac{1}{R_4}-\frac{1}{R_5}\right]V_C+\frac{1}{R_5}V_D=0\]
# Substituting values leads to an equation suitable for inclusion in the system of equations
# \[\frac{1}{6}V_A-\frac{1}{4}V_B-\frac{3}{8}V_C+\frac{1}{8}V_D=0\]
# 
# \paragraph{KCL for Node A}
# The next two equations are straightforward if you are comfortable with the previous examples of nodal analysis.
# \[-I*{R1}-I*{R2}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[-\frac{V_A-0}{R_1}-\frac{V_A-V_B}{R_2}=0\]
# A bit of algebra give us an equation with values and unknown know voltages; suitable for inclusion in the system of equations
# \[\left[-\frac{1}{R_1}-\frac{1}{R_2}\right]V_A+\frac{V_B}{R_2}=0\]
# or with values
# \[-\frac{1}{2}V_A+\frac{1}{6}V_B=0\]
# 
# \paragraph{KCL for Node D}
# Last one!
# \[I*{R5}-I*{R6}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[\frac{V_C-V_D}{R_5}-\frac{V_D-0}{R_6}=0\]
# A bit of algebra give us an equation with values and unknown know voltages; suitable for inclusion in the system of equations
# \[\frac{V_C}{R_5}+\left[-\frac{1}{R_5}-\frac{1}{R_6}\right]V_D=0\]
# or with values
# \[\frac{1}{8}V_C-\frac{13}{40}V_D=0\]
# 
# \paragraph{Solve the System of Equations}
# Let's gather the results of the four equations written above
# \begin{alignat}{4}
# ~&~~\text{V}\_B-&~\text{V}\_C~~&~&=8\nonumber\\
# \frac{1}{6}V_A-&\frac{1}{4}V_B-&\frac{3}{8}V_C+&\frac{1}{8}V_D&=0\nonumber\\
# -\frac{1}{2}V_A+&\frac{1}{6}V_B&~&~&=0\nonumber\\
# &&\frac{1}{8}V_C-&\frac{13}{40}V_D&=0\nonumber
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrrr}
# 0&1&-1&0\\
# \frac{1}{6}&-\frac{1}{4}&-\frac{3}{8}&\frac{1}{8}\\
# -\frac{1}{2}&\frac{1}{6}&0&0\\
# 0&0&\frac{1}{8}&-\frac{13}{40}\\
# \end{array} \right]^{-1}\left[\begin{array}{r}8\\0\\0\\0\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\\V_D\end{array}\right]=\left[\begin{array}{r}1.67~\text{V}\\5.02~\text{V}\\-2.98~\text{V}\\-1.15~\text{V}\end{array}\right]\]
# 
# \paragraph{Find Other Values}
# Now that we have the node voltages we can go find other values in the circuit. I chose $I_O$ through the voltage supply as we have not treated this type of value yet. The typical approach of using Ohm's law by finding the difference in node voltages and dividing by the resistance will not work here since we don't know the resistance of the voltage source. Since ohm's law will not work to find a current we'll rely on the other fundamental law that involves currents, KCL. We'll pick a node adjacent to $I_O$. We'll use node C, but node B would work just as well. Here is the KCL at node C including the term for $I_O$.
# \[I*O-I*{R4}-I\_{R5}=0\]
# Now we use Ohm's law in a similar manner as previously, however, the node voltages are no longer unknowns.
# \[I_O-\frac{V_C-0}{R_4}-\frac{V_C-V_D}{R_5}=0\]
# Now we solve for $I_O$ and substitute the known values
# \[I_O=\frac{-2.98}{4}+\frac{-2.98-(-1.15)}{8}=-975.4~\text{mA}\]
# 
# \end{example}
# 
# \begin{example}
# Find $V_O$ using nodal analysis
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 3~\Om}] (0,3)
# (0,3) to[resistor,lx={$R_2$ and 6~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_3$ and 12~\Om}] (3,0)
# (3,3) to[voltage source,lx={$V_S$ and 8~\text{V}}] (5,3)
# (5,3) to[resistor,lx={$R_4$ and 8~\Om}] (8,3)
# (8,3) to[resistor,lx={$R_5$ and 5~\Om}] (8,0)
# (5,3) to[open,v^=$V_O$] (5,0)
# 
#     (8,0) -- ((0,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# 
# ;
# \end{circuitikz}\end{center}
# 
# \Solution
# When I us this example in class there is a gotcha moment for about half the students. Count how many non-reference nodes before I label them in the next figure. If you said three, you're not alone. Many students miss the node in between $V_S$ and $R_4$. There are, in fact, four non-reference nodes. I'll label them below along with the usual notations. There is also a voltage supply leading us to write a KVL for one equation instead of
# a KCL. Lastly, that voltage supply connects two non-reference nodes forming a super-node. One of the KCL equations will be written for the bounded region that encloses the two nodes connect to the voltage supply.
# 
# Here is the schematic as I would annotate it prior to writing the system of equations for analysis
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 3~\Om}] (0,3)
# (0,3) to[resistor,lx={$R_2$ and 6~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_3$ and 12~\Om}] (3,0)
# (3,3) to[voltage source,lx={$V_S$ and 8~\text{V}}] (5,3)
# (5,3) to[resistor,lx={$R_4$ and 8~\Om}] (8,3)
# (8,3) to[resistor,lx_={$R_5$ and 5~\Om}] (8,0)
# (5,3) to[open,v^=$V_O$] (5,0)
# 
#     (8,0) -- ((0,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# 
#     (0,3) node[above]{A}
#     (3,3) node[above]{B}
#     (5,3) node[above]{C}
#     (8,3) node[above]{D}
# 
# ;
# \draw[blue,-latex] (1,2.5) to[short,thick] (2,2.5);
# \draw[blue,-latex] (6,2.5) to[short,thick] (7,2.5);
# \draw[blue,-latex] (2.5,2) to[short,thick] (2.5,1);
# \draw[blue,-latex] (.5,2) to[short,thick] (.5,1);
# 
# \draw[blue,-latex] (8.5,2) to[short,thick] (8.5,1);
# 
# \draw[dashed,ultra thick,orange] (2.5,2.4) rectangle (5.5,4.1)
# (2.5,4.25) node[right]{Super Node};
# \end{circuitikz}\end{center}
# 
# \paragraph{KVL for $V_S$}
# Here are the questions I ask myself when writing a KVL in this context:
# \begin{enumerate}
# \item Which node is connected to the \textbf{positive} side of the source? \textbf{Node B}
# \item Which node is connected to the \textbf{negative} side of the source? \textbf{Node C}
# \item What is the voltage source value? \textbf{8~\text{V}}
# \end{enumerate}
# The answers given are specific to this example but the questions are common for all KVLs written during nodal analysis. This leads to the KVL equation
# \[V_B-V_C=8\]
# 
# \paragraph{KCL for Super-node (B and C)}
# Look at the bounded region in the annotated schematic above. How many currents flow in or out of that region? All three currents will be included in the KCL
# \[I*{R2}-I*{R3}-I\_{R4}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[\frac{V_A-V_B}{R_2}-\frac{V_B-0}{R_3}-\frac{V_C-V_D}{R_4}=0\]
# breaking up the fractions gives us
# \[\frac{V_A}{R_2}-\frac{V_B}{R_2}-\frac{V_B}{R_3}-\frac{V_C}{R_4}+\frac{V_D}{R_4}=0\]
# Gathering like terms yields
# \[\frac{1}{R_2}V_A+\left[-\frac{1}{R_2}-\frac{1}{R_3}\right]V_B-\frac{1}{R_4}V_C+\frac{1}{R_4}V_D=0\]
# Substituting values leads to an equation suitable for inclusion in the system of equations
# \[\frac{1}{6}V_A-\frac{1}{4}V_B-\frac{1}{8}V_C+\frac{1}{8}V_D=0\]
# 
# \paragraph{KCL for Node A}
# The next two equations are straightforward if you are comfortable with the previous examples of nodal analysis.
# \[-I*{R1}-I*{R2}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[-\frac{V_A-0}{R_1}-\frac{V_A-V_B}{R_2}=0\]
# A bit of algebra give us an equation with values and unknown know voltages; suitable for inclusion in the system of equations
# \[\left[-\frac{1}{R_1}-\frac{1}{R_2}\right]V_A+\frac{V_B}{R_2}=0\]
# or with values
# \[-\frac{1}{2}V_A+\frac{1}{6}V_B=0\]
# 
# \paragraph{KCL for Node D}
# Last one!
# \[I*{R5}-I*{R6}=0\]
# and use Ohm's law where we can to rewrite the currents in terms of the node voltages
# \[\frac{V_C-V_D}{R_5}-\frac{V_D-0}{R_6}=0\]
# A bit of algebra give us an equation with values and unknown know voltages; suitable for inclusion in the system of equations
# \[\frac{V_C}{R_5}+\left[-\frac{1}{R_5}-\frac{1}{R_6}\right]V_D=0\]
# or with values
# \[\frac{1}{8}V_C-\frac{13}{40}V_D=0\]
# 
# \paragraph{Solve the System of Equations}
# Let's gather the results of the four equations written above
# \begin{alignat}{4}
# ~&~~\text{V}\_B-&~\text{V}\_C~~&~&=8\nonumber\\
# \frac{1}{6}V_A-&\frac{1}{4}V_B-&\frac{1}{8}V_C+&\frac{1}{8}V_D&=0\nonumber\\
# -\frac{1}{2}V_A+&\frac{1}{6}V_B&~&~&=0\nonumber\\
# &&\frac{1}{8}V_C-&\frac{13}{40}V_D&=0\nonumber
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrrr}
# 0&1&-1&0\\
# \frac{1}{6}&-\frac{1}{4}&-\frac{1}{8}&\frac{1}{8}\\
# -\frac{1}{2}&\frac{1}{6}&0&0\\
# 0&0&\frac{1}{8}&-\frac{13}{40}\\
# \end{array} \right]^{-1}\left[\begin{array}{r}8\\0\\0\\0\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\\V_D\end{array}\right]=\left[\begin{array}{r}755.9~\text{mV}\\2.268~\text{V}\\-5.732~\text{V}\\-2.205~\text{V}\end{array}\right]\]
# 
# %START EDITING HERE
# \paragraph{Find Other Values}
# Now that we have the node voltages we can go find other values in the circuit. If that value is a voltage look for the node on the positive side of the voltage, $V_C$ in this case. Subtract from that the node voltage on the negative side, ground in this case. Here it is as an equation
# \[V_O=V_C-0=-5.732-0=-5.732~\text{V}\]
# The negative side won't always be connected to ground as it is here. In that case the second term will be non-zero but the form of the equation does not change.
# 
# \end{example}
# 
# ### Nodal Analysis with Dependent Supplies
# 
# \begin{example}
# Find $I_O$ using nodal analysis.
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 8~\Om},i^<=$I_O$] (0,3)
# (0,3) to[current source,lx={$I_{S1}$ and 4~\text{A}}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 2~\Om}] (3,0)
# (3,3) to[controlled current source,lx={$I_{S2}$ and 2$I_O$}] (6,3)
# (6,3) to[resistor,lx={$R_3$ and 4~\Om}] (6,0)
# (0,5) to[resistor,lx={$R_4$ and 1~\Om}] (6,5)
# (0,3) -- (0,5)
# (6,3) -- (6,5)
# 
#     (6,0) -- ((0,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# 
# ;
# \end{circuitikz}\end{center}
# 
# \Solution
# There are no voltage supplies in this circuit so all of the equations will be KCL equations. There are three non-reference nodes so there will be three KCL equations. The difference in this problem is the presence of the dependent current source $I_{S2}$. We'll write an expression for the control variable, $I_O$ in this case. Here is the annotated schematic:
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 8~\Om},i^<=$I_O$] (0,3)
# (0,3) to[current source,lx={$I_{S1}$ and 4~\text{A}}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 2~\Om}] (3,0)
# (3,3) to[controlled current source,lx={$I_{S2}$ and 2$I_O$}] (6,3)
# (6,3) to[resistor,lx={$R_3$ and 4~\Om}] (6,0)
# (0,5) to[resistor,lx={$R_4$ and 1~\Om}] (6,5)
# (0,3) -- (0,5)
# (6,3) -- (6,5)
# 
#     (6,0) -- ((0,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
#     (0,3) node[left]{A}
#     (3,3) node[above]{B}
#     (6,3) node[right]{C}
# 
# ;
# \draw[blue,-latex] (2.5,4.5) to[short,thick] (3.5,4.5);
# \draw[blue,-latex] (.5,2) to[short,thick] (.5,1);
# \draw[blue,-latex] (2.5,2) to[short,thick] (2.5,1);
# \draw[blue,-latex] (5.5,2) to[short,thick] (5.5,1);
# \end{circuitikz}\end{center}
# 
# \paragraph{Control Variable Expression}
# We'll need this expression to relate the control variable to the unknown node voltages. Our goal when writing the system equations is to have equations that are comprised of constants and the unknown variables. The presence of a control variable in the system is address by substituting with this expression.
# 
# This expression is always written using the direction indicated on the schematic, not with your chosen direction during annotation of the schematic. In this case, $V_A$ is at the tail of the arrow, ground (0~\text{V}) is at the tip, and the current flows through $R_1$.
# \[I_O=\frac{V_A-0}{R_1}=\frac{V_A}{R_1}\]
# 
# \paragraph{KCL for Node A}
# The KCL equation for node A is similar to previous examples since it does not involve the dependent supply. We start with the three currents entering or leaving that node
# \[-I*{R1}-I*{S1}-I*{R4}=0\]
# Use KVL and Ohm's law to rewrite the equation in terms of the unknown node voltages
# \[-\frac{V_A-0}{R_1}-I*{S1}-\frac{V*A-V_C}{R_4}=0\]
# A bit of algebra give us an equation with values and unknown know voltages; suitable for inclusion in the system of equations
# \[\left[-\frac{1}{R_1}-\frac{1}{R_4}\right]V_A+\frac{V_C}{R_4}=I*{S1}\]
# or with values
# \[-\frac{9}{8}V_A+V_C=4~\text{A}\]
# 
# \paragraph{KCL for Node B}
# Node B involves the dependent supply so we will use the expression for the control variable we wrote earlier. Other than that substitution, we approach the KCL equation in the same manner. We start with the three currents entering or leaving the node
# \[I*{S1}-I*{R2}-I*{S2}=0\]
# Use KVL and Ohm's law to rewrite the equation in terms of the unknown node voltages. I've also replaced $I*{S2}$ with the gain and control variable for that supply
# \[I*{S1}-\frac{V_B-0}{R_2}-2I*{O}=0\]
# We need to get rid of the control variable. To do so, we substitute the expression for the control variable in terms of the unknown node voltages
# \[I*{S1}-\frac{V_B-0}{R_2}-2\left[\frac{V_A}{R_1}\right]=0\]
# Now that we have an equation comprised only of constants and unknown node voltages we can do some algebra to group like terms
# \[-\frac{2}{R_1}V_A-\frac{V_B}{R_2}=-I*{S1}\]
# and substitute values
# \[-\frac{1}{4}V_A-\frac{1}{2}V_B=-4~\text{A}\]
# 
# \paragraph{KCL for Node C}
# Node B involves the dependent supply so we will use the expression for the control variable we wrote earlier. Other than that substitution, we approach the KCL equation in the same manner. We start with the three currents entering or leaving the node
# \[I*{R4}+I*{S2}-I*{R3}=0\]
# Use KVL and Ohm's law to rewrite the equation in terms of the unknown node voltages. I've also replaced $I*{S2}$ with the gain and control variable for that supply
# \[\frac{V*A-V_C}{R_4}+2I*{O}-\frac{V_C-0}{R_3}=0\]
# We need to get rid of the control variable. To do so, we substitute the expression for the control variable in terms of the unknown node voltages
# \[\frac{V_A-V_C}{R_4}+2\left[\frac{V_A}{R_1}\right]-\frac{V_C-0}{R_3}=0\]
# Now that we have an equation comprised only of constants and unknown node voltages we can do some algebra to group like terms
# \[\left[\frac{1}{R_4}+\frac{2}{R_1}\right]V_A+\left[-\frac{1}{R_3}-\frac{1}{R_4}\right]V_C=0\]
# and substitute values
# \[\frac{5}{4}V_A-\frac{5}{4}V_C=0\]
# 
# \paragraph{Solve the System of Equations}
# Let's gather the results of the three equations written above
# \begin{alignat}{3}
# -\frac{9}{8}V_A&&+V_C&=4~\text{A}\nonumber\\
# -\frac{1}{4}V_A&-\frac{1}{2}V_B&&=-4~\text{A}\nonumber\\
# \frac{5}{4}V_A&&-\frac{5}{4}V_C&=0~\text{A}\nonumber
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrr}
# -\frac{9}{8}&0&1\\
# -\frac{1}{4}&-\frac{1}{2}&0\\
# \frac{5}{4}&0&-\frac{5}{4}
# \end{array} \right]^{-1}\left[\begin{array}{r}4~\text{A}\\-4~\text{A}\\0~\text{A}\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\end{array}\right]=\left[\begin{array}{r}-32~\text{V}\\80~\text{V}\\-32~\text{V}\end{array}\right]\]
# 
# \paragraph{Find Other Values}
# Since we're looking for $I_O$, an expression we've already used in this analysis, we simply use the node voltage values we just calculated in that same expression.
# \[I_O=\frac{V_A-0}{R_1}=\frac{-32~\text{V}}{8~\Omega}=-4~\text{A}\]
# 
# \end{example}
# 
# %%%
# \pagebreak
# %%%
# \begin{example}
# Find $V_O$ using nodal analysis
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 10~\Om}] (0,3)
# (0,3) to[R,lx={$R_2$ and 4~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_3$ and 5~\Om}] (3,0)
# (3,3) to[R,lx={$R_4$ and 2~\Om},v_<=$V_O$] (6,3)
# (6,0) to[current source,lx={I\tss{S3} and 4~\text{A}}] (6,3)
# (0,5) to[current source,lx={$I_{S2}$ and 2~\text{A}}] (6,5)
# (-2,0) to[controlled current source,lx={$I_{S1}$ and 3$V_O$}] (-2,3)
# (-2,3)--(0,3)
# (0,3) -- (0,5)
# (6,3) -- (6,5)
# (6,0) -- ((-2,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# ;
# \end{circuitikz}\end{center}
# 
# \Solution
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 10~\Om}] (0,3)
# (0,3) to[R,lx={$R_2$ and 4~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_3$ and 5~\Om}] (3,0)
# (3,3) to[R,lx={$R_4$ and 2~\Om},v_<=$V_O$] (6,3)
# (6,0) to[current source,lx={I\tss{S3} and 4~\text{A}}] (6,3)
# (0,5) to[current source,lx={$I_{S2}$ and 2~\text{A}}] (6,5)
# (-2,0) to[controlled current source,lx={$I_{S1}$ and 3$V_O$}] (-2,3)
# (-2,3)--(0,3)
# (0,3) -- (0,5)
# (6,3) -- (6,5)
# (6,0) -- ((-2,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# (0,3.2) node[left]{A}
# (3,3) node[above]{B}
# (6,3.2) node[right]{C}
# ;
# \draw[blue,-latex] (1,2.5) to[short,thick] (2,2.5);
# \draw[blue,-latex] (.5,2) to[short,thick] (.5,1);
# \draw[blue,-latex] (2.5,2) to[short,thick] (2.5,1);
# \draw[blue,-latex] (5,2.25) to[short,thick] (4,2.25);
# \end{circuitikz}\end{center}
# \paragraph{Control Variable Expression}
# \[V*O=V_C-V_B\]
# \paragraph{KCL for node A}
# \[I*{S1}-I*{R1}-I*{R2}-I*{S2}=0\]
# \[3V_O-\frac{V_A-0}{R_1}-\frac{V_A-V_B}{R_2}-I*{S2}=0\]
# \[3\left(V*C-V_B\right)-\frac{V_A}{10}-\frac{V_A-V_B}{4}-2=0\]
# \[\left[-\frac{1}{10}-\frac{1}{4}\right]V_A+\left[-3+\frac{1}{4}\right]V_B+3V_C=2\]
# \[-\frac{7}{20}V_A-\frac{11}{4}V_B+3V_C=2\]
# \paragraph{KCL for node B}
# \[I*{R2}-I*{R3}+I*{R4}=0\]
# \[\frac{V*A-V_B}{R_2}-\frac{V_B-0}{R_3}+\frac{V_C-V_B}{R_4}=0\]
# \[\frac{1}{R_2}V_A+\left[-\frac{1}{R_2}-\frac{1}{R_3}-\frac{1}{R_4}\right]V_B+\frac{1}{R_4}V_C=0\]
# \[\frac{1}{4}V_A+\left[-\frac{1}{4}-\frac{1}{5}-\frac{1}{2}\right]V_B+\frac{1}{2}V_C=0\]
# \[\frac{1}{4}V_A-\frac{19}{20}V_B+\frac{1}{2}V_C=0\]
# \paragraph{KCL for node C}
# \[I*{S2}-I*{R4}+I*{S3}=0\]
# \[I*{S2}-\frac{V_C-V_B}{R_4}+I*{S3}=0\]
# \[2-\frac{V_C-V_B}{2}+4=0\]
# \[-\frac{V_C-V_B}{2}=-6\]
# \[\frac{1}{2}V_B-\frac{1}{2}V_C=-6\]
# \paragraph{Solve the System of Equations}
# Let's gather the results of the three equations written above
# \begin{alignat}{3}
# -\frac{7}{20}V_A&-\frac{11}{4}V_B&+3V_C&=2~\text{A}\nonumber\\
# \frac{1}{4}V_A&-\frac{19}{20}V_B&+\frac{1}{2}V_C&=0~\text{A}\nonumber\\
# &\frac{1}{2}V_B&-\frac{1}{2}V_C&=-6~\text{A}\nonumber%alignment
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrr}
# -\frac{7}{20}&-\frac{11}{4}&3\\
# \frac{1}{4}&-\frac{19}{20}&\frac{1}{2}\\
# 0&\frac{1}{2}&-\frac{1}{2}
# \end{array} \right]^{-1}\left[\begin{array}{r}2~\text{A}\\0~\text{A}\\-6~\text{A}\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\end{array}\right]=\left[\begin{array}{r}176.84~\text{V}\\111.58~\text{V}\\123.58~\text{V}\end{array}\right]\]
# \paragraph{Find Other Values}
# \[V_O=V_C-V_B=123.58-111.58=12~\text{V}\]
# 
# \end{example}
# 
# %%%
# \pagebreak
# %%%
# \begin{example}
# Find $I_x$ using nodal analysis.
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_3$ and 24~\Om}] (0,3) to[R,lx={$R_1$ and 8~\Om}] (0,6)
# (3,0) to[R,lx={$R_4$ and 6~\Om}] (3,3) to[R,lx={$R_2$ and 12~\Om},i>=$I_x$] (3,6)
# (0,0) node[sground,scale=0.5]{}
# (3,3) to[controlled voltage source,l=4~$I_x$] (0,3)
# (6,6) to[voltage source,lx={$V_S$ and 15~\text{V}}] (6,0)
# (0,0) to[short] (6,0)
# (0,6) to[short] (6,6)
# ;
# \end{circuitikz}\end{center}
# \Solution
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_3$ and 24~\Om}] (0,3) to[R,lx={$R_1$ and 8~\Om}] (0,6)
# (3,0) to[R,lx={$R_4$ and 6~\Om}] (3,3) to[R,lx={$R_2$ and 12~\Om},i>=$I_x$] (3,6)
# (0,0) node[sground,scale=0.5]{}
# (3,3) to[controlled voltage source,l=4~$I_x$] (0,3)
# (6,6) to[voltage source,lx={$V_S$ and 15~\text{V}}] (6,0)
# (0,0) to[short] (6,0)
# (0,6) to[short] (6,6)
# (0,3) node[left]{A}
# (3,3) node[right]{B}
# (3,6) node[above]{C}
# ;
# \draw[blue,-latex] (.5,2) to[short,thick] (.5,1);
# \draw[blue,-latex] (.5,5) to[short,thick] (.5,4);
# \draw[blue,-latex] (3.5,2) to[short,thick] (3.5,1);
# \draw[blue,-latex] (3.5,4) to[short,thick] (3.5,5);
# \draw[dashed,ultra thick,orange] (-.5,2.1) rectangle (3.5,3.6)
# (.5,3.85) node[right]{Super Node};
# 
#     \end{circuitikz}\end{center}
# 
#     \paragraph{Control Variable Expression}
#     \[I_x=\frac{V_B-V_C}{R_2}\]
# 
#     \paragraph{KVL for super-node (A and B)}
#     \[V_B-V_A=4I_x\]
#     \[V_B-V_A=4\frac{V_B-V_C}{R_2}\]
#     \[V_B-V_A-4\frac{V_B-V_C}{R_2}=0\]
#     \[-V_A+\left[1-\frac{4}{R_2}\right]V_B+\frac{4}{R_2}V_C=0\]
#     \[-V_A+\left[1-\frac{4}{12}\right]V_B+\frac{4}{12}V_C=0\]
#     \[-V_A-\frac{2}{3}V_B+\frac{1}{3}V_C=0\]
# 
#     \paragraph{KCL for super-node (A and B)}
#     \[I_{R1}-I_{R2}-I_{R3}-I_{R4}=0\]
#     \[\frac{V_C-V_A}{R_1}-\frac{V_B-V_C}{R_2}-\frac{V_A-0}{R_3}-\frac{V_B-0}{R_4}=0\]
#     \[\left[-\frac{1}{R_1}-\frac{1}{R_3}\right]V_A+\left[-\frac{1}{R_2}-\frac{1}{R_4}\right]V_B+\left[\frac{1}{R_1}+\frac{1}{R_2}\right]V_C=0\]
#     \[\left[-\frac{1}{8}-\frac{1}{24}\right]V_A+\left[-\frac{1}{12}-\frac{1}{6}\right]V_B+\left[\frac{1}{8}+\frac{1}{12}\right]V_C=0\]
#     \[-\frac{1}{6}V_A-\frac{1}{4}V_B+\frac{5}{24}V_C=0\]
# 
#     \paragraph{KVL for node C}
#     \[V_C-0=V_S\]
#     \[V_C=15~\text{V}\]
# 
#     \paragraph{Solve the System of Equations}
#     Let's gather the results of the three equations written above
#     \begin{alignat}{3}
#     	-V_A&-\frac{2}{3}V_B&+\frac{1}{3}V_C&=0~\text{A}\nonumber\\
#     	-\frac{1}{6}V_A&-\frac{1}{4}V_B&+\frac{5}{24}V_C&=0~\text{A}\nonumber\\
#     	&&V_C&=15~\text{V}\nonumber%alignment
#     \end{alignat}
#     and put them in matrix form
#     \[ \left[ \begin{array}{rrr}
#     -1&-\frac{2}{3}&\frac{1}{3}\\
#     -\frac{1}{6}&-\frac{1}{4}&\frac{5}{24}\\
#     0&0&1
#     \end{array} \right]^{-1}\left[\begin{array}{r}0~\text{A}\\0~\text{A}\\15~\text{V}\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\end{array}\right]=\left[\begin{array}{r}-6~\text{V}\\16.5~\text{V}\\15~\text{V}\end{array}\right]\]
# 
#     \paragraph{Find Other Values}
#     \[I_x=\frac{16.5-15}{12}=125~\text{mA}\]
# 
# \end{example}
# 
# ### Nodal Analysis with an Ideal Operational Amplifier
# 
# \begin{framed}
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=1](opamp){}
# (-1.5,0) node[left]{\textbf{Inputs}}
# (1.5,0) node[right]{\textbf{Output}}
# ;
# \end{circuitikz}
# \end{center}
# \Large\textbf{Assumptions about an ideal op-amp:}\normalsize
# \begin{enumerate}
# \item The voltage at the input nodes are equal (V\tss{+}=V\tss{-})
# \item No current enters or leaves the inputs (I\tss{+}=I\tss{-}=0)
# \end{enumerate}
# \end{framed}
# 
# \begin{example}
# Find $V_O$ using nodal analysis
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=1](opamp){}
# (opamp.out) -- +(1,0) coordinate (output)
# (opamp.-) to[R,l=3~k\Om] ($(opamp.-)+(-3,0)$) to[voltage source,l_=10~\text{V}] ($(opamp.-)+(-3,-3)$)
# (opamp.+) |- ($(opamp.-)+(-3,-3)$)
# (output) to[R,l=5~k\Om,v=$V_O$] ($(output)+(0,-2.5)$) |- ($(opamp.-)+(-3,-3)$)
# (opamp.-) to[short] ($(opamp.-)+(0,1.5)$) to[R,l=15~k\Om] ($(opamp.-)+(3,1.5)$) -| (output)
# ($(opamp.-)+(-3,-3)$) node[sground,scale=0.5]{}
# ;
# \end{circuitikz}
# \end{center}
# This is a circuit that you could easily look up in a book, apply the given equations, and find whatever value you seek. However, if you don't know where to find such a reference, or if the circuit is altered even slightly, this approach will fail. Instead, we can use the assumptions stated above and our knowledge of nodal analysis to develop a system of equations. We can then solve that system as we have previously to find the node voltages and any other values we need.
# 
# \Solution
# The circuit has three non-reference nodes which I will label below. Just as before, the voltage supply leads us to write a KVL equation in place of one of the KCL equations. In a circuit with op-amps we also replace a KCL equation with a KVL for each op-amp. That KVL will reflect the first assumption stated above. Therefore, the system of equations for this analysis will consist of a KVL for the voltage supply, a KVL for the op-amp, and another KCL for one of the nodes.
# 
# Let's start by annotating the circuit just as before. The op-amp is not a passive component and therefore we do not assign it a current direction.%START EDITING HERE
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=1](opamp){}
# (opamp.out) -- +(1,0) coordinate (output)
# (opamp.-) to[R,l=3~k\Om] ($(opamp.-)+(-3,0)$) to[voltage source,l_=10~\text{V}] ($(opamp.-)+(-3,-3)$)
# (opamp.+) |- ($(opamp.-)+(-3,-3)$)
# (output) to[R,l=5~k\Om,v=$V_O$] ($(output)+(0,-2.5)$) |- ($(opamp.-)+(-3,-3)$)
# (opamp.-) to[short] ($(opamp.-)+(0,1.5)$) to[R,l=15~k\Om] ($(opamp.-)+(3,1.5)$) -| (output)
# ($(opamp.-)+(-3,-3)$) node[sground,scale=0.5]{}
# ($(opamp.-)+(-3,0)$) node[left]{A}
# (opamp.-) node[below]{B}
# (output) node[right]{C}
# ;
# \draw[blue,-latex] ($(opamp.-)+(-2,.5)$) to[short,thick] ($(opamp.-)+(-1,.5)$);
# \draw[blue,-latex] ($(opamp.-)+(1,1)$) to[short,thick] ($(opamp.-)+(2,1)$);
# \draw[blue,-latex] ($(output)+(-.9,-0.5)$) to[short,thick] ($(output)+(-.9,-2)$);
# \end{circuitikz}
# \end{center}
# 
# \paragraph{KVL for Node A}
# \[V_A-0=10~\text{V}\]
# \[V_A=10~\text{V}\]
# 
# \paragraph{KVL for Op-amp}
# \[V_B=0~\text{V}\]
# 
# \paragraph{KCL for Node B}
# \[\frac{V_A-V_B}{3k}-\frac{V_B-V_C}{15k}-0=0\]
# \[\frac{1}{3k}V_A+\left[-\frac{1}{3k}-\frac{1}{15k}\right]V_B+\frac{1}{15k}V_C=0\]
# 
# \paragraph{Solve the System}
# Let's gather the results of the three equations written above
# \begin{alignat}{3}
# V_A&&&=10~\text{V}\nonumber\\
# ~&~~~~~~~\text{V}\_B&~&=0~\text{V}\nonumber\\%there has got to be a better way to align this
# \frac{1}{3k}V_A&-\frac{6}{15k}&V_B+\frac{1}{15k}V_C&=0~\text{A}\nonumber
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrr}
# 1&0&0\\
# 0&1&0\\
# \frac{1}{3k}&-\frac{6}{15k}&\frac{1}{15k}
# \end{array} \right]^{-1}\left[\begin{array}{r}10~\text{V}\\0~\text{V}\\0~\text{A}\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\end{array}\right]=\left[\begin{array}{r}10~\text{V}\\0~\text{V}\\-50~\text{V}\end{array}\right]\]
# 
# \paragraph{Find other values}
# \[V_O=V_C-0=-50-0=-50~\text{V}\]
# 
# \end{example}
# 
# \begin{example}
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=-1](opamp){}
# (opamp.+) to[short] ($(opamp.+)+(-2,0)$) to[voltage source,l_=10~\text{V}] ($(opamp.+)+(-2,-4)$) node[sground,scale=0.5]{}
# (opamp.-) to[short] ($(opamp.-)+(0,-1)$) to[R,l_=4~\Om] ($(opamp.-)+(0,-3)$) |- ($(opamp.+)+(-2,-4)$)
# (opamp.out) to[short] ($(opamp.out) +(2,0)$) to[R,l=8~\Om,i=$I_O$] ($(opamp.out) +(2,-3.5)$) |- ($(opamp.+)+(-2,-4)$)
# ($(opamp.-)+(0,-1)$) to[R,l=12~\Om] ($(opamp.-)+(3,-1)$) |- (opamp.out)
# ;
# \end{circuitikz}
# \end{center}
# \Solution
# 
#     \begin{center}
#     	\begin{circuitikz}[american]\draw
#     	(0,0) node[op amp,yscale=-1](opamp){}
#     	(opamp.+) to[short] ($(opamp.+)+(-2,0)$) to[voltage source,l_=10~\text{V}] ($(opamp.+)+(-2,-4)$) node[sground,scale=0.5]{}
#     	(opamp.-) to[short] ($(opamp.-)+(0,-1)$)  to[R,l_=4~\Om] ($(opamp.-)+(0,-3)$) |- ($(opamp.+)+(-2,-4)$)
#     	(opamp.out) to[short] ($(opamp.out) +(2,0)$) to[R,l=8~\Om,i=$I_O$] ($(opamp.out) +(2,-3.5)$) |- ($(opamp.+)+(-2,-4)$)
#     	($(opamp.-)+(0,-1)$) to[R,l=12~\Om] ($(opamp.-)+(3,-1)$) |- (opamp.out)
# 
#     	($(opamp.+)+(-2,0)$) node[left]{A}
#     	($(opamp.-)+(0,-1)$) node[left]{B}
#     	($(opamp.out) +(2,0)$) node[right]{C}
#     	;
#     	\draw[blue,-latex] ($(opamp.-)+(0.5,-1.5)$) to[short,thick] ($(opamp.-)+(0.5,-2.5)$);
#     	\draw[blue,-latex] ($(opamp.-)+(1,-1.5)$) to[short,thick] ($(opamp.-)+(2,-1.5)$);
#     	\draw[blue,-latex] ($(opamp.out) +(1.5,-1)$) to[short,thick] ($(opamp.out) +(1.5,-2.5)$);
#     	\end{circuitikz}
#     \end{center}
# 
# \paragraph{KVL for node A}~
# \[V_A-0=10~\text{V}\]
# \[V_A=10~\text{V}\]
# 
# \paragraph{KVL for op-amp}~
# \[V_A=V_B\]
# \[V_A-V_B=0\]
# 
# \paragraph{KCL for node B}~
# \[-\frac{V_B-0}{4}-\frac{V_B-V_C}{12}-0=0~\text{A}\]
# \[\left[-\frac{1}{4}-\frac{1}{12}\right]V_B+\frac{1}{12}V_C=0~\text{A}\]
# 
# \paragraph{Solve the System}~
# Let's gather the results of the three equations written above
# \begin{alignat}{3}
# V_A&&&=10~\text{V}\nonumber\\
# V_A&-V_B&~&=0~\text{V}\nonumber\\%there has got to be a better way to align this
# ~&-\frac{1}{3}&V_B+\frac{1}{12}V_C&=0~\text{A}\nonumber
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrr}
# 1&0&0\\
# 1&-1&0\\
# 0&-\frac{1}{3}&\frac{1}{12}
# \end{array} \right]^{-1}\left[\begin{array}{r}10~\text{V}\\0~\text{V}\\0~\text{A}\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\end{array}\right]=\left[\begin{array}{r}10~\text{V}\\0~\text{V}\\40~\text{V}\end{array}\right]\]
# 
# \paragraph{Find other values}
# \[I_O=\frac{V_C-0}{8}=\frac{40-0}{8}=5~\text{A}\]
# \end{example}
# 
# \begin{example}
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=-1](opamp){}
# (opamp.out) -- +(1,0) coordinate (output)
# (opamp.-) -- +(-.5,0) -- +(-.5,-1) -| (output)
# (opamp.+) -- +(-1.5,0) coordinate (nodeC) to[R,lx^={$R_2$ and 7~k\Om}] +(-3,0) coordinate (nodeB) to[R,lx^={$R_1$ and 4~k\Om}] +(-3,0) coordinate (nodeA) to[voltage source,lx_={$V_S$ and 2~\text{V}}] +(0,-3) coordinate (grnd) node[sground,scale=0.5]{}
# (nodeC) to[R,lx_={$R_3$ and 10~k\Om}] +(4.5,0) -- (grnd)
# (nodeB) to[R,lx={$R_4$ and 5~k\Om}] +(0,3) -| (output)
# (output) to[short,-o] +(1,0) node[right]{$v_O$(t)}
# (opamp.out) to[short,i=$i_O$(t)] (output)
# ;
# \end{circuitikz}
# \end{center}
# 
# \Solution
# 
#     \begin{center}
#     	\begin{circuitikz}[american]\draw
#     	(0,0) node[op amp,yscale=-1](opamp){}
#     	(opamp.out) -- +(1,0) coordinate (output)
#     	(opamp.-) -- +(-.5,0) -- +(-.5,-1) -| (output)
#     	(opamp.+) -- +(-1.5,0) coordinate (nodeC) to[R,lx^={$R_2$ and 7~k\Om}] +(-3,0) coordinate (nodeB) to[R,lx^={$R_1$ and 4~k\Om}] +(-3,0) coordinate (nodeA) to[voltage source,lx_={$V_S$ and 2~\text{V}}] +(0,-3) coordinate (grnd) node[sground,scale=0.5]{}
#     	(nodeC) to[R,lx_={$R_3$ and 10~k\Om}] +(4.5,0) -- (grnd)
#     	(nodeB) to[R,lx={$R_4$ and 5~k\Om}] +(0,3) -| (output)
#     	(output) to[short,-o] +(1,0) node[right]{$v_O$(t)}
#     	(opamp.out) to[short,i=$i_O$(t)] (output)
# 
#     	(nodeA) node[left]{A}
#     	(nodeB) node[below]{B}
#     	(nodeC) node[above]{C}
#     	($(output) +(.25,0)$) node[above]{D}
#     	;
#     	\draw[blue,-latex] ($(nodeA)+(1,.5)$) to[short,thick] ($(nodeA)+(2,.5)$);
#     	\draw[blue,-latex] ($(nodeB)+(.25,.5)$) to[short,thick] ($(nodeB)+(1.25,.5)$);
#     	\draw[blue,-latex] ($(nodeC)+(.5,-1)$) to[short,thick] ($(nodeC)+(.5,-2)$);
#     	\draw[blue,-latex] ($(nodeB)+(.5,2)$) to[short,thick] ($(nodeB)+(.5,1)$);
#     	\end{circuitikz}
#     \end{center}
# 
# \paragraph{KVL for node A}~
# \[V_A-0=2~\text{V}\]
# \[V_A=2~\text{V}\]
# 
# \paragraph{KCL for node B}~
# \[\frac{V_A-V_B}{R_1}-\frac{V_B-V_C}{R_2}+\frac{V_D-V_B}{R_4}=0~\text{A}\]
# \[\frac{1}{R_1}V_A+\left[-\frac{1}{R_1}-\frac{1}{R_2}-\frac{1}{R_4}\right]V_B+\frac{1}{R_2}V_C+\frac{1}{R_4}V_D=0~\text{A}\]
# \[\frac{1}{4k}V_A-\frac{83}{140k}V_B+\frac{1}{7k}V_C+\frac{1}{5k}V_D=0~\text{A}\]%FIX ME
# 
# \paragraph{KCL for node C}~
# \[\frac{V_B-V_C}{R_2}-\frac{V_C-0}{R_3}+0=0~\text{A}\]
# \[\frac{1}{R_2}V_B+\left[-\frac{1}{R_2}-\frac{1}{R_3}\right]V_C=0~\text{A}\]
# \[\frac{1}{7k}V_B-\frac{17}{70k}V_C=0~\text{A}\]
# 
# \paragraph{KVL for op-amp}~
# \[V_C=V_D\]
# \[V_C-V_D=0\]
# 
# \paragraph{Solve the System}~
# Let's gather the results of the four equations written above
# \begin{alignat}{4}
# V_A&&&&=2~\text{V}\nonumber\\
# \frac{1}{4k}V_A&-\frac{83}{140k}V_B&+\frac{1}{7k}V_C&+\frac{1}{5k}V_D&=0~\text{A}\nonumber\\%there has got to be a better way to align this
# &\frac{1}{7k}V_B&-\frac{17}{70k}V_C&&=0~\text{A}\nonumber\\%there has got to be a better way to align this
# &&V_C&-V_D&=0~\text{V}\nonumber\\
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrrr}
# 1&0&0&0\\
# \frac{1}{4k}&-\frac{83}{140k}&\frac{1}{7k}&\frac{1}{5k}\\
# 0&\frac{1}{7k}&-\frac{17}{70k}&0\\
# 0&0&1&-1
# \end{array} \right]^{-1}\left[\begin{array}{r}2~\text{V}\\0~\text{A}\\0~\text{A}\\0~\text{V}\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\\V_D\end{array}\right]=\left[\begin{array}{r}2~\text{V}\\1.278~\text{V}\\751.9~\text{mV}\\751.9~\text{mV}\end{array}\right]\]
# 
# \paragraph{Find other values}
# \[I*O-I*{R4}-0=0\]
# \[I*O=I*{R4}=\frac{V_D-V_B}{5k}=\frac{751.9~\text{mV}-1.278~\text{V}}{5k}=-105.3~\mu A\]
# How will this change if we connect a load resistor to the output?
# \end{example}
# 
# \begin{example}
# Find $I_O$
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=-1](opamp){}
# (opamp.+) to[R,l_=18~\Om] ($(opamp.+) + (-3,0)$) to[voltage source,l_=4~\text{V}] ($(opamp.+) + (-6,0)$) to[R,l=6~\Om] ($(opamp.+) + (-6,-3)$)
# ($(opamp.+) + (-3,0)$) to[R,l=9~\Om] ($(opamp.+) + (-3,-3)$)
# (opamp.-) |- ($(opamp.+) + (-6,-3)$) node[sground,scale=0.5]{}
# (opamp.+) to[short] ($(opamp.+)+(0,1.5)$) to[R,l=72~\Om] ($(opamp.+)+(3.5,1.5)$) |- (opamp.out)
# (opamp.out) to[short,i=$I_O$] ($(opamp.out)+(1,0)$)
# ($(opamp.out)+(1.11,0)$) to[R,l=12~\Om] ($(opamp.out)+(1.11,-2.5)$) |- ($(opamp.+) + (-6,-3)$)
# ;
# \end{circuitikz}
# \end{center}
# 
# \Solution
# 
#     \begin{center}
#     	\begin{circuitikz}[american]\draw
#     	(0,0) node[op amp,yscale=-1](opamp){}
#     	(opamp.+) to[R,l_=18~\Om] ($(opamp.+) + (-3,0)$) to[voltage source,l_=4~\text{V}] ($(opamp.+) + (-6,0)$) to[R,l=6~\Om] ($(opamp.+) + (-6,-3)$)
#     	($(opamp.+) + (-3,0)$) to[R,l=9~\Om] ($(opamp.+) + (-3,-3)$)
#     	(opamp.-) |- ($(opamp.+) + (-6,-3)$) node[sground,scale=0.5]{}
#     	(opamp.+) to[short] ($(opamp.+)+(0,1.5)$) to[R,l=72~\Om]  ($(opamp.+)+(3.5,1.5)$) |- (opamp.out)
#     	(opamp.out) to[short,i=$I_O$] ($(opamp.out)+(1,0)$)
#     	($(opamp.out)+(1.11,0)$) to[R,l=12~\Om] ($(opamp.out)+(1.11,-2.5)$)  |- ($(opamp.+) + (-6,-3)$)
# 
#     	(nodeA) node[left]{A}
#     	(nodeB) node[above]{B}
#     	($(opamp.+)+(-.2,0)$) node[above]{C}
#     	($(output) +(.35,0)$) node[above]{D}
#     	;
#     	\draw[blue,-latex] ($(opamp.+) + (-6.5,-1)$) to[short,thick] ($(opamp.+) + (-6.5,-2)$);
#     	\draw[blue,-latex] ($(opamp.+) + (-3.5,-1)$) to[short,thick] ($(opamp.+) + (-3.5,-2)$);
#     	\draw[blue,-latex] ($(opamp.+)+(-2,-.5)$) to[short,thick] ($(opamp.+) + (-1,-.5)$);
#     	\draw[blue,-latex] ($(opamp.+)+(1,1)$) to[short,thick] ($(opamp.+)+(2.5,1)$);
#     	\draw[blue,-latex] ($(opamp.out)+(0.61,-.5)$) to[short,thick] ($(opamp.out)+(0.61,-2)$);
#     	\draw[dashed,ultra thick,orange] ($(opamp.+) + (-6.5,1)$) rectangle ($(opamp.+) + (-2.65,-.5)$)
#     		($(opamp.+) + (-6.5,1.25)$) node[right]{Super Node};
# 
#     	\end{circuitikz}
#     \end{center}
# 
# \paragraph{KVL for super-node (A and B)}
# \[V_A-V_B=4~\text{V}\]
# 
# \paragraph{KCL for super-node (A and B)}
# \[-\frac{V_A-0}{6}-\frac{V_B-0}{9}-\frac{V_B-V_C}{18}=0~\text{A}\]
# \[-\frac{1}{6}V_A+\left[-\frac{1}{9}-\frac{1}{18}\right]V_B+\frac{1}{18}V_C=0~\text{A}\]
# \[-\frac{1}{6}V_A-\frac{1}{6}V_B+\frac{1}{18}V_C=0~\text{A}\]
# 
# \paragraph{KVL for op-amp}
# \[V_C=0~\text{V}\]
# 
# \paragraph{KCL for node C}
# \[\frac{V_B-V_C}{18}-\frac{V_C-V_D}{72}+0=0~\text{A}\]
# \[\frac{1}{18}V_B+\left[-\frac{1}{18}-\frac{1}{72}\right]V_C+\frac{1}{72}V_D=0~\text{A}\]
# \[\frac{1}{18}V_B-\frac{5}{72}V_C+\frac{1}{72}V_D=0~\text{A}\]
# 
# \paragraph{Solve the system}
# Let's gather the results of the four equations written above
# \begin{alignat}{4}
# V_A&~-V_B&&&=4~\text{V}\nonumber\\
# -\frac{1}{6}V_A&-\frac{1}{6}V_B&+\frac{1}{18}V_C&&=0~\text{A}\nonumber\\%there has got to be a better way to align this
# &&V_C&&=0~\text{V}\nonumber\\
# &\frac{1}{18}V_B&-\frac{5}{72}V_C&+\frac{1}{72}V_D&=0~\text{A}\nonumber
# \end{alignat}
# and put them in matrix form
# \[ \left[ \begin{array}{rrrr}
# 1&-1&0&0\\
# -\frac{1}{6}&-\frac{1}{6}&\frac{1}{18}&0\\
# 0&0&1&0\\
# 0&\frac{1}{18}&-\frac{5}{72}&\frac{1}{72}
# \end{array} \right]^{-1}\left[\begin{array}{r}4~\text{V}\\0~\text{A}\\0~\text{V}\\0~\text{A}\end{array}\right]=\left[\begin{array}{c}V_A\\V_B\\V_C\\V_D\end{array}\right]=\left[\begin{array}{r}2~\text{V}\\-2~\text{V}\\0~\text{V}\\8~\text{V}\end{array}\right]\]
# 
# \paragraph{Find other values}~
# \[\frac{V_C-V_D}{72}+I_O-\frac{V_D-0}{12}=0\]
# \[I_O=-\frac{0-8}{72}+\frac{8-0}{12}=\frac{7}{9}~\text{A}=777.8~\text{mA}\]
# 
# \end{example}
# 
# ## The Shortcut
# 
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[current source,lx={$I_S$ and 6~\text{A}}] (0,3)
# (0,3) to[resistor,lx={$R_1$ and 2~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 4~\Om}] (3,0)
# (3,3) to[resistor,lx={$R_3$ and 4~\Om}] (6,3)
# (6,3) to[resistor,lx={$R_4$ and 2~\Om}] (6,0)
# (6,0) -- ((0,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# ;
# \end{circuitikz}\end{center}
# 
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[current source,lx={$I_{S1}$ and 2~\text{mA}}] (0,3)
# (0,3) to[resistor,lx={$R_1$ and 4~k\Om}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 2~k\Om}] (3,0)
# (3,3) to[resistor,lx={$R_3$ and 4~k\Om}] (6,3)
# (6,3) to[current source,lx={$I_{S2}$ and 6~\text{mA}}] (6,0)
# (6,0) -- ((0,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# ;
# \end{circuitikz}\end{center}
# 
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[current source,lx={$I_S$ and 2/3~\text{A}}] (0,3)
# (0,3) to[resistor,lx={$R_1$ and 6~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 12~\Om}] (3,0)
# (3,3) to[resistor,lx={$R_3$ and 12~\Om}] (6,3)
# (6,3) to[voltage source,lx^={8~\text{V} and $V_S$}] (6,0)
# (6,0) -- ((0,0)
# (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# ;
# \end{circuitikz}\end{center}
# 
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 3~\Om}] (0,3)
# (0,3) to[resistor,lx={$R_2$ and 6~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_3$ and 12~\Om}] (3,0)
# (3,3) to[voltage source,lx={$V_S$ and 8~\text{V}}] (6,3)
# (6,0) to[R,lx={$R_4$ and 4~\Om}] (6,3)
# (6,3) to[resistor,lx={$R_5$ and 8~\Om}] (9,3)
# (9,3) to[resistor,lx={$R_6$ and 5~\Om}] (9,0)
# 
#     (9,0) -- ((0,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# 
# ;
# \end{circuitikz}\end{center}
# 
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 3~\Om}] (0,3)
# (0,3) to[resistor,lx={$R_2$ and 6~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_3$ and 12~\Om}] (3,0)
# (3,3) to[voltage source,lx={$V_S$ and 8~\text{V}}] (5,3)
# (5,3) to[resistor,lx={$R_4$ and 8~\Om}] (8,3)
# (8,3) to[resistor,lx={$R_5$ and 5~\Om}] (8,0)
# 
#     (8,0) -- ((0,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# 
# ;
# \end{circuitikz}\end{center}
# 
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 8~\Om},i^<=$I_O$] (0,3)
# (0,3) to[current source,lx={$I_{S1}$ and 4~\text{A}}] (3,3)
# (3,3) to[resistor,lx={$R_2$ and 2~\Om}] (3,0)
# (3,3) to[controlled current source,lx={$I_{S2}$ and 2$I_O$}] (6,3)
# (6,3) to[resistor,lx={$R_3$ and 4~\Om}] (6,0)
# (0,5) to[resistor,lx={$R_4$ and 1~\Om}] (6,5)
# (0,3) -- (0,5)
# (6,3) -- (6,5)
# 
#     (6,0) -- ((0,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# 
# ;
# \end{circuitikz}\end{center}
# 
# \begin{center}\begin{circuitikz}\draw
# (0,0) to[R,lx={$R_1$ and 10~\Om}] (0,3)
# (0,3) to[R,lx={$R_2$ and 4~\Om}] (3,3)
# (3,3) to[resistor,lx={$R_3$ and 5~\Om}] (3,0)
# (3,3) to[R,lx={$R_4$ and 2~\Om},v_<=$V_O$] (6,3)
# (6,0) to[current source,lx={I\tss{S3} and 4~\text{A}}] (6,3)
# (0,5) to[current source,lx={$I_{S2}$ and 2~\text{A}}] (6,5)
# (-2,0) to[controlled current source,lx={$I_{S1}$s and 3$V_O$}] (-2,3)
# (-2,3)--(0,3)
# (0,3) -- (0,5)
# (6,3) -- (6,5)
# 
#     (6,0) -- ((-2,0)
#     (0,0) -- (0,-.25) node[sground,scale=0.5]{}
# 
# ;
# \end{circuitikz}\end{center}
# 
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=1](opamp){}
# (opamp.out) -- +(1,0) coordinate (output)
# (opamp.-) to[R,l=3~k\Om] ($(opamp.-)+(-3,0)$) to[voltage source,l_=10~\text{V}] ($(opamp.-)+(-3,-3)$)
# (opamp.+) |- ($(opamp.-)+(-3,-3)$)
# (output) to[R,l=5~k\Om,v=$V_O$] ($(output)+(0,-2.5)$) |- ($(opamp.-)+(-3,-3)$)
# (opamp.-) to[short] ($(opamp.-)+(0,1.5)$) to[R,l=15~k\Om] ($(opamp.-)+(3,1.5)$) -| (output)
# ($(opamp.-)+(-3,-3)$) node[sground,scale=0.5]{}
# ;
# \end{circuitikz}
# \end{center}
# 
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=-1](opamp){}
# (opamp.+) to[short] ($(opamp.+)+(-2,0)$) to[voltage source,l_=10~\text{V}] ($(opamp.+)+(-2,-4)$) node[sground,scale=0.5]{}
# (opamp.-) to[short] ($(opamp.-)+(0,-1)$) to[R,l_=4~\Om] ($(opamp.-)+(0,-3)$) |- ($(opamp.+)+(-2,-4)$)
# (opamp.out) to[short] ($(opamp.out) +(2,0)$) to[R,l=8~\Om,i=$I_O$] ($(opamp.out) +(2,-3.5)$) |- ($(opamp.+)+(-2,-4)$)
# ($(opamp.-)+(0,-1)$) to[R,l=12~\Om] ($(opamp.-)+(3,-1)$) |- (opamp.out)
# ;
# \end{circuitikz}
# \end{center}
# 
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=-1](opamp){}
# (opamp.out) -- +(1,0) coordinate (output)
# (opamp.-) -- +(-.5,0) -- +(-.5,-1) -| (output)
# (opamp.+) -- +(-1.5,0) coordinate (nodeC) to[R,lx^={$R_2$ and 7~k\Om}] +(-3,0) coordinate (nodeB) to[R,lx^={$R_1$ and 4~k\Om}] +(-3,0) coordinate (nodeA) to[voltage source,lx_={$V_S$ and 2~\text{V}}] +(0,-3) coordinate (grnd) node[sground,scale=0.5]{}
# (nodeC) to[R,lx_={$R_3$ and 10~k\Om}] +(4.5,0) -- (grnd)
# (nodeB) to[R,lx={$R_4$ and 5~k\Om}] +(0,3) -| (output)
# (output) to[short,-o] +(1,0) node[right]{$v_O$(t)}
# (opamp.out) to[short,i=$i_O$(t)] (output)
# ;
# \end{circuitikz}
# \end{center}
# 
# \begin{center}
# \begin{circuitikz}[american]\draw
# (0,0) node[op amp,yscale=-1](opamp){}
# (opamp.+) to[R,l_=18~\Om] ($(opamp.+) + (-3,0)$) to[voltage source,l_=4~\text{V}] ($(opamp.+) + (-6,0)$) to[R,l=6~\Om] ($(opamp.+) + (-6,-3)$)
# ($(opamp.+) + (-3,0)$) to[R,l=9~\Om] ($(opamp.+) + (-3,-3)$)
# (opamp.-) |- ($(opamp.+) + (-6,-3)$) node[sground,scale=0.5]{}
# (opamp.+) to[short] ($(opamp.+)+(0,1.5)$) to[R,l=72~\Om] ($(opamp.+)+(3.5,1.5)$) |- (opamp.out)
# (opamp.out) to[short,i=$I_O$] ($(opamp.out)+(1,0)$)
# ($(opamp.out)+(1.11,0)$) to[R,l=12~\Om] ($(opamp.out)+(1.11,-2.5)$) |- ($(opamp.+) + (-6,-3)$)
# ;
# \end{circuitikz}
# \end{center}
# 
# \newpage
# 
# ## Strategy for Nodal Analysis
# 
# The examples I've worked are intended to teach you how to deal with the little oddities that arise when performing nodal analysis. If you master these you will be able to analyze any linear electric circuits. I've also shown you how to use the ``shortcut'' to perform nodal analysis quickly. With practice you may be able to analyze most circuits simply by looking at the circuit and using your calculator to build the system of equations.
# 
# Not all circuits require you to use the techniques introduced here. When I first begin analysis of a circuit I look for certain conditions and I make a plan to deal with them. I will do my best to summarize the strategy I use when analyzing a circuit.
# 
# \begin{enumerate}
# \item \textbf{How many non-reference nodes?} Non-reference nodes are any nodes that are not the ground node. The number of non-reference nodes define how many unknowns will be part of the system and, therefore, how many equations you will have to write.
# \item \textbf{Are there voltage supplies?} Each voltage supply means you will write a KVL equation instead of a KCL. Also notice I say `voltage supply''. I don't say `dependent supply'' or `independent supply'' since the type of voltage supply does not matter. \begin{enumerate} \item \textbf{Is the voltage supply grounded on one side?} This is the simpler of the two conditions created by voltage supplies in the circuit. Just write a KVL for the voltage supply and skip the KCL for the node connected to the other side of the voltage supply. \item \textbf{Does the voltage supply connected to two non-reference nodes?} This condition creates a `super-node''. The KVL is written in the same way as the previous case. The difference here is found in how you will write one of the KCLs. Rather than writing a KCL for a single node you will write a KCL for the region that bounds the two nodes on either side of the voltage supply.
# \end{enumerate}
# \item \textbf{Are there any operational amplifiers?} We use the two assumptions about ideal op-amps to complete the system of equations in this case. The first is that the voltages on the \textbf{inputs} of the op-amp are equal. This is included in the system as a KVL equation. This KVL replaces one of the KCL equations needed to complete the system. You'll still need to write enough KCL equations to complete the system. Find nodes that are not connected to 1) voltage supplies and 2) the \textbf{output} of the op-amp. Nodes connected to the inputs of the op-amp are fair game since we assume no current enters or leaves those inputs.
# \item \textbf{Are there any dependent supplies?} Look for diamond shaped supplies. It does not matter whether they are voltage or current supplies. Locate the control variable on the schematic and write an expression for it in terms of the unknown mesh currents. This expression is written in a similar manner to finding the output values of the analysis. You should use this expression anytime the control variable shows up in the system of equations.
# \item \textbf{Write the equations} If you've answered the questions above you should know which equations you will include in the system. Write them carefully and use good practice with regards to the signs and order of coefficients.
# \item \textbf{Solve the system} Matrix inversion works. So does row-reduced echelon form. If you'd like use software like MATLAB to solve the system. Just find the answer.
# \item \textbf{Find output of analysis} Once you know the node voltages you can find any other value in the circuit. The output of the analysis may take a few different forms.
# \begin{enumerate}
# \item \textbf{Is the value a voltage?} If the value is a voltage start with the node voltage on the positive side of the output. Subtract the node voltage on the negative side of the output.
# \item \textbf{Is the value a current through a single passive component?} If the value is a current through a passive component use a combination of KVL and Ohm's law to find that voltage. Find the voltage as you did for the previous output type respecting passive sign convention for the labeled current direction. Use that voltage and the resistance (or impedance in later chapters) to find the current . This is useful for finding currents that are outputs of the analysis as well as finding currents that are intermediate values for the next type of output value.
# \item \textbf{Is the value a current through a voltage supply or op-amp output?} If the value is a current through one of these components you can find it using a KCL at a node connected to the component. This means you have to find other currents using the previous method. Write a KCL at a node that includes the unknown current. Find all of the other currents entering/leaving the node. Solve for the unknown current.
# \end{enumerate}
# \end{enumerate}
