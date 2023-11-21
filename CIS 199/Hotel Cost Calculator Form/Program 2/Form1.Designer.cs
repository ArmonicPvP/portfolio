namespace Program_2
{
    partial class Program2HotelCalculator
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
            this.numberOfGuestsLabel = new System.Windows.Forms.Label();
            this.numberOfNightsLabel = new System.Windows.Forms.Label();
            this.hotelStarsLabel = new System.Windows.Forms.Label();
            this.numberOfGuestsTextBox = new System.Windows.Forms.TextBox();
            this.numberOfNightsTextBox = new System.Windows.Forms.TextBox();
            this.hotelStarsComboBox = new System.Windows.Forms.ComboBox();
            this.calculateButton = new System.Windows.Forms.Button();
            this.hotelCostLabel = new System.Windows.Forms.Label();
            this.hotelCostOutputLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // numberOfGuestsLabel
            // 
            this.numberOfGuestsLabel.AutoSize = true;
            this.numberOfGuestsLabel.Location = new System.Drawing.Point(128, 51);
            this.numberOfGuestsLabel.Name = "numberOfGuestsLabel";
            this.numberOfGuestsLabel.Size = new System.Drawing.Size(213, 29);
            this.numberOfGuestsLabel.TabIndex = 0;
            this.numberOfGuestsLabel.Text = "Number of Guests:";
            // 
            // numberOfNightsLabel
            // 
            this.numberOfNightsLabel.AutoSize = true;
            this.numberOfNightsLabel.Location = new System.Drawing.Point(133, 105);
            this.numberOfNightsLabel.Name = "numberOfNightsLabel";
            this.numberOfNightsLabel.Size = new System.Drawing.Size(207, 29);
            this.numberOfNightsLabel.TabIndex = 1;
            this.numberOfNightsLabel.Text = "Number of Nights:";
            // 
            // hotelStarsLabel
            // 
            this.hotelStarsLabel.AutoSize = true;
            this.hotelStarsLabel.Location = new System.Drawing.Point(133, 151);
            this.hotelStarsLabel.Name = "hotelStarsLabel";
            this.hotelStarsLabel.Size = new System.Drawing.Size(137, 29);
            this.hotelStarsLabel.TabIndex = 2;
            this.hotelStarsLabel.Text = "Hotel Stars:";
            // 
            // numberOfGuestsTextBox
            // 
            this.numberOfGuestsTextBox.Location = new System.Drawing.Point(366, 51);
            this.numberOfGuestsTextBox.Name = "numberOfGuestsTextBox";
            this.numberOfGuestsTextBox.Size = new System.Drawing.Size(121, 35);
            this.numberOfGuestsTextBox.TabIndex = 1;
            // 
            // numberOfNightsTextBox
            // 
            this.numberOfNightsTextBox.Location = new System.Drawing.Point(366, 105);
            this.numberOfNightsTextBox.Name = "numberOfNightsTextBox";
            this.numberOfNightsTextBox.Size = new System.Drawing.Size(121, 35);
            this.numberOfNightsTextBox.TabIndex = 2;
            // 
            // hotelStarsComboBox
            // 
            this.hotelStarsComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.hotelStarsComboBox.FormattingEnabled = true;
            this.hotelStarsComboBox.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5"});
            this.hotelStarsComboBox.Location = new System.Drawing.Point(366, 151);
            this.hotelStarsComboBox.Name = "hotelStarsComboBox";
            this.hotelStarsComboBox.Size = new System.Drawing.Size(121, 37);
            this.hotelStarsComboBox.TabIndex = 3;
            // 
            // calculateButton
            // 
            this.calculateButton.Location = new System.Drawing.Point(217, 223);
            this.calculateButton.Name = "calculateButton";
            this.calculateButton.Size = new System.Drawing.Size(146, 43);
            this.calculateButton.TabIndex = 4;
            this.calculateButton.Text = "Calculate";
            this.calculateButton.UseVisualStyleBackColor = true;
            this.calculateButton.Click += new System.EventHandler(this.calculateButton_Click);
            // 
            // hotelCostLabel
            // 
            this.hotelCostLabel.AutoSize = true;
            this.hotelCostLabel.Location = new System.Drawing.Point(133, 322);
            this.hotelCostLabel.Name = "hotelCostLabel";
            this.hotelCostLabel.Size = new System.Drawing.Size(131, 29);
            this.hotelCostLabel.TabIndex = 7;
            this.hotelCostLabel.Text = "Hotel Cost:";
            // 
            // hotelCostOutputLabel
            // 
            this.hotelCostOutputLabel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.hotelCostOutputLabel.Location = new System.Drawing.Point(312, 321);
            this.hotelCostOutputLabel.Name = "hotelCostOutputLabel";
            this.hotelCostOutputLabel.Size = new System.Drawing.Size(175, 30);
            this.hotelCostOutputLabel.TabIndex = 8;
            // 
            // Program2HotelCalculator
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(14F, 29F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(643, 450);
            this.Controls.Add(this.hotelCostOutputLabel);
            this.Controls.Add(this.hotelCostLabel);
            this.Controls.Add(this.calculateButton);
            this.Controls.Add(this.hotelStarsComboBox);
            this.Controls.Add(this.numberOfNightsTextBox);
            this.Controls.Add(this.numberOfGuestsTextBox);
            this.Controls.Add(this.hotelStarsLabel);
            this.Controls.Add(this.numberOfNightsLabel);
            this.Controls.Add(this.numberOfGuestsLabel);
            this.Name = "Program2HotelCalculator";
            this.Text = "Program 2 - Hotel Calculator";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label numberOfGuestsLabel;
        private System.Windows.Forms.Label numberOfNightsLabel;
        private System.Windows.Forms.Label hotelStarsLabel;
        private System.Windows.Forms.TextBox numberOfGuestsTextBox;
        private System.Windows.Forms.TextBox numberOfNightsTextBox;
        private System.Windows.Forms.ComboBox hotelStarsComboBox;
        private System.Windows.Forms.Button calculateButton;
        private System.Windows.Forms.Label hotelCostLabel;
        private System.Windows.Forms.Label hotelCostOutputLabel;
    }
}

