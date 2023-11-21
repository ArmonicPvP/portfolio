using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Program_4
{ 
    public class Superhero
    {
        // precondition: must be an int
        // postcondition: stores birth year
        private int birthYear;
        //precondition: must be a char and superHero name must be defined
        //postcondition: stores the first initial of superheroName
        private readonly char initial;
        // precondition: must be bool
        // postcondition: stores a boolean of if they are or aren't on earth
        private bool isOnPlanetEarth;
        // precondition: must have a string, string, string, integer, string
        // postcondition: accepts a string, string, string, integer, and string and assigns them to the variables
        public Superhero(string superheroName, string birthCity, string firstSuperpower, int birthYear, string secondSuperPower)
        {
            this.SuperheroName = superheroName;
            this.BirthCity = birthCity;
            this.FirstSuperpower = firstSuperpower;
            this.BirthYear = birthYear;
            this.SecondSuperpower = secondSuperPower;
        }
        // precondition: must be a string
        // postcondition: stores super hero string
        public string SuperheroName { get; set; }
        // precondition: must be a string
        // postcondition: stores birth city
        public string BirthCity { get; set; }
        // precondition: must be a string
        // postcondition: stores first superpower
        public string FirstSuperpower { get; set; }
        // precondition: value > 0
        // postcondition: sets birth year to birthYear
        public int BirthYear
        {
            get { return birthYear; }
            set
            {
                if (value >= 0)
                {
                    birthYear = value;
                }
                else
                {
                    birthYear = 1999;
                }
            }
        }
        // precondition: must be string
        // postcondition: stores string of second super power
        public string SecondSuperpower { get; set; }
        // precondition: must be string
        // postcondition: gets the first character from the string superheroName
        public char Initial { get { return SuperheroName[0]; } }
        // precondition: needs to be called on Superhero
        // postcondition: sets isOnPlanetEarth to true
        public void OnPlanetEarth()
        {
            isOnPlanetEarth = true;
        }
        // precondition: needs to be called on Superhero
        // postcondition: sets isOnPlantEarth to false
        public void OffPlanetEarth()
        {
            isOnPlanetEarth = false;
        }
        // precondition: must be called
        // postcondition: returns isOnPlanetEarth status
        public bool IsOnPlanetEarth()
        {
            return isOnPlanetEarth;
        }
        // precondition: needs to be called on Superhero
        // postcondition: outpots superhero name, city, first superpower, birth year, second superpower, if they are on earth, and their first initial
        public override string ToString()
        {
            string toString = $"Name: {SuperheroName}" + Environment.NewLine + $"City: {BirthCity}" + Environment.NewLine + $"First Super Power: {FirstSuperpower}" + Environment.NewLine + $"Born in: {BirthYear}" + Environment.NewLine + $"Second Super Power: {SecondSuperpower}" + Environment.NewLine + $"Planet Earth: {IsOnPlanetEarth()}" + Environment.NewLine + $"Initial: {Initial}";
            return toString;
        }
    }
}
