# read source-dest file to create a graph 
# then implement pagerank algorithm 
import networkx as nx
import matplotlib.pyplot as plt
import math
import copy
#from pyvis.network import Network


# remove whitespaces, and newlines
def format_string(a,b):
    source = a.split(' ')
    dest = b.split('\n') 
    return [source[0], dest[0].strip()]

def main():

    G = nx.DiGraph() # create a directed graph 
    testG = nx.DiGraph()
    pagerank = {}
    new_pagerank = {}
    edges = {}
    nodes = set()

    count = 0
    with open("source-dest.txt", encoding='utf-8') as f:
        for line in f.readlines():
            line = line.split('-')
            node = format_string(line[0], line[1])
            source = node[0]
            dest = node[1]
            #if count < 20:
            G.add_edges_from([(source, dest)])
            nodes.add(source)
            nodes.add(dest)

            # save incoming nodes for each source node 
            if dest not in edges:
                edges[dest] = [source]
            else:
                edges[dest].append(source)

            count += 1

    print("Total number of nodes: ", int(G.number_of_nodes())) 
    print("Total number of edges: ", int(G.number_of_edges())) 

    #print(testG.out_degree('DME'))
    #print(edges)
    print(G.in_degree('PEK'))
    print(G.in_degree('CTU'))
    print(G.in_degree('XIY'))
    print(G.in_degree('PVG'))
    print(G.in_degree('CAN'))

    plt.figure(figsize=(100,100))
    nx.draw_random(G, with_labels=True, node_color='lightblue')
    plt.savefig("testGraph.png")

    #net = Network(notebook=True)
    #net.from_nx(G)
    #net.show("test.html")

    espilon = 0.15
    avg_error = 0.00001
    n = len(nodes)
    num_iter = int(math.log(avg_error) / math.log(1 - espilon))

    # initialize pagerank
    for node in nodes:
        pagerank[node] = 1.0 / n

    for i in range(num_iter):
        print("Iteration ", i)
        for node in nodes:
            sum = 0
            if node in edges:
                for j in edges[node]:
                    sum += pagerank[j] / G.out_degree(j)
            new_pagerank[node] = ((1 - espilon) * sum) + (espilon/n)

        pagerank = copy.deepcopy(new_pagerank)
        new_pagerank.clear()

    sorted_pagerank = sorted(pagerank.items(), key=lambda item: item[1], reverse=True) 

    with open("result.txt", "w") as out:
        for i in sorted_pagerank:
            L = [i[0], ":", str(i[1]), "\n"]
            out.writelines(L)
    out.close()


    return 

if __name__ == "__main__":
    main()