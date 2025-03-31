package main;
import java.util.Scanner;
import java.time.LocalDate; 
import java.util.ArrayList;
class Student {
    private int admin_no;
    private String name;
    private double marks;
    Student(int admin_no, String name, double marks) {
        this.admin_no = admin_no;
        this.name = name;
        this.marks = marks;
    }
    void greeting() {
        System.out.println("Hello "+name);
    }
   
    void changeName(String name) {
        this.name = name;
    }
}

class CompStudent extends Student {
    private double os_marks;
    private double rno;
    CompStudent(int admin_no, String name, double marks,double rno, double os_marks) {
        super(admin_no, name, marks);
        this.os_marks = os_marks;
        this.rno = rno;
    } 
    @Override
    void greeting() {
        System.out.println("comp hellos");
    }
}

interface Vehicle {
    void accelerate();
    void brake();
}

class Car implements Vehicle {
    String name;
    public void accelerate() {
        System.out.println("Accelerating");
    }
    public void brake() {
        System.out.println("Braking");
    }
}


public class Main {
    enum consts {
        LOW,
        MEDIUM,
        HIGH
    }
    public static  void main(String[] args) {
        // Student A1 = new Student(1,"Sahil",0.0);
        // Student A2 = new Student(2,"ahil",10.0);
        // Student A3 = new Student(3,"hil",90.0);
        // Student A4 = new Student(4,"Sail",50.0);
        // //A2.greeting("bonjour");
        // // Scanner reader = new Scanner(System.in);
        // // String line = reader.nextLine();
        // // System.out.println(line);
        // // reader.close();
        // CompStudent Aa = new CompStudent(1,"Sahil",100.0, 101, 32);
        // Aa.greeting();
        Car myCar = new Car();
        myCar.accelerate();
        myCar.brake();
        consts level = consts.HIGH;
        System.out.println(level);
        LocalDate myObj = LocalDate.now();
        
        System.out.println(myObj);
        
    }
} 




// String a = "Hello";
// String b = "World";
// float n = (float)Math.sqrt(64);
// System.out.println(n);
// String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
// for(String i: cars) System.out.println(i);

// int[][] numbers = { {1, 2, 3, 4}, {5, 6, 7} };
// System.out.println(call());