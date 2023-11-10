import pandas as pd

data = {
    'age': [25, 30, 35, 40, 22, 28, 32, 45],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'smoker': ['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No']
}

dataset = pd.DataFrame(data)

data_types = dataset.dtypes
print("Tipos de datos en cada columna:")
print(data_types)

dataset['age'] = pd.to_numeric(dataset['age'], errors='coerce')

smoker_counts = dataset.groupby(['gender', 'smoker']).size().unstack().fillna(0)
print("\nCantidad de hombres y mujeres fumadores:")
print(smoker_counts)
