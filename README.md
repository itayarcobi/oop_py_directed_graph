# oop_py_ex3
The first project in oop curse in py

The task is to build a directed graph consisting of vertices and sides when the graph has several operations,
For example, adding a vertex to a graph connecting vertices and deleting vertices and sides,
In addition, there is an algorithm department that allows you to run several algorithms on the graph, for example finding a very short path from two vertices, checking linking components to the vertex or the entire graph and opening and saving the graph as a json file
.
And we run runtime comparisons on given graphs between java python and networkx

********** NodeData
creates a vertex in a graph with values of key,info,tag,pos and weight

*****DiGraph*****
In this class we will perform basic operations on the graph. For example adding a vertex, deleting a vertex, adding a side and deleting a side. And all this by creating dictionaries. One dictionary holds the list of vertices, the second holds the neighbors of each vertex exiting it and the third holds the list of neighbors entering it

*****GraphAlgo*****
In this class we will perform complicated algorithmic tests, for example finding the shortest path between two vertices in a graph, finding a binding element of a particular vertex and finding all the binding elements in a graph.
In addition we will perform save and load from json
And finally we will place the vertices on the x and y axis and represent it using mat plot lib functions

*****
 Comparisons between different languages and with networkx
