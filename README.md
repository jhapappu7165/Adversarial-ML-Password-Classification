# 🔐 Adversarial Machine Learning for Password Strength Classification

Authors: [Pappu Jha](jhapappu.com.np), Hanzla Hamid

Advisor: [Dr. Nick Rahimi](https://sites.google.com/view/nickrahimi/home)

Mentors:  Mr. Oluseyi Olukola, [Mr. Ashim Dahal](https://ashimdahal.github.io)

This repository contains the code and resources used in our research on improving password strength estimation using adversarial machine learning techniques. The goal of the project is to develop robust models that can accurately classify passwords as weak, medium, or strong—even when they exhibit deceptive or adversarial patterns.

---

## 📌 Abstract

Passwords remain one of the most common methods for securing sensitive data in the digital age. However, weak password choices continue to pose significant risks to data security and privacy. This study aims to solve the problem by focusing on developing robust password strength estimation models using adversarial machine learning, a technique that trains models on intentionally crafted deceptive passwords to expose and address vulnerabilities posed by such passwords. We apply five classification algorithms and use two datasets - one with sample sizes of more than 670,000 to train the first three models (Random Forest, Logistic Regression, and Decision Tree) and another with more than 100,000 samples for the last two models (Naive Bayes and XGBoost) - to accommodate different kinds of passwords for training models. Results demonstrate that the adversarial training improves password strength classification accuracy by up to 20\% compared to traditional machine learning models. It highlights the importance of integrating adversarial machine learning into security systems to enhance their robustness against modern adaptive threats.

---

## 🧠 Algorithms Used

- Random Forest (RF)
- Logistic Regression (LOR)
- Naive Bayes (NB)
- Decision Tree (DT)
- XGBoost (XGB)

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Cross-validation performance
- Robustness to adversarial inputs

## 🔚 Conclusion

- This study demonstrated that adversarial machine learning can significantly improve the accuracy and robustness of password strength classification models, achieving up to 20% higher accuracy compared to traditional approaches.

- Future work will focus on generating controlled adversarial datasets, exploring deep architectures like Transformers, and evaluating model robustness using attack strategies such as FGSM and PGD.

## ⭐ Star This Repo

If you found this useful, please consider starring the repo to support the project!
