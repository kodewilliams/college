package main;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class AddressBookManager extends DiskFileController {

    protected FileReader in = null;
    protected FileWriter out = null;
    protected BufferedReader buffer = null;
    private AddressBook currentBook = null;
    private AddressBookEntry currentEntry = null;

    //TODO: create new address book
    public void newBook() {
        currentBook = new AddressBook();
    }

    //TODO: open existing address book
    public void openBook(String name) throws IOException {

        in = this.readFile(name);
        buffer = new BufferedReader(in);
        this.newBook();

        String line = "";
        int i = 1;
        currentEntry = new AddressBookEntry();

        while (line != null && i < 8) {
            line = buffer.readLine();
            if (line != null) {
                if (i == 1) currentEntry.firstName = line;
                if (i == 2) currentEntry.lastName = line;
                if (i == 3) currentEntry.streetAddress = line;
                if (i == 4) currentEntry.city = line;
                if (i == 5) currentEntry.state = line;
                if (i == 6)  currentEntry.zipcode = Integer.valueOf(line);
                if (i == 7) {
                    currentEntry.telephone = line;
                    currentBook.addEntry(currentEntry);
                    //System.out.println("Entry added.");
                    i = 0;
                    currentEntry = new AddressBookEntry();
                }
            }
            i++;
        }

        in.close();
    }

    //TODO: save address book
    public void saveBook(String name) throws IOException {

        out = this.writeFile(name);

        // TODO: Write address book fields to file
        if (currentBook.getEntries().size() > 0 && currentBook != null) {
            for (AddressBookEntry e : currentBook.getEntries()) {
                out.write(e.firstName + "\n");
                out.write(e.lastName + "\n");
                out.write(e.streetAddress + "\n");
                out.write(e.city + "\n");
                out.write(e.state + "\n");
                out.write(e.zipcode + "\n");
                out.write(e.telephone + "\n");
            }
        } else {
            return;
        }

        out.close();
    }

    public AddressBook getCurrentBook() {
        if (currentBook != null) return currentBook;
        else return null;
    }

    public void setCurrentBook(AddressBook book) {
        if (book instanceof AddressBook && book != null) {
            currentBook = book;
        }
    }

}
