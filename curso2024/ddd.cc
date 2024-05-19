// Problema: https://judge.beecrowd.com/pt/problems/view/1050

#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(){
    map<int, string> DDD;    
    DDD[61] = "Brasilia";
    DDD[71] = "Salvador";
    DDD[11] = "Sao Paulo";
    DDD[21] = "Rio de Janeiro";
    DDD[32] = "Juiz de Fora";
    DDD[19] = "Campinas";
    DDD[27] = "Vitoria";
    DDD[31] = "Belo Horizonte";

    int ddd;
    cin >> ddd;
    auto res = DDD.find(ddd);
    if (res != DDD.end()){
        cout << DDD[ddd] << "\n";
    } else {
        cout << "DDD nao cadastrado" << "\n";
    }
}