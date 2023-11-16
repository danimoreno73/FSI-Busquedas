# FSI-Busquedas
Modificacion del codigo Base de Fsi, donde añadimos dos nuevos metodos donde creamos las listas para: Branch and Bound y Branch and Bound with Understimation


## Branch and Bound Search
El algoritmo utiliza un mecanismo de búsqueda de grafos y una cola de prioridad implementada como "BaBList" para gestionar la exploración de posibles soluciones.

### BaBList
Una implementación de cola de prioridad llamada BaBList. Esta estructura de datos es utilizada por la función graph_search para gestionar el orden en el que se exploran los nodos segun su coste acumulado.

## Branch and Bound with Understimation
Al igual que el Branch and Bound Search utiliza un mecanismo de búsqueda de grafos y una cola de prioridad implementada como "OrderedList" para gestionar la exploración de posibles soluciones.

### OrderedList
Una implementación de cola de prioridad llamada OrderedList. Esta estructura de datos es utilizada por la función graph_search para gestionar el orden en el que se exploran los nodos segun su coste acumulado y su heuristica.
