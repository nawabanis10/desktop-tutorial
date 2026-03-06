public class BasicPrograms {

    public static void main(String[] args) {

        // 1. Find length of array
        int arr[] = {10, 20, 30, 40, 50};
        System.out.println("Length of array: " + arr.length);


        // 2. Prime number check
        int num = 7;
        boolean prime = true;

        for(int i = 2; i < num; i++) {
            if(num % i == 0) {
                prime = false;
                break;
            }
        }

        if(prime)
            System.out.println(num + " is a Prime Number");
        else
            System.out.println(num + " is Not a Prime Number");


        // 3. Factorial
        int n = 5;
        int fact = 1;

        for(int i = 1; i <= n; i++) {
            fact = fact * i;
        }

        System.out.println("Factorial of " + n + " is: " + fact);


        // 4. Star Pattern
        System.out.println("Star Pattern:");

        for(int i = 1; i <= 5; i++) {
            for(int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}

