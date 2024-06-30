from flask import *
from MRC import *
from FED import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(cam(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/recommends', methods=['POST'])
def recommends():
    mood = print_label()
    arr = recommend(mood,10)
    name = arr[0]
    artist = arr[1]
    link = arr[2]
    return render_template('recommendations.html',mood=mood,name=name,artist=artist,link=link)

@app.route('/neutral')
def neutral():
    arr = recommend('Neutral',25)
    name = arr[0]
    artist = arr[1]
    link = arr[2]
    return render_template('neutral.html',mood='Neutral',name=name,artist=artist,link=link)

@app.route('/sad')
def sad():
    arr = recommend('Sad',25)
    name = arr[0]
    artist = arr[1]
    link = arr[2]
    return render_template('sad.html',mood='Sad',name=name,artist=artist,link=link)

@app.route('/angry')
def angry():
    arr = recommend('Angry',25)
    name = arr[0]
    artist = arr[1]
    link = arr[2]
    return render_template('angry.html',mood='Angry',name=name,artist=artist,link=link)

@app.route('/happy')
def happy():
    arr = recommend('Happy',25)
    name = arr[0]
    artist = arr[1]
    link = arr[2]
    return render_template('happy.html',mood='Happy',name=name,artist=artist,link=link)

if __name__ == '__main__':
    app.run(debug=True)