class Student {
    int id;
    String name;

    void displayStudent() {
        System.out.println("student id: " + id);
        System.out.println("student name: " + name);
    }

}

class Book {
    int id;
    String name;

    void displayBook() {
        System.out.println("book id: " + id);
        System.out.println("book name: " + name);
    }
}

public class Library {
    public static void main(String[] args) {
        // creat student object
        Student s1 = new Student();
        s1.id = 73611;
        s1.name = "anis nawab";

        // creat book object
        Book s2 = new Book();
        s2.id = 89765;
        s2.name = "java";

        // issue book
        System.out.println("Book issued successfuly");

        // Display details
        s1.displayStudent();
        s2.displayBook();

    }
}
