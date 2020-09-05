import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

class Anonimizer:
    def _fit_discrete(self, column, data):
        le = LabelEncoder()
        le.fit(data)

        return {
            "name": column,
            "encoder": le,
            "model": True
        }

    def _transform_discrete(self, column_meta, data):
        encoder = column_meta['encoder']
        return encoder.transform(data).reshape(-1, 1)

    def _meta_non_discrete(self, column):
        return {
            "name": column,
            "encoder": None
        }

    def fit(self, data, cat_cols: list()):
        self.meta_list = []
        self.cat_cols = cat_cols

        for column in data.columns:
            column_data = df[[column]].values
            if column in self.cat_cols:
                print(f"{column} label_encoded")
                meta = self._fit_discrete(column=column, data=column_data)
                self.meta_list.append(meta)
            else:
                print(f"{column} will stay as is")
                meta = self._meta_non_discrete(column=column)
                self.meta_list.append(meta)

    def transform(self, data):
        values = []
        for meta in self.meta_list:
            if 'model' in meta:
                column_data = data[[meta['name']]].values
                print("transforming column ", meta['name'])
                values.append(self._transform_discrete(meta, column_data))
            else:
                if 'name' in meta:
                    column_data = data[[meta['name']]].values
                    values.append(column_data)

        data = np.concatenate(values, axis=1)

        return data

    def save_model(self, path):
        """Pickles the meta_list and writes it to disk
        """

        pickle.dump(self.meta_list, open(path, 'wb'))

    def load_model(self, path):
        self.meta_list = pickle.load(open(path, 'rb'))
