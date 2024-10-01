import streamlit as st
from openai import OpenAI
import os


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def modify_message(original_message, reply_to_message):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are a helpful assistant that modifies 
             messages to remove inflammatory content,
              taking into account the message it is replying to. \n
            Keep ALL of the meaning but remove anything that could be considered, aggressive, condescending, or mocking.
             Remove any references, metaphors, ideas that are deviating from the key theme and could cause arguments.
               Rewrite in a way to foster healthy and respectful debate \n\n
               Give a detailed an argument as possible based on what they have written.
             return nothing but the modified message""",
            },
            {
                "role": "user",
                "content": f"""Original message to reply to: {reply_to_message}\n\nMessage to modify: {original_message or "not supplied" }\n\n""",
            },
        ],
    )
    return completion.choices[0].message.content


st.title("Message Modifier App")

reply_to_message = st.text_area("Message you want to reply to:", height=100)
original_message = st.text_area("Your message:", height=100)

if st.button("Modify Message"):
    if reply_to_message:
        with st.spinner("Modifying message..."):
            modified_message = modify_message(original_message, reply_to_message)
        st.success("Message modified successfully!")
        st.write("Modified message:")
        st.write(modified_message)
    else:
        st.warning("Please enter message before modifying.")

# st.sidebar.markdown("""
# ## How to use this app:
# 1. Enter the message you're replying to in the first text area.
# 2. Enter your original message in the second text area.
# 3. Click the "Modify Message" button.
# 4. The app will generate a modified, friendly version of your message.
# """)
