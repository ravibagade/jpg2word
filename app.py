
import streamlit as st
import pytesseract
from PIL import Image
from docx import Document
from io import BytesIO

st.set_page_config(
    page_title="JPG to Word Converter",
    page_icon="📄"
)

st.title("JPG to Word Converter")
st.write("Convert JPG images into editable Word documents.")

uploaded_file = st.file_uploader(
    "Upload your JPG image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image",
             use_container_width=True)

    if st.button("Convert to Word"):

        with st.spinner("Extracting text..."):

            extracted_text = pytesseract.image_to_string(image)

            doc = Document()
            doc.add_heading("Converted Content", level=1)
            doc.add_paragraph(extracted_text)

            output = BytesIO()
            doc.save(output)
            output.seek(0)

        st.success("Conversion completed!")

        st.download_button(
            label="Download Word Document",
            data=output,
            file_name="converted_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
