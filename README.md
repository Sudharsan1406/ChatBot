# ChatBot

# 🧠 Memory Chatbot using Groq

A conversational AI chatbot built using **Streamlit** and **Groq LLM** with persistent memory. The chatbot stores conversation history in a JSON file, allowing it to remember previous interactions even after restarting the application.

---

## 🚀 Features

- 💬 Interactive chatbot interface using Streamlit
- ⚡ Powered by Groq LLM (Llama 3.3 70B Versatile)
- 🧠 Persistent chat memory using JSON
- 🔄 Automatically loads previous conversations
- 💾 Saves conversation history after every interaction
- 📜 Displays previous chats on application startup
- 🎯 Maintains recent conversation context for better responses

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- JSON
- OS Module

---

## 📂 Project Structure

```
Memory-Chatbot/
│
├── Chatbot-1.py          # Main Streamlit Application
├── requirements.txt
├── README.md
└── screenshots/
      └── chatbot_ui.png
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/memory-chatbot-groq.git
```

```bash
cd memory-chatbot-groq
```

---

### 2. Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Packages

```text
streamlit
groq
```

---

## 🔑 Configure API Key

**Do NOT hardcode your API key in the source code.**

Create a file named:

```
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY="your_groq_api_key"
```

Then access it in Python:

```python
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)
```

---

## ▶️ Run the Project

```bash
streamlit run Chatbot-1.py
```


## 💬 How It Works

1. User enters a message.
2. Message is added to chat history.
3. Recent conversations are sent to Groq LLM.
4. AI generates a response.
5. Response is displayed.
6. Entire conversation is saved into `chat_history.json`.
7. Previous chats are automatically loaded when the application restarts.

---

## 📈 Future Enhancements

- User authentication
- Multiple chat sessions
- SQLite or MongoDB storage
- Vector database memory
- Voice input/output
- File upload support
- PDF question answering
- Retrieval-Augmented Generation (RAG)
- Chat history search
- Dark mode support

---

## 🔒 Security

Never expose your API key publicly.

Use:

- `.streamlit/secrets.toml`
- Environment Variables

instead of storing the key inside the source code.

---

## 👨‍💻 Author

**Sudharsan M S**

AI Developer | Data Scientist | Machine Learning Enthusiast

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
