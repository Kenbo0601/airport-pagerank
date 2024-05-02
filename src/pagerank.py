# read source-dest file to create a graph 
# then implement pagerank algorithm
import math
import copy


# remove whitespaces, and newlines
def format_string(a,b):
    source = a.split(' ')
    dest = b.split('\n') 
    return [source[0], dest[0].strip()]

def main():

    pagerank = {}
    new_pagerank = {}

    # for each destination, stores sources pointing towards it; non-duplicate
    edges = {}

    nodes = set()

    # opposite of edges, for each source, stores its respective destinations; allows duplicates
    outgoing_edges = {}
    # dictionary where key is (source, dest) and value is number of duplicate edges
    duplicate_edges = {}

    with open("../data/source-dest.txt", encoding='utf-8') as f:
        for line in f.readlines():
            line = line.split(' ')
            node = format_string(line[0], line[1])
            source = node[0]
            dest = node[1]
            nodes.add(source)
            nodes.add(dest)

            # save incoming edges; ignore duplicates
            if dest not in edges:
                edges[dest] = [source]
            elif source not in edges[dest]:
                edges[dest].append(source)
            # total up number of duplicate edges for each (source, destination) pair; default is 1
            if (source, dest) not in duplicate_edges.keys():
                duplicate_edges[(source, dest)] = 1
            else:
                duplicate_edges[(source, dest)] += 1
            # save outgoing edges; allow duplicates ->
            # need this to ensure pagerank is divided by the correct number of edges
            if source not in outgoing_edges:
                outgoing_edges[source] = [dest]
            else:
                outgoing_edges[source].append(dest)

    # handle sink nodes: add edges to everything else
    '''print('Sink nodes')'''
    for node in nodes:
        if node not in outgoing_edges:
            '''print(node)'''
            # add edges to all other nodes; this should not affect duplicate_edges
            for dest in nodes:
                if node != dest:
                    if node not in outgoing_edges:
                        outgoing_edges[node] = [dest]
                    else:
                        outgoing_edges[node].append(dest)

    # values to match those of the cpp file
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
                for j in edges[node]: #j is sources pointing to node dest
                    multiplier = duplicate_edges[(j, node)]
                    sum += (multiplier * pagerank[j]) / (len(outgoing_edges[j]))
            new_pagerank[node] = ((1 - espilon) * sum) + (espilon/n)

        pagerank = copy.deepcopy(new_pagerank)
        new_pagerank.clear()

    sorted_pagerank = sorted(pagerank.items(), key=lambda item: item[1], reverse=True) 

    with open("../output/MultEdges.txt", "w") as out:
        for i in sorted_pagerank:
            L = [i[0], ":", str(i[1]), "\n"]
            out.writelines(L)
    out.close()


    return 

if __name__ == "__main__":
    main()