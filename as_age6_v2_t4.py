# -*- coding: utf-8 -*-
"""As_age6_v2_T4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UrziqUs7QbGTjvvgbtC5DMvDbttd7XOU

analysis classify for allergic1(allergic disease) using RF, CatBoost, and Logistic Regression models for subjects age (age) with adjacent variables (HE_ht (height), HE_wt (weight), HE_BMI (BMI), age_g (age), sex) and features (urban (residence)
ho_incm (income quartile)
D_1_1 (subjective health awareness)
L_BR_FQ (breakfast frequency)
out1 (frequency of eating out)
N_DIET (Meal therapy or not)
LS_1YR (Whether or not to take dietary supplements) ) and interpretate and  find risk factors

# Compare Machine Leraning Tools by PyCaret

1. Setup PyCaret:
"""

pip install pycaret

"""2. Import necessary libraries:"""

import pandas as pd
from pycaret.classification import *

"""3. Load and prepare your data:

"""

data = pd.read_csv('/content/drive/MyDrive/data_6age2.csv')
features = ['N_EN', 'N_CHO', 'N_PROT', 'N_FAT',
'N_SFA', 'N_CHOL', 'N_TDF', 'N_SUGAR', 'N_VA_RAE',
'N_NIAC', 'N_VITC', 'N_CA', 'N_PHOS', 'N_NA', 'N_K', 'N_FE',
'allergic1']
data = data[features]

"""4. Setup the PyCaret environment:

"""

clf1 = setup(data, target = 'allergic1', session_id=123,
             normalize = True, transformation = True,
             remove_multicollinearity = True, multicollinearity_threshold = 0.95)

"""5. Compare Models:

"""

compare_models(include = ['ridge', 'lda', 'gbc', 'ada', 'lightgbm', 'rf', 'et', 'lr', 'dummy',
                          'knn', 'dt', 'svm', 'qda', 'nb'])

"""6. Interpretation:

"""

# For instance, if the LightGBM model is the best:
model1 = create_model('lightgbm')
print(model1)

tuned_model1 = tune_model(model1)
print(tuned_model1)

"""7. Extracting Feature Importances:

"""

plot_model(tuned_model1, plot = 'feature')

"""8. Model Evaluation"""

plot_model(tuned_model1, plot = 'auc')

plot_model(tuned_model1, plot = 'confusion_matrix')

predict_model(tuned_model)

"""9. Model Deployment"""

from weakref import finalize

final_model1 = finalize_model(tuned_model1)
print(final_model1)

save_model(final_model1, 'Final LightGBM Model')

"""Other model

# 2. Random Forest
"""

model2 = create_model('rf')
print(model2)

plot_model(model2, plot = 'feature')

"""# 3. Extra Tree Classifier"""

model3 = create_model('et')
print(model3)

plot_model(model3, plot = 'feature')

"""# 4. Deision Trees Classifier"""

model4 = create_model('dt')
print(model4)

plot_model(model4, plot = 'feature')

"""# 5.Gradient Boosting Classifier"""

model5 = create_model('gbc')
print(model5)

plot_model(model5, plot = 'feature')

"""# Results"""

tuned_model = tuned_model2
plot_model(tuned_model, plot = 'auc')
plot_model(tuned_model, plot = 'confusion_matrix')
predict_model(tuned_model)

from weakref import finalize

final_model = finalize_model(tuned_model)
print(final_model)

save_model(final_model, 'Final Light GBM Model')

tuned_model = tuned_model3
plot_model(tuned_model, plot = 'auc')
plot_model(tuned_model, plot = 'confusion_matrix')
predict_model(tuned_model)

from weakref import finalize

final_model = finalize_model(tuned_model)
print(final_model)

save_model(final_model, 'Final Decision Tree Model')

tuned_model = tuned_model4
plot_model(tuned_model, plot = 'auc')
plot_model(tuned_model, plot = 'confusion_matrix')
predict_model(tuned_model)

from weakref import finalize

final_model = finalize_model(tuned_model)
print(final_model)

save_model(final_model, 'Final Extra Tree Model')

tuned_model = tuned_model5
plot_model(tuned_model, plot = 'auc')
plot_model(tuned_model, plot = 'confusion_matrix')
predict_model(tuned_model)

from weakref import finalize

final_model = finalize_model(tuned_model)
print(final_model)

save_model(final_model, 'Final K Neighbors Classifier Model')