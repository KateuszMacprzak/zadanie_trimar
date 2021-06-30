from flask import Flask

app = Flask(__name__)

@app.route('/<number>')
def give_a_number(number):
    try:
        if int(number)<0:
            return 'Given number must by higher than 0 !'
        if int(number)==0:
            return 'You must not divide by 0 !'
        if int(number)%2==0:
            return 'This number is divide by 2'
        if int(number)%2!=0:
            return 'This number is not divide by 2'
    except ValueError:
        return 'That is wrong type. You must enter a int type !'


if __name__ == '__main__':
    app.run(debug = True)