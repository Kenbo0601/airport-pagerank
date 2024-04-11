# read source-dest file to create a graph 
# then implement pagerank algorithm 
import networkx as nx
import matplotlib.pyplot as plt
import math

# remove whitespaces, and newlines
def format_string(a,b):
    source = a.split(' ')
    dest = b.split('\n') 
    return [source[0], dest[0].strip()]

def main():

    G = nx.DiGraph() # create a directed graph 
    testG = nx.DiGraph()
    pagerank = {}
    nodes = set()

    count = 0
    with open("source-dest.txt", encoding='utf-8') as f:
        for line in f.readlines():
            line = line.split('-')
            l = format_string(line[0], line[1])
            G.add_edges_from([(l[0],l[1])])
            nodes.add(l[0])
            nodes.add(l[1])

            # for testing
            if count < 20:
                testG.add_edges_from([(l[0],l[1])])
            count += 1

    print("Total number of nodes: ", int(G.number_of_nodes())) 
    print("Total number of edges: ", int(G.number_of_edges())) 

    #print(testG.out_degree('DME'))
    print(len(nodes))

    plt.figure(figsize=(10,10))
    nx.draw_networkx(testG, with_labels=True, node_color='lightblue')
    plt.savefig("testGraph.png")


    espilon = 0.15
    avg_error = 0.00001
    n = len(nodes)
    num_iter = int(math.log(avg_error) / math.log(1 - espilon))

    # initialize pagerank
    for node in nodes:
        pagerank[node] = 1.0 / n

    print(pagerank)

    return 

if __name__ == "__main__":
    main()