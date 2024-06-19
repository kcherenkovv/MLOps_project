import io
import streamlit as st
from PIL import Image
from image_processing import generate_image_description

# создание интерфейса загрузки изображений пользователем в приложении Streamlit
def load_image():
    uploaded_file = st.file_uploader("Загрузите изображение для описания")
    if uploaded_file is not None:
        img = Image.open(io.BytesIO(uploaded_file.read()))
        if img.mode != "RGB":
            img = img.convert('RGB')
        st.image(img, caption='Uploaded Image.', use_column_width=True)
        return img
    return None

def main():
    st.title('Описание изображения с помощью Hugging Face модели')
    uploaded_image = load_image()
    
    if uploaded_image:
        description = generate_image_description(uploaded_image)
        st.subheader(f'Описание изображения: {description}')

if __name__ == '__main__':
    main()
