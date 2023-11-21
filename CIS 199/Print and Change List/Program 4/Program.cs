/* Grading ID: K3250
 * Program 4
 * Due 4/18/2022
 * Course CIS199-01
 * Prints out Superhero information based on a predefined list, then edits that superhero information and reprints it, then changes one value on all of them and finally reprints again
 * 
 */
using static System.Console;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Program_4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Superhero Aquaman = new Superhero("Aquaman", "Atlantis", "Telepathic control of acquatic life", 1941, "Utilizing the sacred trident"); // makes a new object with Aquman's info
            Superhero DrStrange = new Superhero("Dr. Strange", "Philadelphia", "Mysitc Arts", 1930, "Time Stone"); // makes a new object with Dr Strange's info
            Superhero Hulk = new Superhero("Hulk", "Campina Grande", "Extremely strong", 1969, "Anger increases strength"); // makes a new object with Hulk's info
            Superhero Spiderman = new Superhero("Spiderman", "Queens", "Sticks to walls", 2001, "Supersense"); // makes a new object with Spiderman's info
            Superhero Ironman = new Superhero("Iron Man", "Long Island", "Extremely smart", 1963, "Super suit"); // makes a new object with Ironman's info
            Superhero[] superheroes = new Superhero[] { Aquaman, DrStrange, Hulk, Spiderman, Ironman }; // makes an array that stores the values of all the objects
            SuperheroPrint(superheroes); // runs the SuperheroPrint method
            Aquaman.OnPlanetEarth(); // sets isOnPlanetEarth to true
            Hulk.OnPlanetEarth(); // sets isOnPlanetEarth to true
            DrStrange.FirstSuperpower = "Mind control"; // redefines Dr Strange's first superpower
            Spiderman.SecondSuperpower = "Strong"; // redefines Spiderman's second superpower
            Ironman.FirstSuperpower = "Rich"; // redefines Ironman's first superpower
            SuperheroPrint(superheroes); // runs the SuperheroPrint method
            foreach (Superhero superhero in superheroes) // sets all Superheroes' isOnPlanetEarth to false
            {
                superhero.OffPlanetEarth();
            }
            SuperheroPrint(superheroes);
        }
        // precondition: must have Superheroes in Superhero array
        // postcondition: prints out Superhero info
        static void SuperheroPrint(Superhero[] superheroes)
        {
            foreach (Superhero superhero in superheroes)
            {
                WriteLine(superhero.ToString());
            }
        }
    }
    
}
