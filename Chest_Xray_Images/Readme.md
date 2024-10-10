# Chest X-Ray Images (Pneumonia) Classification

## Overview
This project focuses on the classification of chest X-ray images to detect pneumonia using deep learning techniques, specifically employing the VGG16 model. The dataset consists of chest X-ray images from pediatric patients, aimed at enhancing diagnostic accuracy in detecting pneumonia.

## Dataset Description
The dataset is organized into three folders:
- **train/**: Contains training images
- **test/**: Contains testing images
- **val/**: Contains validation images

Each folder includes subfolders for the two categories:
- **Pneumonia**
- **Normal**

### Dataset Statistics
- Total images: **5,863**
- Image format: JPEG
- Categories: **2** (Pneumonia/Normal)

The chest X-ray images were selected from retrospective cohorts of pediatric patients aged one to five years from the Guangzhou Women and Children’s Medical Center. All imaging was performed as part of the patients' routine clinical care.

### Quality Control and Grading
For the analysis of chest X-ray images, all radiographs were initially screened for quality, removing any low-quality or unreadable scans. Diagnoses for the images were graded by two expert physicians, and to minimize grading errors, a third expert reviewed the evaluation set.

## Acknowledgements
- **Data Source**: [Mendeley Data](https://data.mendeley.com/datasets/rscbjbr9sj/2)
- **License**: CC BY 4.0
- **Citation**: [Cell Journal Article](http://www.cell.com/cell/fulltext/S0092-8674(18)30154-5)

## Model Used
The project utilizes the **VGG16** model for classifying chest X-ray images into the categories of pneumonia and normal. VGG16 is known for its deep architecture and effective feature extraction capabilities, making it suitable for image classification tasks.

## Conclusion
This project demonstrates the application of deep learning in medical imaging, specifically focusing on the classification of pneumonia in chest X-ray images. By utilizing the VGG16 model, we aim to contribute to improving diagnostic processes and support healthcare professionals in making informed decisions.

![Chest X-Ray Example](insert_image_link_here)
