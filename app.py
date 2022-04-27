
from flask import Flask, redirect, url_for, request, render_template
from forms import PlaceForm
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index_page():
    form  = PlaceForm(request.form)
    if request.method == 'POST' and form.validate():
        address = form.place_name.data
        address_in_format = address.replace(' ','%20')

        nearest_stop = find_stop_near(address_in_format)

        return redirect(url_for('mbta_page', address = address, nearest_stop=nearest_stop))
    return render_template('index.html', form=form)


@app.route('/mbta_station/<address>/<nearest_stop>')
def mbta_page(address, nearest_stop):
    return render_template('mbta.html', address=address, nearest_stop=nearest_stop)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html')

    
if __name__ == "__main__":
    app.run()