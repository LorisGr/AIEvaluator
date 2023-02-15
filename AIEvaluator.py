import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.utils import check_array
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class AIEvaluator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("AI Evaluator")
        self.geometry("400x200")
        
        self.model = None
        self.X_test = None
        self.y_test = None
        
        self.load_model_button = tk.Button(self, text="Load Model", command=self.load_model)
        self.load_model_button.pack()
        
        self.load_data_button = tk.Button(self, text="Load Data", command=self.load_data)
        self.load_data_button.pack()
        
        self.evaluate_button = tk.Button(self, text="Evaluate", command=self.evaluate)
        self.evaluate_button.pack()
        
    def load_model(self):
        file_path = filedialog.askopenfilename()
        # Caricare il modello
        self.model = DecisionTreeClassifier()
        self.model.fit(X_train, y_train)
        
    def load_data(self):
        file_path = filedialog.askopenfilename()
        # Caricare i dati
        data = pd.read_csv(file_path)
        X = data.drop("label", axis=1)
        y = data["label"]
        self.X_test, _, self.y_test, _ = train_test_split(X, y, test_size=0.2, random_state=42)
        
    def evaluate(self):
        if self.model is None:
            messagebox.showerror("Error", "Please load a model first")
            return
        if self.X_test is None or self.y_test is None:
            messagebox.showerror("Error", "Please load data first")
            return
        # Valuta il modello sui dati di test
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        confusion = confusion_matrix(self.y_test, y_pred)
        messagebox.showinfo("Evaluation Results", "Accuracy: {}\nConfusion matrix:\n{}".format(accuracy, confusion))
