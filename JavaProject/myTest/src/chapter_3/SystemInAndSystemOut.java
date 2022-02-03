package chapter_3;

import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

/**
 * @author Luoters
 * @since 2022-01-26
 * Java核心技术卷1 3.7-标准输入和输出
 */
public class SystemInAndSystemOut {
    //标准输入
    public void isSystemIn(){
        System.out.println("----标准输入----");
        Scanner in =new Scanner(System.in);
        String name = in.nextLine();
        String profession = in.nextLine();
        System.out.println(name+" is a "+profession);
    }
    //标准输出
    public void isSystemOut(){
        System.out.println("----标准输出----");
        String name = "Luoters";
        System.out.printf("My name is %s\n",name);
    }
    //标准文件输入
    public void isFileIn(String file){
        System.out.println("----标准文件输入----");
        Path path = Paths.get(file);
        Scanner in = null;
        try {
            in = new Scanner(path);
        } catch (IOException e) {
            e.printStackTrace();
        }
        while (in.hasNext()){
            String line = in.nextLine();
            System.out.println(line);
        }

        in.close();
    }
    //标准文件输出
    public void isFileOut(String file){
        System.out.println("----标准文件输出----");
        FileWriter fw = null;
        PrintWriter out = null;
        try {
            fw = new FileWriter(file, true);
            out = new PrintWriter(fw);
        } catch (IOException e) {
            e.printStackTrace();
        }

        Scanner in = new Scanner(System.in);
        String line =in.nextLine();
        out.println(line);

        out.close();
    }

}
