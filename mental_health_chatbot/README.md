# Mental Health Assistant Chatbot

A supportive, empathetic mental health assistant designed to provide guidance, resources, and a compassionate ear using the Groq "deepseek-r1-distill-llama-70b" model.

## Features

- Interactive chat interface built with Streamlit
- Powered by Groq's "deepseek-r1-distill-llama-70b" model
- Provides mental health support, coping strategies, and resources
- Responsive and intuitive user interface

## Setup Instructions

1. **Clone or download this repository**

   ```sh
   git clone https://github.com/yourusername/mental-health-assistant.git
   cd mental-health-assistant
   ```

2. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Get a Groq API Key**

   - Sign up at [Groq's website](https://www.groq.com)
   - Generate an API key from your dashboard

4. **Set up your environment**

   - Create a `.env` file in the root directory and add your Groq API key:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     ```

5. **Run the application**

   ```sh
   streamlit run app.py
   ```

6. **Use the assistant**

   - Open your browser and go to the URL displayed in the terminal (typically http://localhost:8501)
   - Start chatting with the mental health assistant

## Important Notes

- This assistant is not a replacement for professional mental health care.
- Always consult with qualified mental health professionals for medical advice.
- This tool is for informational and supportive purposes only.

## Customization

You can customize the assistant by modifying the system message in `app.py` to change the AI's behavior and responses.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.