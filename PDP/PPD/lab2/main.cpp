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


int sumForIndex = 0;
int totalSum = 0;

class ProducerConsumerQueue {

private:
    std::condition_variable sendValueCondVar;
    std::condition_variable receiveValueCondVar;
    std::mutex commonMutex;
    std::queue<int> myQueue;
    bool end = false;

public:
    void enqueue(int val) {
        std::unique_lock<std::mutex> lck(commonMutex);
        while (myQueue.size() == 1)
        {
            sendValueCondVar.wait(lck);

        }

        myQueue.push(val);
        receiveValueCondVar.notify_one();
    }


    int dequeue() {
        int ret;

        std::unique_lock<std::mutex> lck(commonMutex);

        while (myQueue.empty())
            receiveValueCondVar.wait(lck);
        ret = myQueue.front();
        myQueue.pop();
        sendValueCondVar.notify_one();
        return ret;

    }


};

void producer(ProducerConsumerQueue* pInQueue,vector<int> v1,vector<int> v2) {
    for (int i = 0; i < v1.size(); i++) {
        int prod = v1[i] * v2[i];



        pInQueue->enqueue(prod);
    }
    pInQueue->enqueue(-1);

}

void adder(ProducerConsumerQueue* pInQueue) {
    int sum = 0;
    while (true) {

        int x = pInQueue->dequeue();

        if (x==-1) {
            break;
        }

        sum += x;
    }
    totalSum = sum;

}
int main()
{
    srand(time(0));
    vector<int> v1;
    vector<int> v2;
    int n = 10;
    int n1, n2;
    for (int i = 0; i < n; i++)
    {
        n1 = rand() % 15; v1.push_back(n1);
        n2 = rand() % 15; v2.push_back(n2);

    }
    ProducerConsumerQueue* firstQueue= new ProducerConsumerQueue;



    thread Consumer(adder,firstQueue);
    thread Producer(producer, firstQueue, v1, v2);

    Producer.join();
    Consumer.join();
    cout << "Total sum is " << totalSum << " and the elements are \n";
    for (int i = 0; i < v1.size(); i++)
        cout <<v1[i]<<" * "<<v2[i]<<" = " << v1[i] * v2[i] << endl;

    return 0;
}