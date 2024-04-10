import numpy as np
import pandas as pd
from keras.models import load_model
from joblib import load

def make_prediction(param1, param2, param3, param4, param5, param6):
    model_loaded = load_model(param6)
    user_input = convert_input(param1, param2, param3, param4, param5)
    prediction = pred(user_input, model_loaded)
    return prediction

def convert_input(param1, param2, param3, param4, param5):

    data = {
    'race_progress': [param1],
    'remaining_pit_stops': [param2],
    'location': [param3],
    'change_compound': [param4],
    'number_of_available_compounds': [param5]
    }

    #Create dataframe
    user_input = pd.DataFrame(data)

    # Load the scaler
    scaler = load('scaler.joblib')

    # Load the encoder
    encoder = load('encoder.joblib')

    # Separate categorical and numerical features
    cat_features = ['remaining_pit_stops', 'location', 'change_compound', 'number_of_available_compounds']
    num_features = ['race_progress']

    # Perform preprocessing on numerical features
    user_input[num_features] = scaler.transform(user_input[num_features])

    # Perform preprocessing on categorical features
    user_input_encoded = encoder.transform(user_input[cat_features])

    # Combine preprocessed numerical and categorical features
    user_input_processed = np.concatenate((user_input_encoded, user_input[num_features]), axis=1)

    return user_input_processed

def decode_prediction(user_input):
    # Load the saved models
    scaler = load('./scaler.joblib')
    encoder = load('./encoder.joblib')
    
    sample = user_input.reshape(29,1)
    print(sample)
    # Determine the size of the encoded categorical data the number of columns the encoder transforms the data into
    num_categorical_features = encoder.transform([['dummy'] * 4]).shape[1]

    # Separate the encoded categorical and numerical parts of the sample
    sample_encoded_cat = sample[:num_categorical_features]
    sample_num = sample[num_categorical_features:]

    print("sample num: ", sample_num)

    # Reshape numerical part to fit scaler's expected input dimensions
    sample_num = sample_num.reshape(1, -1)

    # Inverse transform the numerical part
    sample_num_original = scaler.inverse_transform(sample_num)

    # Inverse transform the categorical part
    # We need to reshape the sample_encoded_cat to match the encoder's expected shape
    sample_encoded_cat = sample_encoded_cat.reshape(1, -1)
    sample_cat_original = encoder.inverse_transform(sample_encoded_cat)

    # Combine the decoded numerical and categorical parts
    decoded_pred = np.concatenate((sample_cat_original.flatten(), sample_num_original.flatten()), axis=0)

    # decoded_sample should contain the original values
    labels = ['Number of remaining pit stops:', 'Location:', 'change Compound:', 'Number of available compounds:', 'Race progression:']
    print('')

    # Display each label with its corresponding data value
    for label, value in zip(labels, decoded_pred):
        print(f"{label} {value}")

    return decoded_pred

def pred(user_input, model_loaded):

    label_encoder = load('label_encoder.joblib')

    # Make a prediction
    predicted_compound_encoded = model_loaded.predict(user_input)
    predicted_compound = np.argmax(predicted_compound_encoded, axis=1)

    # Assuming label_encoder is loaded or available from the training phase
    predicted_compound_label = label_encoder.inverse_transform(predicted_compound)
    predicted_compound_label = predicted_compound_label[0]
    return predicted_compound_label

