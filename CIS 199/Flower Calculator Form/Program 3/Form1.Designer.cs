namespace Program_3
{
    partial class GardenForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.gardenLabel = new System.Windows.Forms.Label();
            this.itemNumberLabel = new System.Windows.Forms.Label();
            this.quantityLabel = new System.Windows.Forms.Label();
            this.calculateButton = new System.Windows.Forms.Button();
            this.flowersCostLabel = new System.Windows.Forms.Label();
            this.baseAdjustedCostLabel = new System.Windows.Forms.Label();
            this.discountPercentLabel = new System.Windows.Forms.Label();
            this.totalPriceLabel = new System.Windows.Forms.Label();
            this.gardenComboBox = new System.Windows.Forms.ComboBox();
            this.itemNumberTextBox = new System.Windows.Forms.TextBox();
            this.quantityTextBox = new System.Windows.Forms.TextBox();
            this.flowersCostOutputBox = new System.Windows.Forms.Label();
            this.baseAdjustedCostOutputBox = new System.Windows.Forms.Label();
            this.discountPercentOutputBox = new System.Windows.Forms.Label();
            this.totalPriceOutputBox = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // gardenLabel
            // 
            this.gardenLabel.AutoSize = true;
            this.gardenLabel.Location = new System.Drawing.Point(190, 29);
            this.gardenLabel.Name = "gardenLabel";
            this.gardenLabel.Size = new System.Drawing.Size(99, 29);
            this.gardenLabel.TabIndex = 0;
            this.gardenLabel.Text = "Garden:";
            // 
            // itemNumberLabel
            // 
            this.itemNumberLabel.AutoSize = true;
            this.itemNumberLabel.Location = new System.Drawing.Point(53, 85);
            this.itemNumberLabel.Name = "itemNumberLabel";
            this.itemNumberLabel.Size = new System.Drawing.Size(236, 29);
            this.itemNumberLabel.TabIndex = 1;
            this.itemNumberLabel.Text = "Entree/Item Number:";
            this.itemNumberLabel.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            // 
            // quantityLabel
            // 
            this.quantityLabel.AutoSize = true;
            this.quantityLabel.Location = new System.Drawing.Point(183, 135);
            this.quantityLabel.Name = "quantityLabel";
            this.quantityLabel.Size = new System.Drawing.Size(106, 29);
            this.quantityLabel.TabIndex = 2;
            this.quantityLabel.Text = "Quantity:";
            // 
            // calculateButton
            // 
            this.calculateButton.AutoSize = true;
            this.calculateButton.Location = new System.Drawing.Point(387, 189);
            this.calculateButton.Name = "calculateButton";
            this.calculateButton.Size = new System.Drawing.Size(123, 39);
            this.calculateButton.TabIndex = 3;
            this.calculateButton.Text = "Calculate";
            this.calculateButton.UseVisualStyleBackColor = true;
            this.calculateButton.Click += new System.EventHandler(this.calculateButton_Click);
            // 
            // flowersCostLabel
            // 
            this.flowersCostLabel.AutoSize = true;
            this.flowersCostLabel.Location = new System.Drawing.Point(128, 251);
            this.flowersCostLabel.Name = "flowersCostLabel";
            this.flowersCostLabel.Size = new System.Drawing.Size(161, 29);
            this.flowersCostLabel.TabIndex = 4;
            this.flowersCostLabel.Text = "Flowers Cost:";
            // 
            // baseAdjustedCostLabel
            // 
            this.baseAdjustedCostLabel.AutoSize = true;
            this.baseAdjustedCostLabel.Location = new System.Drawing.Point(60, 304);
            this.baseAdjustedCostLabel.Name = "baseAdjustedCostLabel";
            this.baseAdjustedCostLabel.Size = new System.Drawing.Size(229, 29);
            this.baseAdjustedCostLabel.TabIndex = 5;
            this.baseAdjustedCostLabel.Text = "Base Adjusted Cost:";
            // 
            // discountPercentLabel
            // 
            this.discountPercentLabel.AutoSize = true;
            this.discountPercentLabel.Location = new System.Drawing.Point(88, 358);
            this.discountPercentLabel.Name = "discountPercentLabel";
            this.discountPercentLabel.Size = new System.Drawing.Size(201, 29);
            this.discountPercentLabel.TabIndex = 6;
            this.discountPercentLabel.Text = "Discount Percent:";
            // 
            // totalPriceLabel
            // 
            this.totalPriceLabel.AutoSize = true;
            this.totalPriceLabel.Location = new System.Drawing.Point(153, 400);
            this.totalPriceLabel.Name = "totalPriceLabel";
            this.totalPriceLabel.Size = new System.Drawing.Size(136, 29);
            this.totalPriceLabel.TabIndex = 7;
            this.totalPriceLabel.Text = "Total Price:";
            // 
            // gardenComboBox
            // 
            this.gardenComboBox.FormattingEnabled = true;
            this.gardenComboBox.Items.AddRange(new object[] {
            "Premium",
            "Standard",
            "Discount"});
            this.gardenComboBox.Location = new System.Drawing.Point(328, 29);
            this.gardenComboBox.Name = "gardenComboBox";
            this.gardenComboBox.Size = new System.Drawing.Size(237, 37);
            this.gardenComboBox.TabIndex = 8;
            // 
            // itemNumberTextBox
            // 
            this.itemNumberTextBox.Location = new System.Drawing.Point(328, 85);
            this.itemNumberTextBox.Name = "itemNumberTextBox";
            this.itemNumberTextBox.Size = new System.Drawing.Size(237, 35);
            this.itemNumberTextBox.TabIndex = 9;
            // 
            // quantityTextBox
            // 
            this.quantityTextBox.Location = new System.Drawing.Point(328, 135);
            this.quantityTextBox.Name = "quantityTextBox";
            this.quantityTextBox.Size = new System.Drawing.Size(237, 35);
            this.quantityTextBox.TabIndex = 10;
            // 
            // flowersCostOutputBox
            // 
            this.flowersCostOutputBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.flowersCostOutputBox.Location = new System.Drawing.Point(323, 251);
            this.flowersCostOutputBox.Name = "flowersCostOutputBox";
            this.flowersCostOutputBox.Size = new System.Drawing.Size(242, 29);
            this.flowersCostOutputBox.TabIndex = 11;
            // 
            // baseAdjustedCostOutputBox
            // 
            this.baseAdjustedCostOutputBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.baseAdjustedCostOutputBox.Location = new System.Drawing.Point(323, 303);
            this.baseAdjustedCostOutputBox.Name = "baseAdjustedCostOutputBox";
            this.baseAdjustedCostOutputBox.Size = new System.Drawing.Size(242, 29);
            this.baseAdjustedCostOutputBox.TabIndex = 12;
            // 
            // discountPercentOutputBox
            // 
            this.discountPercentOutputBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.discountPercentOutputBox.Location = new System.Drawing.Point(323, 357);
            this.discountPercentOutputBox.Name = "discountPercentOutputBox";
            this.discountPercentOutputBox.Size = new System.Drawing.Size(242, 29);
            this.discountPercentOutputBox.TabIndex = 13;
            // 
            // totalPriceOutputBox
            // 
            this.totalPriceOutputBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.totalPriceOutputBox.Location = new System.Drawing.Point(323, 400);
            this.totalPriceOutputBox.Name = "totalPriceOutputBox";
            this.totalPriceOutputBox.Size = new System.Drawing.Size(242, 29);
            this.totalPriceOutputBox.TabIndex = 14;
            // 
            // GardenForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(14F, 29F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(617, 450);
            this.Controls.Add(this.totalPriceOutputBox);
            this.Controls.Add(this.discountPercentOutputBox);
            this.Controls.Add(this.baseAdjustedCostOutputBox);
            this.Controls.Add(this.flowersCostOutputBox);
            this.Controls.Add(this.quantityTextBox);
            this.Controls.Add(this.itemNumberTextBox);
            this.Controls.Add(this.gardenComboBox);
            this.Controls.Add(this.totalPriceLabel);
            this.Controls.Add(this.discountPercentLabel);
            this.Controls.Add(this.baseAdjustedCostLabel);
            this.Controls.Add(this.flowersCostLabel);
            this.Controls.Add(this.calculateButton);
            this.Controls.Add(this.quantityLabel);
            this.Controls.Add(this.itemNumberLabel);
            this.Controls.Add(this.gardenLabel);
            this.Name = "GardenForm";
            this.Text = "The Happy Garden Shop";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label gardenLabel;
        private System.Windows.Forms.Label itemNumberLabel;
        private System.Windows.Forms.Label quantityLabel;
        private System.Windows.Forms.Button calculateButton;
        private System.Windows.Forms.Label flowersCostLabel;
        private System.Windows.Forms.Label baseAdjustedCostLabel;
        private System.Windows.Forms.Label discountPercentLabel;
        private System.Windows.Forms.Label totalPriceLabel;
        private System.Windows.Forms.ComboBox gardenComboBox;
        private System.Windows.Forms.TextBox itemNumberTextBox;
        private System.Windows.Forms.TextBox quantityTextBox;
        private System.Windows.Forms.Label flowersCostOutputBox;
        private System.Windows.Forms.Label baseAdjustedCostOutputBox;
        private System.Windows.Forms.Label discountPercentOutputBox;
        private System.Windows.Forms.Label totalPriceOutputBox;
    }
}

