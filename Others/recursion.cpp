//
// Created by Cachemarra on 2/16/2022.
//

// Librerias
#include <iostream>

// Pre definición de la función de recursión
int recursion(int, int, int, int);

// Función principal para probar el método
int main(){
    int n = 5;
    int a = 46;
    int b = 68;
    int c = 100;

    std::cout << "Respuesta de la recursion\n";
    std::cout << recursion(n, a, b, c);

    return 0;
}

// Método de recursión.
/* n -> int. Número de la secuencia a regresar
 * a, b, c -> int, números de la secuencia.
 * result -> output. Salida esperada.
 */
int recursion(int n, int a, int b, int c){
    // Inicializamos la respuesta
    int result = 0;
    // Utilizamos un switch case para todos los casos
    switch(n){
        case 1:
            return a;
            break;
        case 2:
            return b;
            break;
        case 3:
            return c;
            break;
        default:
            // Iteramos para obtener las suma de los S(n-1) + S(n-2) + S(n-3)
            for(int i=1; i < 4; i++){
                result += recursion(n-i, a, b, c);
            }
            return result;

    } // end switch
    return -1;
} // end recursion
