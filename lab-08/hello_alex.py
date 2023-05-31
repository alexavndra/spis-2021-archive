import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')

def render_main():

    return render_template('home.html')



@app.route('/ctof')

def render_ctof():

    return render_template('ctof.html')



@app.route('/ftoc')

def render_ftoc():

    return render_template('ftoc.html')



@app.route('/mtokm')

def render_mtokm():

    return render_template('mtokm.html')

    

@app.route('/ftoc-result')

def render_ftoc_result():

    try:

        ftemp_result = float(request.args['ftemp'])

        ctemp_result = ftoc(ftemp_result)

        return render_template('ftoc_result.html', ftemp=ftemp_result, ctemp=ctemp_result)

    except ValueError:

        return "Sorry: something went wrong."



@app.route('/ctof-result')

def render_ctof_result():

    try:

        ctemp_result = float(request.args['ctemp'])

        ftemp_result = ctof(ctemp_result)

        return render_template('ctof_result.html', ctemp=ctemp_result, ftemp=ftemp_result)

    except ValueError:

        return "Sorry: something went wrong."



@app.route('/mtokm-result')

def render_mtokm_result():

    try:
        miles_result = float(request.args['miles'])

        km_result = mtokm(miles_result)

        return render_template('mtokm_result.html', km=km_result, miles = miles_result)
        
        # You'll need some code here, and maybe some extra parameters in render_template below...

        return render_template('mtokm.html')

    except ValueError:

        return "Sorry: something went wrong."



def ftoc(ftemp):

   return (ftemp - 32.0) * (5.0 / 9.0)

    

def ctof(ftemp):

   return (ftemp * (9.0 / 5.0)) + 32.0 # replace with correct formula


def mtokm(miles):

    return miles * 1.609344
# You'll probably want a basic function here to convert miles to kilometers too...

    

if __name__=="__main__":

    app.run(host='0.0.0.0')










# decorator
# @app.route("/")

# def hello():

#    return "hey it's alex hope you're doing well!"

# # converts fahrenheit to celsius
# def ftoc(ftemp):

#    return (ftemp - 32.0) * (5.0 / 9.0)

# # decorator
# @app.route('/ftoc/<ftemp_str>')

# # converts fahrenheit to celsius in web
# def convert_ftoc(ftemp_str):

#     ftemp = 0.0

#     try:

#         ftemp = float(ftemp_str)

#         ctemp = ftoc(ftemp)

#         return "In Farenheit: " + ftemp_str + " In Celsius " + str(ctemp) 

#     except ValueError:

#         return "Sorry.  Could not convert " + ftemp_str + " to a number"

# # converts miles to kilometers
# def mtokm(miles):

#     return miles * 1.609

# # decorator
# @app.route('/mtokm/<miles_str>')

# # converts miles to kilometers in web
# def miles_to_km(miles_str):

#   miles = 0.0

#   try:

#     miles = float(miles_str)

#     kilometers = mtokm(miles)

#     return "In miles: " + miles_str + " In kilometers " + str(kilometers)

#   except ValueError:

#     return "Sorry, couldn't convert " + miles_str + " to a number"  


# if __name__ == "__main__":

#    app.run(host='0.0.0.0')