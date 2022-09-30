import math
from unittest.case import doModuleCleanups
from flask import Flask, render_template, redirect, request, flash, url_for, send_from_directory
# from flask_site.forms import AddingImages, RegistrationForm, LoginForm, AdminLogin, AddingPictures, SearchImages, SearchForm, FamilyForm
from flask_site import app
import os
import requests
import time
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_site import bcrypt, db, ALLOWED_EXTENSIONS, secure_filename
# from flask_site.models import AdminInfo, Approval, FamilyMembers, Members, Images, Documents, Approval
# from flask_paginate import Pagination, get_page_parameter, get_page_args
# from werkzeug.security import generate_password_hash, check_password_hash

ticker = "NLY"
api_key = os.environ.get('twelvedata_secretkey')

# get stock price
def get_stock_price(ticker, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker}&apikey=e5927bedce3a4e6aa69b6d8b4f3b0b8f&source=docs"
    response = requests.get(url).json()
    return response

# *******************************************************************
# website routes

@app.route('/', methods=["GET", "POST"])
def index1():
    price = get_stock_price(ticker, api_key)['close'][:-3]
    percent_change = get_stock_price(ticker, api_key)['percent_change'][:-3]
    change = get_stock_price(ticker, api_key)['change'][:-3]
    return render_template('index1.html', stock_price=price, percent_change=percent_change, change=change)


@app.route('/the_power_of_vcf.html')
def the_power_of_vcf():
    return render_template('the_power_of_vcf.html')


@app.route('/our_business.html')
def our_business():
    return render_template('our_business.html')


@app.route('/investors.html', methods=["GET", "POST"])
def investors():
    price = get_stock_price(ticker, api_key)['close'][:-3]
    percent_change = get_stock_price(ticker, api_key)['percent_change'][:-3]
    change = get_stock_price(ticker, api_key)['change'][:-3]
    return render_template('investors.html', stock_price=price, percent_change=percent_change, change=change)

@app.route('/careers.html')
def careers():
    return render_template('careers.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')