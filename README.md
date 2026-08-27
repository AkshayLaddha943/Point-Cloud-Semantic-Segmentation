# Point-Cloud-Semantic-Segmentation
Semantic Segmentation of KITTI Point Cloud Data using SqueezeSegV2

## Network Architecture of the CNN
**Input Tensor:** Point Cloud as a 2D image (Range View Representation)  
**Encoder:** Downsampling the Image  
**Decoder:** Upsampling of the Intermediate Representation  
**Skip Connections:** To preserve higher resolution information  
**Softmax Activation:** Compute Class probabilities for each point  
**Categorical Cross-Entropy:** Compute Classification Error  

**Training:** Trained with Gradient Descent

## Steps to Reproduce
- Jupyter Notebook (.ipynb) file is provided in order to customize and train your own model
- A saved model, trained against a subset of Semantic KITTI dataset is already provided in the models folder 
- Evaluated on the ROSbag data provided by RWTH Aachen University

## Results
