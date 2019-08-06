from flask import Blueprint, render_template,request,redirect,url_for,flash
from werkoot_web.util.measurement.arm import measure
import numpy as np
import cv2


measurements_blueprint = Blueprint('measurements',
                            __name__,
                            template_folder='templates')


@measurements_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('measurements/new.html')

@measurements_blueprint.route('/', methods=['POST'])
def create():
    results = []
    if 'file1' in request.files:
        npimg1 = np.fromfile(request.files['file1'], np.uint8)
        img1 = cv2.imdecode(npimg1, cv2.IMREAD_COLOR)
        if measure(img1):
            results.append(measure(img1))
    if 'file2' in request.files:
        npimg2 = np.fromfile(request.files['file2'], np.uint8)
        img2 = cv2.imdecode(npimg2, cv2.IMREAD_COLOR)
        if measure(img2):
            results.append(measure(img2))
    if 'file3' in request.files:
        npimg3 = np.fromfile(request.files['file3'], np.uint8)
        img3 = cv2.imdecode(npimg3, cv2.IMREAD_COLOR)
        if measure(img3):
            results.append(measure(img3))

    result = 0
    if len(results) == 0:
        return "Unable to get a measurement"
    
    for measurement in results:
        result += measurement

    result = int(result/len(results))

    print(results)
    print(result)

    return render_template('measurements/show.html', result=result)



