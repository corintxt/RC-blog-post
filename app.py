from flask import Flask, render_template, session


app = Flask(__name__)


# Index page
@app.route('/', methods=['GET'])
def index():
    # Define key points
    session['name'] = ''

    session['challenge_you_felt'] = ''
    session['social_interaction'] = ''
    session['technical_achievement'] = ''
    session['personal_achievement'] = ''
    session['unexpected_benefit'] = ''
    session['minor_flaw'] = ''
    session['inspiring_thing'] = ''
    session['metaphor'] = ''

    body_text = '''
    Before I came to R.C., I was .
                '''

    return render_template('layout.html', text=body_text)


if __name__ == '__main__':
    app.secret_key = 'key'
    app.run(debug=True)