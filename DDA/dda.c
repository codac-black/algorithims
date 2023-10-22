#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct
{
    /* data */
    int x;
    int x_round;
    int x_truncate;
    int y;
} Point;

Point* dda(int x1, int x2, int y1, int y2, int *length){
    *length = fmax(abs(x2 - x1), abs(y2 - y1));

    double x_inc = (double)(x2 - x1) / *length;
    double y_inc = (double)(y2 - y1) / *length;

    Point* points = (Point*)malloc(*length * sizeof(Point));

    double x = x1;
    double y = y1;

    for (int i =1; i < *length; ++i){
        int x_round = round(x);
        int x_truncate = (int)x;
        int y_value = round(y);


        points[i - 1].x = x_round;
        points[i - 1].x_round = x_round;
        points[i - 1].x_truncate = x_truncate;
        points[i - 1].y = y_value;

        x += x_inc;
        y += y_inc;

    }

    return points;
}


int main(){
    int x1 = 11, x2 = 4, y1 = 2, y2 = 25;

    int length;

    Point* result = dda(x1, x2, y1, y2, &length);

    // Display the table

    printf("x  | x_round | x_truncate | y \n");

    for (int i = 0; i < length - 1; ++i){
        printf("%2d | %7d | %10d | %d\n", result[i].x, result[i].x_round, result[i].x_truncate, result[i].y);
    }
    free(result);
    return 0;
}
