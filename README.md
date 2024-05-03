# Analysis of airports using Pagerank algorithm 
SDSU CS696 Algorithms for big data - Group project
In this project, we analyzed and ranked airports in the world using pagerank algorithm, developed by Larry Page. 
 - Number of nodes (airports): 3425
 - Option1: only one edge btween source and dest 
 - Option2: handle multiple edges between nodes 

## Folder structure 
```
airport-pagerank 
├── data/
│   ├── airports.txt
│   ├── routes.txt
│   ├── source-dest.csv
│   └── source-dest.txt
├── output/
│   ├── MultiEdges.txt
│   └── SingleEdge.txt
└── src/
    ├── airportsLookup.py
    ├── extractRoutes.py
    ├── generateCSV.py
    ├── pagerank.cpp
    └── pagerank.py
```
## Build
Option 1: Single-edge pagerank 
```
g++ pagerank.cpp
```
Then in your termimal, type 
```
./a.out 
```
to see the result. (this is for unix system)

OPtion 2: Multi-edge pagerank 
```
python3 pagerank.py
```


## Source Data
 - [OpenFlights](https://openflights.org/data.php#airport)