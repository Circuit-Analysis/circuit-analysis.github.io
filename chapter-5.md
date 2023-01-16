# A Sloppy Approach to Circuit Analysis

\label{sec_MacGyver}
\begin{center}
\textit{``Sometimes a desperate man does dumb things.''} -Angus MacGyver
\end{center}

\begin{example}
Find $V_S$ if $P_{R_2}=20$~W.
\begin{center}\begin{circuitikz}\draw
(0,3) to[battery,l_={$V_S$}] (0,0)
(0,3) to[R,lx={\raisebox{1ex}{$R_1$} and \raisebox{2ex}{2~\Om}}] (3,3)
(3,3) to[R,lx={$R_2$ and 5~\Om}] (3,0)
(6,3) to[R,lx={$R_3$ and 4~\Om}] (6,0)
(0,0) -- (6,0)
(3,3) -- (6,3)
;
\end{circuitikz}\end{center}
\end{example}

\begin{example}
Find $V_\text{6k}$ and $V_\text{3k}$.
\begin{center}\begin{circuitikz}\draw
(0,0) to[R,l=6~k\Om,v<= $V_\text{6k}$] (0,3)
(3,0) to[current source,l=1~mA] (3,3)
(6,3) to[R,l=4~k\Om] (6,0)
(9,3) to[R,l=8~k\Om] (9,0)
(3,3) to[R,l=3~k\Om,v= $V_\text{3k}$] (6,3)
(6,3) to[R,l=4~k\Om] (9,3)
(0,0) -- (9,0)
(0,3) -- (3,3)
;
\end{circuitikz}\end{center}
\end{example}

%%%%%%
\pagebreak
%%%%%%

\begin{example}
Find $I_x$.
\begin{center}\begin{circuitikz}\draw
(0,0) to[current source,l=4~mA] (0,3)
(3,3) to[R,i=$I_x$] (3,0)
(6,3) to[controlled current source,l=3$I_x$] (6,0)
(0,0) -- (6,0)
(0,3) -- (6,3)
;
\end{circuitikz}\end{center}
\end{example}

\begin{example}
Find V\tss{AB}.
\begin{center}\begin{circuitikz}\draw
(0,3) to[battery,l_=5~V] (0,0)
(0,3) to[R,v=4~V] (3,3)
(6,3) to[battery,l_=3~V] (3,3)
(6,3) to[R,v<=6~V] (9,3)
(9,3) to[R,v=10~V] (9,0)
(9,0) -- (0,0)
(0,3) node[above]{A}
(9,3) node [above]{B}
(0,0) node[sground,scale=0.5]{}
;
\end{circuitikz}\end{center}
\end{example}
