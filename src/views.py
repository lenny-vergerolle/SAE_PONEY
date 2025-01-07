from .app import app, db
import src.views as views
import src.commands as commands
# import src.models as models


@app.route('/signin', methods=['GET','POST'])
def signin():
    f = InscriptionForm()
    