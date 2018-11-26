from flask import Flask, render_template, request
from sklearn.externals import joblib
import os

app = Flask(__name__, static_url_path='/static/')


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/predict_price', methods=['POST', 'GET'])
def predict_price():
    # get the parameters

    
    district = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    room_type = [0,0,0]

    input_room = request.form['room_type']
    input_district = request.form['district']
    
    
    ##here we will catch an input exception
    try:
        min_nights = int(request.form['min_nights'])
    except ValueError:
        min_nights = 2
    

    district_named = ['Le Plateau-Mont-Royal', 'Le Sud-Ouest', 'Ville-Marie', 
               'Rosemont-La Petite-Patrie', 'Verdun', 'Mercier-Hochelaga-Maisonneuve',
               'Cote-des-Neiges-Notre-Dame-de-Grace','Dorval','Montreal-Ouest',
               'Villeray-Saint-Michel-Parc-Extension','Outremont','Beaconsfield',
               "Baie-d'Urfe",'Mont-Royal','Saint-Leonard','Saint-Laurent','LaSalle',
               'Ahuntsic-Cartierville','Lachine','Cote-Saint-Luc',
               'Riviere-des-Prairies-Pointe-aux-Trembles','Westmount','Montreal-Nord',
               'Pierrefonds-Roxboro','Hampstead','Pointe-Claire','Anjou',
               'Dollard-des-Ormeaux','Kirkland',"L'Ile-Bizard-Sainte-Genevieve",
               'Montreal-Est','Sainte-Anne-de-Bellevue']
    
    district_named_numbered = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                               "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21",
                              "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]
    
    room_type_named = ['Private room', 'Entire home/apt', 'Shared room']
    room_type_named_numbered = ['private', 'entire', 'shared']
    
    index_room = room_type_named_numbered.index(input_room)
    room_type[index_room] = 1

    index_district = district_named_numbered.index(input_district)
    district[index_district] = 1
    search_result = []
    search_result += room_type
    search_result += district
    search_result.append(min_nights) 

    # load the model and predict
    model = joblib.load('model/forest100_regression.pkl')
    prediction = model.predict([search_result])
    predicted_price = prediction.round(1)[0]

    return render_template('results.html',
                           district = district_named[index_district],
                           room_type = room_type_named[index_room],
                           minimum_nights = min_nights,
                           predicted_price = "{:,}".format(predicted_price)
                           )


if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
