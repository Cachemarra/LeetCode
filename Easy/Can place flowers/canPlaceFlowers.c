#include <stdbool.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    // Create a counter var
    int cont = 0;
    
    // Check if the size is 1. If so, check if we can plant. As there's only
    // 1 space, return the anwer
    if(flowerbedSize == 1 && flowerbed[0] == 0){
        cont++;
        return n <= cont;
    }
    // Evaluate if first value can hold a plant.
    if (flowerbed[0] == 0 && flowerbed[1] == 0){
        flowerbed[0] = 1;
        cont++;
    }
        
    // A for loop to iterate over 
    for(int i=1; i<flowerbedSize - 2; i++){
        
        // Check if the current value can hold a flower.
        // If past place, current state and future state are 0's can plant in current.
        if(flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0){
            cont++;
            flowerbed[i] = 1;
        }
    }
    
    // Check if the last place can hold a flower checking it and the before place.
    if(flowerbed[flowerbedSize - 1] == 0 && flowerbed[flowerbedSize - 2] == 0){
        cont++;
        flowerbed[flowerbedSize-1] = 1;
    }
    
    return n <= cont;
}