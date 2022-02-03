package chapter_3;


/**
 * @author Luoters
 * @since 2022-01-22
 *
 */
public class Main {
    public static void main(String[] args) {

        String helloW = "hello world!";
        HelloWorld helloWorld = new HelloWorld();
        helloWorld.isHelloWorld(helloW);

        String file = "C:/Users/Administrator/code/Luoters/JavaProject/myTest/fileIn/鲁迅网红文案.txt";
        SystemInAndSystemOut systemInAndSystemOut = new SystemInAndSystemOut();
//        systemInAndSystemOut.isSystemIn();
        systemInAndSystemOut.isSystemOut();
        systemInAndSystemOut.isFileIn(file);
        systemInAndSystemOut.isFileOut(file);

    }

}
