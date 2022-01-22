package FoodItem;
import java.util.ArrayList;

/***************
 * Class to create an instance of a single serving of food.
 * Constructor takes parameters for name and each macro (carbs, fats, and protiens)
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
