package main;

import java.util.Comparator;

public class AddressBookEntry {

    // Person Attributes
    public String firstName;
    public String lastName;
    public String streetAddress;
    public String city;
    public String state;
    public int zipcode;
    public String telephone;

    // Default constructor
    public AddressBookEntry() {
        // Set attributes using default data
        this.firstName = "First";
        this.lastName = "Last";
        this.streetAddress = "123 Large Scale Avenue";
        this.city = "Washington";
        this.state = "DC";
        this.zipcode = 20059;
        this.telephone = "123-456-7890";
    }

    // Constructor with attributes
    public AddressBookEntry(String firstName, String lastName, String streetAddress,
                            String city, String state, int zipcode, String telephone) {
        // Set attributes using data passed in parameters
        this.firstName = firstName;
        this.lastName = lastName;
        this.streetAddress = streetAddress;
        this.city = city;
        this.state = state;
        this.zipcode = zipcode;
        this.telephone = telephone;
    }

    public AddressBookEntry(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.streetAddress = "n/a";
        this.city = "n/a";
        this.state = "n/a";
        this.zipcode = 00000;
        this.telephone = "n/a";
    }

    public boolean equals(AddressBookEntry e) {

        if( ! (e instanceof AddressBookEntry ) )
            return false;

        return e.firstName.equalsIgnoreCase(this.firstName) &&
                e.lastName.equalsIgnoreCase(this.lastName) &&
                e.streetAddress.equalsIgnoreCase(this.streetAddress) &&
                e.city.equalsIgnoreCase(this.city) &&
                e.state.equalsIgnoreCase(this.state) &&
                e.zipcode == this.zipcode &&
                e.telephone.equalsIgnoreCase(this.telephone);
    }


    // Comparator for sorting entries by name
    public static Comparator<AddressBookEntry> NameComparator = new Comparator<AddressBookEntry>() {

        @Override
        public int compare(AddressBookEntry entry1, AddressBookEntry entry2) {
            String lastName1 = entry1.lastName;
            String lastName2 = entry2.lastName;

            if (lastName1.equals(lastName2)) {
                String firstName1 = entry1.firstName;
                String firstName2 = entry2.firstName;
                return firstName1.compareTo(firstName2);
            }

            return lastName1.compareTo(lastName2);
        }
    };

    // Comparator for sorting entries by ZIP code
    public static Comparator<AddressBookEntry> ZipcodeComparator = new Comparator<AddressBookEntry>() {
        @Override
        public int compare(AddressBookEntry entry1, AddressBookEntry entry2) {
            int zipcode1 = entry1.zipcode;
            int zipcode2 = entry2.zipcode;

            if (zipcode1 == zipcode2) {
                String lastName1 = entry1.lastName;
                String lastName2 = entry2.lastName;
                return lastName1.compareTo(lastName2);
            }

            return zipcode1 - zipcode2;
        }
    };

}
