#include <iostream>
using namespace std;

// Members in class are Private by default

class AbstractEmployee {
    virtual void Promotion() = 0;
};


class Employee:AbstractEmployee {
private:
    string Company;
    int age;

protected:
    string Name;

public:
    void Introduction() {
        cout<<"Name "<< Name<<endl;
        cout<<"Company "<<Company<<endl;
        cout<<"Age "<<age<<endl;
    }
    Employee(string Name, string company, int age) {
        this->Name = Name;
        this->Company = company;
        this->age = age;
    }
    string getName(){
        return this->Name;
    }
    void Promotion() {
        if(this->age > 30) cout<< this->Name <<" got promoted"<<endl;
        else cout<< this->Name <<" not promoted"<<endl;
    }
    // virtual means if there is a reference in child class invoke that or some
    virtual void work() {
        cout<< this->Name << " is checking mail and performing tasks" <<endl;
    }

    // pure virtual function / abstract class
    // virtual void work() = 0;

};

class Developer:public Employee {
public:
    string favouriteLang;
    Developer(string Name, string company, int age, string favLang) 
        :Employee(Name,company,age) {
            this->favouriteLang = favLang;
    }
    void fixBugs() {
        cout<< this->Name <<" likes "<<this->favouriteLang<<endl;
    }
    void work() {
        cout<< this->Name << " is writing "<<this->favouriteLang<<" code." <<endl;
    }
};

class Teacher:public Employee {
public:
    string Subject;
    Teacher(string Name, string company, int age, string subject) 
        :Employee(Name,company,age){
            this->Subject = subject;
    }
    void prepareLesson() {
        cout<< this->Name<<" is preparing "<< this->Subject << " lesson"<<endl;
    }
    void work() {
        cout<< this->Name << " is teaching a "<<this->Subject<< " lesson." <<endl;
    }
};


int main() {

    Developer d = Developer("sahil","None",45,"Python");
    Teacher t = Teacher("ahil","None",40,"Deep Learning");
    
    // Employee *e1 = &d;
    // Employee *e2 = &t;

    Employee *e1 = new Developer("sahil","None",45,"Python");
    Employee *e2 = new Teacher("ahil","None",40,"Deep Learning");

    e1->work();
    e2->work();

    return 0;
}