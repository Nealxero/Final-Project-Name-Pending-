"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Meal
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


api = Blueprint('api', __name__)


@api.route('/user', methods=['GET'])
def show_users():
    users = User.query.all()
    all_users_ll = []
    for user in users:
        all_users_ll.append({
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'url': f'api/user/{user.id}'
            })
    return jsonify(all_users_ll), 200

@api.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()
    try:
        user_final = ({
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'daily_plans': f'./api/user/{user.id}/daily_meals',
            'favorites': f'./api/user/{user.id}/favorites'
            
            })
        return jsonify(user_final), 200
    except Exception as error:
        return jsonify("This user doesn't exists")


        
   

@api.route('/signup', methods=['POST'])
def create_new_user():
    user_email = request.json.get('user-email', None)
    user_password = request.json.get('user-password', None)
    user_username = request.json.get('user-name', None)
    user = User.signup(password=user_password, email=user_email, username=user_username)
    db.session.add(user)
    db.session.commit()

    if user is not None:
        print(user)
        return jsonify({"message":"User created succesfully!"}), 201
    else:
        return jsonify({"message":"Something went wrong, Try again!"}), 500


@api.route('/login', methods=['POST'])
def user_login():
    email = request.json.get('user-email', None)
    password = request.json.get('user-password', None)
    print(request.json)
    user = User.query.filter_by(email=email, password=password).one_or_none()
    if user is None:
        return jsonify({"msg": "Something went wrong, please try again!"}), 401
    
    # token
    access_token = create_access_token(identity=user.email)
    return jsonify({ "token": access_token, "user_id": user.id, "email": user.email })

@api.route('/logout', methods=['DELETE'])
def user_logout():
    session.pop("email", None)
    if user is None:
        return jsonify({"msg": " Succesfully Logged out "})
    return redirect(url_for("login")) 
 

#-------------------------- MEALS -----------------------


@api.route('/meals', methods=['GET'])
def meal_list(): 
    meal = Meal.query.all()
    response_body_meal = list(map(lambda s: s.serialize(), meal))
    return jsonify(response_body_meal), 200

@api.route('/meals/<meal_id>', methods=['GET'])
def get_meal_by_id(meal_id):
    meal = Meal.query.filter_by(id=meal_id).one_or_none()

    try:
        meal_final = ({
            'id':meal.id,
            'name':meal.name,
            'sumarize':meal.sumarize,
            'nutrients':meal.nutrients
            
            })
        return jsonify(meal_final), 200
    except Exception as error:
        return jsonify("This meal doesn't exists")
    
# --------------   User's Favorites --------------------------------
@api.route('/user/<user_id>/favorites', methods=['GET'])
def get_user_favorites(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()
    
    try:
        user_final = ({
            'id':user.id,
            'username':user.username,
            'favorites' : []
            })

        for fav in user.favorites:
            user_final['favorites'].append({
                'id':fav.id,
                'name':fav.name,
                'sumarize':fav.sumarize,
                'nutrients':fav.nutrients,
                'ingredients':fav.ingredients,
            })

        return jsonify(user_final), 200
    except Exception as error:
        return jsonify("This user doesn't have favorites")

# --------------   User's Daily plan --------------------------------
@api.route('/user/<user_id>/daily_meals', methods=['GET'])
def get_user_daily_plan(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()
    return jsonify(user.to_dict()), 200
'''  
    try:
        user_final = ({
            'id':user.id,
            'username':user.username,
            'daily_plans' : []
            })

        for plan in user.daily_plans:
            meal_first= list(map(lambda s: s.serialize_daily_plan(), plan.first_block))
            meal_second= list(map(lambda s: s.serialize_daily_plan(), plan.second_block))
            meal_third= list(map(lambda s: s.serialize_daily_plan(), plan.third_block))

            user_final['daily_plans'].append({
                'daily_plan_id': plan.id,
                'first_block' : { 
                    'meals' : meal_first
                },
                'second_block' : { 
                    'meals' : meal_second
                },
                'third_block' : { 
                    'meals' : meal_third
                }
            })

        return jsonify(user_final), 200

    except Exception as error:
        print('no')
        return jsonify("This user doesn't have daily plans")
        '''






