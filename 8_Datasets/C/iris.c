#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROWS 150
#define MAX_COLS 5

int main() {
    FILE *file;
    char line[100];
    float data[MAX_ROWS][MAX_COLS];
    int row = 0;

    file = fopen("bezdekIris.data", "r");
    if (file == NULL) {
        printf("Error: No se puede abrir el archivo.\n");
        return 1;
    }

    char label[20]; // Buffer to store the string
    while (fgets(line, sizeof(line), file) && row < MAX_ROWS) {
        sscanf(line, "%f,%f,%f,%f,%s", 
               &data[row][0], &data[row][1], &data[row][2], &data[row][3], label);
        row++;
    }

    fclose(file);

    // Verificación: imprime las primeras 5 filas
    for (int i = 0; i < 5; i++) {
        printf("%f %f %f %f\n", data[i][0], data[i][1], data[i][2], data[i][3]);
    }

    return 0;
}
