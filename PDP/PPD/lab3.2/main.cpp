#include <iostream>
#include <thread>
#include <random>
#include <mutex>
#include <vector>
#include <cstdlib>
#include <time.h>
#include <Windows.h>
#include <optional>
#include <queue>
#include <condition_variable>
using namespace std;

// Declare no of threads and matrixes size.
int startRandTime()
{
    srand(time(0));
    return 0;
}

int dummy = startRandTime(); // Used to initialize a new random seed before assigning global variables
int m = 20;
int n = 20;
int k = 20;
int noThreads = 5;
vector<vector<int>> firstMatrix; //(m,n)
vector<vector<int>> secondMatrix; //(n,k)
vector<vector<int>> resultMatrix; //(m,k)


void printResultMatrix() {

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < k; j++)
        {
            cout << resultMatrix[i][j] << " ";
        }
        cout << "\n";
    }

}

int calculateResultMatrixCell(int row, int col)
{

    //Calculates the result for one cell of the resulting matrix
    // row = the M from first matrix
    // col = the K from second matrix
    int totalSum = 0;

    for (int i = 0; i < n; i++)
    {


        totalSum = totalSum + (firstMatrix[row][i] * secondMatrix[i][col]);

    }

    return totalSum;
}


void threadCalculate(vector<pair<int, int>> cellsToCalculate)
{
    int cellValue;
    // Take every pair of positions and calculate for each the value

    for (int i = 0; i < cellsToCalculate.size(); i++)
    {
        cellValue = calculateResultMatrixCell(cellsToCalculate[i].first, cellsToCalculate[i].second);

        resultMatrix[cellsToCalculate[i].first][cellsToCalculate[i].second] = cellValue;

    }


}


void splitByRows()
{
    int noElems = m * k;
    while (noThreads % noElems == 0)
    {
        // Make sure we have localNoThreads not equal to 0
        noThreads = rand();
    }


    int localNoThreads = noThreads % noElems; // Have less threads than workload
    cout << "\nStarting to parse by rows workload of "<< noElems <<" cells to "<<localNoThreads << " threads.\n";
    int noCellsPerThread = noElems / localNoThreads; // Split workload

    int counter = 0;
    int threadIndex = 0;
    std::vector<std::thread> threads;
    vector<pair<int,int>> cellsToCalculate;
    // Up until -1, so the last one gets also the modulus (noElems % localNoThreads + noElems/localNoThreads)
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < k; j++)
        {
            cellsToCalculate.push_back(make_pair(i,j));
            counter++;
            if(threadIndex != localNoThreads - 1) // Give to last thread also rest of division workload
                if (counter == noCellsPerThread)
                {
                    // Start thread with the given cells
                    threads.emplace_back(threadCalculate, cellsToCalculate);
                    threadIndex++;
                    cellsToCalculate.clear();
                    counter = 0;
                }
        }
    }
    threads.emplace_back(threadCalculate, cellsToCalculate);
    for (int i = 0; i < localNoThreads; i++)
        threads[i].join();

    printResultMatrix();

}

void splitByColumns()
{
    int noElems = m * k;
    while (noThreads % noElems == 0)
    {
        // Make sure we have localNoThreads not equal to 0
        noThreads = rand();
    }


    int localNoThreads = noThreads % noElems; // Have less threads than workload
    cout << "\nStarting to parse by columns workload of " << noElems << " cells to " << localNoThreads << " threads.\n";
    int noCellsPerThread = noElems / localNoThreads; // Split workload

    int counter = 0;
    int threadIndex = 0;
    std::vector<std::thread> threadsCols;
    vector<pair<int, int>> cellsToCalculate;
    // Up untill -1, so the last one gets also the modulus (noElems % localNoThreads + noElems/localNoThreads)
    for (int j = 0; j < k; j++)
    {
        for (int i = 0; i < m; i++)
        {
            cellsToCalculate.push_back(make_pair(i, j));
            counter++;
            if (threadIndex != localNoThreads - 1) // Give to last thread also rest of division workload
                if (counter == noCellsPerThread)
                {
                    // Start thread with the given cells
                    threadsCols.emplace_back(threadCalculate, cellsToCalculate);
                    threadIndex++;
                    cellsToCalculate.clear();
                    counter = 0;
                }
        }
    }
    threadsCols.emplace_back(threadCalculate, cellsToCalculate);

    for (int i = 0; i < localNoThreads; i++)
        threadsCols[i].join();

    printResultMatrix();


}

void splitRandomly() {
    int noElems = m * k;
    while (noThreads % noElems == 0)
    {
        // Make sure we have localNoThreads not equal to 0
        noThreads = rand();
    }

    int randK = rand() % k;
    while (randK == 0)
    {
        randK = rand() % k;
    }
    int localNoThreads = noThreads % noElems; // Have less threads than workload
    cout << "\nStarting to parse randomly workload of " << noElems << " cells to " << localNoThreads << " threads going from "<<randK<<" by "<<randK<<" elements \n";



    std::vector<std::thread> threadsCols;
    vector<vector<pair<int, int>>> cellsToCalculate;
    vector<pair<int, int>> emptyVector;
    for (int i = 0; i < k; i++)
    {

        cellsToCalculate.push_back(emptyVector);
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < k; j++)
        {
            // Push to corresponding group
            cellsToCalculate[(i + j) % randK].push_back(make_pair(i, j));


        }
    }


    for (int i = 0; i < cellsToCalculate.size(); i++)
    {
        // Give group of positions to calculate
        threadsCols.emplace_back(threadCalculate, cellsToCalculate[i]);
    }

    for (int i = 0; i < cellsToCalculate.size(); i++)
        threadsCols[i].join();

    printResultMatrix();

}









int main()
{
    // Make sure columns have valid size
    while (m == 0)
        m = 20;
    while (n == 0)
        n = 20;
    while (k == 0)
        k = 20;
    vector<int> rowOfMatrix;
    cout << "First matrix size is: m: " << m << " and n: " << n;
    cout << "\nSecond matrix size is: n: " << n << " and k: " << k;
    cout << "\nResulting matrix size is: m: " << m << " and k: " << k;

    auto start_time = std::chrono::high_resolution_clock::now();


    //Generate random elements for firstMatrix
    for (int i = 0; i < m; i++)
    {
        rowOfMatrix.clear();
        for (int j = 0; j < n; j++)
        {
            int elem = rand() % 20;
            rowOfMatrix.push_back(elem);
        }
        firstMatrix.push_back(rowOfMatrix);
    }
    // Generate random elements for secondMatrix
    for (int i = 0; i < n; i++)
    {
        rowOfMatrix.clear();
        for (int j = 0; j < k; j++)
        {
            int elem = rand() % 20;
            rowOfMatrix.push_back(elem);
        }
        secondMatrix.push_back(rowOfMatrix);
    }
    // Assign the result matrix with zeros
    for (int i = 0; i < m; i++)
    {
        rowOfMatrix.clear();
        for (int j = 0; j < k; j++)
        {
            rowOfMatrix.push_back(0);
        }
        resultMatrix.push_back(rowOfMatrix);
    }

    splitByRows();
    // Assign the result matrix with zeros
    resultMatrix.clear();
    for (int i = 0; i < m; i++)
    {
        rowOfMatrix.clear();
        for (int j = 0; j < k; j++)
        {
            rowOfMatrix.push_back(0);
        }
        resultMatrix.push_back(rowOfMatrix);
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time);

    cout << "Matrix multiplication took " << duration.count() << " nano." << endl;


    splitByColumns();
    // Assign the result matrix with zeros
    resultMatrix.clear();
    for (int i = 0; i < m; i++)
    {
        rowOfMatrix.clear();
        for (int j = 0; j < k; j++)
        {
            rowOfMatrix.push_back(0);
        }
        resultMatrix.push_back(rowOfMatrix);
    }




    splitRandomly();
    // Assign the result matrix with zeros
    resultMatrix.clear();
    for (int i = 0; i < m; i++)
    {
        rowOfMatrix.clear();
        for (int j = 0; j < k; j++)
        {
            rowOfMatrix.push_back(0);
        }
        resultMatrix.push_back(rowOfMatrix);
    }




    return 0;
}

