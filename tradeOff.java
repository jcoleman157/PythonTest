import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class tradeOff {
    private String[] names = new String[10];
    private double[] gpa = new double[10];
    private String[] id = new String[10];
    private static File myFile = new File("tradeOff.txt");
    public static void main(String[] args){
        long line = getLineNum();
        for(int i = 0; i <= line; i++){
            if(i % 3 == 1){

            }
        }
    }
    public static long getLineNum(){
        long line = 0;
        Path path = Paths.get("tradeOff.txt");
        try {
            line = Files.lines(path).count();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        return line;
    }
}

