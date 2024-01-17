#include <iostream>
#include <vector>

template <typename T>
void minmax (std::vector<T>& list, T& min, T& max){

    min=list[0];
    max=list[0];

    for (int i = 0; i < list.size(); i++){
        if (min > list[i]){
            min=list[i];
        }
        if (max < list[i]){
            max=list[i];
        }
    }
}

int main(){

    std::vector<float> list = {1.03,5,5.02,0.95,4};
    float min = 0, max = 0;

    minmax(list, min, max);



    std::cout << min << " " << max;
}

