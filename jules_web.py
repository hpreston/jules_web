from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeee!", my_list=[0,1,2,3,4,5], title="Home")

@app.route("/status")
def status():
    return render_template('template.html', my_string="Wheeee!", my_list=[0,1,2,3,4,5], title="Status")

@app.route("/inventory")
def inventory():
    # ToDo - working on updating jules_app for the needed api calls for this to work
    # ToDo - need to build out the template for the display of returned data
    return render_template('inventory.html', title="Inventory")

@app.route("/schedule")
def schedule():
    return render_template('template.html', my_string="Wheeee!", my_list=[0,1,2,3,4,5], title="Schedule")

@app.route("/notify")
def notify():
    return render_template('template.html', my_string="Wheeee!", my_list=[0,1,2,3,4,5], title="Notify")

@app.route("/settings")
def settings():
    return render_template('template.html', my_string="Wheeee!", my_list=[0,1,2,3,4,5], title="Settings")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
