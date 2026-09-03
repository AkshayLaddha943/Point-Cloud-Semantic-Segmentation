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
- A saved model, is already provided in the models folder for reference
- Evaluated on the ROSbag data provided by RWTH Aachen University

## Training
The model was trained for 10 epochs on Semantic KITTI Dataset featuring 28 classes.

| Model                                                                  | size<br><sup>(pixels)</sup> | mAP<sup>val<br>50-95</sup> | mAP<sup>val<br>50-95(e2e)</sup> | Speed<br><sup>CPU ONNX<br>(ms)</sup> | Speed<br><sup>T4 TensorRT10<br>(ms)</sup> | params<br><sup>(M)</sup> | FLOPs<br><sup>(B)</sup> |
| ---------------------------------------------------------------------- | --------------------------- | -------------------------- | ------------------------------- | ------------------------------------ | ----------------------------------------- | ------------------------ | ----------------------- |
| [SqueezeSegV2](https://platform.ultralytics.com/ultralytics/yolo26/yolo26n) | 640                         | 40.9                       | 40.1                            | 38.9 ± 0.7                           | 1.7 ± 0.0                                 | 2.4                      | 5.5                     |


## Results
