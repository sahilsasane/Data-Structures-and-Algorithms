#include <iostream>
#include <string>
#include <list>
using namespace std;

class car {
public:
    string Name;
    int speed;

    car(string name, int speed) : Name(name), speed(speed) {}
    
    friend ostream& operator<<(ostream& COUT,const car&);
    friend car operator+(const car&, const car&);

    bool operator==(const car& c1) const{ 
        return this->Name == c1.Name;
    }
};

ostream& operator<<(ostream& COUT, const car& c){
    COUT<<"Name: "<< c.Name <<endl;
    COUT<<"Speed: "<< c.speed << endl;
    return COUT;
}

car operator+(car const& c1, car const& c2){
    return car("combined",c1.speed+c2.speed);
}

class fleet {
public:
    list<car> Fleet;

    void operator+=(car& c1){
        this->Fleet.push_back(c1);
    }
    void operator-=(car& c1) {
        this->Fleet.remove(c1);
    }
};

ostream& operator<<(ostream& COUT, fleet& f){
    COUT<<"Fleet: "<<endl;
    for(car c: f.Fleet)
        COUT << c;
    
    return COUT;
}


int main() {
    car c1 = car("Fiat",50);
    car c2 = car("bmw",200);
    // cout<<c1;
    car c3 = c1 + c2;
    // cout<<c3;
    fleet carFleet;
    carFleet += c1;
    carFleet += c2;
    carFleet += c3;
    cout << carFleet;
    carFleet -= c1;
    cout << carFleet;

    return 0;
}