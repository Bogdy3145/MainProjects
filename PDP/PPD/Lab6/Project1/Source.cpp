#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <thread>
#include <vector>
#include <fstream>
#include <time.h>
#include <mutex>
#include <set>
using namespace std;

vector<int> hPath;
bool existsCycle = false;
int n, m;

int noOfVertexes = 50;
int edgesNumber = 10; // 50 + 10
int MAX_THREADS = 5000;
bool THREAD_LIMIT_REACHED = false;

void searchPath(vector<vector<bool>> graph, vector<int> path, set<int> visited, int pos, int thread_counter)
{
    vector<std::thread> myThreads;
   
    path.push_back(pos); // Put current vertex in path
    visited.insert(pos);
    
    if (thread_counter >= MAX_THREADS)
        THREAD_LIMIT_REACHED = true;
    
    if (path.size() == graph[0].size())
    {
        int lastVertex = path[path.size() - 1];
        if (graph[lastVertex][path[0]] == 1) // Edge between last and first from path
        {
            path.push_back(path[0]);
            hPath = path;
            existsCycle = true;
        }
    }
    else {
       
        
        vector<bool> neighbours = graph[pos];
        for (int i = 0; i < neighbours.size(); i++)
            if (neighbours[i] == 1)
            {
              
                if (visited.find(i) == visited.end()) {
                    if (THREAD_LIMIT_REACHED == false)
                        myThreads.emplace_back(searchPath, graph, path,visited, i, thread_counter+1); //Path does not contain already the neighbour
                    else
                    {
                        searchPath(graph, path,visited, i, thread_counter + 1);
                    }
                }

            }
        
        for (std::thread& thread : myThreads) {
            thread.join();
        }
    }
    
   
} 


void printGraph(vector<vector<bool>> myGraph)
{
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << myGraph[i][j] << " ";
        }
        cout << endl;
    }
}

void fillGraphWithZero(vector<vector<bool>>& myGraph)
{
    vector<bool>partial;
    n = noOfVertexes; // No of vertexes
    for (int i = 0; i < n; i++)
    {
        partial.push_back(0);
    }
    for (int i = 0; i < n; i++)
    {
        myGraph.push_back(partial);
    }
}

void generateGraph(vector<vector<bool>>& myGraph)
{

    fillGraphWithZero(myGraph);
    
   
    for (int i = 0; i < myGraph.size() - 1; i++)
    {
        myGraph[i][i + 1] = 1; // Make sure there is one cycle that contains all vertexes
    }

    myGraph[myGraph.size() - 1][0] = 1; // Make sure there is one cycle that contains all vertexes

    srand(time(0));
    int edges = edgesNumber;
    for (int i = 0; i < edges; i++)
    {
        // Add random edges to make the search harder
        int row = rand() % noOfVertexes;
        int col = rand() % noOfVertexes;
        myGraph[row][col] = 1;
    }
    
}

int main() {
    vector<vector<bool>> myGraph;

    generateGraph(myGraph);
    
    //printGraph(myGraph);

    vector<int> path;
    set<int> visited;
    int start = 0;
    searchPath(myGraph, path,visited,start, 0);

    

    if (existsCycle)
    {
        cout << "Cycle exists:\n";
        for (int i = 0; i < hPath.size(); i++)
        {
            cout << hPath[i] << " ";
        }
        cout << "\n";
    }
    else
        cout << "No Hamiltonean cycle exists.\n";

    return 0;
}