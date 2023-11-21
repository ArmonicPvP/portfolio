/* Grading ID: K3250
 * Program 3
 * Due 4/1/2022
 * Course CIS199-01
 * Gets the total cost of flowers based on garden type, flower type, and quantity
 * 
 */

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Program_3
{
    public partial class GardenForm : Form
    {
        public GardenForm()
        {
            InitializeComponent();
        }

        private void calculateButton_Click(object sender, EventArgs e)
        {
            const double FULL_PRICE_100 = 1; // defines our discount for < 6
            const double FULL_PRICE_95 = .95; // defines our discount for bulk quantities from 6-15
            const double FULL_PRICE_90 = .9; // defines our discount for bulk quantities from 16-20
            const double FULL_PRICE_85 = .85; // defines our discount for bulk quantities from 21+

            string[] gardenArray; // defines our array for the Garden choices
            double[] gardenRateArray; // defines our array for the Garden rates related to the choices
            int[] flowerNumberArray; // defines our array for our flower numbers
            double[] costFlowerArray; // defines our array for the cost of the flower related to the flower numbers
            string foundGardenArray = ""; // defines our variable for when we find what garden type they've chosen from gardenArray
            double foundGardenRateArray = 0; // defines our variable for when we find what garden rate is from gardenRateArray
            double foundFlowerNumberArray = 0; // defines our variable for when we find what garden flower number they have chosen
            double foundCostFlowerArray = 0; // defines our variable for when we find what flower costs from costFlowerArray
            double percentFullPrice = 1; // defines the discount they will get, set to 1 because that's the no discount price
            bool foundGarden = false; // defines the stopping boolean for when we find what garden type they've chosen from gardenArray
            bool foundFlower = false; // defines the stopping boolean for when we find what flower number they've chosen from flowerNumberArray
            int itemNumber; // defines the variable for the item number they choose
            int quantity; // defines the variable for the quantity they choose

            gardenArray = new string [] { "Premium", "Standard", "Discount" }; // creates our garden types array
            gardenRateArray = new double[] { 1.1, 1, 0.9 }; // creates our garden rates array
            flowerNumberArray = new int[] { 10001, 10002, 10003, 10004, 10005, 10006, 10007 }; // creates our flower numbers array
            costFlowerArray = new double[] { 7.87, 9.51, 10.73, 9.99, 11.99, 5, 4.58 }; // creates our flower costs array

            if (gardenComboBox.SelectedIndex > -1) // tests if garden combo box is selected
            {
                if (int.TryParse(itemNumberTextBox.Text, out itemNumber) && itemNumber >= 10001 && itemNumber <= 10007) // tests if item number text box is valid and in-between 10001-10007
                {
                    if (int.TryParse(quantityTextBox.Text, out quantity) && quantity > 0) // tests if our quantity is valid and greater than 0
                    {
                        for (int i = 0; i < gardenArray.Length && !foundGarden; i++) // loops through our garden array to find the garden they chose and if it does, stops
                        {
                            if (gardenArray[i] == gardenComboBox.Text) // tests if it finds the garden type they chose and if it does it saves it and the rate
                            {
                                foundGarden = true;
                                foundGardenArray = gardenArray[i];
                                foundGardenRateArray = gardenRateArray[i];
                            }
                        }
                        for (int j = 0; j < flowerNumberArray.Length && !foundFlower; j++) // loops through our flowerNumber array to find the flower number they chose and if it does, stops
                        {
                            if (flowerNumberArray[j] == itemNumber) // tests if it finds the flower number they chose and if it does saves it and the cost
                            {
                                foundFlower = true;
                                foundFlowerNumberArray = flowerNumberArray[j];
                                foundCostFlowerArray = costFlowerArray[j];
                            }
                        }
                        if (quantity >= 6 && quantity <= 15) // tests if quantity qualifies for 5% discount
                        {
                            percentFullPrice = FULL_PRICE_95;
                        }
                        if (quantity >= 16 && quantity <= 20) // tests if quantity qualifies for 10% discount
                        {
                            percentFullPrice = FULL_PRICE_90;
                        }
                        if (quantity >= 21)
                        {
                            percentFullPrice = FULL_PRICE_85; // tests if quantity qualifies for 15% discount
                        }
                        flowersCostOutputBox.Text = $"{foundCostFlowerArray * quantity:C}"; // outputs our flower cost
                        baseAdjustedCostOutputBox.Text = $"{foundCostFlowerArray * quantity * foundGardenRateArray:C}"; // outputs our adjusted price of flowers * garden rate
                        discountPercentOutputBox.Text = $"{FULL_PRICE_100 - percentFullPrice:P2}"; // outputs our discount based on quantity
                        totalPriceOutputBox.Text = $"{foundCostFlowerArray * quantity * foundGardenRateArray * percentFullPrice:C}"; // outputs the final price
                    }
                    else
                    {
                        quantityTextBox.Text = "Enter a number greater than 1.";
                    }
                }
                else
                {
                    itemNumberTextBox.Text = "Enter a number from 10001-10007.";
                }
            }
            else
            {
                totalPriceOutputBox.Text = "Garden?";
            }
        }
    }
}
