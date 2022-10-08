from flask import Flask, request, make_response, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from app import app
from app import db, models
from app.models import *

from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"






# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** Autorization and Registration*********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# *********************************************** #
# Registration PhysEntity
# Input: 
# nickname - str
# password - str
# fio - str
# birthDate - str
# email - str
# phoneNumber - str
# agreement - str
# Output:

# 201 - Created
# Agreeement = False -> Error: Agreements not accepted'
# 400 - Front Error
# 500 - Back Error

# http://127.0.0.1:5000/Registration/UsPh?nickname=Egor&password=1234&fio=VEM&birthdate=06061999&email=test_acc@mail.ru&phonenumber=8999999&agreement=True
# *********************************************** #
@app.route('/Registration/UsPh', methods = ['POST'])
def registration_ph():
	try:
		args = request.args.to_dict()
		if args.get("agreement") == 'True':
			Phys = PhysEntity(
				NickName = args.get("nickname"),
				Password = args.get("password"),
				FIO = args.get("fio"),
				BirthDate = datetime.strptime(args.get("birthdate"), "%d%m%Y").date(), # date.strftime("%d-%m-%Y")
				Email = args.get("email"),
				PhoneNumber = args.get("phonenumber"),
				Agreement = (args.get("agreement") == 'True'),
				CreateDate = datetime.now().date(),
				UpdateDate = datetime.now().date(),
				UpdateUsId = 1
				)
			db.session.add(Phys)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		else:
			return make_response(jsonify({'Error': 'Agreements not accepted'}))
	except (TypeError, NameError, ValueError) as exp:
		return make_response(jsonify({'Error': str(exp)}), 400)
	except Exception as exp:
		return make_response(jsonify({'Error': str(exp)}), 500)

# *********************************************** #
# Registration LegEntity

# Input: 
# nickname - str
# password - str
# fio - str
# companyname - str
# phoneNumber - str
# email - str
# adressfact1 - str
# adressfact2 - str
# adressfact3 - str
# adressleg - str
# agreement - str
# acct_no - str
# kor_no - str
# bik - str
# kpp - str
# ogrn - str
# inn - str
# providerfio - str
# providerphonenumber - str
# provideremail - str

# Output:
# 201 - Created
# Agreeement = False -> Error: Agreements not accepted'
# 400 - Front Error
# 500 - Back Error

# http://127.0.0.1:5000/Registration/UsLeg?nickname=Adam&password=1234co&fio=VAM&companyname=CompanyNo1&phonenumber=888888888&email=test_acc_co@mail.ru&adressfact1=Moscow&adressfact2=NN&adressleg=MoscowLeg&agreement=True&acct_no=400011122200&kor_no=1122&bik=4444&kpp=1222&ogrn=993344&inn=3777228893&providerfio=PAS&providerphonenumber=7744443308&provideremail=prov_mail@mail.ru
# *********************************************** #
@app.route('/Registration/UsLeg', methods = ['POST'])
def registration_leg():
	try:
		args = request.args.to_dict()
		if args.get("agreement") == 'True':
			Leg = LegEntity(
				NickName = args.get("nickname"),
				Password = args.get("password"),
				FIO = args.get("fio"),
				CompanyName = args.get("companyname"),
				PhoneNumber = args.get("phonenumber"),				
				Email = args.get("email"),
				AdressFact1 = args.get("adressfact1"),
				AdressFact2 = args.get("adressfact2"),
				AdressFact3 = args.get("adressfact3"),
				AdressLeg = args.get("adressleg"),				
				Agreement = (args.get("agreement") == 'True'),
				Acct_no = args.get("acct_no"),
				Kor_no = args.get("kor_no"),
				Bik = args.get("bik"),
				Kpp = args.get("kpp"),
				Ogrn = args.get("ogrn"),
				Inn = args.get("inn"),
				ProviderFIO = args.get("providerfio"),
				ProviderPhoneNumber = args.get("providerphonenumber"),
				ProviderEmail = args.get("provideremail"),
				CreateDate = datetime.now().date(),
				UpdateDate = datetime.now().date(),
				UpdateUsId = 1
				)
			db.session.add(Leg)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		else:
			return make_response(jsonify({'Error': 'Agreements not accepted'}))
	except (TypeError, NameError, ValueError) as exp:
		return make_response(jsonify({'Error': str(exp)}), 400)
	except Exception as exp:
		return make_response(jsonify({'Error': str(exp)}), 500)

# *********************************************** #
# Registration Shop
# Input: 
# shopname - str
# descrshort - str
# descrfull - str
# topic_1 - str
# topic_2 - str
# topic_3 - str
# topic_4 - str
# topic_5 - str
# topic_6 - str
# topic_7 - str
# topic_8 - str
# topic_9 - str
# topic_10 - str
# mindaysmkad
# mindaysmo
# mindaysrf
# costmkad
# costmo
# costrf
# Output:
# 201 - Created
# 400 - Front Error
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserLeg1/ShopReg?&shopname=Magazine1&descrshort=First_Magazin_for_test&descrfull=My_first_magazine_for_testing_back&topic_1=t1&topic_2=t2&topic_3=t3&topic_4=t4&mindaysmkad=3&mindaysmo=5&costmkad=300&costmo=500
# &topic_5=&topic_6=&topic_7=&topic_8=&topic_9=&topic_10=
# *********************************************** #
@app.route('/Root/UserLeg<UsLegId>/ShopReg', methods = ['POST'])
def registration_shop(UsLegId):
	try:
		args = request.args.to_dict()
		Sh = Shop(
			ShopName = args.get("shopname"),
			DescrShort = args.get("descrshort"),
			DescrFull = args.get("descrfull"),
			Topic_1 = args.get("topic_1"),
			Topic_2 = args.get("topic_2"),
			Topic_3 = args.get("topic_3"),
			Topic_4 = args.get("topic_4"),
			Topic_5 = args.get("topic_5"),
			Topic_6 = args.get("topic_6"),
			Topic_7 = args.get("topic_7"),
			Topic_8 = args.get("topic_8"),
			Topic_9 = args.get("topic_9"),
			Topic_10 = args.get("topic_10"),
			UsLegId = UsLegId,
			CreateDate = datetime.now().date())
		db.session.add(Sh)
		db.session.commit()

		Sh1 = db.session.query(Shop).filter_by(ShopName = args.get("shopname"), UsLegId = UsLegId).first()
		Del = Delivery(
			MinDaysMKAD = args.get("mindaysmkad"),
			MinDaysMO = args.get("mindaysmo"),
			MinDaysRF = args.get("mindaysrf"),
			CostMKAD = args.get("costmkad"),
			CostMO = args.get("costmo"),
			CostRF = args.get("costrf"),
			ShopId = Sh1.ShopId,
			UsLegId = UsLegId,
			CreateDate = datetime.now().date(),
			UpdateDate = datetime.now().date())
		db.session.add(Del)
		db.session.commit()
		return make_response(jsonify({'Status' : 'Created'}), 201)
	except (TypeError, NameError, ValueError) as exp:
		return make_response(jsonify({'Error': str(exp)}), 400)
	except Exception as exp:
		return make_response(jsonify({'Error': str(exp)}), 500)


# *********************************************** #
# Autorization
# Input:
# email
# nickname
# phonenumber
# password

# Output:
# 200 - OK
# 400 - Empty Field
# 500 - Back Error
# 'Error' - Incorrect Password

# http://127.0.0.1:5000/autorization?nickname=Egor&password=1234
# http://127.0.0.1:5000/autorization?email=test_acc@mail.ru&password=1234
# http://127.0.0.1:5000/autorization?phonenumber=8999999&password=1234
# *********************************************** #
@app.route('/Autorization', methods = ['GET'])
def autorization():
	try:
		args = request.args.to_dict()
		get_pass = args.get("password")
		if len(get_pass) != 0:
			if args.get("email"):
				true_pass = db.session.query(PhysEntity).filter(PhysEntity.Email == args.get("email")).first().Password
				if get_pass == true_pass:
					return make_response(jsonify({'Status': 'OK'}), 200)
				else:
					return make_response(jsonify({'Error': 'Incorrect password'}))
			elif args.get("nickname"):
				true_pass= db.session.query(PhysEntity).filter(PhysEntity.NickName == args.get("nickname")).first().Password
				if get_pass == true_pass:
					return make_response(jsonify({'Status': 'OK'}), 200)
				else:
					return make_response(jsonify({'Error': 'Incorrect password'}))
			elif args.get("phonenumber"):
				true_pass = db.session.query(PhysEntity).filter(PhysEntity.PhoneNumber == args.get("phonenumber")).first().Password
				if get_pass == true_pass:
					return make_response(jsonify({'Status': 'OK'}), 200)
				else:
					return make_response(jsonify({'Error': 'Incorrect password'}))
			else:
				return make_response(jsonify({'Error': 'Empty Login Field'}), 400)
		else:
			return make_response(jsonify({'Error': 'Empty Password Field'}), 400)
	except Exception as exp:
		return make_response(jsonify({'Error': str(exp)}), 500)




# , 'truePass': str(true_pass), 'get_nick': args.get("nickname"), 'get_pass': args.get("password")





# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** Working UserPh with own Profile and Feed *********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# Get PhUser Feed
# def get_post_json(post):
# 	new_post = {}
# 	for field in vars(post):
# 		if field == 'PostId':
# 			new_post['PostId'] = url_for('post_work_ph', post.UsPhId, post.PostId, _external = True)
# 		else:
# 			new_post[field] = post[field]
# 	return new_post

# lambda post: vars(post) for post in result



# *********************************************** #
# Get UserPh Feed

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/UserFeed
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/UserFeed', methods = ['GET'])
def get_user_feed(UsPhId):
	try:
		result = db.session.query(Post).filter(Post.UsPhId == UsPhId).order_by(Post.CreateDate).all()
		return make_response(jsonify({'Status': 'OK', 'Body': [post.serialize for post in result]}), 200)
	except Exception as exp:
		return make_response(jsonify({'Error': str(exp)}), 500)


# *********************************************** #
# Create PhUser new Post
# Input:
# descrshort
# descrfull
# topic_1
# topic_2
# topic_3
# topic_4
# topic_5
# topic_6
# topic_7
# topic_8
# topic_9
# topic_10

# Output:
# 201 - Created
# 400 - Front Error
# 500 - Back Error

# ! Можно реализовать возврат вместо PostId весь путь к данному посту
# Либо же возвращать PostId и при необходимости формировать путь к нему в ручную (до его EndPoint)

# http://127.0.0.1:5000/Root/UserPh1/UserFeed/AddPost?descrshort=My first post&descrfull=My first Post full descr&topic_1=t1&topic_2=t2&topic_3=t3&topic_4=t4
# http://127.0.0.1:5000/Root/UserPh1/UserFeed/AddPost?descrshort=My second post&descrfull=My second Post full descr&topic_1=t1&topic_2=t2&topic_3=t3&topic_4=t4
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/UserFeed/AddPost', methods = ['POST'])
def add_post_ph(UsPhId):
	try:
		args = request.args.to_dict()
		post = Post(
			ProductFlg = False,
			DescrShort = args.get("descrshort"),
			DescrFull = args.get("descrfull"),
			LikesCnt = 0,
			UsPhId = UsPhId,
			Topic_1 = args.get("topic_1"),
			Topic_2 = args.get("topic_2"),
			Topic_3 = args.get("topic_3"),
			Topic_4 = args.get("topic_4"),
			Topic_5 = args.get("topic_5"),
			Topic_6 = args.get("topic_6"),
			Topic_7 = args.get("topic_7"),
			Topic_8 = args.get("topic_8"),
			Topic_9 = args.get("topic_9"),
			Topic_10 = args.get("topic_10"),
			CreateDate = datetime.now().date())
		db.session.add(post)
		db.session.commit()
		return make_response(jsonify({'Status': 'Created'}), 201)
	except (TypeError, NameError, ValueError) as exp:
		return make_response(jsonify({'Error': str(exp)}), 400)
	except Exception as exp:
		return make_response(jsonify({'Error': str(exp)}), 500)


# *********************************************** #
# Get UserPh Post info:
# Input in EndPoint:
# UsPhId
# PostId

# Output:
# 200 - OK
# 500 - Back Error

# Take post to UserPh Saved
# Input in EndPoint:
# UsPhId
# PostId

# Output:
# 201 - Created
# 500 - Back Error

# Delete post from UserPh Saved
# Input in EndPoint:
# UsPhId
# PostId

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/UserFeed/Post1
# http://127.0.0.1:5000/Root/UserPh1/UserFeed/Post1
# http://127.0.0.1:5000/Root/UserPh1/UserFeed/Post1
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/UserFeed/Post<PostId>', methods = ['GET', 'POST', 'DELETE'])
def post_work_ph(UsPhId, PostId):
	if request.method == 'GET':
		try:
			post = db.session.query(Post).filter(Post.PostId == PostId).first()
			return make_response(jsonify({'Status': 'OK', 'Body': post.serialize}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			fav = Favourite(
				UsPhId = UsPhId,
				PostId = PostId,
				ProductFlg = False,
				CreateDate = datetime.now().date())
			db.session.add(fav)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			fav = db.session.query(Favourite).filter_by(UsPhId = UsPhId, PostId = PostId).first()
			db.session.delete(fav)
			db.session.commit()
			# query(Favourite).filter(Favourite.UsPhId == UsPhId).filter(Favourite.PostId == PostId).delete(synchronize_session = 'fetch')
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)


# *********************************************** #
# Update UserPh Post:
# Input in EndPoint:
# UsPhId
# PostId
# Input:
# Все существующие поля поста с учетом обновлений. В форме корректировки нужно во всех полях выводить текущие значения
# переменных, нужные пользователь изменит. После нажатия кнопки забрать все значения из полей и передать их

# Output:
# 200 - OK
# 400 - Front Error
# 500 - Back Error

# Delete Post
# Input in EndPoint:
# UsPhId
# PostId

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/UserFeed/Post1/Edit?descrshort=My first post updated&descrfull=My first Post full descr&topic_1=t1&topic_2=t2&topic_3=t3&topic_4=t4
# http://127.0.0.1:5000/Root/UserPh1/UserFeed/Post2/Edit
# *********************************************** #

@app.route('/Root/UserPh<UsPhId>/UserFeed/Post<PostId>/Edit', methods = ['PUT', 'DELETE'])
def edit_post_ph(UsPhId, PostId):
	if request.method == 'PUT':
		try:
			args = request.args.to_dict()
			post = db.session.query(Post).filter_by(PostId = PostId, UsPhId = UsPhId).first()

			post.DescrShort = args.get("descrshort")
			post.DescrFull = args.get("descrfull")
			post.Topic_1 = args.get("topic_1")
			post.Topic_2 = args.get("topic_2")
			post.Topic_3 = args.get("topic_3")
			post.Topic_4 = args.get("topic_4")
			post.Topic_5 = args.get("topic_5")
			post.Topic_6 = args.get("topic_6")
			post.Topic_7 = args.get("topic_7")
			post.Topic_8 = args.get("topic_8")
			post.Topic_9 = args.get("topic_9")
			post.Topic_10 = args.get("topic_10")

			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except (TypeError, NameError, ValueError) as exp:
			return make_response(jsonify({'Error': str(exp)}), 400)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			post = db.session.query(Post).filter_by(PostId = PostId, UsPhId = UsPhId).first()
			db.session.delete(post)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)

# *********************************************** #
# Working with comments UserPh

# Get all comments of the post
# input in EndPoint:
# UsPhId
# PostId

# Output:
# 200 - OK
# 500 - Back Error

# Post a new comment
# input in EndPoint:
# UsPhId
# PostId

# Input:
# Comment parameters

# Output:
# 201 - Created
# 400 - Front Error
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/UserFeed/Post1/Comments
# http://127.0.0.1:5000/Root/UserPh1/UserFeed/Post1/Comments?text=My first Comment
# *********************************************** #

@app.route('/Root/UserPh<UsPhId>/UserFeed/Post<PostId>/Comments', methods = ['GET', 'POST'])
def comm_ph(UsPhId, PostId):
	if request.method == 'GET':
		try:
			result = db.session.query(Comment).filter_by(PostId = PostId).order_by(Comment.CreateDate).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [comm.serialize for comm in result]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			comm = Comment(
				Text = args.get("text"),
				LikesCnt = 0,
				PostId = PostId,
				UsPhId_p = UsPhId,
				UsPhId_c = UsPhId,
				CreateDate = datetime.now().date())
			db.session.add(comm)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except (TypeError, NameError, ValueError) as exp:
			return make_response(jsonify({'Error': str(exp)}), 400)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)


# *********************************************** #
# Edit UserPh Comment

# Edit
# input in EndPoint:
# UsPhId
# PostId
# ComId
# Input:
# Comment parameters to edit

# Output:
# 200 - OK
# 400 - Front Error
# 500 - Back Error


# Delete
# input in EndPoint:
# UsPhId
# PostId
# ComId

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/UserFeed/Post1/Comments/Comment1?text=My first Comment updated
# http://127.0.0.1:5000/Root/UserPh1/UserFeed/Post1/Comments/Comment1
# *********************************************** #

@app.route('/Root/UserPh<UsPhId>/UserFeed/Post<PostId>/Comments/Comment<ComId>', methods = ['PUT', 'DELETE'])
def edit_comment_ph(UsPhId, PostId, ComId):
	if request.method == 'PUT':
		try:
			args = request.args.to_dict()
			comm = db.session.query(Comment).filter_by(PostId = PostId, ComId = ComId).first()

			comm.Text = args.get("text")

			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except (TypeError, NameError, ValueError) as exp:
			return make_response(jsonify({'Error': str(exp)}), 400)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			comm = db.session.query(Comment).filter_by(PostId = PostId, ComId = ComId).first()
			db.session.delete(comm)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)




# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** SUBSCRIBES Users*********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# *********************************************** #
# Get UserPh Subscribes for another Users
# Input in EndPoint:
# UsPhId

# Output:
# 200 - OK
# 500 - Back Error


# Make a subscribe for another user from list view
# Input in EndPoint:
# UsPhId

# Input:
# UsPhIdForSubscr

# Output:
# 201 - Created
# 500 - Back Error


# Cancel subscribe for another user from list view
# Input in EndPoint:
# UsPhId

# Input:
# UsPhIdForSubscr OR
# ShopId

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Subscribes/Users
# http://127.0.0.1:5000/Root/UserPh1/Subscribes/Users?usphidforsubscr=2
# http://127.0.0.1:5000/Root/UserPh1/Subscribes/Users?usphidforsubscr=2
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Subscribes/Users', methods = ['GET', 'POST', 'DELETE'])
def subscr_ph_us(UsPhId):
	if request.method == 'GET':
		try:
			# Getting all UsPhId's for which current user have a subscribe
			result = db.session.query(Subscribe).filter(Subscribe.UsPhId == UsPhId, Subscribe.UsPhIdForSubscr != None).order_by(Subscribe.SubscrDate).all()
			subs_id = [sub['UsPhIdForSubscr'] for sub in [subscr.serialize_u for subscr in result]]
			# Getting Users by thos UsPhId's
			users = db.session.query(PhysEntity).filter(PhysEntity.UsPhId.in_(subs_id)).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [us.serialize_short for us in users]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			subscr = Subscribe(
				UsPhId = UsPhId,
				UsPhIdForSubscr = args.get("usphidforsubscr"),
				SubscrDate = datetime.now().date())
			db.session.add(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			args = request.args.to_dict()
			subscr = db.session.query(Subscribe).filter_by(UsPhId = UsPhId, UsPhIdForSubscr = args.get("usphidforsubscr")).first()
			db.session.delete(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)



# *********************************************** #
# Working with Profiles of users

# Get inforamtion abour profile
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which profile we looking

# Output:
# 200 - OK
# 500 - Back Error


# Make a subscribe for this profile
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which profile we looking

# Output:
# 201 - Created
# 500 - Back Error


# Return a subscribe for this profile
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which profile we looking

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/Users/Profile2
# http://127.0.0.1:5000/Root/UserPh1/Users/Profile2
# http://127.0.0.1:5000/Root/UserPh1/Users/Profile2
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Users/Profile<UsPhId>', methods = ['GET', 'POST', 'DELETE'])
def profile_us(UsPhIdMain, UsPhId):
	if request.method == 'GET':
		try:
			profile = db.session.query(PhysEntity).filter_by(UsPhId = UsPhId).first()
			return make_response(jsonify({'Status': 'OK', 'Body': profile.serialize}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			subscr = Subscribe(
				UsPhId = UsPhIdMain,
				UsPhIdForSubscr = UsPhId,
				SubscrDate = datetime.now().date())
			db.session.add(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			subscr = db.session.query(Subscribe).filter_by(UsPhId = UsPhIdMain, UsPhIdForSubscr = UsPhId).first()
			db.session.delete(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)




# *********************************************** #
# Another User's Feed

# Get Feed
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which Feed we looking

# Output:
# 200 - OK
# 500 - Back Error


# Make a subscribe for this profile
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which profile we looking

# Output:
# 201 - Created
# 500 - Back Error


# Return a subscribe for this profile
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which profile we looking

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2
# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2
# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Users/Feed<UsPhId>', methods = ['GET', 'POST', 'DELETE'])
def feed_us(UsPhIdMain, UsPhId):
	if request.method == 'GET':
		try:
			result = db.session.query(Post).filter_by(UsPhId = UsPhId).order_by(Post.CreateDate).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [post.serialize for post in result]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			subscr = Subscribe(
				UsPhId = UsPhIdMain,
				UsPhIdForSubscr = UsPhId,
				SubscrDate = datetime.now().date())
			db.session.add(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			subscr = db.session.query(Subscribe).filter_by(UsPhId = UsPhIdMain, UsPhIdForSubscr = UsPhId).first()
			db.session.delete(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)



# *********************************************** #
# Actions with post of another user

# Get post information
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which post we looking
# PostId

# Output:
# 200 - OK
# 500 - Back Error


# Take post to UserPh Saved
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which post we looking
# PostId

# Output:
# 201 - Created
# 500 - Back Error


# Delete post from UserPh Saved
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which post we looking
# PostId

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2/Post3
# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2/Post3
# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2/Post3
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Users/Feed<UsPhId>/Post<PostId>', methods = ['GET', 'POST', 'DELETE'])
def post_us(UsPhIdMain, UsPhId, PostId):
	if request.method == 'GET':
		try:
			post = db.session.query(Post).filter_by(PostId = PostId).first()
			return make_response(jsonify({'Status': 'OK', 'Body': post.serialize}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			fav = Favourite(
				UsPhId = UsPhIdMain,
				PostId = PostId,
				ProductFlg = False,
				CreateDate = datetime.now().date())
			db.session.add(fav)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			fav = db.session.query(Favourite).filter_by(UsPhId = UsPhIdMain, PostId = PostId).first()
			db.session.delete(fav)
			db.session.commit()
			# query(Favourite).filter(Favourite.UsPhId == UsPhId).filter(Favourite.PostId == PostId).delete(synchronize_session = 'fetch')
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)


# *********************************************** #
# Get all comments of the post
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which post we looking
# PostId

# Output:
# 200 - OK
# 500 - Back Error


# Post a new comment
# Input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which post we looking
# PostId

# Input:
# Comment text

# Output:
# 201 - Created
# 400 - Front Error
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2/Post3/Comments
# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2/Post3/Comments?text=My third comment for testing
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Users/Feed<UsPhId>/Post<PostId>/Comments', methods = ['GET', 'POST'])
def comments_us(UsPhIdMain, UsPhId, PostId):
	if request.method == 'GET':
		try:
			result = db.session.query(Comment).filter_by(PostId = PostId).order_by(Comment.CreateDate).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [comm.serialize for comm in result]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			comm = Comment(
				Text = args.get("text"),
				LikesCnt = 0,
				PostId = PostId,
				UsPhId_p = UsPhId,
				UsPhId_c = UsPhIdMain,
				CreateDate = datetime.now().date())
			db.session.add(comm)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except (TypeError, NameError, ValueError) as exp:
			return make_response(jsonify({'Error': str(exp)}), 400)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)

# *********************************************** #
# Edit Comment of the post
# input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which post we looking
# PostId
# ComId

# Input:
# Comment text to edit

# Output:
# 200 - OK
# 400 - Front Error
# 500 - Back Error


# Delete comment of the post
# input in EndPoint:
# UsPhIdMain, who looking
# UsPhId, which post we looking
# PostId
# ComId

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2/Post3/Comments/Comment2?text=text updated
# http://127.0.0.1:5000/Root/UserPh1/Users/Feed2/Post3/Comments/Comment2
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Users/Feed<UsPhId>/Post<PostId>/Comments/Comment<ComId>', methods = ['PUT', 'DELETE'])
def edit_comments_us(UsPhIdMain, UsPhId, PostId, ComId):
	if request.method == 'PUT':
		try:
			args = request.args.to_dict()
			comm = db.session.query(Comment).filter_by(PostId = PostId, ComId = ComId).first()

			comm.Text = args.get("text")

			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except (TypeError, NameError, ValueError) as exp:
			return make_response(jsonify({'Error': str(exp)}), 400)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			comm = db.session.query(Comment).filter_by(PostId = PostId, ComId = ComId).first()
			db.session.delete(comm)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)









# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** SUBSCRIBES Shops*********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# *********************************************** #
# Get UserPh Subscribes for Shop
# Input in EndPoint:
# UsPhId

# Output:
# 200 - OK
# 500 - Back Error


# Make a subscribe for Shop from list view
# Input in EndPoint:
# UsPhId

# Input:
# UsPhIdForSubscr OR
# ShopId

# Output:
# 201 - Created
# 500 - Back Error


# Cancel subscribe for Shop from list view
# Input in EndPoint:
# UsPhId

# Input:
# UsPhIdForSubscr OR
# ShopId

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Subscribes/Shops
# http://127.0.0.1:5000/Root/UserPh1/Subscribes/Shops?shopid=3
# http://127.0.0.1:5000/Root/UserPh1/Subscribes/Shops?shopid=3
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Subscribes/Shops', methods = ['GET', 'POST', 'DELETE'])
def subscr_ph_sh(UsPhId):
	if request.method == 'GET':
		try:
			# Getting all UsPhId's for which current user have a subscribe
			result = db.session.query(Subscribe).filter(Subscribe.UsPhId == UsPhId, Subscribe.ShopId != None).order_by(Subscribe.SubscrDate).all()
			subs_id = [sub['ShopId'] for sub in [subscr.serialize_sh for subscr in result]]
			# Getting Users by thos UsPhId's
			shops = db.session.query(Shop).filter(Shop.ShopId.in_(subs_id)).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [sh.serialize_short for sh in shops]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			subscr = Subscribe(
				UsPhId = UsPhId,
				ShopId = args.get("shopid"),
				SubscrDate = datetime.now().date())
			db.session.add(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			args = request.args.to_dict()
			subscr = db.session.query(Subscribe).filter_by(UsPhId = UsPhId, ShopId = args.get("shopid")).first()
			db.session.delete(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)




# *********************************************** #
# Working with Profiles of shops

# Get inforamtion abour profile
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which profile we looking

# Output:
# 200 - OK
# 500 - Back Error


# Make a subscribe for this profile
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which profile we looking

# Output:
# 201 - Created
# 500 - Back Error


# Return a subscribe for this profile
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which profile we looking

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/Shops/Profile3
# http://127.0.0.1:5000/Root/UserPh1/Shops/Profile3
# http://127.0.0.1:5000/Root/UserPh1/Shops/Profile3
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Shops/Profile<ShopId>', methods = ['GET', 'POST', 'DELETE'])
def profile_sh(UsPhIdMain, ShopId):
	if request.method == 'GET':
		try:
			profile = db.session.query(Shop).filter_by(ShopId = ShopId).first()
			return make_response(jsonify({'Status': 'OK', 'Body': profile.serialize}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			subscr = Subscribe(
				UsPhId = UsPhIdMain,
				ShopId = ShopId,
				SubscrDate = datetime.now().date())
			db.session.add(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			subscr = db.session.query(Subscribe).filter_by(UsPhId = UsPhIdMain, ShopId = ShopId).first()
			db.session.delete(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)




# *********************************************** #
# Shop's Feed

# Get Feed
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which Feed we looking

# Output:
# 200 - OK
# 500 - Back Error


# Make a subscribe for this profile
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which profile we looking

# Output:
# 201 - Created
# 500 - Back Error


# Return a subscribe for this profile
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which profile we looking

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3
# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3
# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Shops/Feed<ShopId>', methods = ['GET', 'POST', 'DELETE'])
def feed_sh(UsPhIdMain, ShopId):
	if request.method == 'GET':
		try:
			result = db.session.query(Post).filter_by(ShopId = ShopId).order_by(Post.CreateDate).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [post.serialize for post in result]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			subscr = Subscribe(
				UsPhId = UsPhIdMain,
				ShopId = ShopId,
				SubscrDate = datetime.now().date())
			db.session.add(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			subscr = db.session.query(Subscribe).filter_by(UsPhId = UsPhIdMain, ShopId = ShopId).first()
			db.session.delete(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)



# *********************************************** #
# Actions with post of shop

# Get post information
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which post we looking
# PostId

# Output:
# 200 - OK
# 500 - Back Error


# Take post to UserPh Favouroite
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which post we looking
# PostId

# Output:
# 201 - Created
# 500 - Back Error


# Add post to UserPh Backet
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which post we looking
# PostId

# Input:
# backet=true

# Output:
# 201 - Created
# 500 - Back Error


# Delete post from UserPh Favouroite
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which post we looking
# PostId

# Output:
# 200 - OK
# 500 - Back Error




# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3/Post5
# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3/Post5
# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3/Post5?backet=true
# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3/Post5
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Shops/Feed<ShopId>/Post<PostId>', methods = ['GET', 'POST', 'DELETE'])
def post_sh(UsPhIdMain, ShopId, PostId):
	if request.method == 'GET':
		try:
			post = db.session.query(Post).filter_by(PostId = PostId).first()
			return make_response(jsonify({'Status': 'OK', 'Body': post.serialize}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			if args.get("backet") == 'true':
				back = Backet(
					UsPhId = UsPhIdMain,
					PostId = PostId,
					ShopId = ShopId,
					CreateDate = datetime.now().date())
				db.session.add(back)
				db.session.commit()
				return make_response(jsonify({'Status': 'Created'}), 201)
			else:
				fav = Favourite(
					UsPhId = UsPhIdMain,
					PostId = PostId,
					ProductFlg = True,
					ShopId = ShopId,
					CreateDate = datetime.now().date())
				db.session.add(fav)
				db.session.commit()
				return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			fav = db.session.query(Favourite).filter_by(UsPhId = UsPhIdMain, PostId = PostId).first()
			db.session.delete(fav)
			db.session.commit()
			# query(Favourite).filter(Favourite.UsPhId == UsPhId).filter(Favourite.PostId == PostId).delete(synchronize_session = 'fetch')
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)


# *********************************************** #
# Get all comments of the post
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which post we looking
# PostId

# Output:
# 200 - OK
# 500 - Back Error


# Post a new comment
# Input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which post we looking
# PostId

# Input:
# Comment text

# Output:
# 201 - Created
# 400 - Front Error
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3/Post5/Comments
# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3/Post5/Comments?text=My new comment for testing product posts
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Shops/Feed<ShopId>/Post<PostId>/Comments', methods = ['GET', 'POST'])
def comments_sh(UsPhIdMain, ShopId, PostId):
	if request.method == 'GET':
		try:
			result = db.session.query(Comment).filter_by(PostId = PostId).order_by(Comment.CreateDate).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [comm.serialize for comm in result]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			comm = Comment(
				Text = args.get("text"),
				LikesCnt = 0,
				PostId = PostId,
				ShopId_p = ShopId,
				UsPhId_c = UsPhIdMain,
				CreateDate = datetime.now().date())
			db.session.add(comm)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except (TypeError, NameError, ValueError) as exp:
			return make_response(jsonify({'Error': str(exp)}), 400)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)

# *********************************************** #
# Edit Comment of the post
# input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which post we looking
# PostId
# ComId

# Input:
# Comment text to edit

# Output:
# 200 - OK
# 400 - Front Error
# 500 - Back Error


# Delete comment of the post
# input in EndPoint:
# UsPhIdMain, who looking
# ShopId, which post we looking
# PostId
# ComId

# Output:
# 200 - OK
# 500 - Back Error

# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3/Post5/Comments/Comment3?text=text updated
# http://127.0.0.1:5000/Root/UserPh1/Shops/Feed3/Post5/Comments/Comment3
# *********************************************** #

@app.route('/Root/UserPh<UsPhIdMain>/Shops/Feed<ShopId>/Post<PostId>/Comments/Comment<ComId>', methods = ['PUT', 'DELETE'])
def edit_comments_sh(UsPhIdMain, ShopId, PostId, ComId):
	if request.method == 'PUT':
		try:
			args = request.args.to_dict()
			comm = db.session.query(Comment).filter_by(PostId = PostId, ComId = ComId).first()

			comm.Text = args.get("text")

			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except (TypeError, NameError, ValueError) as exp:
			return make_response(jsonify({'Error': str(exp)}), 400)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			comm = db.session.query(Comment).filter_by(PostId = PostId, ComId = ComId).first()
			db.session.delete(comm)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)








# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** SUGGESTIONS Users *********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# *********************************************** #
# Get UserPh Suggestions for another Users
# Input in EndPoint:
# UsPhId

# Output:
# 200 - OK
# 500 - Back Error


# Make a subscribe for another user from list view
# Input in EndPoint:
# UsPhId

# Input:
# UsPhIdForSubscr

# Output:
# 201 - Created
# 500 - Back Error


# Cancel subscribe for another user from list view
# Input in EndPoint:
# UsPhId

# Input:
# UsPhIdForSubscr 

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Suggestions/Users
# http://127.0.0.1:5000/Root/UserPh1/Suggestions/Users?usphidforsubscr=2
# http://127.0.0.1:5000/Root/UserPh1/Suggestions/Users?usphidforsubscr=2
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Suggestions/Users', methods = ['GET', 'POST', 'DELETE'])
def sugg_ph_us(UsPhId):
	pass




# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** SUGGESTIONS Shops *********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# *********************************************** #
# Get UserPh Suggestions for Shops
# Input in EndPoint:
# UsPhId

# Output:
# 200 - OK
# 500 - Back Error


# Make a subscribe for Shop from list view
# Input in EndPoint:
# UsPhId

# Input:
# ShopId

# Output:
# 201 - Created
# 500 - Back Error


# Cancel subscribe for Shop from list view
# Input in EndPoint:
# UsPhId

# Input:
# ShopId

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Suggestions/Shops
# http://127.0.0.1:5000/Root/UserPh1/Suggestions/Shops?shopid=3
# http://127.0.0.1:5000/Root/UserPh1/Suggestions/Shops?shopid=3
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Suggestions/Shops', methods = ['GET', 'POST', 'DELETE'])
def sugg_ph_sh(UsPhId):
	pass





# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** Subscribers Users *********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #



# *********************************************** #
# Get UserPh Subscribers 
# Input in EndPoint:
# UsPhId

# Output:
# 200 - OK
# 500 - Back Error


# Make a subscribe for another user from list view
# Input in EndPoint:
# UsPhId

# Input:
# UsPhIdForSubscr

# Output:
# 201 - Created
# 500 - Back Error


# Cancel subscribe for another user from list view
# Input in EndPoint:
# UsPhId

# Input:
# UsPhIdForSubscr

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Subscribers/Users
# http://127.0.0.1:5000/Root/UserPh1/Subscribers/Users?usphidforsubscr=2
# http://127.0.0.1:5000/Root/UserPh1/Subscribers/Users?usphidforsubscr=2
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Subscribers/Users', methods = ['GET', 'POST', 'DELETE'])
def subscrs_ph_us(UsPhId):
	if request.method == 'GET':
		try:
			# Getting all UsPhId's for which current user have a subscribe
			result = db.session.query(Subscribe).filter(Subscribe.UsPhIdForSubscr == UsPhId).order_by(Subscribe.SubscrDate).all()
			subrs_id = [sub['UsPhId'] for sub in [subscr.serialize_u for subscr in result]]
			# Getting Users by thos UsPhId's
			users = db.session.query(PhysEntity).filter(PhysEntity.UsPhId.in_(subrs_id)).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [us.serialize_short for us in users]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			subscr = Subscribe(
				UsPhId = UsPhId,
				UsPhIdForSubscr = args.get("usphidforsubscr"),
				SubscrDate = datetime.now().date())
			db.session.add(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			args = request.args.to_dict()
			subscr = db.session.query(Subscribe).filter_by(UsPhId = UsPhId, UsPhIdForSubscr = args.get("usphidforsubscr")).first()
			db.session.delete(subscr)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)





# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** FAVOURITES *********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# *********************************************** #
# Get UserPh Favourites 
# Input in EndPoint:
# UsPhId

# Output:
# 200 - OK
# 500 - Back Error


# Take post to backet
# Input in EndPoint:
# UsPhId

# Input:
# PostId
# ShopId
# backet = true

# Output:
# 201 - Created
# 500 - Back Error


# Take post to favourites back
# Input in EndPoint:
# UsPhId

# Input:
# PostId
# ShopId

# Output:
# 201 - Created
# 500 - Back Error


# Delete post from favourites
# Input in EndPoint:
# UsPhId

# Input:
# PostId
# ShopId

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Favourites/ShPosts
# http://127.0.0.1:5000/Root/UserPh1/Favourites/ShPosts?shopid=3&postid=5
# http://127.0.0.1:5000/Root/UserPh1/Favourites/ShPosts?shopid=3&postid=5&backet=true
# http://127.0.0.1:5000/Root/UserPh1/Favourites/ShPosts?shopid=3&postid=5
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Favourites/ShPosts', methods = ['GET', 'POST', 'DELETE'])
def favs_sh(UsPhId):
	if request.method == 'GET':
		try:
			# Getting all UsPhId's favourite posts of shops, their PostIds
			result = db.session.query(Favourite).filter(Favourite.UsPhId == UsPhId, Favourite.ProductFlg == True).all()
			post_id = [f['PostId'] for f in [fav.serialize_sh for fav in result]]
			# Getting Posts with theese PostId
			posts = db.session.query(Post).filter(Post.PostId.in_(post_id)).order_by(Post.CreateDate).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [post.serialize for post in posts]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			if args.get("backet") == 'true':
				back = Backet(
					UsPhId = UsPhId,
					PostId = args.get("postid"),
					ShopId = args.get("shopid"),
					CreateDate = datetime.now().date())
				db.session.add(back)
				db.session.commit()
				return make_response(jsonify({'Status': 'Created'}), 201)
			else:
				fav = Favourite(
					UsPhId = UsPhId,
					PostId = args.get("postid"),
					ShopId = args.get("shopid"),
					ProductFlg = True,
					CreateDate = datetime.now().date())
				db.session.add(fav)
				db.session.commit()
				return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			args = request.args.to_dict()
			fav = db.session.query(Favourite).filter_by(UsPhId = UsPhId, PostId = args.get("postid"), ShopId = args.get("shopid")).first()
			db.session.delete(fav)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)


# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** SAVED *********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# *********************************************** #
# Get UserPh Saved 
# Input in EndPoint:
# UsPhId

# Output:
# 200 - OK
# 500 - Back Error



# Take post to Saved back
# Input in EndPoint:
# UsPhId

# Input:
# PostId

# Output:
# 201 - Created
# 500 - Back Error


# Delete post from Saved
# Input in EndPoint:
# UsPhId

# Input:
# PostId

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Favourites/UsPosts
# http://127.0.0.1:5000/Root/UserPh1/Favourites/UsPosts?postid=3
# http://127.0.0.1:5000/Root/UserPh1/Favourites/UsPosts?postid=3
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Favourites/UsPosts', methods = ['GET', 'POST', 'DELETE'])
def favs_us(UsPhId):
	if request.method == 'GET':
		try:
			# Getting all UsPhId's favourite posts of users, their PostIds
			result = db.session.query(Favourite).filter(Favourite.UsPhId == UsPhId, Favourite.ProductFlg == False).all()
			post_id = [f['PostId'] for f in [fav.serialize_us for fav in result]]
			# Getting Posts with theese PostId
			posts = db.session.query(Post).filter(Post.PostId.in_(post_id)).order_by(Post.CreateDate).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [post.serialize for post in posts]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			fav = Favourite(
				UsPhId = UsPhId,
				PostId = args.get("postid"),
				ProductFlg = False,
				CreateDate = datetime.now().date())
			db.session.add(fav)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			args = request.args.to_dict()
			fav = db.session.query(Favourite).filter_by(UsPhId = UsPhId, PostId = args.get("postid")).first()
			db.session.delete(fav)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)




# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** BACKET *********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# *********************************************** #
# Get UserPh Backet 
# Input in EndPoint:
# UsPhId

# Output:
# 200 - OK
# 500 - Back Error



# Take post to Backet back
# Input in EndPoint:
# UsPhId

# Input:
# PostId
# ShopId

# Output:
# 201 - Created
# 500 - Back Error


# Delete post from Backet
# Input in EndPoint:
# UsPhId

# Input:
# PostId
# ShopId

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Backet
# http://127.0.0.1:5000/Root/UserPh1/Backet?postid=5&shopid=3
# http://127.0.0.1:5000/Root/UserPh1/Backet?postid=5&shopid=3
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Backet', methods = ['GET', 'POST', 'DELETE'])
def baket_sh(UsPhId):
	if request.method == 'GET':
		try:
			# Getting all UsPhId's posts in backet, their PostIds
			result = db.session.query(Backet).filter(Backet.UsPhId == UsPhId).all()
			post_id = [b['PostId'] for b in [back.serialize for back in result]]
			# Getting Posts with theese PostId
			posts = db.session.query(Post).filter(Post.PostId.in_(post_id)).order_by(Post.CreateDate).all()
			return make_response(jsonify({'Status': 'OK', 'Body': [post.serialize for post in posts]}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			back = Backet(
				UsPhId = UsPhId,
				PostId = args.get("postid"),
				ShopId = args.get("shopid"),
				CreateDate = datetime.now().date())
			db.session.add(back)
			db.session.commit()
			return make_response(jsonify({'Status': 'Created'}), 201)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			args = request.args.to_dict()
			back = db.session.query(Backet).filter_by(UsPhId = UsPhId, PostId = args.get("postid"), ShopId = args.get("shopid")).first()
			db.session.delete(back)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)






# *********************************************** #
# Get information about post in backet
# Input in EndPoint:
# UsPhId
# BackId

# Output:
# 200 - OK
# 500 - Back Error


# Make an order
# Input in EndPoint:
# UsPhId
# BackId

# Input:
# add=true
# cntitems
# sumcost
# deliveryflg
# deliverycost
# deliverydate
# orderstatuscode
# getitemway
# checklink
# orderqrlink


# Output:
# 201 - Created
# 400 - Front Error
# 500 - Back Error


# Delete Post from Backet
# Input in EndPoint:
# UsPhId
# BackId

# Output:
# 200 - OK
# 500 - Back Error


# Return Post to Backet
# Input in EndPoint:
# UsPhId
# BackId

# Input:
# PostId
# ShopId

# Output:
# 201 - Created
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Backet/Back5?add=true&postid=5&shopid=3&cntitems=4&sumcost=400&deliveryflg=True&deliverycost=40&deliverydate=2022-09-04&getitemway=1&checklink=link&orderqrlink=qrlink
# http://127.0.0.1:5000/Root/UserPh1/Backet/Back4?postid=5&shopid=3
# http://127.0.0.1:5000/Root/UserPh1/Backet/Back4
# *********************************************** #

@app.route('/Root/UserPh<UsPhId>/Backet/Back<BackId>', methods = ['GET', 'POST', 'DELETE'])
def order_add(UsPhId, BackId):
	if request.method == 'GET':
		try:
			back = db.session.query(Backet).filter(Backet.BackId == BackId).first()
			post = db.session.query(Post).filter_by(PostId = back.PostId).first()
			return make_response(jsonify({'Status': 'OK', 'Body': post.serialize}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'POST':
		try:
			args = request.args.to_dict()
			if args.get("add") == 'true':
				order = Order(
					CntItems = args.get("cntitems"),
					SumCost = args.get("sumcost"),
					DeliveryFlg = (args.get("deliveryflg") == 'True'),
					DeliveryCost = args.get("deliverycost"),
					DeliveryDate = args.get("deliverydate"),
					OrderStatusCode = 1,
					GetItemWay = args.get("getitemway"),
					CheckLink = args.get("checklink"),
					OrderQRLink = args.get("orderqrlink"),
					PostId = args.get("postid"),
					ShopId = args.get("shopid"),
					UsPhId = UsPhId,
					BackId = BackId,
					CreateDate = datetime.now().date(),
					UpdateStDate = datetime.now().date())
				db.session.add(order)
				db.session.commit()
				return make_response(jsonify({'Status': 'Created'}), 201)
			else:
				back = Backet(
					UsPhId = UsPhId,
					PostId = args.get("postid"),
					ShopId = args.get("shopid"),
					CreateDate = datetime.now().date())
				db.session.add(back)
				db.session.commit()
				return make_response(jsonify({'Status': 'Created'}), 201)
		except (TypeError, NameError, ValueError) as exp:
			return make_response(jsonify({'Error': str(exp)}), 400)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			back = db.session.query(Backet).filter_by(BackId = BackId, UsPhId = UsPhId).first()
			db.session.delete(back)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)





# *********************************************** #
# Get All Orders
# Input in EndPoint:
# UsPhId

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Orders
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Orders', methods = ['GET'])
def get_orders(UsPhId):
	try:
		result = db.session.query(Order).filter_by(UsPhId = UsPhId).order_by(Order.CreateDate).all()
		return make_response(jsonify({'Status': 'OK', 'Body': [order.serialize for order in result]}), 200)
	except Exception as exp:
		return make_response(jsonify({'Error': str(exp)}), 500)



# *********************************************** #
# Get Order information
# Input in EndPoint:
# UsPhId
# OrderId

# Output:
# 200 - OK
# 500 - Back Error


# Cancel Order
# Input in EndPoint:
# UsPhId
# OrderId

# Output:
# 200 - OK
# 500 - Back Error


# http://127.0.0.1:5000/Root/UserPh1/Orders/Order1
# http://127.0.0.1:5000/Root/UserPh1/Orders/Order1
# *********************************************** #
@app.route('/Root/UserPh<UsPhId>/Orders/Order<OrderId>', methods = ['GET', 'DELETE'])
def order_edit(UsPhId, OrderId):
	if request.method == 'GET':
		try:
			order = db.session.query(Order).filter_by(OrderId = OrderId).first()
			return make_response(jsonify({'Status': 'OK', 'Body': order.serialize}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)
	elif request.method == 'DELETE':
		try:
			order = db.session.query(Order).filter_by(OrderId = OrderId).first()
			db.session.delete(order)
			db.session.commit()
			return make_response(jsonify({'Status': 'OK'}), 200)
		except Exception as exp:
			return make_response(jsonify({'Error': str(exp)}), 500)


# *********************************************** #
# Update Status of Order
# Input in EndPoint
# OrderId

# Input:
# StatusCode

# Output:
# 200 - OK
# 400 - Front Error
# 500 - Back Error


# http://127.0.0.1:5000/Root/Order2?statuscode=2
# *********************************************** #
@app.route('/Root/Order<OrderId>', methods = ['POST'])
def status_update(OrderId):
	try:
		args = request.args.to_dict()
		order = db.session.query(Order).filter(Order.OrderId == OrderId).first()
		order.OrderStatusCode = args.get("statuscode")
		db.session.commit()
		return make_response(jsonify({'Status': 'OK'}), 200)
	except (TypeError, NameError, ValueError) as exp:
		return make_response(jsonify({'Error': str(exp)}), 400)
	except Exception as exp:
		return make_response(jsonify({'Error': str(exp)}), 500)






# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# *********************************************** Else*********************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #
# ****************************************************************************************************************************************************************************************************************************************************************************************** #


# @app.route('/Fav/<nickname>', methods = ['GET', 'POST'])
# def temp_foo(nickname):
# 	fav = Favourite(2, 2, 2)
# 	db.session.add(fav)
# 	db.session.commit()
# 	return "Its done"


# www.example.com/search?name=John&location=Miami

# def foo():
# 	args = request.args
# 	return args
# args.to_dict()
# args.get("name")