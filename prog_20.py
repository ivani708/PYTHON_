{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Wf5KrEb6vrkR"
      },
      "source": [
        "# Welcome to Colab!"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.datasets import load_iris\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report\n",
        "#load dataset\n",
        "iris = load_iris()\n",
        "X = iris.data\n",
        "Y = iris.target\n",
        "df=pd.DataFrame(X,columns=iris.feature_names)\n",
        "df[\"species\"]=iris.target\n",
        "print(df.head())\n",
        "print(\"Features Name : \", iris.feature_names)\n",
        "print(\"Target Data: \", iris.target)\n"
      ]