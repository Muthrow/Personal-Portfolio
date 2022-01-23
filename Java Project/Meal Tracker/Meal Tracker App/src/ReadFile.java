import java.io.FileNotFoundException;
import java.io.FileReader;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class ReadFile {
    public void loadJSON() {
        JSONParser parser = new JSONParser();

        Object obj = parser.parse(new FileReader(file))
    }
}