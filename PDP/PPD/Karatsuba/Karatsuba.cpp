#include <iostream>
#include "Polinom.cpp"
#include <chrono>

int main() {

    Polynomial poly1(100);
    Polynomial poly2(100);  // Generate a random polynomial of degree 3

    // O(n^2) sequential multiplication time
    auto start = std::chrono::high_resolution_clock::now();
    Polynomial resultNSquaredSequential = poly1.multiplyNSquaredSequential(poly2);
    auto stop = std::chrono::high_resolution_clock::now();
    auto durationNSquaredSequential = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

    //  O(n^2) parallel multiplication time
    start = std::chrono::high_resolution_clock::now();
    Polynomial resultNSquaredParallel = poly1.multiplyNSquaredParallel(poly2);
    stop = std::chrono::high_resolution_clock::now();
    auto durationNSquaredParallel = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

    //  Karatsuba sequential multiplication time
    start = std::chrono::high_resolution_clock::now();
    Polynomial resultKaratsubaSequential = poly1.multiplyKaratsubaSequential(poly2);
    stop = std::chrono::high_resolution_clock::now();
    auto durationKaratsubaSequential = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

    //  Karatsuba parallel multiplication time
    start = std::chrono::high_resolution_clock::now();
    Polynomial resultKaratsubaParallel = poly1.multiplyKaratsubaParallel(poly2);
    stop = std::chrono::high_resolution_clock::now();
    auto durationKaratsubaParallel = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

   
    std::cout << "Polynomial 1: " << poly1 << std::endl;
    std::cout << "Polynomial 2: " << poly2 << std::endl;
    std::cout << "Multiplication O(n^2) sequential result: " << " (Time: " << durationNSquaredSequential.count() << " microseconds)" << std::endl;
    std::cout << "Multiplication O(n^2) parallel result: " << " (Time: " << durationNSquaredParallel.count() << " microseconds)" << std::endl;
    std::cout << "Multiplication Karatsuba sequential result: " << " (Time: " << durationKaratsubaSequential.count() << " microseconds)" << std::endl;
    std::cout << "Multiplication Karatsuba parallel result: " << " (Time: " << durationKaratsubaParallel.count() << " microseconds)" << std::endl;
}
