from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('Flood_Predictor.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/Flood-predict', methods=['POST'])
def predict_flood():
    try:
        data = request.get_json()

        feature_vector = data['feature_vector']

        prediction = model.predict([feature_vector])
        print(prediction)

        response = {'prediction': prediction[0]}

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
   app.run(default=True)



