import java.util.ArrayList;
import org.json.JSONStringer;
import org.json.JSONException;

/***************
 * Class to create an instance of a single serving of food.
 ***************/
public class FoodItem {

    private String name;
    private ArrayList<Integer> macros = new ArrayList<Integer>();
    // Constructor
    public FoodItem(String foodName, int carbs, int fats, int protien){
        this.name = foodName;
        this.macros.add(carbs);
        this.macros.add(fats);
        this.macros.add(protien);
        return;
    }

    // Use the JSONStringer object to place our data into a string with JSON syntax
    public String toJSON(){
        JSONStringer foodString = new JSONStringer();
        String jsonText;
        try {
            jsonText = foodString
            .object()
            .key(this.name)
            .array()
            .value(this.macros.get(0))
            .value(this.macros.get(1))
            .value(this.macros.get(3))
            .endArray()
            .endObject()
            .toString();
        } catch (JSONException e) {
            String fail = "Failed to convert to string";
            return fail;
        }
        return jsonText;
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
