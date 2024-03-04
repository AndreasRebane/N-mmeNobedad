using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Globalization;
using System.Net.Http;
using System.Xml;

namespace Weather_Prediction
{

    public partial class Form1 : Form
    {
        // API Related
        static String apiSiteURI = $"https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php";
        static bool hasWeatherData = false;
        static string weatherData = "";
        static String temperature;

        public Form1()
        {
            InitializeComponent();

            // Get Weather Data
            HttpClient httpClient = new HttpClient();
            HttpResponseMessage responseMessage = httpClient.GetAsync(apiSiteURI).Result;

            // Save request status
            hasWeatherData = responseMessage.IsSuccessStatusCode;
            Console.WriteLine($"Request status: {hasWeatherData}");

            // Don't extract content if request failed
            if (!hasWeatherData) return;
            weatherData = responseMessage.Content.ReadAsStringAsync().Result.ToLower();

            datePicker.MinDate = DateTime.Today;
        }

        private void getPredictionButton_Click(object sender, EventArgs e)
        {
            // If request failed don't go further
            if (!hasWeatherData) return;

            try
            {
                // Get the date and format (3-4-2024)
                String dateTime, day, month;
                if (datePicker.Value.Day < 10) day = "0" + datePicker.Value.Day.ToString();
                else day = datePicker.Value.Day.ToString();

                if (datePicker.Value.Month < 10) month = "0" + datePicker.Value.Month.ToString();
                else month = datePicker.Value.Month.ToString();

                dateTime = (String)datePicker.Value.Year.ToString() + "-" + month + "-" + day;

                String locationData = locationChooser.Text.ToLower();
                if (locationData == "tallinn-harku") locationData = "harku";

                // Get Temperature
                int dateIndex = weatherData.IndexOf(dateTime);
                int locationIndex = weatherData.IndexOf(locationData, dateIndex);
                int locationEndIndex = weatherData.IndexOf("</place>", locationIndex);
                temperature = weatherData.Substring(weatherData.IndexOf("tempmin>", locationIndex) + 8, weatherData.IndexOf("tempmin>", locationIndex) + 16);
                temperature = temperature.Substring(0, temperature.IndexOf("tempmin") - 2) + " C";

            } 
            catch 
            {
                temperature = "Midagi läks valesti! Proovi uuesti.";
            }
            resultTemperatureBox.Text = temperature;
        }
    }
}
