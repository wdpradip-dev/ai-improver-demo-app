import streamlit as st
from groq import Groq

# Replace with your actual API key
client = Groq(api_key="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")

def improve_text(text):
    prompt = f"Improve this text and correct grammar:\n\n{text}"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content


# 🎨 Streamlit UI
st.title("✍️ AI Text Improver App")
st.markdown("---")
st.markdown("### 🔹 Perfect for emails, resumes, and assignments")

st.write("Improve your grammar and writing instantly!")

user_text = st.text_area("Enter your text here:")

if st.button("Improve Text"):
    if user_text:
        with st.spinner("Improving your text..."):
            improved = improve_text(user_text)
            st.success("Improved Version:")
            st.write(improved)
    else:
        st.warning("Please enter some text.")
