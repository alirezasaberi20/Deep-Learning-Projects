## Dataset Description

### Overview

The dataset used in this project is the **RSI-CB256 Satellite Image Classification Dataset**, which is designed for classifying satellite imagery. It contains satellite images from a variety of sources, including different sensors and Google Maps snapshots, and is divided into **four distinct classes**. This dataset has been curated to advance research in **remote sensing (RS)** and provide a robust foundation for developing and testing image interpretation algorithms.

### Dataset Context

In recent years, the field of **remote sensing image interpretation** has seen significant progress, driven by the need for **automatic interpretation of satellite images**. As the availability of RS images increases, there is a growing demand for intelligent systems that can analyze these images effectively. This dataset serves as a benchmark to address those needs, allowing researchers to develop and refine models for RS image classification.

### Data Content

The RSI-CB256 dataset plays a critical role in advancing the development of **intelligent algorithms** for RS image analysis, specifically for **scene classification**. Each image in the dataset is labeled into one of four distinct classes, which helps build deep learning models capable of distinguishing between different satellite image types. The diverse origins of the images—from various **satellite sensors** and **Google Maps snapshots**—ensure a rich variety of visual data.

### Relevance to Project

In my project, I utilized this dataset to build and train a deep learning model for classifying satellite images into one of the four categories. I used a **pretrained DenseNet121 model** to leverage its powerful feature extraction capabilities. By fine-tuning the final layers of this model, I was able to achieve a robust and accurate classification system that generalizes well across different types of satellite imagery.

### Model Used

The **DenseNet121** model was chosen for its efficiency in handling complex image classification tasks. Using a pretrained version of DenseNet121, I froze the base layers and fine-tuned the fully connected layers to adapt to the specific classes in the RSI-CB256 dataset. This approach significantly improved the performance and training time.

### Dataset Link

The dataset can be found [here](https://www.kaggle.com/datasets/mahmoudreda55/satellite-image-classification) on Kaggle.

