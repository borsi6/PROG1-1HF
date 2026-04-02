#include <iostream>
#include <windows.h>

using namespace std;

int main() {
    int x = 10, y = 5;
    int dx = 1, dy = 1;
    int maxX = 80, maxY = 10;
    
    while (true) {
        system("cls"); //képernyő törlése

        for (int i = 0; i < y; i++) cout << "\n";
        for (int i = 0; i < x; i++) cout << " ";
        cout << "O";

        cout << flush;
        Sleep(100);

        x += dx;
        y += dy;

        if (x <= 0 || x >= maxX - 1) dx *= -1;
        if (y <= 0 || y >= maxY - 1) dy *= -1;

    }
    
    return 0;
}
