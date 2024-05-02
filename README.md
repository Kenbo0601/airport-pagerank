# Analysis of airports using Pagerank algorithm 
SDSU CS696 Algorithms for big data - Group project

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