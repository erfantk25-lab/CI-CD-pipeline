import json
from pathlib import Path
from sklearn.metrics import roc_auc_score
import numpy as np

# TEMPORÄRA TESTDATA – ersätt med din riktiga modell senare
y_true = np.array([0, 1, 1, 0, 1])
y_pred = np.array([0.1, 0.8, 0.7, 0.2, 0.9])

def save_metrics(y_true, y_pred):
    roc_auc = roc_auc_score(y_true, y_pred)

    # Skapa outputs-mappen om den inte finns
    Path("outputs").mkdir(exist_ok=True)

    # Skriv mätvärden till fil
    matvarden = {"roc_auc": roc_auc}

    with open("outputs/matvarden.json", "w") as f:
        json.dump(matvarden, f, indent=2)

    print("✔ matvarden.json skapad!")

# Kör funktionen
save_metrics(y_true, y_pred)

