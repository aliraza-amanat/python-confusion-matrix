"""
Monosnap Confusion Matrix
"""
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# Read keywords.csv and reference.csv
keywords_df = pd.read_csv('keywords-reran.csv')
reference_df = pd.read_csv('reference.csv')

# Create a set of reference object keys for faster lookup
reference_set = set(reference_df['object_key'])


# Function to check if an object key is in the reference set
def is_reference(object_key):
    return 1 if object_key in reference_set else 0


# Apply the is_reference function to create the 'reference' column
keywords_df['reference'] = keywords_df['object_key'].apply(is_reference)

# Calculate confusion matrix
conf_matrix = confusion_matrix(keywords_df['has_keyword'], keywords_df['reference'])

# Extract values from confusion matrix
true_pos = conf_matrix[1, 1]
false_pos = conf_matrix[0, 1]
true_neg = conf_matrix[0, 0]
false_neg = conf_matrix[1, 0]

# Create DataFrame for confusion matrix
confusion_matrix_df = pd.DataFrame({
    'true pos': [true_pos],
    'false pos': [false_pos],
    'true neg': [true_neg],
    'false neg': [false_neg]
})

# Save confusion matrix to CSV
confusion_matrix_df.to_csv('confusion_matrix_summary.csv', index=False)

# Output confusion matrix
print("Confusion Matrix:")
print(confusion_matrix_df)

# Plot confusion matrix
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(2)
plt.xticks(tick_marks, ['Actual 0', 'Actual 1'], rotation=45)
plt.yticks(tick_marks, ['Predicted 0', 'Predicted 1'])
plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.savefig('confusion_matrix_plot.png')

plt.show()
