### Purpose of App

This app is a prototype to see if large language models can help act as mediators between people in an argument.

### Things you will need for this app

- WSL2 or Ubuntu (currently Windows and macOS are **not** supported)
- Python 3
- Ollama
- A local large language model that works with Ollama. This repository uses Dolphin Mistral 7b, but you can change this in `app.py`

### How to install this app

1. Go to your terminal.
2. Clone this repository using `git clone -b Ollama-Version https://github.com/astrosnat/friendlydebateapp.git`.
3. Change the working directory with the command `cd ~/friendlydebateapp`.
4. Run `python3 -m venv venv`.
5. Run `source venv/bin/activate`.
6. Use `pip install -r requirements.txt`.
7. In a new terminal window, run `ollama serve` to start ollama.
8. In your original terminal window, run `streamlit run app.py`.
9. Open your Streamlit app in your browser of choice.
10. Have fun!
