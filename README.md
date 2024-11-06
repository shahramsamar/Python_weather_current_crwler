# Python Weather Current Data Crawler

A Python script to gather and display real-time weather data from online sources. This project demonstrates web scraping techniques and APIs for collecting current weather information.

## Features

- **Real-Time Weather Data**: Retrieves up-to-date weather information, including temperature, humidity, wind speed, and more.
- **Web Scraping & APIs**: Combines traditional web scraping techniques with API requests for reliable weather data.
- **Customizable**: Easily modify the script to fetch weather data for different locations or add additional parameters.

## Requirements

- **Python 3.x**
- **pip** for installing dependencies

### Libraries

The project uses the following Python libraries:

- `requests`: For making HTTP requests to APIs
- `BeautifulSoup4`: For parsing HTML data when scraping
- `pandas` (optional): For organizing and saving data
- `json` and `time`: For handling JSON responses and managing request intervals

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/python_weather_current_crwler.git
    cd python_weather_current_crwler
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage

- **Run the script:**

    ```bash
    python weather_crawler.py
    ```

- The script will output current weather details for the specified location(s).
- Modify the script to change the location or add more data parameters as needed.

### Project Structure

- `weather_crawler.py`: The main script for scraping weather data.
- `requirements.txt`: Lists all project dependencies.

## Contributing

Contributions are welcome! Feel free to submit pull requests for adding new weather data sources, enhancing data handling, or improving script functionality.

## Disclaimer

Ensure that scraping complies with the terms of service of any websites or APIs used in this project.

