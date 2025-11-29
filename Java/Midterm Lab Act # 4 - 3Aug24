// Grade calculator

import java.util.Scanner;

public class Javachips 
{
  public static void main(String[] args) 
  {
    Scanner scanner = new Scanner(System.in);

    System.out.print("\nStudent ID Number: ");
    String id = scanner.nextLine();

    System.out.print("Name: ");
String name = scanner.nextLine();

    System.out.print("Course/Subject: ");
    String course = scanner.nextLine();

    System.out.println("-----PRELIM-----"); 

    System.out.println("QUIZZES");

    System.out.print("Quiz #1: ");
    float q1 = scanner.nextFloat();

    System.out.print("Quiz #2: "); 
    float q2 = scanner.nextFloat();

    System.out.println("SEATWORKS"); 
    System.out.print("SeatWork #1: ");
    float sw1 = scanner.nextFloat();

    System.out.print("SeatWork #2: ");
    float sw2 = scanner.nextFloat();

    System.out.println("LAB ACTIVITIES: ");

    System.out.print("Lab 1: ");
    float l1 = scanner.nextFloat();

    System.out.print("Lab 2: ");
    float l2 = scanner.nextFloat();

    System.out.print("Lab 3: ");  
    float l3 = scanner.nextFloat();

    System.out.println("CLASS");

    float fc = (q1 + q2 + sw1 + sw2 + l1 + l2+ l3) / (7);
    System.out.println("Standing: " + fc);

    System.out.print("Prelim Exam: ");
    float e1 = scanner.nextFloat();

  double PE = (fc * 0.60) + (e1 * 0.40);
    System.out.print("Prelim Grade:" + PE);

    System.out.println("\n-----MIDTERM-----");
    System.out.println("QUIZZES");

    System.out.print("Quiz #1: ");
    float mq1 = scanner.nextFloat();

    System.out.print("Quiz #2: "); 
    float mq2 = scanner.nextFloat();

    System.out.println("SEATWORKS"); 
    System.out.print("SeatWork #1: ");
    float msw1 = scanner.nextFloat();

    System.out.print("SeatWork #2: ");
    float msw2 = scanner.nextFloat();

    System.out.println("LAB ACTIVITIES: ");
    System.out.print("Lab 1: ");
    float ml1 = scanner.nextFloat();

    System.out.print("Lab 2: ");
    float ml2 = scanner.nextFloat();

    System.out.print("Lab 3: ");  
    float ml3 = scanner.nextFloat();

    System.out.println("CLASS");
    float mc = (mq1 + mq2 + msw1 + msw2 + ml1 + ml2+ ml3) / (7);
    System.out.print("Standing: " + mc);

    System.out.println("Midterm Exam: ");
    float e2 = scanner.nextFloat();
    double MG = (mc * 0.60) + (e2 * 0.40);

    System.out.println("Midterm Grade: " + MG);
    System.out.println("-----FINAL-----");
    System.out.println("QUIZZES");

    System.out.print("Quiz #1: ");
    float fq1 = scanner.nextFloat();

    System.out.print("Quiz #2: "); 
    float fq2 = scanner.nextFloat();

    System.out.println("SEATWORKS"); 
    System.out.print("SeatWork #1: ");
    float fsw1 = scanner.nextFloat();

    System.out.print("SeatWork #2: ");
    float fsw2 = scanner.nextFloat();

    System.out.println("LAB ACTIVITIES: ");
    System.out.print("Lab 1: ");
    float fl1 = scanner.nextFloat();

    System.out.print("Lab 2: ");
    float fl2 = scanner.nextFloat();

    System.out.print("Lab 3: ");  
    float fl3 = scanner.nextFloat();

    System.out.println("CLASS");

    float fs = (fq1 + fq2 + fsw1 + fsw2 + fl1 + fl2+ fl3) / (7);
    System.out.print("Standing: " + fs);

    System.out.println("Final Exam: ");
    float e3 = scanner.nextFloat();

    double TFG = (fs * 0.60) + (e3 * 0.40);

    System.out.print("Tentative Final Grade: " + TFG );
    float tfgrade = scanner.nextFloat();

    double PG = (tfgrade * 0.30) + (MG * 0.30) + (TFG * 0.40);

    System.out.print("Final Grade: " + PG);

    int equi;
    equi = scanner.nextInt();

    if (equi >= 98)
    {
    System.out.print("1.00");
    }

    else if (equi >= 95)
    {
    System.out.print("1.25");
    }

    else if (equi >= 92)
    {
    System.out.print("1.50");
    }

    else if (equi >= 89)
    {
    System.out.print("1.75");
    }
         
    else if (equi >= 86)
    {
    System.out.print("2.00");
    }

    else if (equi >= 81)
    {
    System.out.print("2.25");
    }

    else if (equi >= 75)
    {
    System.out.print("2.50");
    }

    else if (equi >= 71)
    {
    System.out.print("2.75");
    }

    else if (equi == 70)
    {
    System.out.print("3.00");
    }

    else if (equi < 69)
    {
    System.out.print("5.00 (Failed)");
    }

    System.out.print("Equivalent: " + equi);

    scanner.close();
  }
}
