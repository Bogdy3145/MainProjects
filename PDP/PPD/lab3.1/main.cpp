#include <iostream>
#include <thread>
#include <vector>
#include <functional>
#include <condition_variable>
#include <list>
#include <mutex>
#include <random>
#include <ctime>

using namespace std;

// Global variables for matrix sizes
int m = 0, n = 0, k = 0;
vector<vector<int>> firstMatrix;
vector<vector<int>> secondMatrix;
vector<vector<int>> resultMatrix;
mutex resultMatrixMutex;
int noThreads = 5;

// Basically the Priority Queue, but with lambda functions instead of 2 numbers
class ThreadPool {
public:
    explicit ThreadPool(size_t nrThreads) : m_end(false) {
        m_threads.reserve(nrThreads);
        for (size_t i = 0; i < nrThreads; ++i) {
            m_threads.emplace_back([this]() { this->run(); });
        }
    }

    ~ThreadPool() {
        close();
        for (std::thread& t : m_threads) {
            t.join();
        }
    }



    void close() {
        {
            unique_lock<mutex> lck(m_mutex);
            m_end = true;
        }
        m_cond.notify_all();
    }

    void enqueue(function<void()> func) {
        {
            unique_lock<mutex> lck(m_mutex);
            m_queue.push_back(move(func));
        }
        m_cond.notify_one();
    }

private:
    void run() {
        while (true) {
            function<void()> toExec;
            {
                unique_lock<mutex> lck(m_mutex);
                m_cond.wait(lck, [this] { return m_end || !m_queue.empty(); });
                if (m_queue.empty() && m_end) {
                    return;
                }
                toExec = move(m_queue.front());
                m_queue.pop_front();
            }
            toExec();
        }
    }

    mutex m_mutex;
    condition_variable m_cond;
    list<function<void()>> m_queue;
    bool m_end;
    vector<thread> m_threads;
};


void printMatrix(vector<vector<int>> matrixToPrint) {

    cout << "The Matrix is:\n";
    for (int i = 0; i < matrixToPrint.size(); i++)
    {
        for (int j = 0; j < matrixToPrint[0].size(); j++)
        {
            cout << matrixToPrint[i][j] << " ";
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


void splitByRows(ThreadPool& pool) {
    int noElems = m * k;
    int noCellsPerThread = noElems / noThreads;
    int remainder = noElems % noThreads;
    vector<pair<int, int>> cellsToCalculate;
    int cellCount = 0;
    int taskCellLimit = noCellsPerThread;
    for (int row = 0; row < m; row++)
    {
        for (int col = 0; col < k; col++)
        {
            cellsToCalculate.push_back(std::make_pair(row, col));

            cellCount++;

            if (remainder > 0)
            {
                taskCellLimit++; // If there are extra cells, add one more to this task's limit
                remainder--; // Decrement the number of extra cells remaining
            }

            // If the cell count reaches the task limit, enqueue the task
            if (cellCount == taskCellLimit) {

                pool.enqueue([cells = cellsToCalculate]() {

                    for (auto& cell : cells) {

                        int result = calculateResultMatrixCell(cell.first, cell.second);
                        resultMatrix[cell.first][cell.second] = result;
                    }
                });
                cellsToCalculate.clear(); // Clear the list for the next batch of cells
                cellCount = 0; // Reset the cell count for the next task
                taskCellLimit = noCellsPerThread;
            }
        }
    }

    // Enqueue any remaining cells that did not form a full task
    if (!cellsToCalculate.empty()) {
        pool.enqueue([cells = move(cellsToCalculate)]() {
            for (auto& cell : cells) {
                resultMatrix[cell.first][cell.second] = calculateResultMatrixCell(cell.first, cell.second);
            }
        });
    }
}


void splitByColumns(ThreadPool& pool) {
    int noElems = m * k;
    int noCellsPerThread = noElems / noThreads;
    int remainder = noElems % noThreads;
    vector<pair<int, int>> cellsToCalculate;
    int cellCount = 0;
    int taskCellLimit = noCellsPerThread;
    for (int col = 0; col < k; col++)
    {
        for (int row = 0; row < m; row++)
        {
            cellsToCalculate.push_back(std::make_pair(row, col));
            cellCount++;

            if (remainder > 0)
            {
                taskCellLimit++; // If there are extra cells, add one more to this task's limit
                remainder--; // Decrement the number of extra cells remaining
            }

            // If the cell count reaches the task limit, enqueue the task
            if (cellCount == taskCellLimit) {

                pool.enqueue([cells = cellsToCalculate]() {

                    for (auto& cell : cells) {

                        int result = calculateResultMatrixCell(cell.first, cell.second);
                        resultMatrix[cell.first][cell.second] = result;
                    }
                });
                cellsToCalculate.clear(); // Clear the list for the next batch of cells
                cellCount = 0; // Reset the cell count for the next task
                taskCellLimit = noCellsPerThread;
            }
        }
    }

    // Enqueue any remaining cells that did not form a full task
    if (!cellsToCalculate.empty()) {
        pool.enqueue([cells = move(cellsToCalculate)]() {
            for (auto& cell : cells) {
                resultMatrix[cell.first][cell.second] = calculateResultMatrixCell(cell.first, cell.second);
            }
        });
    }
}

void splitRandomly(ThreadPool& pool) {
    int noElems = m * k;
    int cellsPerTask = noElems / noThreads;
    int remainder = noElems % noThreads;
    int randK = rand() % noThreads;
    vector<vector<pair<int, int>>> cellsToCalculate(randK);

    // Populate the task lists
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < k; ++j) {
            int index = (i * k + j) % randK;
            cellsToCalculate[index].emplace_back(i, j);
        }
    }

    // Enqueue the tasks to the thread pool
    for (int i = 0; i < cellsToCalculate.size(); i++) {
        pool.enqueue([cells = move(cellsToCalculate[i])]() {
            for (auto& cell : cells) {
                int value = calculateResultMatrixCell(cell.first, cell.second);
                resultMatrix[cell.first][cell.second] = value;

            }
        });
    }
}

int main() {
    srand(time(0));

    // Initialize matrix dimensions and the number of threads
    while (m == 0)
        m = 20;
    while (n == 0)
        n = 20;
    while (k == 0)
        k = 20;

    cout << "First matrix size is: m: " << m << " and n: " << n;
    cout << "\nSecond matrix size is: n: " << n << " and k: " << k;
    cout << "\nResulting matrix size is: m: " << m << " and k: " << k << "\n";

    vector<int> rowOfMatrix;

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


    auto start_time = std::chrono::high_resolution_clock::now();

    // Create a thread pool

    ThreadPool pool(noThreads);

    splitByRows(pool);
    //splitByColumns(pool);
    //splitRandomly(pool);


    // Close the pool and wait for all tasks to finish
    pool.close();

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time);

    cout << "Matrix multiplication took " << duration.count() << " nano." << endl;

    cout << "\nThe first matrix is:\n";
    printMatrix(firstMatrix);

    cout << "\nThe second matrix is:\n";
    printMatrix(secondMatrix);

    cout << "\nThe result matrix is:\n";
    printMatrix(resultMatrix);



    return 0;
}
