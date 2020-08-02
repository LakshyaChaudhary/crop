import flask
import pickle
import keras

# Use pickle to load in the pre-trained model.
with open(f'model/_Crop_Train_.pkl', 'rb') as f:
    modelCrop = pickle.load(f)

# with open(f'model/_Humidity_.pkl', 'rb') as f:
#     modelHumidity = pickle.load(f)

# with open(f'model/_NDVI_.pkl', 'rb') as f:
#     modelNDVI = pickle.load(f)

# with open(f'model/_Soil_Moisture_.pkl', 'rb') as f:
#     modelMoisture = pickle.load(f)

# with open(f'model/_Temp_.pkl', 'rb') as f:
#     modelTemp = pickle.load(f)


humidity = [0.008913,0.010115,0.009910,0.010643]


app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
    	year = flask.request.form['year']
    	# tpred_data = humidity.reshape((humidity.shape[0], humidity.shape[1], 1))
    	# humid2020 = modelHumidity.predict(humidity, verbose=0)
    	# print(humid2020)


if __name__ == '__main__':
    app.run()