# WhatsApp Chat Analyzer
This repository contains code for a WhatsApp chat analyzer built using Streamlit, a Python library for creating interactive web applications. The analyzer allows you to upload a WhatsApp chat export file and gain insights from the chat data.

## Getting Started
To run the WhatsApp chat analyzer locally, follow the steps below:

1. Clone the repository to your local machine:
 - `git clone https://github.com/your-username/whatsapp-chat-analyzer.git`

2. Navigate to the project directory:
- `cd whatsapp-chat-analyzer`

3. Install the required dependencies. It is recommended to use a virtual environment:
- `pip install -r requirements.txt`

4. Run the Streamlit app:
- `streamlit run app.py`

5. Access the app in your browser at http://localhost:8501.

# Usage
1. Choose a WhatsApp chat export file using the file uploader in the sidebar.

2. Once the file is uploaded, the app will preprocess the data and display the chat data in a dataframe.

3. Select a user from the sidebar dropdown to show analysis specific to that user. Choose "Overall" to view overall analysis of the group chat.

4. Click the "Show Analysis" button to display statistics about the selected user, including total messages, total words, media shared, and number of links shared.

5. If "Overall" is selected, the app will also identify the busiest user in the group and display a bar chart of their activity. Additionally, a dataframe will be shown with the user's activity details.

6.  A word cloud will be displayed showing the most frequently used words by the selected user.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
The code in this repository was inspired by various open-source projects and tutorials. Special thanks to the contributors of the dependencies used in this project.

Feel free to contribute to this project by submitting issues or pull requests. Enjoy analyzing your WhatsApp chats!
