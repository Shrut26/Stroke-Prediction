# Stroke Prediction
Stroke is the 2nd leading cause of death globally, responsible for approximately 11% of
total deaths. The given <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vQBkbBa7swoXVRNgWzDQDhAFZDp_MvcAPusdQkE7y_FcFVx0SjCvXY8uIbzmsbX6hvOWXL1AjLjzjDq/pub?output=csv">Dataset<a> is used to predict whether a patient is likely to get a
stroke based on the input parameters like gender, age, various diseases, and smoking
status.

<h3> Deployed the web app at this <a href = "https://share.streamlit.io/shrut26/stroke-prediction/main/app.py">link</a></h3>
<h2>Environment Set-up</h2>

  - Install [python](https://www.python.org/downloads/) 
  - The python libraries required to execute the code are enlisted below, run the following commands(for python 3) in command prompt(for Windows) to download the respective libraries(use pip instead of pip3 for python 2).
       - Numpy 
         
         ```
         pip3 install numpy
         ```
       - OpenCV
         
         ```
         pip install opencv-python
         ```
                  
         
       - Tensorflow
         
         ```
         pip install tensorflow
         ```
         
       - Keras
         ```
         pip install keras
         ```
       - Matplotlib
                  
         ```
         pip3 install matplotlib
         ```
      
  - Following files would be required to set-up the required environment for proper working of this project:
      - [yolov3 weights](https://pjreddie.com/media/files/yolov3.weights)
      - yolov3.cfg (file given in the repo)
      - coco.names (file given in the repo)
