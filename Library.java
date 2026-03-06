// Simple Library System Using Java OOP
// Student Class
class Student {
    int id;
    String name;

    void displayStudent() {
        System.out.println("Student ID: " + id);
        System.out.println("Student Name: " + name);
    }
}

// Book Class
class Book {
    int bookId;
    String bookName;

    void displayBook() {
        System.out.println("Book ID: " + bookId);
        System.out.println("Book Name: " + bookName);
    }
}

// Main Class
public class Library {
    public static void main(String[] args) {

        // Create Student Object
        Student s1 = new Student();
        s1.id = 101;
        s1.name = "Anis";

        // Create Book Object
        Book b1 = new Book();
        b1.bookId = 1;
        b1.bookName = "Java";

        // Issue Book
        System.out.println("Book Issued Successfully!\n");

        // Display Details
        s1.displayStudent();
        b1.displayBook();
    }
}
