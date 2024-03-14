from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd

app = Flask(__name__)

city_coords = {
    'Melbourne': (-37.8136, 144.9631),
    'Geelong': (-38.1499, 144.3617),
    'Sydney': (-33.8688, 151.2093),
}

@app.route('/')
def home():
    return render_template('home.html', cities=city_coords.keys())

@app.route('/about')
def about():
    # 读取 CSV 文件
    df = pd.read_csv('lga_uv_vic.csv')
    # 转换为 JSON
    chart_data = df.to_json(orient='records')
    return render_template('about.html', chart_data=chart_data)

@app.route('/get_uv', methods=['POST'])
def get_uv():
    city = request.form.get('city')
    if city in city_coords:
        lat, lng = city_coords[city]
        uv_index = get_uv_index(lat, lng)
        return jsonify({'uv_index': uv_index})
    else:
        return jsonify({'error': 'City not found'})

def get_uv_index(lat, lng):
    url = "https://api.openuv.io/api/v1/uv"
    headers = {
        "x-access-token": "",
        "Content-Type": "application/json"
    }
    params = {
        'lat': lat,
        'lng': lng
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data['result']['uv']

if __name__ == '__main__':
    app.run(debug=True)
