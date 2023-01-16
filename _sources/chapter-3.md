# Equivalent Components

## Series, Parallel, Neither, Both

Elements in a circuit can be connected in four different ways:
\begin{itemize}
\item Series
\item Parallel
\item Neither
\item Both
\end{itemize}
Students often assume that two elements are either in parallel or series. Beware of this false dichotomy and avoid it by studying the definitions of series and parallel connections carefully.

In series or parallel, some components can be combined. When neither, they can not.

### Series Resistors

Two elements connected in series share one node \textbf{exclusively}.
\begin{center}\begin{circuitikz}\draw
(-3,3) to[R,l=$R_1$] (0,3)
(3,3) to[R,l_=$R_2$] (0,3)
;
\end{circuitikz}\end{center}
When two resistors are in series they can be redrawn as a single resistor
\begin{center}\begin{circuitikz}\draw
(-3,3) to[R,l=$R_1$+$R_2$] (0,3)
;
\end{circuitikz}\end{center}
When two elements are in series, the same current flows through each.
\[ I*{R1}=I*{R2}\]

### Parallel Resistors

Two elements are in parallel when they are connected to the same two nodes.

\begin{center}\begin{circuitikz}\draw
(0,0) to[R,l=$R_1$] (0,3)
(2,0) to[R,l=$R_2$] (2,3)
(0,0) -- (2,0)
(0,3) -- (2,3)
;
\end{circuitikz}\end{center}

When two resistors are in parallel they can be redrawn as a single resistor
\begin{center}\begin{circuitikz}\draw
(0,0) to[R,l=$G_1$+$G_2$] (0,3)
;
\end{circuitikz}\end{center}

The conductances add. Recall that
\[G=\frac{1}{R}\]
so
\[\frac{1}{R_P}=\frac{1}{R_1}+\frac{1}{R_2}\]
Solving for $R_P$ and adding additional resistors
\[R_P=\frac{1}{\frac{1}{R_1}+\frac{1}{R_2}+\dots+\frac{1}{R_N}}\]
The value of two resistors in parallel is commonly expressed as
\[R_P=\frac{R_1R_2}{R_1+R_2}\]

Careful:
\begin{itemize}
\item They may not be drawn geometrically parallel.

    \begin{center}\begin{circuitikz}\draw
    (0,0) to[R,l=$R_1$] (0,3)
    (0,3) to[R,l=$R_2$] (3,3)
    (3,3) -- (3,0)
    (0,0) -- (3,0)
    ;
    \end{circuitikz}\end{center}
    $R_1$ and $R_2$ are in parallel.

    \item If they are drawn geometrically parallel they may not be

connected in parallel.
\begin{center}\begin{circuitikz}\draw
(0,0) to[R,l=$R_1$] (0,3)
(0,3) to[R,l=$R_2$] (3,3)
(3,3) to[R,l=$R_3$] (3,0)
(0,0) -- (3,0)
;
\end{circuitikz}\end{center}
$R_1$ and $R_3$ are \textbf{not} in parallel.
How are they connected?

\end{itemize}

## More Complex Circuits

\begin{example}
Find $R_{AB}$
\begin{center}\begin{circuitikz}\draw
(0,3) to[R,l=5\Om] (3,3)
(3,3) to[R,l=6\Om] (3,0)
(3,3) to[R,l=2\Om] (6,3)
(6,3) to[R,l=4\Om] (6,0)
(9,3) to[R,l=4\Om] (9,0)
(0,0) -- (9,0)
(6,3) -- (9,3)
(0,0) node[above]{A}
(0,3) node[below]{B}
;
\end{circuitikz}\end{center}
\Solution
$R_{AB}$=7.4\Om
\end{example}

\begin{example}
Find $R_{AB}$
\begin{center}\begin{circuitikz}[scale=1.5]\draw
(0,3) to[R,l=10\Om] (3,3)
(6,3) to[R,l=1\Om] (9,3)
(3,3) to[R,l=1\Om] (6,3)
(3,3) to[R,l_=3\Om] (3,0)
(6,3) to[R,l=4\Om] (6,0)
(9,3) to[R,l=5\Om] (9,0)
(3,3) to[R,l=6\Om] (4.5,1.5) -- (6,0)
(3,0) to[R,l=12\Om] (4.5,1.5) -- (6,3)
(0,0) -- (9,0)
(0,0) node[above]{A}
(0,3) node[below]{B}
;
\end{circuitikz}\end{center}
\Solution
$R_{AB}$=11.2\Om
\end{example}

\begin{example}
Find $R_{AB}$
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,0) to[R,l=3k\Om] (3,3)
(3,3) to[R,l=5k\Om] (6,0)
(0,0) to[R,l=2k\Om] (3,-3)
(3,-3) to[R,l=6k\Om] (6,0)
(0,0) -- (1,0)
(5,0) -- (6,0)

    (1,0) node[right]{A}
    (5,0) node[left]{B}
    ;
    \end{circuitikz}\end{center}

\Solution
$R_{AB}$=4k\Om
\end{example}

## Series Voltage Supplies

\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,2.5) to[voltage source,lx_={$V_1$ and 6~V}] (0,0)
(0,5) to[voltage source,lx_={$V_2$ and 12~V}] (0,2.5)
(0,5) to[short] (3,5)
(3,5) to[R,lx={$R$ and 9~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}
\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,3) to[voltage source,lx_={$V_1$+$V_2$ and 18~V}] (0,0)
(0,3) to[short] (3,3)
(3,3) to[R,lx={$R$ and 9~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}

\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,2.5) to[voltage source,lx_={$V_1$ and 7~V}] (0,0)
(0,2.5) to[voltage source,lx^={$V_2$ and 14~V}] (0,5)
(0,5) to[short] (3,5)
(3,5) to[R,lx={$R$ and 21~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}
\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,3) to[voltage source,lx_={$V_1-V_2$ and -7~V}] (0,0)
(0,3) to[short] (3,3)
(3,3) to[R,lx={$R$ and 21~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}

\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,2.5) to[voltage source,lx_={$V_1$ and 7~V}] (0,0)
(0,2.5) to[voltage source,lx^={14~V and $V_2$}] (0,5)
(0,5) to[short] (3,5)
(3,5) to[R,lx={$R$ and 21~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}
\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,0) to[voltage source,lx^={7~V and $V_2-V_1$}] (0,3)
(0,3) to[short] (3,3)
(3,3) to[R,lx={$R$ and 21~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}

\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,2.5) to[voltage source,lx_={$V_1$ and 8~V}] (0,0)
(0,2.5) to[R,lx={$R$ and 3~\Om}] (0,5)
(3,5) to[voltage source,lx_={\raisebox{1ex}{$V_2$} and \raisebox{3ex}{16~V}}] (0,5)
(3,5) to[R,lx={$R$ and 21~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}
\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,3) to[voltage source,lx_={$V_1-V_2$ and -7~V}] (0,0)
(0,3) to[short] (3,3)
(3,3) to[R,lx={$R$ and 21~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}

\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,2.5) to[voltage source,lx_={$V_1$ and 8~V}] (0,0)
(0,2.5) to[R,lx={$R$ and 3~\Om}] (0,5)
(0,5) to[voltage source,lx^={\raisebox{3ex}{$V_2$} and \raisebox{1ex}{16~V}}] (3,5)
(3,5) to[R,lx={$R$ and 21~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}
\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,3) to[voltage source,lx_={$V_1-V_2$ and -7~V}] (0,0)
(0,3) to[short] (3,3)
(3,3) to[R,lx={$R$ and 21~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)

    ;
    \end{circuitikz}\end{center}

\end{minipage}

## Parallel Current Supplies

\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,0) to[current source,lx_={$I_1$ and 3~A}] (0,3)
(3,0) to[current source,lx_={$I_2$ and 2~A}] (3,3)
(0,3) to[short] (6,3)
(6,3) to[R,lx={$R$ and 10~\Om},i=$I_R$] (6,0)
(0,0) to[short] (6,0)
;
\end{circuitikz}\end{center}
\end{minipage}
\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,0) to[current source,lx_={$I_1$+$I_2$ and 5~A}] (0,3)
(0,3) to[short] (3,3)
(3,3) to[R,lx={$R$ and 10~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)
;
\end{circuitikz}\end{center}
\end{minipage}

\vspace{0.5cm}

\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,0) to[current source,lx_={$I_1$ and 3~A}] (0,3)
(3,3) to[current source,lx^={$I_2$ and 2~A}] (3,0)
(0,3) to[short] (6,3)
(6,3) to[R,lx={$R$ and 10~\Om},i=$I_R$] (6,0)
(0,0) to[short] (6,0)
;
\end{circuitikz}\end{center}
\end{minipage}
\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,0) to[current source,lx^={$I_1$+$I_2$ and 5~A}] (0,3)
(0,3) to[short] (3,3)
(3,3) to[R,lx={$R$ and 10~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)
;
\end{circuitikz}\end{center}
\end{minipage}

\vspace{0.5cm}

\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,0) to[current source,lx_={$I_1$ and 3~A}] (0,3)
(3,3) to[current source,lx^={$I_2$ and 2~A}] (3,0)
(0,3) to[short] (6,3)
(6,3) to[R,lx={$R$ and 10~\Om},i=$I_R$] (6,0)
(0,0) to[short] (6,0)
;
\end{circuitikz}\end{center}
\end{minipage}
\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,3) to[current source,lx_={$I_1$+$I_2$ and 5~A}] (0,0)
(0,3) to[short] (3,3)
(3,3) to[R,lx={$R$ and 10~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)
;
\end{circuitikz}\end{center}
\end{minipage}

\vspace{0.5cm}

\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,0) to[current source,lx_={$I_1$ and 3~A}] (0,3)
(4,3) to[current source,lx^={$I_2$ and 2~A}] (4,0)
(0,3) to[short] (6,3)
(2,3) to[R,lx={$R$ and 10~\Om}] (2,0)
(6,3) to[R,lx={$R$ and 10~\Om},i=$I_R$] (6,0)
(0,0) to[short] (6,0)
;
\end{circuitikz}\end{center}
\end{minipage}
\begin{minipage}{0.48\textwidth}
\begin{center}\begin{circuitikz}[scale=1]\draw
(0,3) to[current source,lx_={$I_1$+$I_2$ and 5~A}] (0,0)
(0,3) to[short] (3,3)
(3,3) to[R,lx={$R$ and 10~\Om},i=$I_R$] (3,0)
(0,0) to[short] (3,0)
;
\end{circuitikz}\end{center}
\end{minipage}

## Delta-Wye Conversions

\begin{align}
R_a &= \frac{R_1 R_2}{R_1 + R_2 + R_3} \\
R_b &= \frac{R_1 R_3}{R_1 + R_2 + R_3} \\
R_c &= \frac{R_2 R_3}{R_1 + R_2 + R_3}
\end{align}

    \begin{center}\begin{circuitikz}[scale=0.75]\draw
    (0,0) to[R,l={$R_a$}] (-2.5,1.5)  node[circle,fill,label=above:A] {}
    (0,0) to[R,l={$R_b$}] (2.5,1.5)  node[circle,fill,label=above:B] {}
    (0,0) to[R,l={$R_c$}] (0,-3)  node[circle,fill,label=below:C] {}
    ;
    (0,0) node[above]{A};
    \end{circuitikz}\end{center}

\begin{align}
R_1 &= \frac{R_a R_b + R_b R_c + R_a R_c}{R_c} \\
R_2 &= \frac{R_a R_b + R_b R_c + R_a R_c}{R_b} \\
R_3 &= \frac{R_a R_b + R_b R_c + R_a R_c}{R_a}
\end{align}

    \begin{center}\begin{circuitikz}[scale=0.75]\draw
    (2.5,1.5) to[R,l={$R_1$}] (-2.5,1.5) 	node[circle,fill,label=above:A] {}
    (-2.5,1.5) to[R,l={$R_2$}] (0,-3) node[circle,fill,label=above:C] {}
    (0,-3) to[R,l={$R_3$}] (2.5,1.5) node[circle,fill,label=above:B] {}
    ;
    \end{circuitikz}\end{center}
