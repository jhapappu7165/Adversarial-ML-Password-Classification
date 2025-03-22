import ML_Naive_Bayes as ml_nb
from joblib import load
import pandas as pd 

def load_and_preprocess_data(passwords):
    df = pd.DataFrame({'password': passwords})

    df['password_length'] = df['password'].apply(len)
    df['n_uppercase'] = df['password'].str.count(r'[A-Z]')
    df['n_lowercase'] = df['password'].str.count(r'[a-z]')
    df['n_digits'] = df['password'].str.count(r'[0-9]')
    df['n_special'] = df['password'].str.count(r'[^A-Za-z0-9]')
    df['has_uppercase'] = (df['n_uppercase'] > 0).astype(int)
    df['has_lowercase'] = (df['n_lowercase'] > 0).astype(int)
    df['has_digits'] = (df['n_digits'] > 0).astype(int)
    df['has_special'] = (df['n_special'] > 0).astype(int)    
    df['n_unique'] = df['password'].apply(lambda x: len(set(x)))    
    return df.drop(columns=['password']) #drop 'password' column before returning


def predict_password_strength(model, passwords, strength_labels):
    try:
        features = load_and_preprocess_data(passwords)
        predictions = model.predict(features)
        probabilities = model.predict_proba(features)

        results = pd.DataFrame({
            'Password': passwords,
            'Predicted Strength': [strength_labels[p] for p in predictions],
            'Confidence': [max(prob) * 100 for prob in probabilities]
        })

        for i, strength in strength_labels.items():
            results[f'{strength} Probability'] = probabilities[:, i] * 100

        return results
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("*****IMBALANCED MODEL*****")
    model = load('imbalanced_model.joblib') #DE-SERIALIZATION
    passwords = ['p@ssword', 'a', '1', 'ab', '12']
    strength_labels = {0: 'Weak', 1: 'Medium', 2: 'Strong'}
    results = predict_password_strength(model, passwords, strength_labels)
    print(results)

    test_df = load_and_preprocess_data(["ab", "12"])
    print('\n', '\n', test_df)



    print('\n', "BALANCED MODEL")
    model = load('balanced_model.joblib') #DE-SERIALIZATION
    passwords = ['p@ssword', 'a', '1', 'ab', '12']
    strength_labels = {0: 'Weak', 1: 'Medium', 2: 'Strong'}
    results = predict_password_strength(model, passwords, strength_labels)
    print(results)

if __name__ == "__main__":
    main()
