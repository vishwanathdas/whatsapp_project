
# Django WhatsApp Messaging Project

This project allows you to send WhatsApp messages to multiple groups using a Django web application.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How it works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running this project, make sure you have the following installed:

- Python (version 3.x)
- Django (version 3.x)
- pyautogui (Python library for automating GUI interactions)
- Google Chrome or any other supported browser (for WhatsApp web)

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/your_username/whatsapp_project.git
cd whatsapp_project

2. Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate # On Windows, use: venv\Scripts\activate


3. Install the required Python packages:

   pip install -r requirements.txt
   Django>=3.2,<4.0
   pyautogui>=0.9.52


## Usage

1. Run the Django development server:

python manage.py runserver


2. Open your web browser and navigate to `http://127.0.0.1:8000/`.

3. Fill in the form with the group IDs (separated by commas) and the message you want to send.

4. Click the "Send Message" button to send the WhatsApp messages.

## How it works

The Django application provides a web interface to send WhatsApp messages. It uses the `pyautogui` library to automate interactions with the web browser. When you submit the form, the server will process the input and initiate the WhatsApp web interface. After a short delay, the application will open individual group chats and send the specified message.

Please note that automating the web browser with `pyautogui` may not be the most robust solution and has limitations. Consider using WhatsApp API services for more reliable and scalable solutions.

## Contributing

Contributions are welcome! If you find any issues or want to improve the project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).

