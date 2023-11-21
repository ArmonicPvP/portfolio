/* Grading ID: K3250
 * Program 2
 * Due 3/10/2022
 * Course CIS199-01
 * Calculates the hotel cost based on number of guests, number of nights, and hotel stars
 * 
 */

using System;
using System.Windows.Forms;

namespace Program_2
{
    public partial class Program2HotelCalculator : Form
    {
        public Program2HotelCalculator()
        {
            InitializeComponent();
        }

        private void calculateButton_Click(object sender, EventArgs e)
        {
            const int FLAT_FEE_1 = 100; // flat fee for 1 guest
            const int FLAT_FEE_2 = 150; // flat fee for 2 guests
            const int FLAT_FEE_3 = 250; // flat fee for 3 guests
            const int FLAT_FEE_4_7 = 400; // flat fee for 4 guests
            const int ROOM_RATE_DAILY = 100; // rate for daily (1-6)
            const int ROOM_RATE_WEEKLY = 75; // rate for weekly (7-30)
            const int ROOM_RATE_MONTHLY = 25; //rate for monthly (31+)
            const double TWO_STAR_MULT = 1.5; // two start rate multiplication
            const double THREE_STAR_MULT = 2.5; // three star rate multiplication
            const int FOUR_STAR_MULT = 3; // four star rate multiplication
            const int FIVE_STAR_MULT = 4; // five star rate multiplication

            int numberOfGuests, numberOfNights, hotelStars; // defines our number of guests, number of nights, and hotel stars
            double hotelCost = 0; // defines hotel cost as a double and sets it to 0

            if (int.TryParse(numberOfGuestsTextBox.Text, out numberOfGuests) && numberOfGuests >= 1 && numberOfGuests <= 7)
            {
                if (int.TryParse(numberOfNightsTextBox.Text, out numberOfNights) && numberOfNights >= 1)
                {
                    if (hotelStarsComboBox.SelectedIndex >= 0)
                    {
                        int.TryParse(hotelStarsComboBox.Text, out hotelStars); // assigns the hotel stars to the variable
                        if (numberOfNights < 7)
                        {
                            hotelCost = numberOfNights * ROOM_RATE_DAILY; // assigns hotelCost to the # of nights times the daily room rate
                        }
                        if (numberOfNights >= 7 && numberOfNights < 31)
                        {
                            hotelCost = numberOfNights * ROOM_RATE_WEEKLY; // assigns hotelCost to the # of nights times the weekly room rate
                        }
                        if (numberOfNights >= 31)
                        {
                            hotelCost = numberOfNights * ROOM_RATE_MONTHLY; // assigns hotelCost to the # of nights times the monthly room rate
                        }
                        switch (numberOfGuests)
                        {
                            case 1:
                                hotelCost += FLAT_FEE_1; // assigns hotelCost to the value from before plus the flat fee for 1 guest
                                break;
                            case 2:
                                hotelCost += FLAT_FEE_2; // assigns hotelCost to the value from before plus the flat fee for 2 guests
                                break;
                            case 3:
                                hotelCost += FLAT_FEE_3; // assigns hotelCost to the value from before plus the flat fee for 3 guests
                                break;
                            case 4:
                            case 5:
                            case 6:
                            case 7:
                                hotelCost += FLAT_FEE_4_7; // assigns hotelCost to the value from before plus the flat fee for 4, 5, 6, and 7 guests
                                break;
                        }
                        switch (hotelStars)
                        {
                            case 2:
                                hotelCost *= TWO_STAR_MULT; // assigns hotelCost to the value from before times the star multiplier of 2
                                break;
                            case 3:
                                hotelCost *= THREE_STAR_MULT; // assigns hotelCost to the value from before times the star multiplier of 3
                                break;
                            case 4:
                                hotelCost *= FOUR_STAR_MULT; // assigns hotelCost to the value from before times the star multiplier of 4
                                break;
                            case 5:
                                hotelCost *= FIVE_STAR_MULT; // assigns hotelCost to the value from before times the star multiplier of 5
                                break;
                        }
                        hotelCostOutputLabel.Text = $"{hotelCost:C}";
                    }
                    else
                    {
                        hotelCostOutputLabel.Text = "Hotel stars?";
                    }
                }
                else
                {
                    numberOfNightsTextBox.Text = "Enter a value greater than 1!";
                }
            }
            else
            {
                numberOfGuestsTextBox.Text = "Enter a value between 1 & 7!";
            }
        }
    }
}
