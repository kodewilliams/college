package test;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.*;

public class DiskFileControllerTest {
    FileReader reader;
    FileWriter writer;
    String expected = null;
    String filename = "random.txt";

    @BeforeEach
    void setup() throws IOException {
        writer = new FileWriter(filename);
        writer.write("File I/O works.");
        writer.close();

        reader = new FileReader(filename);
        BufferedReader buffer = new BufferedReader(reader);
        expected = buffer.readLine();
        reader.close();
    }

    @Test
    void writeToFile() throws IOException {

        Path path = Paths.get(".", filename);
        Files.deleteIfExists(path);

        writer = new FileWriter(filename);
        writer.write("It works.");
        assertNotNull(writer);
        assertTrue(Files.exists(path));
        Files.deleteIfExists(path);

    }

    @Test
    void readFromFile() throws IOException {
        BufferedReader tempReader = new BufferedReader(new FileReader(filename));
        String actual = tempReader.readLine();
        assertTrue(expected.equalsIgnoreCase(actual));
        tempReader.close();
    }

}
