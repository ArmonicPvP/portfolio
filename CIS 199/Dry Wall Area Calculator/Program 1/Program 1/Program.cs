/* Grading ID: K3250
 * Program 1
 * Due: 2/15/2022
 * CIS199-01
 * Dry Wall and Window installation calculator to calculate the cost of installation
 */


using static System.Console;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Program_1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double walls = 2; // defines that there are 2 walls that will be the same length in the house, 2 side walls and 2 front walls
            double windowFee = 100; // fee for Window installation
            double tenPercentFee = 1.1; // percentage fee for board breakage that the supplier charges

            WriteLine("Welcome to the Dry Wall and Window Installation Calulator\n");

            Write("Enter the length of the front (in feet): ");
            double lengthFront = double.Parse(ReadLine()); // get and store user input for the length of the front wall in square feet

            Write("Enter the length of the side (in feet): ");
            double lengthSide = double.Parse(ReadLine()); // get and store user input for the length of the side wall in square feet

            Write("Enter the height (in feet): ");
            double height = double.Parse(ReadLine()); // get and store user input for the height of the walls in square feet

            Write("Enter 1 if you want a window. Enter 0 if you do not: ");
            int window = int.Parse(ReadLine()); // get and store user input if they want a window or not

            Write("Enter cost of dry wall per square foot: ");
            double drywallCost = double.Parse(ReadLine()); // get and store user input on the cost of dry wall per square foot

            Write("Enter cost of labor per square foot: ");
            double laborCost = double.Parse(ReadLine()); // get and store user input on the cost of laber for square foot

            double totalSquareFeet = lengthFront * height * walls + lengthSide * height * walls + lengthSide * lengthFront; // calculates the total square footage of the walls, including the ceiling
            double totalSquareFeetTenPercent = totalSquareFeet * tenPercentFee; // calculates the total dry wall footage, adding on the 10% drywall fee
            double totalLaborCost = totalSquareFeetTenPercent * laborCost; // calculates the total labor cost
            double totalDrywallCost = totalSquareFeetTenPercent * drywallCost; // calculates the total cost of the drywall
            double totalCost = totalLaborCost + totalDrywallCost + window * windowFee; // calculates the total cost of everything, drywall, labor, and window

            WriteLine($"\nTotal square feet needed: {totalSquareFeet:N}");
            WriteLine($"10% extra square feet: {totalSquareFeetTenPercent:N}");
            WriteLine($"Labor cost: {totalLaborCost:C}");
            WriteLine($"Material cost: {totalDrywallCost:C}");
            WriteLine($"Total cost: {totalCost:C}");
        }
    }
}
