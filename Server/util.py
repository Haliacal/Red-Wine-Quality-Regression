import pickle
import numpy as np
__model = None

def get_quality(*inputs):
    return __model.predict([np.array(inputs)])[0]


def load_saved_artifacts():
    print("Loading Artifacts...")
    global __model

    with open("Server/artifacts/wine_quality_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Artifacts loaded !!")

if __name__ == "__main__":
    load_saved_artifacts()
    print(predict_quality(0.70,0.00,1.9,0.076,11.0,34.0,3.51,0.56,9.4))