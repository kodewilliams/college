package test;

import main.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

public class AddressBookManagerTest {

    AddressBookManager mgr = new AddressBookManager();
    AddressBook testBook = new AddressBook();

    @BeforeEach
    void setup() {
        testBook = new AddressBook();
        testBook.addEntry(new AddressBookEntry("John", "Doe",
                "123 Anon Street", "Washington", "DC",
                20001, "1234567890"));
        testBook.addEntry(new AddressBookEntry("Kode", "Williams",
                "1 Howard Place", "Washington", "DC",
                20002, "1234567890"));
        testBook.addEntry(new AddressBookEntry("Mya", "Harris",
                "2 Howard Place", "Washington", "DC",
                20001, "1234567890"));
        testBook.addEntry(new AddressBookEntry("Bernard", "Woolfolk",
                "3 Howard Place", "Washington", "DC",
                20004, "1234567890"));
        testBook.addEntry(new AddressBookEntry("Wayne", "Frederick",
                "4 Howard Place", "Washington", "DC",
                20003, "1234567890"));
    }

    @Test
    void createAddressBook() {
        mgr.newBook();
        assertNotNull(mgr.getCurrentBook());
        assertTrue(mgr.getCurrentBook() instanceof AddressBook);
    }

    @Test
    void saveAddressBook() throws IOException {
        Path path = Paths.get(".", "test-write.txt");
        Files.deleteIfExists(path);
        mgr.setCurrentBook(testBook);
        mgr.saveBook("test-write.txt");
        assertTrue(Files.exists(path));
        Files.deleteIfExists(path);
    }

    @Test
    void readAddressBook() throws IOException {
        Path path = Paths.get(".", "test-read.txt");
        assertTrue(Files.exists(path));
        mgr.openBook("test-read.txt");
        assertNotNull(mgr.getCurrentBook());

        ArrayList<AddressBookEntry> expected = testBook.getEntries();
        ArrayList<AddressBookEntry> actual =  mgr.getCurrentBook().getEntries();

        for (int i = 0; i < expected.size(); i++)
            assertTrue(expected.get(i).equals(actual.get(i)));
    }

    @Test
    void saveAddressBookAsName() throws IOException {
        String filename = "arbitrary.txt";
        Path path = Paths.get(".", filename);
        Files.deleteIfExists(path);
        mgr.setCurrentBook(testBook);
        mgr.saveBook(filename);
        assertTrue(Files.exists(path));
        Files.deleteIfExists(path);
    }

}
