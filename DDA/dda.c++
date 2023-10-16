#include <iostream>
#include <vector>
#include <iomanip>

struct Point {
    int x;
    int x_round;
    int x_truncate;
    int y;
};

std::vector<Point> dda(int x1, int x2, int y1, int y2) {
    int length = std::max(std::abs(x2 - x1), std::abs(y2 - y1));

    double x_inc = static_cast<double>(x2 - x1) / length;
    double y_inc = static_cast<double>(y2 - y1) / length;
    
    std::vector<Point> points;

    double x = x1;
    double y = y1;

    for (int i = 1; i < length; ++i) {
        int x_round = static_cast<int>(x + 0.5);
        int x_truncate = static_cast<int>(x);
        int y_value = static_cast<int>(y);
        
        points.push_back({ x_round, x_truncate, y_value, y1 });
        
        x += x_inc;
        y += y_inc;
    }

    return points;
}

int main() {
    int x1 = 11, x2 = 4, y1 = 2, y2 = 25;

    std::vector<Point> result = dda(x1, x2, y1, y2);

    // Display the table
    std::cout << "x | x_round | x_truncate | y" << std::endl;
    for (const Point& point : result) {
        std::cout << std::setw(2) << point.x << " | "
                  << std::setw(7) << point.x_round << " | "
                  << std::setw(10) << point.x_truncate << " | "
                  << point.y << std::endl;
    }

    return 0;
}
