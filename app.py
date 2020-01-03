from flask import Flask, render_template, request
from svm_func import train_svm, test_svm, predict_svm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from time import time



app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_method():
	return render_template('home.html')


@app.route('/predict', methods=['POST']) 
def login_user():

	if(request.form['space']=='None'):
		data = []
		string = 'value'
		for i in range(1,31):
			data.append(float(request.form['value'+str(i)]))
		for i in range(30):
			print(data[i])
	else:
		string = request.form['space']
		data = string.split()
		print(data)
		print("Type:", type(data))
		print("Length:", len(data))
		for i in range(30):
			print(data[i])
		data = [float(x.strip()) for x in data]
		for i in range(30):
			print(data[i])

	data_np = np.asarray(data, dtype = float)
	data_np = data_np.reshape(1,-1)
	out, acc, t = predict_svm(clf, data_np)

	if(out==1):
		output = 'Malignant'
	else:
		output = 'Benign'

	acc_x = acc[0][0]
	acc_y = acc[0][1]
	if(acc_x>acc_y):
		acc = acc_x
	else:
		acc=acc_y
	return render_template('result.html', output=output, accuracy=round(acc*100,3), time=t)
	

if __name__=='__main__':
	global clf 
	clf = train_svm()
	test_svm(clf)
	print("Done")
	app.run(port=4995)

