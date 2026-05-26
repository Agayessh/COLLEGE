// telecom part 2, keypad edition

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class PhonebookProgram 
{
  static ArrayList<String> names = new ArrayList<>();
  static ArrayList<String> nums = new ArrayList<>();
  static Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) 
  {
    System.out.println("==== Sir Jay Telecom ====");
    System.out.print("Please Enter your SIM card PIN Number: ");
    int pin = scanner.nextInt();

    if (pin == 0000) 
    {
      Menu();
      Options();
    }
  }

  static void Menu() 
  {
    System.out.println("=====Welcome to Sir Jay Telecom=====");
    System.out.println("****A Telecom that Always On-Line****");
    System.out.println();

    System.out.println("\n=====================================");
    System.out.println("|10:00AM              >>|");
    System.out.println("|                  |");
    System.out.println("|                  |");
    System.out.println("|                  |");
    System.out.println("|   A Telecom that         |");
    System.out.println("|   Always On-Line         |");
    System.out.println("|   Call and Text Na!       |");
    System.out.println("|                  |");
    System.out.println("|                  |");
    System.out.println("|                  |");
    System.out.println(" ====================================");

    System.out.println("|                  |");
    System.out.println("|  [ 1 ]   [ 2 ]   [ 3 ]    |");
    System.out.println("|  [ 4 ]   [ 5 ]   [ 6 ]    |");
    System.out.println("   [ 7 ]   [ 8 ]   [ 9 ]    |");
    System.out.println("|  [ * ]   [ 0 ]   [ # ]    |");
    System.out.println("|                  |");
    System.out.println(" ====================================");
  }

  static void Options() 
  {
    System.out.println("Sir Jay Telecom");
    System.out.println("1 - Add phonebook entry");
    System.out.println("2 - Delete phonebook entry");
    System.out.println("3 - View all entries");
    System.out.println(" a - alphabetical order");
    System.out.println(" b - increasing order of telephone numbers");

    System.out.println("4 - Search entries");
    System.out.println(" a - by name");
    System.out.println(" b - by telephone number");

    System.out.println("5 - Quit");
    int option = scanner.nextInt();
    scanner.nextLine(); // Consume newline character

    switch (option) 
    {
      case 1:
        addPhonebookEntry();
        break;

      case 2:
        deletePhonebookEntry();
        break;

      case 3:
        Entries();
        break;

      case 4:
        search();
        break;

      case 5:
        System.out.println("Quit");
        break;

      default:
        System.out.println("Invalid option. Please try again.");

        Options();
        break;
    }
  }

  static void addPhonebookEntry() 
  {
    System.out.print("Enter name: ");
    String name = scanner.nextLine();
    System.out.print("Enter telephone number: ");

    String number = scanner.nextLine();

    names.add(name);
    nums.add(number);
    Options();
  }

  static void Entries() 
  {
    System.out.println("a - alphabetical order");
    System.out.println("b - by telephone number");
    char option = scanner.next().charAt(0);

    scanner.nextLine();

    switch (option) 
    {
      case 'a':
        Collections.sort(names);
        displayEntries();
        break;

      case 'b':
        Collections.sort(nums, Comparator.comparing(String::toString));
        displayEntries();
        break;

      default:
        System.out.println("Empty");

        Options();
        break;
    }
  }

  static void displayEntries() 
  {
    System.out.println();
    for (int i = 0; i < names.size(); i++) 
    {
      System.out.println("\nName: " + names.get(i));
      System.out.print("Number: " + nums.get(i));
    }

    System.out.println();
    System.out.println();
    Options();
  }

  static void deletePhonebookEntry() 
  {
    names.remove(names);
    nums.remove(nums);
    System.out.println("Deleted phonebook entries");
    Options();
  }
  
  static void search()
  {
    System.out.println("a - by name");
    System.out.println("b - by telephone number");
    char option = scanner.next().charAt(0);
    scanner.nextLine();
    switch (option) 

    {
      case 'a':
        byname();
        break;

      case 'b':
        byphone();
        break;

      default:
        System.out.println("Invalid option. Please try again");

        search();
        break;
    }
  }

  static void byname()
  {
    String bname = scanner.nextLine();
    boolean found = false;

    for (int i = 0; i < names.size(); i++) 
    {
    if (names.get(i).equalsIgnoreCase(query)) 
    {
      System.out.println("\nName: " + names.get(i));
      System.out.println("Number: " + nums.get(i));
      found = true;
    }
    }

    if (!found) 
    {
    System.out.println("No matching entries found!");
    }

    Options(); // Return to options menu after searching
  }

  static void byphone()
  {
    String bphone = scanner.nextLine();
    boolean found = false;

    for (int i = 0; i < names.size(); i++) 
    {
    if (nums.get(i).equalsIgnoreCase(query)) 
    {
      System.out.println("\nName: " + nums.get(i));
      System.out.println("Number: " + nums.get(i));
      found = true;
    }
    }

    if (!found) 
    {
    System.out.println("No matching entries found!");
    }

    Options(); // Return to options menu after searching
  }
}
