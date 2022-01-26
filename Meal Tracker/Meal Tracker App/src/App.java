import java.util.Scanner;
import java.util.ArrayList;
// import java.io.File;
// import java.io.IOException;
// import FoodItem.FoodItem;
// import org.json.JSONArray;

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

/***************
 * Class to create an instance of a single serving of food.
 ***************/
public class FoodItem {

    private String name;
    ArrayList<Integer> macros = new ArrayList<Integer>();

    // Constructor
    public FoodItem(String foodName, int carbs, int fats, int protien){
        this.name = foodName;
        this.macros.add(carbs);
        this.macros.add(fats);
        this.macros.add(protien);
        return;
    }

    public void print() {
        // print info to the user.
        return;
    }

    public String getName(){
        return name;
    }

    public int getGramsCarbs(){
        return macros.get(0);
    }

    public int getGramsFats(){
        return macros.get(1);
    }

    public int getGramsProtien(){
        return macros.get(2);
    }

    public int getCaloriesCarbs(){
        return (getCaloriesCarbs() * 4);
    }

    public int getCaloriesFats(){
        return (getCaloriesFats() * 9);
    }

    public int getCaloriesProtien(){
        return (getCaloriesProtien() * 4);
    }

    public int getCaloriesTotal(){
        return (getCaloriesCarbs() + getCaloriesFats() + getCaloriesProtien());
    }
}
