#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    string input = "Hello world from C++";
    istringstream iss(input);
    vector<string> tokens;
    string token;

    while (getline(iss, token, ' ')) {
        tokens.push_back(token);
    }

    for (const auto& t : tokens) {
        cout << t << endl;
    }

    return 0;
}
