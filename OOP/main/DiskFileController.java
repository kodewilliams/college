package main;

import java.io.FileReader;
import java.io.FileWriter;

public class DiskFileController {

    public FileReader readFile(String filename) {
        FileReader f = null;
        try {
            f = new FileReader(filename);
        } catch (Exception e) {
            System.out.print("Error reading from file.");
        } finally {
            return f;
        }
    }

    public FileWriter writeFile(String filename) {
        FileWriter f = null;
        try {
            f = new FileWriter(filename);
        } catch (Exception e) {
            System.out.print("Error writing to file.");
        } finally {
            return f;
        }
    }
}
