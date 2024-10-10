# Brain Tumor MRI Classification

## Overview
This project focuses on the early detection and classification of brain tumors using deep learning techniques, specifically leveraging the DenseNet121 model. The application of deep learning in medical imaging aims to enhance diagnostic accuracy and support timely treatment decisions.

## What is a Brain Tumor?
A brain tumor is a collection or mass of abnormal cells in the brain. The rigid structure of the skull means that any growth within this confined space can lead to increased pressure, potentially causing brain damage and posing life-threatening risks. Brain tumors can be classified as:
- **Cancerous (malignant)**
- **Noncancerous (benign)**

## Importance of the Subject
Early detection and accurate classification of brain tumors are crucial in the medical field. Improved diagnostic methods assist healthcare professionals in selecting the most effective treatment options, ultimately saving lives.

## Methods
Deep learning approaches have revolutionized health diagnosis, providing impactful solutions. According to the World Health Organization (WHO), accurate brain tumor diagnosis involves:
1. **Detection** of the tumor
2. **Location identification** within the brain
3. **Classification** based on malignancy, grade, and type

This project utilizes a Convolutional Neural Network (CNN)-based multi-task classification approach, allowing for simultaneous classification of brain MRI images across different tasks. Additionally, the model is capable of tumor location identification through segmentation techniques.

## About the Dataset
The dataset used in this project is a combination of the following three sources:
1. **Figshare**
2. **SARTAJ Dataset**
3. **Br35H**

This dataset contains **7023 images** of human brain MRI scans classified into four categories:
- **Glioma**
- **Meningioma**
- **No Tumor**
- **Pituitary Tumor**

**Note:** The "No Tumor" class images were sourced from the Br35H dataset. It was observed that the SARTAJ dataset had categorization issues for the glioma class images. Consequently, images from the SARTAJ dataset were removed and replaced with images from the Figshare site.

### Important Note on Image Size
Please be aware that the images in this dataset may vary in size. It is recommended to resize the images to a uniform size after preprocessing and removing any extra margins.

## Dataset Link
You can access the dataset on Kaggle: [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

## Model Used
The project employs the **DenseNet121** model for classifying brain MRI images into the aforementioned categories.

## Conclusion
This project illustrates the potential of deep learning in medical imaging, particularly in the realm of brain tumor detection and classification. By leveraging the capabilities of DenseNet121, we aim to contribute to the field of early diagnosis and enhance treatment methodologies for patients with brain tumors.
