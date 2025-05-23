from flask import Flask, render_template, request, abort

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Katsayılar (örnek değerler)
    home_coef = 0.2         # kg CO2 / m²
    light_coef = 0.05       # kg CO2 / saat
    device_coef = 0.9       # kg CO2 / cihaz

    # Hesaplama formülü
    result = (size * home_coef) + (lights * light_coef) + (device * device_coef)
    return round(result, 2)  # Virgülden sonra 2 basamaklı yuvarla 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<size>')
def transportations(size):
    return render_template(
        'ulaşım.html', 
        size=size
    )

@app.route('/<size>/<lights>')
def nutritions(size, lights):
    return render_template(
        'beslenme.html',                           
        size=size, 
        lights=lights                           
    )

@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    try:
        size = int(size)
        lights = int(lights)
        device = int(device)
    except ValueError:
        abort(400)  # Geçersiz veri varsa kullanıcıya hata göster

    result = result_calculate(size, lights, device)

    return render_template(
        'end.html',                           
        size=size, 
        lights=lights,
        device=device,
        result=result  # <<<< önemli: result şablona gönderiliyor
    )

if __name__ == '__main__':
    app.run(debug=True)
