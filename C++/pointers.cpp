#include <bits/stdc++.h>

using namespace std;

void greet() {
    cout << "Hello, World!" << endl;
}

int main() {
    int a = 10;
    int *p = &a;
    cout << a << endl;
    cout << p <<endl;
    cout << *p <<endl;

    int *nptr = nullptr;
    // Pointers and Arrays
    int arr[] = {10,20,30};
    p = arr;
    cout<<*p<<endl;
    cout<<*(p+1)<<endl;
    
    // Dynamic Memory Allocation
    int* b = new int[5]; // Allocate array of 5 ints
    for (int i = 0; i < 5; i++) b[i] = i;
    delete[] b; 

    void(*funcptr)() = greet;
    funcptr();

    // Pointers to Pointers
    int x = 10;
    int* pt = &x;      // Pointer to `x`
    int** pp = &pt;    // Pointer to pointer `p`

    cout << **pp <<endl;     // Access value of `x` through `pp`

    string str = "Hello";
    void *sptr = &str;

    cout << *(static_cast<string*>(sptr)) << endl;

    // Smart Pointers
    unique_ptr<int> up = make_unique<int>(10);
    unique_ptr<int> up2 = make_unique<int>(12);

    // Shared pointers
    shared_ptr<int> p1 = make_shared<int>(20);
    shared_ptr<int> p2 = p1; // Shared ownership
    cout<< *p2 <<endl;
    return 0;
}