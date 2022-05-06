/**
 * @file main.cpp
 * @author Khazret (Violblink@gmail.com)
 * @brief 
 * @version 0.1
 * @date 2022-05-06
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using std::ofstream;
using std::ifstream;
using std::vector;
using std::string;

double NewthonMethod(double, double, double, double, double, double);

double f(double, double, double, double, double, double);
double df(double, double, double);

int main()
{
    //Создаем файл параметров и результатов
    ifstream Read("Config.txt");
    ofstream Write("Data.txt");

    string str1, str2;

    //Кол-во точек по х и t соответственно
    double N, J;

    //Предел по времени
    double T;

    //Погрешность
    double epsilon;

    Read >> str1 >> str2;

    Read >> N;  //Считываем N

    Read >> str1 >> str2;

    Read >> J;  //Считываем J

    Read >> str1 >> str2;

    Read >> T;  //Считываем T

    Read >> str1 >> str2;

    Read >> epsilon;  //Считываем T

    double Np = N + 1;
    double Jp = J + 1;

    //шаги по сетке
    double dx = 0.0 + 1/N;
    double dt = 0.0 + T/J;

    //Создаем сетку Lattis[t][x]
    vector<vector<double>> Lattis(Jp, vector<double>(Np));

    //Граничные условия по координате
    for(int i = 0; i <= N; i++)
    {
        Lattis[0][i] = 2 - (4/M_PI)*atan(-i * dx + 2);
    }

    //Граничные условия по времени
    for(int j = 0; j <= J; j++)
    {
        Lattis[j][0] = (2 - (4/M_PI)*atan(2)) * exp(-dt * j);
    }

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < J; j++)
        {
            Lattis[j + 1][i + 1] = NewthonMethod(dx, dt, Lattis[j + 1][i],
             Lattis[j][i], Lattis[j][i + 1], epsilon);
//            std::cout << "i = " << i << " j  = " << j << "\n" <<Lattis[i][j] << "\n";
        }
    }

    for(int i = 0; i <= N; i++)
    {
        for(int j = 0; j <= J; j++)
        {
            Write << Lattis[j][i] << "\n";
        }
    }
}

double NewthonMethod(double dx, double dt, double j, double nj, double n, double epsilon)
{
    vector<double> y(2);

    y[0] = nj;
    y[1] = nj - f(nj, dx, dt, j, nj, n)/df(nj, dx, dt);

    while (abs((y[1] - y[0])/(1 - (y[1] - y[0])/(y[0] - y[1]))) >= epsilon)
    {
        y[0] = y[1];
        y[1] = y[1] - f(y[1], dx, dt, j, nj, n)/df(y[1], dx, dt);
    }
    
    return y[1];
}

double f(double x, double dx, double dt, double j, double nj, double n)
{
    return (pow(x, 2) + 2 * (dx/dt) * x + 2 * (dx/dt) * (j - nj - n) - (pow(j, 2) + pow(nj, 2) - pow(n, 2)));
}

double df(double x, double dx, double dt)
{
    return (2 * x + 2 * (dx/dt));
}