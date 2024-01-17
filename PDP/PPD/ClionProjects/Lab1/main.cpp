#include <iostream>
#include <thread>
#include <random>
#include <mutex>
#include <vector>
#include <cstdlib>
#include <time.h>
#include <Windows.h>
using namespace std;


//Product: -Price long long int
//			-Quantity int
//Bill:	- Multiple Products
//		-Total price long long int
//Record: -Multiple  Bills
//
//Check inventory- random time - validate that all the money are justified by the recorded bills.

class Product
{

public:
    void setQuantity(int newQuant) { this->quantity = newQuant; }
    void subtractFromQuantity(int subtractedQuantity) { this->quantity = this->quantity - subtractedQuantity; }
    int getQuantity() { return this->quantity;}
    void setPrice(long long int newPrice) { this->price = newPrice; }
    long long int getPrice() { return this->price; }
    string getName() { return this->name; }
    void setName(string newName) { this->name = newName; }
    int getId() { return this->id; }
    void setId(int newId) { this->id = newId; }
private:
    string name;
    int id;
    long long int price;
    int quantity;


};

class Bill
{
public:
    vector<Product*> getProducts() { return this->myProducts; }
    void addProduct(Product* p) { this->myProducts.push_back(p); addToTotal(p->getPrice() * p->getQuantity()); }
    long long int getTotal() { return this->total; }
    void addToTotal(long long int newProductPrice) { this->total=this->total+newProductPrice; }
private:
    long long int total=0;
    vector<Product*> myProducts;



};

int generateNumberOfProducts()
{
    srand(time(0));
    int noProds = rand() % 100;
    int secondary = (rand() % 100) * (rand() % 100);
    noProds = noProds * secondary;
    noProds = noProds % 10;
    return noProds;

}

int noProdsGlobal = generateNumberOfProducts();
int noThreadsQuit = 0;
vector<mutex> mutexes(noProdsGlobal);
mutex marketBillsMutex;
vector<Bill*> marketBills;
vector <Product*> marketInventory;
long long int marketTotalProfit = 0;


void startShopping(int id) {

    srand(id);
    int randomProductId;
    bool stopWhenProductWithZeroQuantityIsGenerated = false;
    int randomQuantityToBuy;
    int priceOfProduct;

    //Do multiple Bills
    while (true) {


        //Choose a random number of products to compose a Bill
        Bill* currentBill = new Bill();
        int randomNoProdsPerBill = rand() % 10;

        while (randomNoProdsPerBill != 0)
        {
            //Choose a random product and buy it
            randomProductId = rand() % (marketInventory.size());

            mutexes[randomProductId].lock();
            if (marketInventory[randomProductId]->getQuantity() > 0)
            {

                if (marketInventory[randomProductId]->getQuantity() == 1)
                {
                    randomQuantityToBuy = 1;
                }
                else
                {
                    randomQuantityToBuy = rand() % marketInventory[randomProductId]->getQuantity();

                }

                priceOfProduct = marketInventory[randomProductId]->getPrice();


                marketInventory[randomProductId]->subtractFromQuantity(randomQuantityToBuy);

                Product* newProduct = new Product();
                newProduct->setId(marketInventory[randomProductId]->getId());
                newProduct->setPrice(priceOfProduct);
                newProduct->setQuantity(randomQuantityToBuy);

                currentBill->addProduct(newProduct);
            }
            else
            {
                stopWhenProductWithZeroQuantityIsGenerated = true;

            }

            mutexes[randomProductId].unlock();

            randomNoProdsPerBill--;
        }

        //Add bill to market records
        marketBillsMutex.lock();
        marketBills.push_back(currentBill);
        marketTotalProfit = marketTotalProfit + currentBill->getTotal();
        cout << "Purchase in value of " << currentBill->getTotal() << " for bill " << marketBills.size() - 1 << " has been made by thread "<< id;
        cout << ". Market profit is now: " << marketTotalProfit << endl;
        if (stopWhenProductWithZeroQuantityIsGenerated == true)
            cout << "Thread with ID: " << id << " will quit.\n";
        noThreadsQuit++;
        marketBillsMutex.unlock();

        //Stop when a product with quantity 0 was picked(after adding the current bill to the record)
        if (stopWhenProductWithZeroQuantityIsGenerated == true)
            break;


        //Wait before creating another bill
        Sleep(rand());





    }
}

void randomInventoryCheck(int noThreads)
{
    while (true) {

        //Wait before checking
        Sleep(rand());

        for (int i = 0; i < noProdsGlobal; i++)
        {
            //Block all mutexes for all products
            mutexes[i].lock();
        }


        //Block records mutex
        marketBillsMutex.lock();
        cout << "Checking all bills within the market record...\n";

        long long int calculatedMarketTotal=0;
        //Loop through all bills

        for (int i = 0; i < marketBills.size(); i++)
        {
            //Get total stored for a bill
            long long int totalPerBill = marketBills[i]->getTotal();
            long long int calculatedBillTotal=0;
            vector<Product*> productsPerBill = marketBills[i]->getProducts();
            //Loop through all products for one bill
            for (int j = 0; j < productsPerBill.size(); j++)
            {
                //Calculate total for a bill, product by product
                calculatedBillTotal = calculatedBillTotal +
                                      (productsPerBill[j]->getQuantity() * productsPerBill[j]->getPrice());

            }

            //Verify stored total for a bill with calculated total for a bill
            if (totalPerBill == calculatedBillTotal)
            {
                cout << "Total for bill " << i << " is valid" << endl;
            }
            else
            {
                cout << "Total for bill " << i << " is wrong. Please stop stealing from our shop!" << endl;
            }

            //Add bill total to total profit
            calculatedMarketTotal = calculatedMarketTotal + totalPerBill;
        }
        //Verify marketProfit with calculated total profit
        if (marketTotalProfit == calculatedMarketTotal)
        {
            cout << "Profit was legally acquired for this market. Profit is: "<<marketTotalProfit << endl;
        }
        else
        {
            cout << "Profit was not legally acquired for this market. Calling ANAF..." << endl;
        }
        marketBillsMutex.unlock();


        for (int i = 0; i < noProdsGlobal; i++)
        {
            //Unlock all mutexes for all products
            mutexes[i].unlock();
        }

        if(noThreadsQuit == noThreads)
            break;
        if (noThreads == 0)
            break;
    }
}



int main()
{
    int newQuantity;
    long long int newPrice;
    srand(time(0));
    std::vector<std::thread> threads;
    cout << "No of product entities available:" << noProdsGlobal << endl;

    for (int i = 0; i < noProdsGlobal; i++)
    {

        //Generate new products in inventory
        newPrice = rand() % 10;
        newQuantity = rand();

        Product* newProduct = new Product();
        newProduct->setPrice(newPrice);
        newProduct->setQuantity(newQuantity);
        newProduct->setId(i);
        marketInventory.push_back(newProduct);

    }

    int noThreads = 2 * noProdsGlobal;

    cout << "No of threads used:" << noThreads << endl;

    //Time to time check
    thread periodicCheck(randomInventoryCheck,noThreads);

    for (int i = 0; i < noThreads; i++)
    {
        //Start threads
        threads.emplace_back(startShopping,i);
    }


    for (int i = 0; i < noThreads; i++)
    {
        //Wait for threads
        threads[i].join();
    }


    periodicCheck.join();

    cout << "\nAll threads have ended! Making final check \n";


    //End check
    thread finalCheck(randomInventoryCheck,0);
    finalCheck.join();

    return 0;
}