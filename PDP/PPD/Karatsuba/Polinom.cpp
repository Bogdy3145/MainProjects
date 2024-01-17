#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <thread>
#include <mutex>

class Polynomial {
private:
    std::vector<int> coefficients;
    int degree;

    void generateCoefficients(int degree) {
        coefficients.clear();
        this->degree = degree;  
        srand(time(0));
        for (int i = 0; i <= degree; i++) {
            int coefficient = std::rand() % 10 * (std::rand() % 2 == 0 ? 1 : -1);
            while (coefficient == 0 && i == degree) {
                coefficient = std::rand() % 10 * (std::rand() % 2 == 0 ? 1 : -1);
            }
            coefficients.push_back(coefficient);
        }
    }

public:
    Polynomial(std::vector<int> coefficients) : coefficients(coefficients) {
        degree = coefficients.size() - 1;
    }

    Polynomial(int degree) : degree(degree) {
       
        generateCoefficients(degree);
    }

    std::vector<int> getCoefficients() const {
        return coefficients;
    }

    int getDegree() const {
        return degree;
    }

    void setCoefficients(std::vector<int> coefficients) {
        this->coefficients = coefficients;
        degree = coefficients.size() - 1;  
    }

    void setDegree(int degree) {
        this->degree = degree;
        generateCoefficients(degree);
    }

    Polynomial multiplyNSquaredSequential(const Polynomial& other) const {
        int resultDegree = degree + other.getDegree();
        std::vector<int> resultCoefficients(resultDegree + 1, 0);

        for (int i = 0; i <= degree; i++) {
            for (int j = 0; j <= other.getDegree(); j++) {
                resultCoefficients[i + j] += coefficients[i] * other.getCoefficients()[j];
            }
        }

        return Polynomial(resultCoefficients);
    }

    Polynomial multiplyNSquaredParallel(const Polynomial& other) const {
        int resultDegree = degree + other.getDegree();
        std::vector<int> resultCoefficients(resultDegree + 1, 0);
        std::mutex resultMutex;  // Mutex to protect resultCoefficients

        std::vector<std::thread> threads;

        // Create a separate thread for each term of the outer poly
        // Each thread will calculate the multiplication of one term from the outer poly with all the terms of the inner poly
        for (int i = 0; i <= degree; i++) {
            threads.emplace_back([this, &resultCoefficients, &other, &resultMutex, i]() {
                for (int j = 0; j <= other.getDegree(); j++) {
                    // Lock the resultCoefficients with a mutex while updating
                    std::lock_guard<std::mutex> lock(resultMutex);
                    resultCoefficients[i + j] += coefficients[i] * other.getCoefficients()[j];
                }
                });
        }

        for (auto& thread : threads) {
            thread.join();
        }

        return Polynomial(resultCoefficients);
    }


    Polynomial multiplyKaratsubaSequential(const Polynomial& other) const {
        int n = std::max(degree, other.getDegree()) + 1;
        std::vector<int>  secondCoeff = other.getCoefficients();

        // Make sure secondCoeff has at least n elements by adding leading zeros
        if (secondCoeff.size() < n) {
            secondCoeff.resize(n, 0);
        }

        // End condition
        if (n == 1) {
            std::vector<int> resultCoefficients = { coefficients[0] * secondCoeff[0] };
            return Polynomial(resultCoefficients);
        }

        int mid = n / 2;
        

        // Split first poly
        std::vector<int> a0(coefficients.begin(), coefficients.begin() + mid);
        std::vector<int> a1(coefficients.begin() + mid, coefficients.end());

        // Split second poly
        std::vector<int> b0(secondCoeff.begin(), secondCoeff.begin() + std::min(mid, other.getDegree() + 1));
        std::vector<int> b1(secondCoeff.begin() + std::min(mid, other.getDegree() + 1), secondCoeff.begin() + std::min(2 * mid, other.getDegree() + 1));

        // Create 4 new polynomial instances
        Polynomial a0Poly(a0);
        Polynomial a1Poly(a1);
        Polynomial b0Poly(b0);
        Polynomial b1Poly(b1);

        // Multiply second with fourth
        Polynomial z0 = a0Poly.multiplyKaratsubaSequential(b0Poly);

        // first with third
        Polynomial z2 = a1Poly.multiplyKaratsubaSequential(b1Poly);

        // The (P1(X)+P2(X)) * (Q1(X)+Q2(X)) - 1(X)* Q1(X) - P2(X)*Q2(X)
        Polynomial z1 = (a0Poly + a1Poly).multiplyKaratsubaSequential(b0Poly + b1Poly) - z0 - z2;

        std::vector<int> resultCoefficients(2 * n - 1, 0);

        // Copy the coefficients of z0 to the corresponding positions in resultCoefficients
        for (int i = 0; i <= z0.getDegree(); i++) {
            resultCoefficients[i] += z0.getCoefficients()[i];
        } 

        // Copy the coefficients of z1 to the positions shifted by mid in resultCoefficients
        for (int i = 0; i <= z1.getDegree(); i++) {
            resultCoefficients[i + mid] += z1.getCoefficients()[i];
        }

        // Copy the coefficients of z2 to the positions shifted by 2 * mid in resultCoefficients
        for (int i = 0; i <= z2.getDegree(); i++) {
            resultCoefficients[i + 2 * mid] += z2.getCoefficients()[i];
        }

        return Polynomial(resultCoefficients);
    }

    Polynomial multiplyKaratsubaParallel(const Polynomial& other) const {
        int n = std::max(degree, other.getDegree()) + 1;
        std::vector<int> secondCoeff = other.getCoefficients();

        // Make sure secondCoeff has at least n elements by adding leading zeros
        if (secondCoeff.size() < n) {
            secondCoeff.resize(n, 0);
        }

        // End condition
        if (n == 1) {

            std::vector<int> resultCoefficients = { coefficients[0] * secondCoeff[0] };
            return Polynomial(resultCoefficients);
        }

        int mid = n / 2;
        // Declare resultCoefficients here
        std::vector<int> resultCoefficients(2 * n - 1, 0);
        std::mutex resultMutex;

        // Split first poly
        std::vector<int> a0(coefficients.begin(), coefficients.begin() + mid);
        std::vector<int> a1(coefficients.begin() + mid, coefficients.end());

        // Split second poly
        std::vector<int> b0(secondCoeff.begin(), secondCoeff.begin() + std::min(mid, other.getDegree() + 1));
        std::vector<int> b1(secondCoeff.begin() + std::min(mid, other.getDegree() + 1), secondCoeff.begin() + std::min(2 * mid, other.getDegree() + 1));

        // Create 4 new polynomial instances
        Polynomial a0Poly(a0);
        Polynomial a1Poly(a1);
        Polynomial b0Poly(b0);
        Polynomial b1Poly(b1);

        // Multiply second with fourth in parallel
        std::thread threadZ0([&]() {
            Polynomial z0 = a0Poly.multiplyKaratsubaParallel(b0Poly);
            
            for (int i = 0; i <= z0.getDegree(); i++) {
                resultCoefficients[i] += z0.getCoefficients()[i];
            }
            });

        // first with third in parallel
        std::thread threadZ2([&]() {
            Polynomial z2 = a1Poly.multiplyKaratsubaParallel(b1Poly);
            
            for (int i = 0; i <= z2.getDegree(); i++) {
                resultCoefficients[i + 2 * mid] += z2.getCoefficients()[i];
            }
            });

        // The (P1(X)+P2(X)) * (Q1(X)+Q2(X)) in parallel
        std::thread threadZ1([&]() {
            Polynomial z0 = a0Poly.multiplyKaratsubaParallel(b0Poly);

            Polynomial z2 = a1Poly.multiplyKaratsubaParallel(b1Poly);

            Polynomial z1 = (a0Poly + a1Poly).multiplyKaratsubaParallel(b0Poly + b1Poly)-z0-z2;
           
            for (int i = 0; i <= z1.getDegree(); i++) {
                resultCoefficients[i + mid] += z1.getCoefficients()[i];
            }
            });

        // Join the threads
        threadZ0.join();
        threadZ2.join();
        threadZ1.join();

        return Polynomial(resultCoefficients);
    }



    Polynomial operator+(const Polynomial& other) const {
        int n = std::max(degree, other.getDegree()) + 1;
        std::vector<int> resultCoefficients(n, 0);

        for (int i = 0; i <= degree; ++i) {
            resultCoefficients[i] += coefficients[i];
        }

        for (int i = 0; i <= other.getDegree(); ++i) {
            resultCoefficients[i] += other.getCoefficients()[i];
        }

        return Polynomial(resultCoefficients);
    }


    Polynomial operator-(const Polynomial& other) const {
        int n = std::max(degree, other.getDegree()) + 1;
        std::vector<int> resultCoefficients(n, 0);

        for (int i = 0; i <= degree; ++i) {
            resultCoefficients[i] += coefficients[i];
        }

        for (int i = 0; i <= other.getDegree(); ++i) {
            resultCoefficients[i] -= other.getCoefficients()[i];
        }

        return Polynomial(resultCoefficients);
    }

    friend std::ostream& operator<<(std::ostream& os, const Polynomial& poly) {
        for (int i = poly.degree; i >= 0; i--) {
            if (poly.coefficients[i] != 0) {
                if (poly.coefficients[i] > 0 && i != poly.degree) {
                    os << "+";
                }
                os << poly.coefficients[i];
                if (i > 0) {
                    os << "x^" << i;
                }
            }
        }
        return os;
    }
};
