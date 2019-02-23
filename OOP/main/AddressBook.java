package main;

import java.util.ArrayList;
import java.util.Collections;

public class AddressBook {

    // Data structure containing entries
    private ArrayList<AddressBookEntry> entries = new ArrayList<>();


    public void addEntry(AddressBookEntry newEntry) {
        entries.add(newEntry);
    }


    public void editEntry(int index, AddressBookEntry newEntry) {
        if (index < entries.size() && entries != null)
            entries.set(index, newEntry);
    }


    public void deleteEntry(int index) {
        if (index < entries.size() && entries != null)
            entries.remove(index);
    }


    public void deleteAllEntries() {
        if (!entries.isEmpty() && entries != null)
            entries.clear();
    }


    public void sortByLastName() {
        if (!entries.isEmpty() && entries != null)
            Collections.sort(entries, AddressBookEntry.NameComparator);
    }


    public void sortByZipCode() {
        if (!entries.isEmpty() && entries != null)
            Collections.sort(entries, AddressBookEntry.ZipcodeComparator);
    }


    public ArrayList<AddressBookEntry> getEntries() {
        if (!entries.isEmpty() && entries != null)
            return entries;
        return null;
    }

}
