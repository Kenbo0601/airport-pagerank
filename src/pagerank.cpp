#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

// Custom comparison function to compare pairs based on the second value
bool compareSecond(const std::pair<std::string, double>& a, const std::pair<std::string, double>&b) {
    return a.second > b.second;
}

// function to sort pageranks
std::vector<std::pair<std::string, double> > sort_pagerank(std::map<std::string,double> pagerank)
{
    std::vector<std::pair <std::string, double> > sorted_pagerank;

    for(auto& itr : pagerank) {
        sorted_pagerank.push_back(itr);
    }

    sort(sorted_pagerank.begin(), sorted_pagerank.end(), compareSecond); // call sort func from algorithm lib

    return sorted_pagerank;
}


int main() {

    std::ifstream file("source-dest.txt"); // Change "edges.txt" to your file name
    if (!file.is_open()) {
        std::cerr << "Unable to open file" << std::endl;
        return 1;
    }

    std::cout << "Opened file successfully" << std::endl;

    std::map<std::string, std::vector<std::string> > edges;
    std::map<std::string, double> pagerank; 
    std::set<std::string> nodes;
    std::map<std::string, int> out_degree;
    std::string from_id, to_id;

    while (file >> from_id >> to_id) {
        // Process the edge here
        if(std::find(edges[to_id].begin(), edges[to_id].end(), from_id) != edges[to_id].end()) {
            std::cout << to_id << " already has an edge from " << from_id << std::endl;
        } else {
            edges[to_id].push_back(from_id);
            out_degree[from_id]++;
            nodes.insert(from_id);
            nodes.insert(to_id);
        }
    } 

    file.close();
    std::cout << "Done reading the file" << std::endl;


    // handle sink nodes: add edges to everything else 
    std::cout << "Adding edges to all nodes from sink nodes ... " << std::endl;
    for(std::string node: nodes) {
        if(out_degree[node] == 0) {
            std::cout << node << std::endl;
            for(std::string node_second : nodes) {
                if(node != node_second) {
                    edges[node_second].push_back(node);
                    out_degree[node]++;
                }
            }
        }
    }
    std::cout << "Done adding edges." << std::endl;

    for ( const auto &p : edges)
    {
        std::cout << p.first << " :";
        for ( const auto &s : p.second )
        {
            std::cout << ' ' << s;
        }
        std::cout << std::endl;
    }

    double epsilon = 0.15, avg_error = 0.00001;
    int n = nodes.size();
    int num_iterations = (int) (std::log(avg_error) / std::log(1 - epsilon));

    // Initialize pagerank
    for (std::string node : nodes) {
        pagerank[node] = 1.0 / n;
    }

    std::map<std::string, double> new_pagerank; // store new pagerank at each iteration
    std::vector<std::pair <std::string, double> > sorted_pagerank; //store sorted pagerank

    for(int i = 0; i < num_iterations; ++i) {
        std::cout << "Iteration " <<  i << std::endl;
        for(std::string node : nodes) {
            double sum = 0;
            std::vector<std::string> from_edges = edges[node];
            for(int j = 0; j < from_edges.size(); ++j) {
                sum += pagerank[from_edges[j]] / out_degree[from_edges[j]];
            }
            //we dont want to update each node of pagerank during the same iteration, so store then in a temp map
            new_pagerank[node] = ((1 - epsilon) * sum) +  (epsilon/n); 
        }

        pagerank = new_pagerank;
        new_pagerank.clear();
    }

    // function call for sorting
    // sorted values are stored in sorted_pagerank
    sorted_pagerank = sort_pagerank(pagerank);
    pagerank.clear();

    // write result in a txt file and store top five nodes in a set 
    std::ofstream outfile("SingleEdge.txt", std::ofstream::trunc); // erase the contents of the file if exists
    int count = 1;
    for(auto& itr : sorted_pagerank) {
        outfile << itr.first << ", " << itr.second << "\n";
    }
    outfile.close();

    return 0;
}