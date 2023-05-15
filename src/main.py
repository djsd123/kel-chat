import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title="Kel-Chat - An LLM-powered Streamlit app", page_icon='🙊')

with st.sidebar:
    st.title('🤗💬 Kel-Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](<https://streamlit.io/>)
    - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM model
    
    💡 Note: No API key required!
    ''')
    add_vertical_space(5)
    st.write('Made with 💕 by [Kel](https://github.com/djsd123)')



# 'past' denotes the human user's input and 'generated' indicates the bot's response.
GENERATED_STATE = 'generated'
PAST_STATE = 'past'

if GENERATED_STATE not in st.session_state:
    st.session_state[GENERATED_STATE] = ["Hello 👋🏼, I'm Kel-Chat, how may I help you?"]

if PAST_STATE not in st.session_state:
    st.session_state[PAST_STATE] = ['Hi!']

input_container = st.container()
colored_header(label='', description='', color_name='blue-70')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

## Applying the user input box
with input_container:
    user_input = get_text()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot()
    response = chatbot.chat(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)

    if st.session_state[GENERATED_STATE]:
        for i in range(len(st.session_state[GENERATED_STATE])):
            message(st.session_state[PAST_STATE][i], is_user=True, key=str(i) + '_user')
            message(st.session_state[GENERATED_STATE][i], key=str(i))
