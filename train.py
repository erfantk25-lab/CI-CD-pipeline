import json
from pathlib import Path
from sklearn.metrics import roc_auc_score

def save_metrics(y_true, y_pred):
    roc_auc = roc_auc_score(y_true, y_pred)

    Path("outputs").mkdir(exist_ok=True)

    matvarden = {"roc_auc": roc_auc}

    with open("outputs/matvarden.json", "w") as f:
        json.dump(matvarden, f, indent=2)

    print("✔ matvarden.json skapad!")

# Exempel på hur du anropar funktionen:
# y_true = ...
# y_pred = ...
# save_metrics(y_true, y_pred)
