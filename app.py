from flask import Flask, Response, redirect,render_template, request
from camera import Video
# initialize app
app = Flask(__name__)

# index route
@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
# video route
@app.route('/video_feed')
def video_feed():
    return Response(gen(Video()), mimetype='multipart/x-mixed-replace; boundary=frame')

# register organization route
@app.route('/registerorg')
def registerorg():
    return render_template('register_org.html')

#add member route
@app.route('/addmember',methods=['GET','POST'])
def addmember():
    if request.method == 'POST':
        # get data from form
        name = request.form['name']
        # add member to database
        return redirect('/')
    return render_template('add_member.html')

# login route
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)