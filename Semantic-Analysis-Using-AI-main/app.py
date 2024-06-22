from flask import *
from werkzeug.utils import secure_filename
import os  
app = Flask(__name__)  
UPLOAD_FOLDER = 'images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/topic', methods = ['POST'])  
def topic():  
    if request.method == 'POST':  
        f = request.files['file']  
        #f.save(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        
        return render_template("topic.html")
        #return render_template("file_upload_form.html")  




@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':
        text=request.form['text'] 
        outfile=open("data.txt","w")
        outfile.write(text)
        outfile.close()
        return render_template("success.html")



        

if __name__ == '__main__':  
    app.run(debug = True)  


