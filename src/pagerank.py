# read source-dest file to create a graph 
# then implement pagerank algorithm 
import networkx as nx
import matplotlib.pyplot as plt
import math
import copy


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

    outgoing_edges = {}  # opposite of edges, for each source, stores its respective destinations
    duplicate_edges = {} # dictionary where key is (source, dest) and value is number of duplicate edges

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
            ''' Thu: Do you mean incoming edges for each destination node for the above comment?
            My assumption is that edges stores at each destination a list of source airports that point to it;
            From that, I tried to avoid storing duplicate source airports associated with that destination airport
            since duplicate_edges stores the number of edges from src -> dest at (source, destination)/;
            Outgoing_edges is similar to edges but instead, stores at each source a list of destination airports 
            it points to. I figured that len(outgoing_edges[source]) would give the total number of outgoing edges, 
            including duplicate edges, to give the total number of edges.
            The resulting result.txt looks similar to output.txt, although I'm not sure if that was what I should have
            been aiming for...'''
            if dest not in edges:
                edges[dest] = [source]
            elif source not in edges[dest]:
                edges[dest].append(source)
            if (source, dest) not in duplicate_edges.keys():
                duplicate_edges[(source, dest)] = 1
            else:
                duplicate_edges[(source, dest)] += 1
            if source not in outgoing_edges: # the opposite of edges, stores destinations from the source
                outgoing_edges[source] = [dest]
            else:
                outgoing_edges[source].append(dest)
            count += 1
            '''Thu: Feel free to delete any repetitive stuff I wrote, I was just trying things out to make it work!'''

    print("Total number of nodes: ", int(G.number_of_nodes())) 
    print("Total number of edges: ", int(G.number_of_edges()))

    #print(testG.out_degree('DME'))
    #print(edges)
    
    #plt.figure(figsize=(10,10))
    #pos = nx.kamada_kawai_layout(G)
    #node_options = {"node_color": "lightblue", "node_size":30}
    #edge_options = {"width": .50, "alpha":.5, "edge_color": "black"}
    #nx.draw_networkx_nodes(G, pos, **node_options)
    #nx.draw_networkx_edges(G, pos, **edge_options)
    #plt.savefig("testGraph.png")


    #espilon = 0.15
    espilon = 0.2
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
                for j in edges[node]: #j is sources pointing to node dest
                    #if (j, node) in duplicate_edges.keys():
                        #multiplier = duplicate_edges[(j, node)]
                    #else:
                        #multiplier = 1
                    multiplier = duplicate_edges[(j, node)]
                    sum += (multiplier * pagerank[j]) / (len(outgoing_edges[j]))
                    #sum += pagerank[j]) / G.out_degree(j)
            new_pagerank[node] = ((1 - espilon) * sum) + (espilon/n)
            #print("node: ", node, " - pagerank: ",new_pagerank[node])

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