package test;

import main.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

public class AddressBookTest {
    AddressBook testBook = new AddressBook();
    AddressBookEntry testEntry;

    @BeforeEach
    void setup() {
        testEntry = new AddressBookEntry("John", "Doe",
                "123 Anon Street", "Washington", "DC",
                20001, "1234567890");
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
    void getEntries() {
        ArrayList<AddressBookEntry> expected = new ArrayList<>();
        expected.add(new AddressBookEntry("Kode", "Williams",
                "1 Howard Place", "Washington", "DC",
                20002, "1234567890"));
        expected.add(new AddressBookEntry("Mya", "Harris",
                "2 Howard Place", "Washington", "DC",
                20001, "1234567890"));
        expected.add(new AddressBookEntry("Bernard", "Woolfolk",
                "3 Howard Place", "Washington", "DC",
                20004, "1234567890"));
        expected.add(new AddressBookEntry("Wayne", "Frederick",
                "4 Howard Place", "Washington", "DC",
                20003, "1234567890"));

        for (int i = 0; i < expected.size(); i++)
            assertTrue(expected.get(i).equals(testBook.getEntries().get(i)));
    }

    @Test
    void addEntry() {
        testBook.addEntry(testEntry);
        ArrayList<AddressBookEntry> results = testBook.getEntries();
        AddressBookEntry expected = results.get(results.size()-1);
        assertTrue(expected.equals(testEntry));
    }

    @Test
    void editEntry() {
        testBook.editEntry(0, testEntry);
        ArrayList<AddressBookEntry> results = testBook.getEntries();
        AddressBookEntry expected = results.get(0);
        assertTrue(expected.equals(testEntry));
    }

    @Test
    void deleteEntry() {
        testBook.deleteEntry(0);

        ArrayList<AddressBookEntry> results = testBook.getEntries();
        AddressBookEntry actual = results.get(0);
        AddressBookEntry expected = new AddressBookEntry("Kode", "Williams",
                "1 Howard Place", "Washington", "DC",
                20002, "1234567890");

        assertTrue(results.size() < 4);
        assertFalse(expected.equals(actual));
    }

    @Test
    void deleteAllEntries() {
        testBook.deleteAllEntries();

        assertNull(testBook.getEntries());
    }

    @Test
    void sortByLastName() {
        ArrayList<AddressBookEntry> expected = new ArrayList<>();
        expected.add(new AddressBookEntry("Wayne", "Frederick",
                "4 Howard Place", "Washington", "DC",
                20003, "1234567890"));
        expected.add(new AddressBookEntry("Mya", "Harris",
                "2 Howard Place", "Washington", "DC",
                20001, "1234567890"));
        expected.add(new AddressBookEntry("Kode", "Williams",
                "1 Howard Place", "Washington", "DC",
                20002, "1234567890"));
        expected.add(new AddressBookEntry("Bernard", "Woolfolk",
                "3 Howard Place", "Washington", "DC",
                20004, "1234567890"));

        testBook.sortByLastName();
        ArrayList<AddressBookEntry> actual = testBook.getEntries();

        for (int i = 0; i < expected.size(); i++)
            assertTrue(expected.get(i).equals(actual.get(i)));
    }

    @Test
    void sortByZipCode() {
        ArrayList<AddressBookEntry> expected = new ArrayList<>();
        expected.add(new AddressBookEntry("Mya", "Harris",
                "2 Howard Place", "Washington", "DC",
                20001, "1234567890"));
        expected.add(new AddressBookEntry("Kode", "Williams",
                "1 Howard Place", "Washington", "DC",
                20002, "1234567890"));
        expected.add(new AddressBookEntry("Wayne", "Frederick",
                "4 Howard Place", "Washington", "DC",
                20003, "1234567890"));
        expected.add(new AddressBookEntry("Bernard", "Woolfolk",
                "3 Howard Place", "Washington", "DC",
                20004, "1234567890"));

        testBook.sortByZipCode();
        ArrayList<AddressBookEntry> actual = testBook.getEntries();

        for (int i = 0; i < expected.size(); i++)
            assertTrue(expected.get(i).equals(actual.get(i)));
    }
}
