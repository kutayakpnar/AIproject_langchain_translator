#Integrate OPENAI
import os
from constants import openai_key
from langchain.llms import OpenAI
import json
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain #Whenever you give prompt

os.environ['OPENAI_API_KEY']=openai_key

st.title("Davon Translator")
sentence2 = st.text_input("Enter a sentence to translate:")
target_language2 = st.selectbox("Select the target language:", ["German", "Turkish", "French"])
language_codes = {
    "German": "de",
    "Turkish": "tr",
    "French": "fr"
}

# Check if both inputs are provided
if sentence2 and target_language2:
    # Define language prompt
    template = '''In an easy way, translate the following sentence '{sentence}' into '{target_language}' '''
    language_prompt = PromptTemplate(
        input_variables=['sentence', 'target_language'],
        template=template
    )

    # Format the language prompt with user input
    language_prompt.format(sentence=sentence2, target_language=target_language2)

    # Create OpenAI model instance
    llm = OpenAI(temperature=0.7)
    chain = LLMChain(llm=llm, prompt=language_prompt)

    # Call chain with user input
    output_json = chain({'sentence': sentence2, 'target_language': target_language2})

    # Extract the translated text from the JSON response and remove newline characters
    translated_text = output_json.get('text', '').replace('\n', '')

    # Display the translated text
    st.subheader("Translation Result:")
    st.write(translated_text)
else:
    st.warning("Please enter a sentence and a target language.")

# To run the Streamlit app, use the following command:
# streamlit run your_script.py