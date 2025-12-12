// online ordering

import java.util.Scanner;

public class Orderdaa {
   public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);

       System.out.println("Sir Jay's Store");
       System.out.println("New York @ Cubao QC");
       System.out.println("Vat Reg Tin# 1232840 ");
       System.out.println("===============");
       System.out.print("\nCustomer's Name: ");
       String CN = scanner.nextLine();

       System.out.print("1st Product: ");
       String P1 = scanner.nextLine();

       System.out.print("Price: ");
       double Pr1 = scanner.nextDouble();

       System.out.print("Quantity: ");
       int Quan = scanner.nextInt();

       double Tot = Pr1 * Quan;
       System.out.println("-----------------");

       scanner.nextLine(); // Consume newline character

       System.out.print("\n2nd Product: ");
       String P2 = scanner.nextLine();

       System.out.print("Price: ");
       double Pr2 = scanner.nextDouble();

       System.out.print("Quantity: ");
       int Quan2 = scanner.nextInt();

       double Tot2 = Pr2 * Quan2;
       System.out.println("*******************************");

       double sub = Tot + Tot2;

       System.out.print("SUBTOTAL: ");
       System.out.println(sub);
       System.out.print("Cash: ");
       double Money = scanner.nextDouble();
       double tira = Money - sub;
       System.out.print("Change: ");
       System.out.println(tira);
       System.out.println("\nCustomer's Name: " + CN);
       System.out.println("1st Product: " + P1);
       System.out.println("Price: " + Pr1);
       System.out.println("Quantity: " + Quan);
       System.out.println("Total: " + Tot);
       System.out.println("-----------------------");

       System.out.println("2nd Product: " + P2);
       System.out.println("Price: " + Pr2);
       System.out.println("Quantity: " + Quan2);
       System.out.println("Total: " + Tot2);
       System.out.println("*******************************");

       System.out.println("SUBTOTAL: " + sub);
       System.out.println("Cash: " + Money);
       System.out.println("Change: " + tira);
       System.out.println("Press any key to continue. . .");
       scanner.close();
   }

}
