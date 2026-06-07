# Phishing Email Detection Model

A Scikit-learn based machine learning project that classifies emails as **Phishing** or **Safe** using textual content and simple URL or keyword-related features. Scikit-learn provides built-in tools for confusion matrices and classification workflows, and phishing email detection projects commonly use TF-IDF style text features with standard classifiers for this task.

## Features

- Train on a dataset of phishing and legitimate emails.[web:41]
- Extract textual features using TF-IDF vectorization.[web:41]
- Analyze simple manual indicators such as URL count, suspicious keywords, digits, exclamation marks, and uppercase ratio.
- Classify emails as `Phishing` or `Safe` using Logistic Regression.
- Display model accuracy and save a confusion matrix image using Scikit-learn metrics tools.[web:43][web:49]
- Includes an interactive CLI menu for testing custom email text.

## Project structure

```text
phishing-email-detection-model/
├── phishing_email_detection.py
├── sample_emails.csv
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/your-username/phishing-email-detection-model.git
cd phishing-email-detection-model
pip install -r requirements.txt
```

## Dataset format

The CSV dataset should contain these columns:

```text
email_text,label
"Verify your account immediately",Phishing
"Meeting scheduled for tomorrow",Safe
```

## Usage

Train with the bundled sample dataset:

```bash
python phishing_email_detection.py
```

Train with your own dataset:

```bash
python phishing_email_detection.py --dataset your_dataset.csv
```

Train and skip the interactive menu:

```bash
python phishing_email_detection.py --dataset your_dataset.csv --no-menu
```

## Output artifacts

After training, the script saves:
- `artifacts/phishing_model.joblib`
- `artifacts/metrics.json`
- `artifacts/confusion_matrix.png`

## Model workflow

1. Load phishing and safe email samples.
2. Split the dataset into training and testing sets.
3. Convert email text into TF-IDF features.
4. Extract manual email indicators such as URLs and suspicious keywords.
5. Train a Logistic Regression classifier.
6. Evaluate accuracy and confusion matrix.[web:43][web:49]
7. Predict whether new emails are `Phishing` or `Safe`.

## Example console output

```text
============================================================
       Phishing Email Detection Model Results
============================================================
 Accuracy         : 83.33%
 Training Samples : 9
 Testing Samples  : 3
 Confusion Matrix :
   [Phishing->Phishing, Phishing->Safe] = [1, 0]
   [Safe->Phishing, Safe->Safe]         = [0, 2]
============================================================
```

## Future improvements

- Add better URL domain analysis
- Use larger real-world datasets
- Compare multiple ML models
- Add email header analysis
- Build a GUI or Flask web interface

## Ethics note

This project is meant for cybersecurity education and defensive detection research. It should be used to analyze email content for safety, not to create phishing content or enable abuse.

## Author

**Pawan Kumar V**  
Cybersecurity Student | Machine Learning & Security Projects
