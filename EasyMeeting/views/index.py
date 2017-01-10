#! encoding=utf-8
from flask import Blueprint, request, make_response, abort, render_template, g

index=Blueprint('index', __name__, template_folder='../frontend')

@index.route('/')
def indexhtml():
	return render_template('dist/index.html')