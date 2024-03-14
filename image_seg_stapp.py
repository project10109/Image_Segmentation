
import streamlit as st
from PIL import Image
from keras_segmentation.pretrained import pspnet_50_ADE_20K 
import cv2

from PIL import Image

def main():
    """Main function of the Streamlit app."""
    import streamlit as st
    import os
    # Title and description
    st.title("Image Segmentation App")
    import streamlit as st

    model1 = pspnet_50_ADE_20K() # load the pretrained model trained on ADE20k dataset
    # Create a container for the side header
    side_header = st.container()

    # Use a nested container for better styling
    with side_header.container():
    # Employ st.sidebar for side positioning
        st.sidebar.header("Upload and Segment Image")
        st.sidebar.write("Upload an image and see its basic segmentation")

        # # File upload element within the sidebar
        image_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

        # st.write("Upload an image and see its basic segmentation")

        #st.title("Test our model")
        # image_file = st.file_uploader("Upload Image",type=["jpg", "png", "jpeg"])
        # print('image_file name',image_file.name)
        # image2 = Image.open('/Users/dhanashreekarande/Downloads/'+uploaded_file.name)
    # st.image(image2, caption="Original Image", use_column_width=True)
    # image2 = cv2.imread('/Users/dhanashreekarande/Downloads/'+uploaded_file.name)
        if image_file is not None:
            orig_image = Image.open(image_file)
            st.header("Original Image")
            st.image(orig_image, caption="Original Image", use_column_width=True)
            im = orig_image.save('input.jpg')

            img = cv2.imread('input.jpg')

# image2 = Image.open('/Users/dhanashreekarande/Downloads/'+name)

    # image2 = cv2.imread('/Users/dhanashreekarande/Downloads/'+name)
            if st.button('Perform Image Segmentation'):

                out = model1.predict_segmentation(inp=img,overlay_img=True,out_fname="/tmp/image__output.png")
                out_nonoverlay = model1.predict_segmentation(inp=img,overlay_img=False,out_fname="/tmp/image__nonoverlay_output.png")




    # Define allowed image folder path
    image_folder = '/tmp/'
    output_filename='image__output.png'

    output_filename_nonoverlay='image__nonoverlay_output.png'

    if output_filename_nonoverlay and output_filename_nonoverlay.endswith(('.jpg', '.png', '.jpeg')):
      image_path = os.path.join(image_folder, output_filename_nonoverlay)
      print('image_path',image_path)
      if os.path.exists(image_path):
          out_image = Image.open(image_path)
          st.subheader("Segmented Image ")
          st.image(out_image, caption=f"Segmented Image ", use_column_width=True,width=1600)
          os.remove(image_path)

    if output_filename and output_filename.endswith(('.jpg', '.png', '.jpeg')):
      image_path = os.path.join(image_folder, output_filename)
      print('image_path',image_path)
      if os.path.exists(image_path):
          out_image = Image.open(image_path)
          st.subheader("Segmented Image with Overlay over Original Image")
        #   st.image(out_image, caption=output_filename, use_column_width=True)
          st.image(out_image, caption=f"Segmented Image with Overlay over Original Image", use_column_width=True,width=1600)
          os.remove(image_path)






if __name__ == "__main__":
    main()
