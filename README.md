# Automated_Reverse_Image_Search
This script automates reverse image searches on Google Images using Selenium. It processes a list of image URLs from an input Excel file, performs a search, extracts matching product links based on brand name and base URL, and saves the results to an output Excel file. 

# Automated Reverse Image Search with Selenium and Pandas

## Description
This script automates reverse image searches on Google Images using Selenium. It processes a list of image URLs from an input Excel file, performs a search, extracts matching product links based on brand name and base URL, and saves the results to an output Excel file. The automation helps in verifying product listings and price monitoring efficiently.

## Features
- Automates reverse image search on Google Images
- Extracts product links based on brand name and base URL
- Saves results in an organized Excel file
- Configures Selenium for optimal browsing settings

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Google Chrome browser
- ChromeDriver compatible with your Chrome version
- Required Python packages:
  ```sh
  pip install pandas selenium openpyxl
  ```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/automated-reverse-image-search.git
   cd automated-reverse-image-search
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Prepare an input Excel file with the following columns:
   - `image_url`: Direct link to the image
   - `base_url`: Base website to filter results
   - `brand_name`: Brand name for title matching
2. Update the script with the correct paths for:
   ```python
   input_file = "your_input_file.xlsx"  # Replace with actual file path
   output_file = "your_output_file.xlsx"  # Replace with actual file path
   service = Service(executable_path="path_to_chromedriver")  # Replace with actual path
   ```
3. Run the script:
   ```sh
   python script.py
   ```
4. The output file will contain matched URLs for verification.

## Best Practices for Open Source Contributions
- **Code Style**: Follow PEP8 standards for Python.
- **Documentation**: Maintain clear and concise documentation.
- **Testing**: Ensure scripts run error-free before committing.
- **Issue Tracking**: Use GitHub Issues for tracking bugs and improvements.
- **Pull Requests**: Follow a structured commit message format and detailed PR descriptions.
- **Security**: Avoid committing sensitive data such as credentials.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request.

