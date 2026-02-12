# 🧠 One Brain, Two Heads: A DeBERTa-Based Multi-Task Framework for Crime Detection on Twitter (X)

## 📌 Overview

---

Social media platforms such as **Twitter (now X)** generate massive volumes of real-time textual data related to crime, conflict, and public safety. However, tweets are often **short, noisy, and context-dependent**, making automated crime detection a challenging research problem.

This project introduces a **unified multi-task transformer framework** called:

---

> **🧠 One Brain, Two Heads**

The architecture leverages a **shared DeBERTa-v3-base encoder** with two parallel task-specific heads to simultaneously:

✅ Detect crime-related tweets (Binary Classification)
✅ Categorize crime into fine-grained sub-types (Multi-Class Classification)

Unlike many prior works, this approach is **fully text-only**, scalable, and does not rely on metadata or multimodal inputs.

---

## 🚀 Key Contributions

✔️ Novel **multi-task architecture** reducing error propagation
✔️ Hybrid dataset construction with **zero-shot labeling + human verification**
✔️ Weighted composite loss to address **class imbalance**
✔️ Transformer-based contextual modeling for noisy social media text
✔️ Achieved strong performance without auxiliary metadata

---

## 🏗️ Architecture: One Brain, Two Heads

**Shared Encoder ("Brain"):**

* DeBERTa-v3-base
* 12 transformer layers
* Hidden size: 768

**Parallel Expert Heads:**

### 🔹 Head A — Binary Detection

Predicts whether a tweet contains criminal intent.

* Dense Layer (768 → 1)
* Sigmoid activation
* Optimized using **Binary Cross-Entropy Loss**

---

### 🔹 Head B — Multi-Class Categorization

Identifies the specific crime type.

* Dense Layer (768 → 6)
* Softmax activation
* Optimized using **Focal Loss** to handle class imbalance

---

## ⚙️ Composite Loss Function

```
L_total = λ1 * L_BCE + λ2 * L_Focal
```

Where:

| Parameter | Value | Purpose                                 |
| --------- | ----- | --------------------------------------- |
| λ1        | 0.3   | Prevents majority class dominance       |
| λ2        | 0.7   | Prioritizes fine-grained classification |
| γ         | 2.0   | Focuses training on hard examples       |

---

## 📊 Dataset Construction Pipeline

A hybrid annotation framework was designed to ensure both **scalability and label quality**.

### Data Sources

* Public Tweets to Police India
* Crime Tweets Dataset
* How ISIS Uses Twitter
* Sexual Violence Dataset

### Preprocessing Steps

1. Data cleaning (URLs, emojis, duplicates removed)
2. Zero-shot labeling using **BART-large-MNLI**
3. Manual verification for low-confidence samples
4. SBERT embeddings + K-Means clustering for crime sub-types

---

## 🧾 Crime Categories

* Armed Combat & Weaponry
* Counter-Terrorism & Arrests
* Crimes Against Civilians
* Extremist Propaganda
* Sexual Violence

---

## 🧪 Experimental Setup

| Parameter           | Value                  |
| ------------------- | ---------------------- |
| Framework           | PyTorch + Hugging Face |
| Optimizer           | AdamW                  |
| Learning Rate       | 1e-5                   |
| Batch Size          | 16                     |
| Epochs              | 6                      |
| Scheduler           | Cosine with warm-up    |
| Max Sequence Length | 128                    |
| Dropout             | 0.3                    |

---

## 📈 Results

| Model             | Parameters | Binary Accuracy | Multi-Class Accuracy |
| ----------------- | ---------- | --------------- | -------------------- |
| BERTweet-Base     | 135M       | 85.82%          | 78.90%               |
| BERTweet-Large    | 355M       | 86.79%          | 80.04%               |
| ⭐ DeBERTa-v3-Base | 184M       | **87.30%**      | **80.08%**           |

👉 DeBERTa outperformed larger models, highlighting the strength of **disentangled attention** for nuanced crime-context understanding.

---

## 🔎 Error Analysis

The model showed:

✅ Near-perfect sensitivity for **Sexual Violence**
✅ Strong minority-class handling via Focal Loss

Primary confusion occurred between:

> Counter-Terrorism vs. Extremist Propaganda

— largely due to semantic overlap.

---

## 💻 Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
pip install -r requirements.txt
```

---

## ▶️ Usage

Example training workflow:

```bash
python train.py
```

Example inference:

```bash
python predict.py --text "Police arrested the suspect after the attack."
```

---

## ⚠️ Note on Models & Dataset

Large trained models and datasets are **not included** in this repository due to GitHub size limits.

👉 (Add Google Drive / HuggingFace link here)

---

## 🔮 Future Work

* Real-time streaming crime detection
* Multilingual transformer support
* Explainable AI for law enforcement
* Multimodal fusion with images/video

---

## 🎓 Research Impact

This work demonstrates that:

> **Text alone can support scalable, efficient, and reliable real-time crime monitoring.**

The proposed architecture provides a practical foundation for automated public-safety intelligence systems.

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome!

If you find this project useful, consider giving it a ⭐ on GitHub.
