# model saving/loading

The data is from https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data

After simple preprocessing from the original `Wine.csv` into `wine_data.csv`:

    ...
    columns = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash',
     'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
     'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
    wine_data = pd.read_csv('Wine.csv', names=columns)
    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    wine_data['Class'] = le.fit_transform(wine_data['Class'])
    wine_data.to_csv('wine_data.csv', index = False)
    ...
    