
import streamlit as st
import cv2
import numpy as np


st.header('''
Autonomous System Enabling Node and Edge Detection, Path Optimization, and Effective Color-coded Box Management in Diverse Robotic Environments
''')
st.subheader('By Deeksha Jayanth & Chetna Mundra')

def load_image(file_path):
    img = cv2.imread(file_path)
    if img is None:
        st.warning(f"Error loading {file_path}. Using a placeholder image.")
        img = placeholder_image()
    return img

def placeholder_image():
    # Create a placeholder image (you can customize this based on your needs)
    return np.full((100, 100, 3), 255, dtype=np.uint8)

# File paths
img1_path = r"hd.jpg"
img2_path = r"hd1.png"
img3_path = r"hd4.png"

# Load images
img1 = load_image(img1_path)
img2 = load_image(img2_path)
img3 = load_image(img3_path)

# Display images
st.subheader("Input Images")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(img1, caption="Original Map", width=None)

with col2:
    st.image(img3, caption="Different Areas", width=None)

with col3:
    st.image(img2, caption="Packages", width=None)

st.subheader("Input and Output")
video_path = "Untitled design.mp4"
col1,col2 = st.columns([500,100])
# Display the video with CSS styling
with col1:
    st.video(video_path, format="video/mp4", start_time=0)
         

st.subheader("Methodology")
st.subheader("1. Node Detection")
cols1, cols2, cols3, cols4 = st.columns(4)

node1= load_image('colormapped (5).png')
node2= load_image('colormapped (6).png')
node3= load_image('colormapped (7).png')
node4= load_image('colormapped (8).png')
with cols1:
    st.image(node1, caption="Blurred", width=None)
with cols2:
    st.image(node2, caption="Dialated", width=None)
with cols3:
    st.image(node3, caption="Canny", width=None)
with cols4:
    st.image(node4, caption="Dialated 2", width=None)

st.subheader("2. Edge Detection & Weights of Edges")
cols1, cols2, cols3, cols4 = st.columns(4)

edge1= load_image('colormapped (9).png')
edge2= load_image('colormapped (10).png')
edge3= load_image('colormapped (11).png')
edge4= load_image('colormapped (12).png')
with cols1:
    st.image(edge1, caption="Blurred", width=None)
with cols2:
    st.image(edge2, caption="Dialated", width=None)
with cols3:
    st.image(edge3, caption="Canny", width=None)
with cols4:
    st.image(edge4, caption="Dialated 2", width=None)

st.subheader("3. Mapping of Nodes and Edges")
cols1, cols2, cols3 = st.columns(3)

map1= load_image('map1.png')
map2= load_image('map2.png')
map3= load_image('map3.png')

with cols1:
    st.image(map1, caption="Coordinates of Nodes", width=None)
with cols2:
    st.image(map2, caption="Weights of Edges", width=None)
with cols3:
    st.image(map3, caption="Indexing Of Graph", width=None)

st.subheader("4. Tracking HSV Values and Mapping Different Areas")
cols1, cols2, cols3 = st.columns(3)

map1= load_image('slide3.png')
map2= load_image('hd4.png')
map3= load_image('colormapped (1).png')

with cols1:
    st.image(map1, caption="Different Areas", width=None)
with cols2:
    st.image(map2, caption="Input Map", width=None)
with cols3:
    st.image(map3, caption="Areas Identified", width=None)

st.subheader("5. Tracking Different boxes")
cols1, cols2, cols3 = st.columns(3)

map1= load_image('slide4.png')
map2= load_image('hd1.png')
map3= load_image('colormapped (4).png')

with cols1:
    st.image(map1, caption="Different Boxes", width=None)
with cols2:
    st.image(map2, caption="Input Map", width=None)
with cols3:
    st.image(map3, caption="Boxes Identified", width=None)

st.subheader("6. Sample Mapping ")
st.text("{'manufacturing unit': {3: 'blue', 5: 'blue', 16: 'green', 30: 'red'}, 'drop off': {17: 'green', 18: 'red', 31: 'blue'}, 'collection area': {19: 'green', 20: 'blue', 32: 'blue', 33: 'red'}")

st.subheader("7. Ordered List in which Nodes need to be visited")
st.write("- Floyd-Warshal Algorithm - List is made in which order boxes should be picked up and dropped off.")
st.write("- BFS Traversal - Traverses the above list in pairs of destination and source, collects the nodes and path to be taken and finds the shortest path once it matches the weight from above algorithm.")
st.write("- For each of the pairs, from the given 8 possible ways to provide directions, It is provided from the table by using simple maths.")
st.write('- For curved regions, the direction is simply changed using the same table twice. ')

st.subheader("8. Giving Directions to the Bot & Curved Edges")
st.image('colormapped (3).png', caption="Table to give Directions", width=None)
cols1, cols2, cols3 = st.columns(3)

img1= load_image('dir.png')
img2= load_image('ce1.png')
img3= load_image('ce2.png')

# Display images in the same row with equal height and responsive width
col1, col2, col3 = st.columns([450, 250, 250])

with col1:
    st.image(img1, caption="All Possible Directions",width=None)

with col2:
    st.image(img2, caption="Curved Edges", width=None)

with col3:
    st.image(img3, caption="Special Case", width=None)

st.subheader("Comparison With Existing Methods")
st.image('Web_Photo_Editor (1).jpg', caption="Using Hough Transformations and Clustering Nodes and Edges",width=None)

st.subheader("Conclusion and Future Scope")
st.text('''
The proposed autonomous system utilizes computer vision and advanced technologies 
to enhance operational efficiency in diverse settings, including warehouses, 
factories, and outdoor spaces. Its adaptability and potential for expansion make 
it a versatile solution for precise node identification, edge recognition, and 
task prioritization, promising innovation beyond traditional applications.''')
