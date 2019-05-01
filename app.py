from flask import Flask, render_template, session


app = Flask(__name__)


# Index page
@app.route('/', methods=['GET'])
def index():
    # Define key points
    session['name'] = 'Corin Faife'

    session['challenge_you_felt'] = 'debugging Flask for the first time'
    session['social_interaction'] = 'game nights with new friends'
    session['technical_achievement'] = 'deploying my first web app'
    session['personal_achievement'] = 'learning how to ask for help'
    session['unexpected_benefit'] = 'a short commute in the morning'
    session['minor_flaw'] = 'getting overtired'
    session['inspiring_thing'] = 'talking politics with people who care'

    body_text = '''
    Before I came to R.C., I was ___
                '''

    return render_template('layout.html', text=body_text)


if __name__ == '__main__':
    app.secret_key = 'key'
    app.run(debug=True)