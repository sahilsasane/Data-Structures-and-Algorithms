//package Threads;

import java.util.Timer;

public class Main extends Thread {
    public static int amount = 0;

    public static void main(String[] args) {
        // if implements Runnable
        // Main obj = new Main();
        // Thread thread = new Thread(obj);
        // thread.start();
        // System.out.println("outside of thread");
        Main thread = new Main();
        thread.start();
        while (thread.isAlive()) {
            System.out.println("Waiting...");
        }
        // Update amount and print its value
        System.out.println("Main: " + amount);
        amount++;
        System.out.println("Main: " + amount);
    }

    public void run() {
        amount++;
    }
}
