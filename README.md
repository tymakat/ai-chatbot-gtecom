# ai-chatbot-gtecom

## Introduction
This document will provide you with detailed instructions on how to setup and launch a simple implementation of an AI chatbot that specializes in providing high quality customer service.

### Architecture
- Streamlit: Used for UI, specifically displaying chatbot messages in real time  
- Pytest: Used for testing the dataset reading logic  
- Pandas: Used for simple operations with CSV datasets  
- Langchain: Used to initialize an LLM, process user messages and provide responses  

### Prerequisites

1. **Install required python dependencies**

Navigate to the root folder of the repository (where `.git` is located) and run:

```bash
pip install -r requirements.txt
```

2. **Create a `.env` file with an OpenAI API key**

Request an API key from a responsible employee (it should normally be provided to you via email).  
Create a `.env` file in the root folder of the repository and paste the following information:

```env
OPEN_AI_APIKEY="API key that was provided to you in the email"
```

---

### Testing the project

Run the following command from the root folder of the repository (important):

```bash
streamlit run implementation/logic/streamlit_interface.py
```

A new browser window should pop up in a few seconds.  
You can now have a conversation with the chatbot by entering your message.

---

### Running unit tests

To run the unit tests, navigate to the root folder of the repository and run:

```bash
pytest implementation/tests
```

There should be **3/3 successfully executed unit tests**.

---

### Known issues

There are multiple issues to be aware of that should be fixed if the work on this project will be continued:

1. Currently the project can only be tested from the root folder of the repository. A better implementation would be to implement logic for fetching the path to the project's root folder at runtime.

2. No specific versions of libraries in the `requirements.txt`. Due to the limited deadline, specific versions for the third-party libraries were not provided. This can cause problems in the distant future.
