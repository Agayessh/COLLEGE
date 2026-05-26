/* Create a JAVA program using input / output statement that compute the employee salary where the following inputs are, 
EmpName, EmpDept, RatePerHour NoHrsWorked. 
Calculate the employee deduction and the Net salary of the employee, and print 
the employee salary information. */

import java.util.Scanner;

public class EmployeeSalaryCalculator {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    // Input

    System.out.print("Employee Name: ");
    String EN = scanner.nextLine();

    System.out.print("Department: ");
    String ED = scanner.nextLine();

    System.out.print("Rate per Hour: ");
    double RPH = scanner.nextDouble();

    System.out.print("Number of Hours worked: ");
    double NHW = scanner.nextDouble();

    // Calculate Gross Pay
    double grossPay = RPH * NHW;

    // Calculate Deductions
    double sss = grossPay * 0.05;
    double wTax = grossPay * 0.10;
    double PagIbig = 100;
    double PhilHealth = 150;
    double totalDeduction = sss + wTax + PagIbig + PhilHealth;

    // Calculate Net Salary
    double netSalary = grossPay - totalDeduction;

    // Output
    System.out.println("\nEmployee Name: " + EN);
    System.out.println("Employee Department: " + ED);
    System.out.println("Rate per Hour: " + RPH);
    System.out.println("NHW: " + NHW);
    System.out.println("Gross Pay: " + grossPay);
    System.out.println("SSS: " + sss);
    System.out.println("W/ Tax: " + wTax);
    System.out.println("Pag-ibig: " + PagIbig);
    System.out.println("PH: " + PhilHealth);
    System.out.println();

    System.out.println("Net Salary: " + netSalary);



     

    scanner.close();

  }

}
