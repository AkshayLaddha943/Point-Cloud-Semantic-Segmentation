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
- The eval workspace validates the trained model on a rosbag file provided by RWTH Aachen University
- A saved model, is already provided in the models folder for reference

## Training
The model has been trained for 20 epochs on Semantic KITTI Dataset featuring 11 classes.

| Model                                                                  | width x height | epochs | loss | miou | params<br><sup>(M)</sup> | FLOPs<br><sup>(B)</sup> |
| ---------------------------------------------------------------------- | --------------------------- | -------------------------- | ------------------------------- | ------------------------------------ | ----------------------------------------- | ------------------------ | ----------------------- |
| [SqueezeSegV2](https://platform.ultralytics.com/ultralytics/yolo26/yolo26n) | 240 x 32                         | 20                      | 40.1                            | 38.9 ± 0.7                           | 1.7 ± 0.0                                 | 2.4                      | 5.5                     |


## Results
