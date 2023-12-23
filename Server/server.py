from flask import Flask, request, jsonify,request
import util
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi"

@app.route('/predict_quality', methods=['POST'])
def predict_quality():
    va = float(request.form["volatile_acidity"]) 
    ca = float(request.form["citric_acid"]) 
    rs = float(request.form["residual_sugar"])  
    ch = float(request.form["chlorides"])  
    fsd = float(request.form["free_sulfur_dioxide"]) 
    tsd = float(request.form["total_sulfur_dioxide"]) 
    ph = float(request.form["ph"]) 
    su = float(request.form["sulphates"]) 
    al = float(request.form["alcohol"]) 

    
    response = jsonify({
        'estimated_quality': int(util.get_quality(va,ca,rs,ch,fsd,tsd,ph,su,al))
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Wine Quality Prediction...")
    util.load_saved_artifacts()
    app.run()