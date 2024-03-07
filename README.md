# Regex Clone Web App

🚀 This Flask-based web application enables users to input a test string and a regular expression (regex) to discover all matching patterns. Additionally, it offers a functionality to validate the validity of provided email IDs. 📧

## Features

- Users can input a test string and a regular expression (regex) to find matches.
- Displays all the matches found in the test string based on the provided regex.
- Validates email IDs based on regex patterns.
- Deployed on AWS Cloud for accessibility. ☁️

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Install Dependencies:**
   Navigate into the project directory and install the required dependencies using pip:
   ```bash
   cd regex-clone-app
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   Run the Flask application using the following command:
   ```bash
   python app.py
   ```
   The app will be accessible at `http://localhost:5000` in your web browser.

## Usage

1. **Input Test String and Regex:**
   - Navigate to the home page (`http://localhost:5000`) in your web browser.
   - Input the test string and the regular expression into the provided form fields.
   - Click on the submit button to find matches.

2. **Validate Email IDs:**
   - Access the email validation route (`http://localhost:5000/validator`) in your web browser.
   - Input the email ID to be validated into the provided form field.
   - Click on the submit button to validate the email ID.

## Contributors

- [Vijay sada](https://github.com/vijaysada) 👨‍💻

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
