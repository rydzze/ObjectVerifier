# ObjectVerifier


## Original Author

This project is created and maintained by [rydzze](https://github.com/rydzze).


## Introduction

Pattern recognition is a process of using machine learning algorithms to classify input data into various objects, classes, or categories based on identifying patterns, features, or regularities within the data. This project addresses an operational challenge in a semiconductor and machine tooling contract manufacturer, which currently relies on a labour-intensive and error-prone manual stock counting process. The goal is to develop an automated parts recognition and counting system to improve stock management accuracy and efficiency. By leveraging pattern recognition techniques, the system will identify and count various parts from images, significantly reducing manual effort and errors.


## Problem Statements and Objectives

### Problem Statements
1. **Manual Stock Counting**:
   - The current process is labour-intensive and prone to errors, leading to inaccuracies in stock levels and part identification.
2. **Operational Inefficiency**:
   - Manual counting is time-consuming and inefficient, impacting overall operational efficiency.
3. **Error-Prone Identification**:
   - Human errors in part identification can lead to mismanagement of stock and resources.


### Objectives
1. **Develop Accurate Pattern Recognition System**:
   - Create a robust system for accurate part recognition and counting using PCA and machine learning models.
2. **User-Friendly Interface**:
   - Implement a simple and intuitive interface for users to upload images and visualize recognition results.
3. **Integrate Advanced Counting Algorithms**:
   - Use OpenCV and YOLOv8 to ensure accurate part counting and validate with various parts arrangements.


## Design Description and Implementation

The project uses PCA for dimensionality reduction and SVM and KNN for classification tasks, optimizing computational complexity and classifier efficiency. The system includes visualization of training and testing sets, comprehensive performance evaluation metrics, and model export in pickle format for easy deployment. A GUI developed with HTML, CSS, and JavaScript for the front end, and Python with the Django framework for the back end allows users to upload images and see classification results. The counting algorithm, implemented with OpenCV and YOLOv8, uses parameters like 24 epochs and image size of 1600 pixels, with training on Google Colab, ensuring effective model training and evaluation.


## Experiment Setup

High-resolution images were captured using a Canon EOS M50 Mark II and a SIGMA 50mm lens, with around 289 raw images collected for four distinct objects. A miniature studio with diverse backdrops and lighting conditions ensured effective pattern recognition. Each image was systematically tagged, and details were recorded for reproducibility. For recognition purposes, 55 images per object were selected and split into 60% training and 40% testing sets, following standard machine learning model training and testing procedures to ensure accurate system performance assessment.


## Sample Images of Objects for Recognition

<table>
  <tr>
    <td style="text-align: center;">
      <strong>Object 1</strong><br>
      <img src="https://github.com/rydzze/ObjectVerifier/assets/86187059/da4ab698-586b-41f9-80b3-61ee22007798" alt="Object 1" style="width: 100%;">
    </td>
    <td style="text-align: center;">
      <strong>Object 2</strong><br>
      <img src="https://github.com/rydzze/ObjectVerifier/assets/86187059/cd5db498-9209-48e7-854f-0a2bad09d22a" alt="Object 2" style="width: 100%;">
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">
      <strong>Object 3</strong><br>
      <img src="https://github.com/rydzze/ObjectVerifier/assets/86187059/255e2b8b-b532-42b9-9db9-5a4a1858b179" alt="Object 3" style="width: 100%;">
    </td>
    <td style="text-align: center;">
      <strong>Object 4</strong><br>
      <img src="https://github.com/rydzze/ObjectVerifier/assets/86187059/d8d85de2-15f5-4e29-9a69-0ce6087011fe" alt="Object 4" style="width: 100%;">
    </td>
  </tr>
</table>


## Performance Evaluation

### Support Vector Machine (SVM)
**Accuracy**: 0.875 (87.5%)

<table>
  <head>
    <td><strong>Classification Report</strong></td>
    <td><strong>Confusion Matrix</strong></td>
  </head>
  <tr>
    <td>
      <table>
        <thead>
          <tr>
            <th>Object</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>F1-Score</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>0.65</td>
            <td>1.00</td>
            <td>0.78</td>
          </tr>
          <tr>
            <td>2</td>
            <td>1.00</td>
            <td>0.56</td>
            <td>0.72</td>
          </tr>
          <tr>
            <td>3</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
          </tr>
          <tr>
            <td>4</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
          </tr>
        </tbody>
      </table>
    </td>
    <td style="text-align: center;">
      <img src="https://github.com/rydzze/ObjectVerifier/assets/86187059/77007959-b833-4db9-a75a-17e958be7418" alt="Confusion Matrix" style="width: 100%;">
    </td>
  </tr>
</table>

### K-Nearest Neighbours (KNN)
**Accuracy**: 0.693 (69.3%)

<table>
  <head>
    <td><strong>Classification Report</strong></td>
    <td><strong>Confusion Matrix</strong></td>
  </head>
  <tr>
    <td>
      <table>
        <thead>
          <tr>
            <th>Object</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>F1-Score</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>0.61</td>
            <td>0.70</td>
            <td>0.65</td>
          </tr>
          <tr>
            <td>2</td>
            <td>0.64</td>
            <td>0.56</td>
            <td>0.60</td>
          </tr>
          <tr>
            <td>3</td>
            <td>0.87</td>
            <td>0.57</td>
            <td>0.68</td>
          </tr>
          <tr>
            <td>4</td>
            <td>0.71</td>
            <td>1.00</td>
            <td>0.83</td>
          </tr>
        </tbody>
      </table>
    </td>
    <td style="text-align: center;">
      <img src="https://github.com/rydzze/ObjectVerifier/assets/86187059/c1e936dc-9d03-49be-b8de-1b77848f0850" alt="Confusion Matrix" style="width: 100%;">
    </td>
  </tr>
</table>


## User Interface

![image](https://github.com/rydzze/ObjectVerifier/assets/86187059/7eab54eb-04dc-435e-80de-559b13fb92b8)
![image](https://github.com/rydzze/ObjectVerifier/assets/86187059/ac1d676a-d979-408b-bbef-7f3c3fdd2265)


## DISCLAIMER

The counting algorithm is not fully developed as the YOLOv8 model was primarily built to detect objects. However, the best model from the training phase was exported and is available for further development. This model can serve as a foundation for enhancing the counting algorithm to achieve more accurate and reliable results in the future.


## Contributors

We'd like to give credit to the following contributors who have helped in the development of this project:

- [Muhammad Ariff Ridzlan](https://github.com/rydzze)
- [Muhammad Hafiz](https://github.com/IbnAsmuni)
- [Muhammad Sufi Kai](https://github.com/juniechuu)
- [Chew Jia Jun](https://github.com/JiaJun-Chew)


---

## [Google Drive Link](https://drive.google.com/drive/folders/1n7XPssmnlnPYAvxD96D1TJIbkQQjsiEm?usp=sharing) for Actual Project Files w/ ML Models
- **dataset.h5** can be found in `Parts Recognition` dir. 
- **pca.pkl**, **svm.pkl**, and **knn.pkl** can be found in `webapp/ml_models` dir.
