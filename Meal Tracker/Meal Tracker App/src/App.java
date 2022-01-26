import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import org.json.JSONArray;
// import FoodItem.FoodItem;

public class App {
    public static void main(String[] args) throws Exception{

        Boolean end = false;
        Scanner input = new Scanner(System.in);
        while(!end){
            System.out.println("What would you like to do?\n\n1. New day entry\n2. View previous day\n3. View nutrition facts\n4. Exit");
            // Receive user input and execute choice
            int choice = input.nextInt();
            switch(choice) {
                case 1:
                    // new day
                    System.out.println("New Day");
                    break;
                case 2:
                    // Prompt for day
                    // View previous day
                    System.out.println("Previous Day");
                    break;
                case 3:
                    // Prompt for food
                    // Show food
                    System.out.println("Facts");
                    break;
                case 4:
                    // Exit loop
                    System.out.println("Exiting Program...");
                    end = true;
                    break;
                default:
                    System.out.println("Invalid. \nPlease choose a valid option");
                    break;
        }
    }
        input.close();
    }
}