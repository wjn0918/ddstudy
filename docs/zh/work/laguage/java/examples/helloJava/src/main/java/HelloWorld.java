import java.io.IOException;
import java.util.Properties;

public class HelloWorld {

    public static void main(String[] args) throws IOException {
        Properties properties = new Properties();

        properties.load(HelloWorld.class.getClassLoader().getResourceAsStream("cs.txt"));

        System.out.println(properties.getProperty("123"));

    }
}
