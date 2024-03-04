namespace Weather_Prediction
{
    partial class Form1
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
            this.getPredictionButton = new System.Windows.Forms.Button();
            this.locationChooser = new System.Windows.Forms.ComboBox();
            this.datePicker = new System.Windows.Forms.DateTimePicker();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.resultTemperatureBox = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // getPredictionButton
            // 
            this.getPredictionButton.Location = new System.Drawing.Point(114, 155);
            this.getPredictionButton.Name = "getPredictionButton";
            this.getPredictionButton.Size = new System.Drawing.Size(121, 23);
            this.getPredictionButton.TabIndex = 0;
            this.getPredictionButton.Text = "Get Prediction";
            this.getPredictionButton.UseVisualStyleBackColor = true;
            this.getPredictionButton.Click += new System.EventHandler(this.getPredictionButton_Click);
            // 
            // locationChooser
            // 
            this.locationChooser.FormattingEnabled = true;
            this.locationChooser.Location = new System.Drawing.Point(114, 128);
            this.locationChooser.Name = "locationChooser";
            this.locationChooser.Size = new System.Drawing.Size(121, 21);
            this.locationChooser.TabIndex = 1;
            // 
            // datePicker
            // 
            this.datePicker.Location = new System.Drawing.Point(114, 102);
            this.datePicker.MaxDate = new System.DateTime(2025, 1, 1, 0, 0, 0, 0);
            this.datePicker.MinDate = new System.DateTime(2024, 1, 1, 0, 0, 0, 0);
            this.datePicker.Name = "datePicker";
            this.datePicker.Size = new System.Drawing.Size(200, 20);
            this.datePicker.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(63, 102);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(30, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Date";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(63, 131);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(48, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "Location";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft YaHei", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(47, 66);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(141, 22);
            this.label3.TabIndex = 6;
            this.label3.Text = "Enter Basic Data";
            // 
            // resultTemperatureBox
            // 
            this.resultTemperatureBox.AutoSize = true;
            this.resultTemperatureBox.Location = new System.Drawing.Point(164, 209);
            this.resultTemperatureBox.Name = "resultTemperatureBox";
            this.resultTemperatureBox.Size = new System.Drawing.Size(0, 13);
            this.resultTemperatureBox.TabIndex = 7;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(111, 209);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(50, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "Tulemus:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.resultTemperatureBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.datePicker);
            this.Controls.Add(this.locationChooser);
            this.Controls.Add(this.getPredictionButton);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button getPredictionButton;
        private System.Windows.Forms.ComboBox locationChooser;
        private System.Windows.Forms.DateTimePicker datePicker;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label resultTemperatureBox;
        private System.Windows.Forms.Label label4;
    }
}

