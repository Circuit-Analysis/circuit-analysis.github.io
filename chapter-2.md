# Anatomy of a Circuit

## Nodes

\begin{itemize}
\item Any point in a circuit that 2 or more elements are connected.
\item Voltage at all points on the node is constant.
\end{itemize}
\begin{center}\begin{circuitikz}\draw
(-3,3) to[R] (0,3)
(3,3) to[R] (0,3)
(0,0) to[R] (0,3)
(0,3) node[above]{Node}
;
\end{circuitikz}\end{center}

## Branches

Any current path between two nodes
\begin{center}\begin{circuitikz}\draw
(0,6) to[battery] (0,0)
(3,0) to[R] (3,6)
(6,0) to[R] (6,3)
(6,3) to[R] (6,6)
(0,0) -- (6,0)
(0,6) -- (6,6)
;
\end{circuitikz}\end{center}

%%%%%%%%%%%%%%%%%%%%%%%%%%%
\pagebreak
%%%%%%%%%%%%%%%%%%%%%%%%%%%

## Loops

Any closed path in a circuit. (Begin and end at the same node)
\begin{center}\begin{circuitikz}\draw
(0,3) to[battery] (0,0)
(3,0) to[R] (3,3)
(6,0) to[R] (6,3)
(3,3) to[R] (6,3)
(3,0) to[R] (6,0)
(6,-3) to[R] (6,0)
(6,-3) to[R] (3,-3)
(3,-3) -- (3,0)
(0,0) -- (3,0)
(0,3) -- (3,3)
;
\centerarc[red,->,thick](1.5,1.5)(225:-45:5mm)
\centerarc[blue,->,thick](4.5,1.5)(225:-45:5mm)
\centerarc[orange,->,thick](4.5,-1.5)(225:-45:5mm)
\end{circuitikz}\end{center}
Loops over opens

## Meshes

\begin{itemize}
\item Any closed path in a circuit. (Begin and end at the same node)
\item Has no intermediate branches
\end{itemize}

\begin{center}\begin{circuitikz}\draw
(0,3) to[battery] (0,0)
(3,0) to[R] (3,3)
(6,0) to[R] (6,3)
(3,3) to[R] (6,3)
(3,0) to[R] (6,0)
(6,-3) to[R] (6,0)
(6,-3) to[R] (3,-3)
(3,-3) -- (3,0)
(0,0) -- (3,0)
(0,3) -- (3,3)
;
\centerarc[red,->,thick](1.5,1.5)(225:-45:5mm)
\draw[red,thick] (1.5,1.5) node{$I_1$};
\centerarc[blue,->,thick](4.5,1.5)(225:-45:5mm)
\draw[blue,thick] (4.5,1.5) node{$I_2$};
\centerarc[orange,->,thick](4.5,-1.5)(225:-45:5mm)
\draw[orange,thick] (4.5,-1.5) node{$I_3$};

\end{circuitikz}\end{center}
