import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import FoodItem.FoodItem;
JSON.simple.jar

public class App {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        System.out.println("What would you like to do?\n\n1. New day entry\n2. View previous day\n3. View nutrition facts");


        // Receive user input and execute choice
        int choice = input.nextInt();
        switch(choice) {
            case 1:
            // new day
            case 2:
            // Prompt for day
            // View previous day
            case 3:
            // Prompt for food
            // Show food
            default:
            System.out.println("Invalid. \nPlease choose a valid option");
        }
    }
}
