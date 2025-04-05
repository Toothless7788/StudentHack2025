from flask import Flask, render_template
from py_apps.main import read_xml_file_paths
from py_apps.web_tester import WebTester

xml_file_paths = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/test")
def test():
    # Read web-testing-config.xml
    xml_file_paths = read_xml_file_paths()

    # Run the code
    # Multiple case
    for xml_file_path in xml_file_paths:
        web_tester = WebTester(xml_file_path)
        web_tester.run()

    return "Test run"