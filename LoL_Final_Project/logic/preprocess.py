from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.compose import make_column_selector
from sklearn.pipeline import make_pipeline

def preprocess(df):

    # Preprocess data to make ready for training model

    num_transformer = StandardScaler()
    cat_transformer = OneHotEncoder(handle_unknown='ignore',sparse=True)

    preproc = make_column_transformer(
        (num_transformer, make_column_selector(dtype_include=['int64', 'float64'])),
        (cat_transformer, make_column_selector(dtype_include=['object','bool'])),
        remainder='passthrough'
    )

    pipe = make_pipeline(preproc)

    X = pipe.fit_transform(df)

    return X
