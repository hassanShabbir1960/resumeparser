from flask import Flask, render_template, request
import os 

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
            f.save(os.path.join("uploads", f.filename))
        # return 'file uploaded successfully'
            return render_template('index.html',Fname="Hasan", Lname="Shabbir",email="kh@gm.com",contact="030158")
        except:
            return render_template('index.html')
		      

    if request.method == 'GET':
       return render_template('index.html')
		
if __name__ == '__main__':
   app.run(debug = True)