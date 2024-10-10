# Instance Segmentation with Mask R-CNN

This project demonstrates how to perform instance segmentation using the Mask R-CNN model with a ResNet-50 backbone and Feature Pyramid Network (FPN) from the `torchvision` library. The model is pre-trained on the COCO dataset and is capable of detecting objects and segmenting each object instance in an image.

## Project Overview

Instance segmentation involves detecting objects in an image and creating a mask for each instance. In this project, we use the Mask R-CNN model to segment objects in an input image (in this example, a cat sitting on a laptop). The segmentation masks are then visualized using `matplotlib`.

<img src='https://github.com/alirezasaberi20/Deep-Learning-Projects/blob/main/InstanceSegmenta/cat_laptop.jpg' width=300>
<img src='https://github.com/alirezasaberi20/Deep-Learning-Projects/blob/main/InstanceSegmenta/cat_seg.png' width=300>

### Features:
- **Pre-trained Mask R-CNN Model:** The model is pre-trained on the COCO dataset and can be used for a variety of object detection and segmentation tasks.
- **Object Detection & Segmentation:** The model predicts bounding boxes, labels, and instance masks for detected objects.
- **Visualization:** The segmented masks are overlaid on the original image for visualization.

## Installation

To run this project, you need to install the required dependencies. You can install them using pip:

```bash
pip install torch torchvision matplotlib pillow
