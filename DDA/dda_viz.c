#include <stdio.h>
#include <math.h>

void dda(int x1, int x2, int y1, int y2) {
    int length = fmax(abs(x2 - x1), abs(y2 - y1));

    double x_inc = (double)(x2 - x1) / length;
    double y_inc = (double)(y2 - y1) / length;

    for (int i = 0; i < length; ++i) {
        int x_round = round(x1);
        int x_truncate = (int)x1;
        int y_value = round(y1);

        // Print the points on a simple graph paper
        for (int j = 0; j < 30; ++j) {
            for (int k = 0; k < 30; ++k) {
                if (x_truncate == j && y_value == k) {
                    printf("* ");
                } else if (x_round == j && y_value == k) {
                    printf("o ");
                } else if (j == 15 && k == 15) {
                    printf("+ ");
                } else if (j == 15) {
                    printf("| ");
                } else if (k == 15) {
                    printf("- ");
                } else {
                    printf("  ");
                }
            }
            printf("\n");
        }
        printf("\n");

        x1 += x_inc;
        y1 += y_inc;
    }
}

int main() {
    int x1 = 11, x2 = 4, y1 = 2, y2 = 25;

    dda(x1, x2, y1, y2);

    return 0;
}
