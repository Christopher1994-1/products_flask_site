import math
from unittest.case import doModuleCleanups
from flask import Flask, render_template, redirect, request, flash, url_for, send_from_directory
# from flask_site.forms import AddingImages, RegistrationForm, LoginForm, AdminLogin, AddingPictures, SearchImages, SearchForm, FamilyForm
from flask_site import app
import os
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_site import bcrypt, db, ALLOWED_EXTENSIONS, secure_filename
# from flask_site.models import AdminInfo, Approval, FamilyMembers, Members, Images, Documents, Approval
# from flask_paginate import Pagination, get_page_parameter, get_page_args
# from werkzeug.security import generate_password_hash, check_password_hash




# *******************************************************************
# website routes

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/the_power_of_vcf.html')
def the_power_of_vcf():
    return render_template('the_power_of_vcf.html')