from flask import Flask, render_template, request
from silk_worm import pred_silkworm_diseases
from silk_leaf import pred_leaf_diseases

from price import price_app  # import the price blueprint

app = Flask(__name__)

# Register the price blueprint
app.register_blueprint(price_app)

@app.route('/')
def index():
    return render_template('main_index.html')

@app.route('/team1')
def team1():
    return render_template('index_silk.html')

@app.route('/team2')
def team2():
    return render_template('index_leaf.html')

@app.route('/fla_k')
def fla_k():
    return render_template('silkworm_Flacheria_ka.html')

@app.route('/fla_e')
def fla_e():
    return render_template('silkworm_Flacheria.html')

@app.route('/gra_k')
def gra_k():
    return render_template('silkworm_Grasseria_ka.html')

@app.route('/gra_e')
def gra_e():
    return render_template('silkworm_Grasseria.html')

@app.route('/mus_k')
def mus_k():
    return render_template('silkworm_muscardin_ka.html')

@app.route('/mus_e')
def mus_e():
    return render_template('silkworm_muscardin.html')

@app.route('/pab_k')
def pab_k():
    return render_template('silkworm_pabrin_ka.html')

@app.route('/pab_e')
def pab_e():
    return render_template('silkworm_pabrin.html')


@app.route('/home')
def home():
     return render_template('signin.html')

@app.route('/Home')
def Home():
     return render_template('main_index.html')

@app.route('/Main')
def Main():
     return render_template('main.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/week1_k')
def week1_k():
    return render_template('week1_k.html')

@app.route('/week1')
def week1():
    return render_template('week1.html')

@app.route('/week2_k')
def week2_k():
    return render_template('week2_k.html')

@app.route('/week2')
def week2():
    return render_template('week2.html')

@app.route('/week3_k')
def week3_k():
    return render_template('week3_k.html')

@app.route('/week3')
def week3():
    return render_template('week3.html')

@app.route('/week4_k')
def week4_k():
    return render_template('week4_k.html')

@app.route('/week4')
def week4():
    return render_template('week4.html')

@app.route('/week5_k')
def week5_k():
    return render_template('week5_k.html')

@app.route('/week5')
def week5():
    return render_template('week5.html')

pages = {
    'week1': 'week1.html',
    'week2': 'week2.html',
    'week3': 'week3.html',
    'week4': 'week4.html',
    'week5': 'week5.html'
}

@app.route('/stage', methods=['GET', 'POST'])
def stage():
    if request.method == 'POST':
        user_input = request.form['input']
        if user_input in pages:
            return render_template(pages[user_input])
        else:
            return "Error: Page not found."
    else:
        return render_template('index_stage.html')

@app.route('/predict1', methods=['GET', 'POST'])
def predict1():
    if request.method == 'POST':
        file = request.files['image']
        file_path = 'static/uploads/' + file.filename
        file.save(file_path)
        pred, output_page = pred_silkworm_diseases(image_path=file_path)
        return render_template(output_page, pred_output=pred, user_image=file_path)
    return render_template('index_silk.html')

control = {
    'Leaf rust disease': [
        'Choose rust-resistant plant varieties.',
        'Remove and destroy infected plant debris.',
        'Practice crop rotation to disrupt the disease cycle.',
        'Monitor plants regularly for early detection of leaf rust.',
        '',
        'ಕನ್ನಡ',
        '',
        'ಹುಳು ಸಹಿಷ್ಣು ಸಸ್ಯ ಬಗ್ಗೆ ಆಯ್ಕೆ ಮಾಡಿ.',
        'ಹಾಳಾದ ಮರ ಭಾಗಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ನಾಶ ಮಾಡಿ.',
        'ರೋಗ ಚಕ್ರವನ್ನು ಭಂಗಿಸಲು ಬೆಳೆಯ ಬದಲಾವಣೆಗಳನ್ನು ಅನುಸರಿಸಿ.',
        'ಎಲೆ ಹುಳು ಸಮಯದಲ್ಲಿ ನಿಯಮಿತವಾಗಿ ಪರಿಶೀಲಿಸಿ.'
    ],
    'Leaf Spot Disease': [
        'Remove infected leaves and debris.',
        'Use appropriate chemicals.',
        'Avoid overwatering.',
        'Trim affected parts.',
        'Regular monitoring.',
        '',
        'ಕನ್ನಡ',
        '',
        'ಹಾಳಾದ ಎಲೆಗಳನ್ನು ಮತ್ತು ಅವುಗಳ ನಾಶಮಾಡಿ.',
        'ಯೋಗ್ಯ ರಸಾಯನಿಕ ದ್ರವ್ಯಗಳನ್ನು ಬಳಸಿ.',
        'ಅತಿ ಹೆಚ್ಚು ನೀರು ಹಾಕದಿರಿ.',
        'ಪ್ರಭಾವಿತ ಭಾಗಗಳನ್ನು ಕತ್ತರಿಸಿ.',
        'ನಿಯಮಿತವಾಗಿ ಪರಿಶೀಲಿಸಿ.'
    ],
    'Mulberry Stem Canker': [
        'Remove and destroy infected mulberry stems and leaves.',
        'Cut infected branches at least 20 cm below visible signs of infection.',
        'Maintain proper irrigation, fertilization, and spacing between trees.',
        'Avoid planting mulberry trees in previously infected areas.',
        'Consider using resistant or tolerant mulberry tree varieties.',
        '',
        'ಕನ್ನಡ',
        '',
        'ಹಾಳಾದ ಮಲ್ಬೆರಿ ನರಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ಎಲೆಗಳನ್ನು ನಾಶಮಾಡಿ.',
        'ಹಾಳಾದ ಶಾಖೆಗಳನ್ನು ದೃಷ್ಟಿಗೆ ಬರುವ ಹೊರಗೆ ಕಡಿಮೆಯಾದಷ್ಟು 20 ಸೆ.ಮೀ. ಕಡಿಮೆಯಾಗಿ ಕಡೆಗಣಿಸಿ.',
        'ಯಥಾವತ್ತಾಗಿ ನೀರಾವರಿ, ಉರ್ವರಕಗಳನ್ನು ಮತ್ತು ಮರಗಳ ನಡುವೆ ಸಂಘಟಿಸಿ.',
        'ಮುಂದುವರೆಯದಂತೆ ಮಲ್ಬೆರಿ ಮರಗಳನ್ನು ಹೊಂದಿಸುವ ಪ್ರದೇಶದಲ್ಲಿ ಮಲ್ಬೆರಿ ಮರಗಳನ್ನು ನೆಟ್ಟಗೆ ಹಾಕುವುದನ್ನು ಬಿಡಿಸಿ.',
        'ಹೊಸದಾಗಿ ಬಂದಿರುವುದನ್ನು ಅಥವಾ ತಾಳೆಯಾಗಿರುವುದನ್ನು ಬಳಸುವುದು ಪರಿಶೀಲಿಸಿ.'
    ],
    'Powdery Mildew': [
        'Rotate crops and avoid planting the same crop in the same location consecutively.',
        'Avoid overhead irrigation and keep leaves dry.',
        'Prune and remove infected plant parts regularly.',
        'Provide adequate spacing between plants to improve air circulation.',
        '',
        'ಕನ್ನಡ',
        '',
        'ಬೆಳೆಗಳನ್ನು ಪುನರಾವರ್ತಿಸಿ ಮತ್ತು ಅದೇ ಸ್ಥಳದಲ್ಲಿ ಸರಿಯಾದ ಬೆಳೆಯನ್ನು ನೆಡುವುದನ್ನು ವಿರೋಧಿಸಿ.',
        'ಮೇಲಿನ ನೀರಾವರಣವನ್ನು ತಡೆಹಿಡಿದು ಎಲೆಗಳನ್ನು ಒಣಗಿಸಿ ಇರಿಸಿ.',
        'ಹೋರಾಟ ಮಾಡಲು ಮತ್ತು ಹೊಂದಿದ ಸಸ್ಯ ಭಾಗಗಳನ್ನು ನಿರ್ಮೂಲಗೊಳಿಸಲು ನಿಯಮಿತವಾಗಿ ಕತ್ತರಿಸಿ.',
        'ಬೆಳೆಗಳ ನಡುವೆ ಸರಿಯಾದ ಹಂತವನ್ನು ಕಾಯುವಂತೆ ಸರಿಯಾದ ಅಂತರವನ್ನು ನೀಡಿ.'
    ],
    'Root Knot Disease': [
        'Remove and destroy infected plant residues to prevent nematode buildup.',
        'Incorporate organic matter to improve soil and indirectly suppress nematode populations.',
        'Cover the soil with plastic sheets during hot months to kill nematodes.',
        'Avoid overwatering to minimize nematode activity.',
        'Regularly check for root knot disease symptoms and take action promptly.',
        '',
        'ಕನ್ನಡ',
        '',
        'ಹಾಳಾದ ಬೆಳೆಯ ಮರಗಳ ಅವಶೇಷಗಳನ್ನು ತೆಗೆದುಹಾಕಲು ನೇಮತೋಡುಗಳ ಕುಟುಕುವುದನ್ನು ತಡೆಯಿರಿ.',
        'ಗಾಳಿಮಾರುಗಳ ಜನಸಂಖ್ಯೆಯನ್ನು ಹೆಚ್ಚಿಸಲು ಜೈವಿಕ ಪದಾರ್ಥಗಳನ್ನು ಸೇರಿಸಲು ಮಣ್ಣು ಮೇಲೆ ಸುಧಾರಿಸಿ.',
        'ಗರಿಗಳ ಮೂಲಕ ಬೆಳೆಗಳ ಕೆಳಗೆ ಪಾತ್ರಗಳನ್ನು ಹಾಕಿ ನೇಮತೋಡುಗಳನ್ನು ಕೊಲ್ಲಲು ಗೆದ್ದುಹಾಕಿ.',
        'ನೇಮತೋಡುಗಳ ಸಕ್ರಿಯತೆಯನ್ನು ಕಡಿಮೆಗೊಳಿಸಲು ಅತಿಯಾಗಿ ನೀರು ಹಾಕಬೇಡಿ.',
        'ರೂಟ್ ನಾಟ್ ರೋಗದ ಲಕ್ಷಣಗಳನ್ನು ನಿಯಮಿತವಾಗಿ ಪರಿಶೀಲಿಸಿ ತಕ್ಷಣ ಕ್ರಿಯೆ ಹಾಕಿ.'
    ],
    'leaf is healthy': []
}

@app.route('/predict2', methods=['GET', 'POST'])
def predict2():
    if request.method == 'POST':
        file = request.files.get('image')
        if not file:
            return render_template('index_leaf.html', error='No file uploaded')
        file_path = 'static/uploads/' + file.filename
        file.save(file_path)
        pred, output_page = pred_leaf_diseases(image_path=file_path)
        # If prediction isn't recognized (e.g. model not loaded), avoid KeyError
        if pred not in control:
            # Render the returned output_page without control messages
            return render_template(output_page, pred_output=pred, user_image=file_path)
        return render_template(output_page, pred_output=pred, c_m=control[pred], user_image=file_path)
    return render_template('index_leaf.html')

if __name__ == '__main__':
    app.run(debug=True)
