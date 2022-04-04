# Stroke Prediction
Stroke is the 2nd leading cause of death globally, responsible for approximately 11% of
total deaths. The given <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vQBkbBa7swoXVRNgWzDQDhAFZDp_MvcAPusdQkE7y_FcFVx0SjCvXY8uIbzmsbX6hvOWXL1AjLjzjDq/pub?output=csv">Dataset<a> is used to predict whether a patient is likely to get a
stroke based on the input parameters like gender, age, various diseases, and smoking
status.

<h3> Deployed the web app at this <a href = "https://share.streamlit.io/shrut26/stroke-prediction/main/app.py">link</a></h3>
<h2>Environment Set-up</h2>

  - Install [Anaconda](https://www.anaconda.com/products/distribution) python
  - Navigate to the cloned repository.
    ```
    cd <project_directory_name>     #   Stroke-Prediction
    ```
  - Create a new virtual environment and activate it.
    ```
    conda activate env
    ```
  - Use pip to install other dependencies from `requirements.txt`
    ```
    pip install -r requirements.txt
    ```
  - run the web app locally
    ```
    streamlit run app.py
    ```
