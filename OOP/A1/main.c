#include <stdio.h>

int prime(int x){

    int counter=0;

    for (int i=1;i<=x;i++){
        if (x%i==0)
            counter++;
    }
    if (counter==2)
        return 1;

    return 0;

}

int relatively_prime(int a,int b){
    int min;

    if (a==1 || b==1)
        return 1;


    if (a<b)
        min=a;
    else
        min=b;

    for(int i=2;i<=min;i++){
        if (a%i==0 && b%i==0)
            return 0;
    }
    return 1;


}

int longest_subseq(int array[], int limit,int *max,int *ending_point){

    int i=0;

    if (limit!=0) {

        for (i = 0; i < limit; i++) {
            printf("%d", array[i]);
            printf("%s", " ");
        }

        printf("%s", "\n");


        //printf("%d", relatively_prime(array[0],array[1]));

        int counter = 1;

        for (i = 0; i < limit - 1; i++) {
            if (relatively_prime(array[i], array[i + 1])) {
                counter++;
//                        printf("%d",counter);
//                        printf("%s"," ");
            } else {
                if (counter > *max) {
                    *max = counter;
                    *ending_point = i;
                }
                counter = 1;
            }

        }
        if (counter > *max) {
            *max = counter;
            *ending_point = limit - 1;
        }

    }
    return 0;

}

void menu(){
    printf("%s","\n");
    printf("%s","1. Read an array \n");
    printf("%s","2. First N prime numbers \n");
    printf("%s","3. Longest subsequence in the array so that every 2 consecutive elements are relatively prime \n");
    printf("%s","4. Exit \n");
}

int main() {
    int number,i,limit=0;
    number=0;
    int array[100];

    while (number != 4){
        menu();

        scanf("%d", &number);

        if (number==1){
            printf("%s","How many elements? \n");
            scanf("%d", &limit);

            for (i=0;i<limit;i++) {
                scanf("%d", &array[i]);
            }

            for (i=0;i<limit;i++) {
                printf("%d", array[i]);
                printf("%s"," ");

            }

        }
        else
            if (number==2){
                int n,aux=0,x=2;

                scanf("%d",&n);

                while (aux<n){
                    if(prime(x)){
                        printf("%d",x);
                        printf("%s"," ");
                        aux++;
                        }

                    x++;
                }
            }
            else if (number==3) {

                int max=0;
                int ending_point=0;
                longest_subseq(array,limit,&max,&ending_point);


//                printf("%d",ending_point,max);
//                printf("%s","\n");

                    if (max == 1) {
                        printf("%s", "There is no such subsequence");
                    } else {
                        for (i = ending_point - max + 1; i <= ending_point; i++) {
                            printf("%d", array[i]);
                            printf("%s", " ");
                        }
                    }
                }



    };
}


