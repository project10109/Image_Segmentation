
# import streamlit as st
# from PIL import Image
# from keras_segmentation.pretrained import pspnet_50_ADE_20K 
# import cv2

# from PIL import Image

# def main():
#     """Main function of the Streamlit app."""
#     import streamlit as st
#     import os
#     # Title and description
#     st.title("Image Segmentation App")
#     import streamlit as st

#     model1 = pspnet_50_ADE_20K() # load the pretrained model trained on ADE20k dataset
#     # Create a container for the side header
#     side_header = st.container()

#     # Use a nested container for better styling
#     with side_header.container():
#         # Employ st.sidebar for side positioning
#         st.sidebar.header("Upload an image to see its segmentation")

#         # # File upload element within the sidebar
#         image_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

        
#         if image_file is not None:
#             orig_image = Image.open(image_file)
#             st.header("Original Image")
#             st.image(orig_image, caption="Original Image", use_column_width=True)
#             im = orig_image.save('input.jpg')

#             img = cv2.imread('input.jpg')

#             if st.button('Perform Image Segmentation'):

#                 out = model1.predict_segmentation(inp=img,overlay_img=True,out_fname="dataset1/images_prepped_test/image__output.png")
#                 out_nonoverlay = model1.predict_segmentation(inp=img,overlay_img=False,out_fname="dataset1/images_prepped_test/image__nonoverlay_output.png")




#     # Define allowed image folder path
#     image_folder = '/Users/dhanashreekarande/Desktop/SSIT Projects/image_segmentation/dataset1/images_prepped_test/'
#     output_filename='image__output.png'

#     output_filename_nonoverlay='image__nonoverlay_output.png'

#     if output_filename_nonoverlay and output_filename_nonoverlay.endswith(('.jpg', '.png', '.jpeg')):
#       image_path = os.path.join(image_folder, output_filename_nonoverlay)
#       print('image_path',image_path)
#       if os.path.exists(image_path):
#           out_image = Image.open(image_path)
#           st.subheader("Segmented Image ")
#           st.image(out_image, caption=f"Segmented Image ", use_column_width=True,width=1600)
#           os.remove(image_path)

#     if output_filename and output_filename.endswith(('.jpg', '.png', '.jpeg')):
#       image_path = os.path.join(image_folder, output_filename)
#       print('image_path',image_path)
#       if os.path.exists(image_path):
#           out_image = Image.open(image_path)
#           st.subheader("Segmented Image with Overlay over Original Image")
#         #   st.image(out_image, caption=output_filename, use_column_width=True)
#           st.image(out_image, caption=f"Segmented Image with Overlay over Original Image", use_column_width=True,width=1600)
#           os.remove(image_path)


# if __name__ == "__main__":
#     main()




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
    import streamlit as st
    from streamlit_option_menu import option_menu

    model1 = pspnet_50_ADE_20K() # load the pretrained model trained on ADE20k dataset
    # Create a container for the side header
    
    with st.sidebar:
        
        selected = option_menu('Image Segmentation',

                              ['About Project',
                               'Project Contributors',
                               'Image Segmentation'
                                ],
                              icons=['activity','activity','activity'],
                              default_index=0)

    if (selected == 'About Project'):
    # page title
      st.title("Image Segmentation App")
      
      st.markdown('## Problem Statement :')

      st.markdown('##### The goal of semantic image segmentation is to categorise each pixel in an image such that it may be separated into several items that are distinct from one another and the backdrop.')


#      st.markdown('## Aim of the project lies in the meticulous dissection of a digital image into semantically meaningful regions.')
      st.markdown('## Objective')
      st.markdown('##### This image segmentation project tackles the challenge of intelligently dividing images into distinct regions. By leveraging cutting-edge computer vision techniques, we aim to accurately separate objects, backgrounds, or specific features within an image.')

      
      #Applications
      st.markdown('## Applications')

      st.markdown ('### 1.Medical Images')
      st.markdown ('##### Automated segmentation of body scans can help doctors to perform diagnostic tests. For example, models can be trained to segment tumor.')
      
      st.markdown ('### 2.Autonomous vehicles')
      st.markdown ('##### Autonomous vehicles such as self-driving cars can benefit from automated segmentation where cars can detect drivable regions or perform obstacle detection.')
      
      st.markdown ('### 3.Satellite image analysis')
      st.markdown ('##### Aerial images can be used to segment different types of land. Automated land mapping can also be done.')


    if (selected == 'Project Contributors'):
      st.markdown("# 1. Muskan Tahiliani")
      st.markdown("# 2. Vivek karnewar")
      st.markdown("# 3. Ziyan Ali")
      st.markdown("# 4. Karan ghugal")
      st.markdown("# 5. Ameera Siddiqui")

    if (selected == 'Image Segmentation'):

      # side_header = st.container()

      # Use a nested container for better styling
      # with side_header.container():
          # Employ st.sidebar for side positioning
      st.title('Image Segmentation')
      st.markdown("### Upload an image to see its segmentation")

      # # File upload element within the sidebar
      image_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

      
      if image_file is not None:
          orig_image = Image.open(image_file)
          st.header("Original Image")
          st.image(orig_image, caption="Original Image", use_column_width=True)
          im = orig_image.save('input.jpg')

          img = cv2.imread('input.jpg')

          if st.button('Perform Image Segmentation'):

              out = model1.predict_segmentation(inp=img,overlay_img=True,out_fname="dataset1/images_prepped_test/image__output.png")
              out_nonoverlay = model1.predict_segmentation(inp=img,overlay_img=False,out_fname="dataset1/images_prepped_test/image__nonoverlay_output.png")




      # Define allowed image folder path
      image_folder = '/Users/dhanashreekarande/Desktop/SSIT Projects/image_segmentation/dataset1/images_prepped_test/'
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




