#AI Evaluator

AI Evaluator is a Python application that allows you to load a trained machine learning model and evaluate its performance on a given dataset. The application provides a graphical user interface (GUI) built using the tkinter library, which allows you to easily load a model and a test dataset, and view the evaluation results.

Requirements
To run AI Evaluator, you need to have the following software installed on your system:

Python 3.x
NumPy
pandas
scikit-learn
tkinter
You can install these dependencies using pip, the Python package installer:

```
pip install numpy pandas scikit-learn tkinter 
```

Usage
To use AI Evaluator, follow these steps:

Clone the repository to your local machine.

Install the required dependencies (see above).

Open a terminal or command prompt and navigate to the directory containing the cloned repository.

Run the aievaluator.py script by typing the following command:

```
python aievaluator.py
```

The application window will open. Click the "Load Model" button to select a trained machine learning model. The model should be in the format supported by scikit-learn, such as a decision tree or a random forest.

Click the "Load Data" button to select a test dataset in CSV format. The dataset should contain one column for the target variable and one or more columns for the input features.

Click the "Evaluate" button to evaluate the model on the test dataset. The evaluation results, including the accuracy and confusion matrix, will be displayed in a message box.


Credits
This project was created by LorisGr. 
