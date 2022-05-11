## What is this repository for?

Welcome to the Neural-Lego repo!

This repo is used for developing COMP208 project, containing codes and related materials.

You can try the website via: [TRY ME](http://124.220.206.81/)

## Run it on Your Machine

- create conda env

```
conda create -n neural-lego python=3.8
```

- activate env

```
conda activate neural-lego
```

- install dependencies

```
pip install -r requirements.txt
```

- run the backend server

```
cd .\backend\
python manage.py runserver
```

- run the frontend

```
cd .\front\
npm install
npm run serve
```

- visit website

```
http://127.0.0.1:8000/
```

## Overview of Neural-Lego

As artificial intelligence advances, a rising number of people from various industries and research fields are keen to master deep learning (DL). Our project is tailored for all those AI enthusiasts, whether novices or specialists, allowing them to develop AI models without writing any code. Concretely, there are two key motives and features of our project. First, considering that constructing an AI model comes with a lot of repeatability and modularity, such as data preprocessing, network construction and result visualization, we facilitate users to build models by drawing a flowchart of the network topology via graphical interfaces instead of writing pythonic code. Next, we provide a modular AI programming community based on the core feature mentioned above, forming a technical discussion environment. In brief, our project is a web-based platform that assists users to better utilize and explore DL.

### Framework of Neural-Lego

![image](https://user-images.githubusercontent.com/67728009/167746738-89f1012e-492f-4268-8c5f-120e429f6855.png)

At the module level, Neural Lego is a platform that consists of the above components. 

#### Infrastructure layer
Infrastructure layer offers the foundation for code-free and end-to-end model training. Data Server provides an infrastructure for users to manage and retrieve train data. The trainer provides the flexibility to build deep learning algorithms. It also includes an Auto-ML module that allows flowcharts to be converted into PyTorch code and the model to be automatically trained. Model Manager provides functionalities related to model training such as model storage, hyperparameter storage, training result storage, etc. to facilitate model management. 

#### Workflow layer
Workflow layer covers the whole process of creating and training a model. Project initialization is to start a project. Model Creation focuses on build the neural network via the canvas by dragging the module we provided. After the neural network is built, Model training process will conduct validation check and model training and testing. In the end, the result of the training process is displayed by visualization.

#### Interface layer
Interface layer tries to present a user-friendly interface for the underlying system. The Project Management module gives users a simple way to manage projects. Model Creator is an intuitive interface that allows users to quickly develop neural networks and create stunning layouts. To accomplish the effectiveness of one-click training, the Model Trainer module provides a user-friendly hyperparameter setting interface and a simple training button.

## Project Plans

![gantt](https://user-images.githubusercontent.com/67728009/167746962-948bf230-0564-47c0-88c7-8567025f1a1d.jpg)

## Third-party Libraries
- For frontend framework, we used [vue.js](https://vuejs.org/)
- For backend framework, we used [Django](https://www.djangoproject.com/)
- For model construction, we used [PyTorch](https://pytorch.org/)
- For training results visualization, we used [sklearn](https://scikit-learn.org/stable/)
- For canvas function, we used [go.js](https://gojs.net/latest/index.html)
- We deployed our website on [Tencent Cloud](https://intl.cloud.tencent.com/)

## Contact Us

Any problems or suggestion, email pin.qian77@gmail.com

## License

This project is licensed under [GPL-3.0 License](https://github.com/pinqian77/neural-canvas/blob/main/LICENSE).
