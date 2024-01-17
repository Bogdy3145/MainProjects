#include <iostream>
#include <mpi.h>
#include <vector>

struct Polynomial {
    std::vector<int> coefficients;

    Polynomial(std::vector<int> coeffs) : coefficients(coeffs) {}

    Polynomial() = default;

    void padZeros(int n) {
        coefficients.insert(coefficients.begin(), n, 0);
    }

    Polynomial operator+(const Polynomial& other) const {
        Polynomial result;
        result.coefficients.resize(std::max(coefficients.size(), other.coefficients.size()), 0);

        for (size_t i = 0; i < coefficients.size(); ++i) {
            result.coefficients[i] += coefficients[i];
        }

        for (size_t i = 0; i < other.coefficients.size(); ++i) {
            result.coefficients[i] += other.coefficients[i];
        }

        return result;
    }

    Polynomial operator-(const Polynomial& other) const {
        Polynomial result;
        result.coefficients.resize(std::max(coefficients.size(), other.coefficients.size()), 0);

        for (size_t i = 0; i < coefficients.size(); ++i) {
            result.coefficients[i] += coefficients[i];
        }

        for (size_t i = 0; i < other.coefficients.size(); ++i) {
            result.coefficients[i] -= other.coefficients[i];
        }

        return result;
    }
};

std::ostream& operator<<(std::ostream& os, const Polynomial& poly) {
    int degree = static_cast<int>(poly.coefficients.size()) - 1;

    for (int i = degree; i >= 0; --i) {
        if (poly.coefficients[i] != 0) {
            if (i != degree) {
                os << ((poly.coefficients[i] > 0) ? " + " : " - ");
            }

            if (std::abs(poly.coefficients[i]) != 0 || i == 0) {
                os << std::abs(poly.coefficients[i]);
                if (i != 0) {
                    os << "x";
                    if (i != 1) {
                        os << "^" << i;
                    }
                }
            } else {
                if (i == 1) {
                    os << "x";
                }
            }
        }
    }

    return os;
}

Polynomial multiplyPolynomialsRegularMPI(const Polynomial& poly1, const Polynomial& poly2) {
    int world_size, world_rank;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    int m = poly1.coefficients.size();
    int n = poly2.coefficients.size();
    int result_size = m + n - 1;

    // Each process will compute a part of the result
    std::vector<int> local_result(result_size, 0);

    std::vector<int> coeffs2 = poly2.coefficients;

    // Broadcast the second polynomial to all processes
    MPI_Bcast(coeffs2.data(), n, MPI_INT, 0, MPI_COMM_WORLD);

    // Calculate the range of indices this process will handle
    int local_start = world_rank * (m / world_size);
    int local_end = (world_rank == world_size - 1) ? m : (world_rank + 1) * (m / world_size);

    for (int i = local_start; i < local_end; ++i) {
        for (int j = 0; j < n; ++j) {
            local_result[i + j] += poly1.coefficients[i] * poly2.coefficients[j];
        }
    }

    // Gather all partial results
    std::vector<int> global_result(result_size, 0);
    MPI_Reduce(local_result.data(), global_result.data(), result_size, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (world_rank == 0) {
        // The master process now has the complete result
        return Polynomial(global_result);
    } else {
        // Other processes return an empty polynomial
        return Polynomial();
    }
}

int main2(int argc, char** argv) {
    // Initialize MPI
    MPI_Init(&argc, &argv);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    // Define two polynomials (example coefficients)
    // Note: In a real-world scenario, you might want to read these from input
    std::vector<int> coeffs1 = {1, 3, 5}; // Represents 1 + 3x + 5x^2
    std::vector<int> coeffs2 = {2, 4};    // Represents 2 + 4x

    Polynomial poly1(coeffs1);
    Polynomial poly2(coeffs2);

    // Multiply the polynomials using MPI
    Polynomial result = multiplyPolynomialsRegularMPI(poly1, poly2);

    // Only process 0 will print the result
    if (world_rank == 0) {
        std::cout << "Result of polynomial multiplication: " << result << std::endl;
    }

    // Finalize MPI
    MPI_Finalize();

    return 0;
}