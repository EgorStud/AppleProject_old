from flask import url_for
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     nickname = db.Column(db.String(64), index = True, unique = True)
#     email = db.Column(db.String(120), index = True, unique = True)
#     role = db.Column(db.SmallInteger, default = ROLE_USER)

#     def __repr__(self):
#         return '<User %r>' % (self.nickname)
# Метод __repr__ говорит Python как выводить объекты этого класса.

class PhysEntity(db.Model):
	UsPhId = db.Column(db.Integer, nullable = False, primary_key = True)
	NickName = db.Column(db.String(20), nullable = False)
	Password = db.Column(db.String(20), nullable = False)
	FIO = db.Column(db.String(40), nullable = False)
	BirthDate = db.Column(db.Date, nullable = False)
	Email = db.Column(db.String(40), nullable = False)
	PhoneNumber = db.Column(db.String(20), nullable = False)
	Agreement = db.Column(db.Boolean, nullable = False)
	CreateDate = db.Column(db.Date, nullable = False)
	UpdateDate = db.Column(db.Date, nullable = False)
	UpdateUsId = db.Column(db.Integer, nullable = False)

	@property
	def serialize_short(self):
		return {'UsPhId': self.UsPhId,
	    'NickName': self.NickName,
		'FIO': self.FIO}

	@property
	def serialize(self):
		return {'UsPhId': self.UsPhId,
	    'NickName': self.NickName,
		'FIO': self.FIO,
		'BirthDate': self.BirthDate,
		'Email': self.Email,
		'PhoneNumber': self.PhoneNumber}

	def __repr__(self):
		return '<Ph User %r>' % (self.NickName)


class Subscribe(db.Model):
	SubscrId = db.Column(db.Integer, nullable = False, primary_key = True)
	UsPhId = db.Column(db.Integer, nullable = False)
	UsPhIdForSubscr = db.Column(db.Integer, nullable = True)
	ShopId = db.Column(db.Integer, nullable = True)
	# UsLegId = db.Column(db.Integer, nullable = True) - This is unnecessary information
	SubscrDate = db.Column(db.Date, nullable = False)

	@property
	def serialize_u(self):
		return {
		'UsPhIdForSubscr': self.UsPhIdForSubscr,
		'UsPhId': self.UsPhId}

	@property
	def serialize_sh(self):
		return {'ShopId': self.ShopId}

	def __repr__(self):
		return '<Subscribe %r>' % (self.SubscrId) 


class Favourite(db.Model):
	FavId = db.Column(db.Integer, nullable = False, primary_key = True)
	UsPhId = db.Column(db.Integer, nullable = False) # Кто добавляет в избранное 
	PostId = db.Column(db.Integer, nullable = False)
	ShopId = db.Column(db.Integer, nullable = True)
	ProductFlg = db.Column(db.Boolean, nullable = False)
	CreateDate = db.Column(db.Date, nullable = False)

	# def __init__(self, UsPhId, PostId, ShopId, ProductFlg):
	# 	self.UsPhId = UsPhId
	# 	self.PostId = PostId
	# 	self.ShopId = ShopId
	# 	self.ProductFlg = ProductFlg

	@property
	def serialize_sh(self):
		return {'UsPhId': self.UsPhId,
		'ShopId': self.ShopId,
		'PostId': self.PostId}

	@property
	def serialize_us(self):
		return {'UsPhId': self.UsPhId,
		'PostId': self.PostId}


	def __repr__(self):
		return '<Ph Favourite %r>' % (self.FavId)


class Backet(db.Model):
	BackId = db.Column(db.Integer, nullable = False, primary_key = True)
	UsPhId = db.Column(db.Integer, nullable = False)
	PostId = db.Column(db.Integer, nullable = False)
	ShopId = db.Column(db.Integer, nullable = False)
	CreateDate = db.Column(db.Date, nullable = False)

	# def __init__(self, UsPhId, PostId, ShopId):
	# 	self.UsPhId = UsPhId
	# 	self.PostId = PostId
	# 	self.ShopId = ShopId

	@property
	def serialize(self):
		return {'UsPhId': self.UsPhId,
		'ShopId': self.ShopId,
		'PostId': self.PostId}


	def __repr__(self):
		return '<Ph Backet %r>' % (self.BackId)


class LegEntity(db.Model):
	UsLegId = db.Column(db.Integer, nullable = False, primary_key = True)
	NickName = db.Column(db.String(20), nullable = False)
	Password = db.Column(db.String(20), nullable = False)
	FIO = db.Column(db.String(40), nullable = False)
	CompanyName = db.Column(db.String(40), nullable = False)
	PhoneNumber = db.Column(db.String(20), nullable = False)
	ImgAvId = db.Column(db.Integer, nullable = True)
	Email = db.Column(db.String(40), nullable = False)
	AdressFact1 = db.Column(db.String(80), nullable = False)
	AdressFact2 = db.Column(db.String(80), nullable = True)
	AdressFact3 = db.Column(db.String(80), nullable = True)
	AdressLeg = db.Column(db.String(80), nullable = False)
	Agreement = db.Column(db.Boolean, nullable = False)
	Acct_no = db.Column(db.String(34), nullable = False)
	Kor_no = db.Column(db.String(20), nullable = False)
	Bik = db.Column(db.String(10), nullable = False)
	Kpp = db.Column(db.String(10), nullable = False)
	Ogrn = db.Column(db.String(15), nullable = False)
	Inn = db.Column(db.String(12), nullable = False)
	ProviderFIO = db.Column(db.String(40), nullable = False)
	ProviderPhoneNumber = db.Column(db.String(20), nullable = True)
	ProviderEmail = db.Column(db.String(40), nullable = True)
	CreateDate = db.Column(db.Date, nullable = False)
	UpdateDate = db.Column(db.Date, nullable = False)
	UpdateUsId = db.Column(db.Integer, nullable = False)

	def __repr__(self):
		return '<Leg User %r>' % (self.NickName)


class AvaFile(db.Model):
	ImgId = db.Column(db.Integer, nullable = False, primary_key = True)
	FileFormat = db.Column(db.String(10), nullable = False)
	FileBody = db.Column(db.Boolean, nullable = True)
	UsLegId = db.Column(db.Integer, nullable = False)

	def __repr__(self):
		return '<AvaFile %r>' % (self.ImgId)


class Post(db.Model):
	PostId = db.Column(db.Integer, nullable = False, primary_key = True)
	ProductFlg = db.Column(db.Boolean, nullable = False)
	DescrShort = db.Column(db.String(100), nullable = True)
	DescrFull = db.Column(db.String(400), nullable = True)
	LikesCnt = db.Column(db.Integer, nullable = False)
	ProductName = db.Column(db.String(40), nullable = True)
	AvailibleFlg = db.Column(db.Boolean, nullable = True)
	Cost = db.Column(db.Integer, nullable = True)
	UsLegId = db.Column(db.Integer, nullable = True)
	ShopId = db.Column(db.Integer, nullable = True)
	UsPhId = db.Column(db.Integer, nullable = True)
	Topic_1 = db.Column(db.String(20), nullable = True)
	Topic_2 = db.Column(db.String(20), nullable = True)
	Topic_3 = db.Column(db.String(20), nullable = True)
	Topic_4 = db.Column(db.String(20), nullable = True)
	Topic_5 = db.Column(db.String(20), nullable = True)
	Topic_6 = db.Column(db.String(20), nullable = True)
	Topic_7 = db.Column(db.String(20), nullable = True)
	Topic_8 = db.Column(db.String(20), nullable = True)
	Topic_9 = db.Column(db.String(20), nullable = True)
	Topic_10 = db.Column(db.String(20), nullable = True)
	CreateDate = db.Column(db.Date, nullable = False)

	@property
	def serialize(self):
		return {'ProductFlg': self.ProductFlg,
		'DescrShort': self.DescrShort,
		'DescrFull': self.DescrFull,
		'LikesCnt': self.LikesCnt,
		'Topic_1': self.Topic_1,
		'Topic_2': self.Topic_2,
		'Topic_3': self.Topic_3,
		'Topic_4': self.Topic_4,
		'Topic_5': self.Topic_5,
		'Topic_6': self.Topic_6,
		'Topic_7': self.Topic_7,
		'Topic_8': self.Topic_8,
		'Topic_9': self.Topic_9,
		'Topic_10': self.Topic_10,
		'CreateDate': self.CreateDate}

	def __repr__(self):
		return '<Post %r>' % (self.PostId)


class PostFile(db.Model):
	FileId = db.Column(db.Integer, nullable = False, primary_key = True)
	FileType = db.Column(db.String(10), nullable = False)
	FileFormat = db.Column(db.String(10), nullable = False)
	FileBody = db.Column(db.Boolean, nullable = True)
	QRFlg = db.Column(db.Boolean, nullable = False)
	PostId = db.Column(db.Integer, nullable = False)
	CreateDate = db.Column(db.Date, nullable = False)

	def __repr__(self):
		return '<PostFile %r>' % (self.FileId)	


class Comment(db.Model):
	ComId = db.Column(db.Integer, nullable = False, primary_key = True)
	Text = db.Column(db.String(200), nullable = False)
	LikesCnt = db.Column(db.Integer, nullable = False)
	PostId = db.Column(db.Integer, nullable = False)
	UsPhId_p = db.Column(db.Integer, nullable = True)
	ShopId_p = db.Column(db.Integer, nullable = True)
	UsPhId_c = db.Column(db.Integer, nullable = False)
	# UsLegId_c = db.Column(db.Integer, nullable = True)
	CreateDate = db.Column(db.Date, nullable = False)

	@property
	def serialize(self):
		return {'Text': self.Text,
		'LikesCnt': self.LikesCnt,
		# 'PostId': self.PostId,
		'UsPhId_p': self.UsPhId_p,
		'ShopId_p': self.ShopId_p,
		'UsPhId_c': self.UsPhId_c,
		# 'UsLegId_c': self.UsLegId_c, - Они не могут оставлять комментарии
		'CreateDate': self.CreateDate}

	def __repr__(self):
		return '<Comment %r>' % (self.ComId)


class Shop(db.Model):
	ShopId = db.Column(db.Integer, nullable = False, primary_key = True)
	ShopName = db.Column(db.String(40), nullable = False)
	DescrShort = db.Column(db.String(100), nullable = False)
	DescrFull = db.Column(db.String(400), nullable = True)
	UsLegId = db.Column(db.Integer, nullable = False)
	Topic_1 = db.Column(db.String(20), nullable = True)
	Topic_2 = db.Column(db.String(20), nullable = True)
	Topic_3 = db.Column(db.String(20), nullable = True)
	Topic_4 = db.Column(db.String(20), nullable = True)
	Topic_5 = db.Column(db.String(20), nullable = True)
	Topic_6 = db.Column(db.String(20), nullable = True)
	Topic_7 = db.Column(db.String(20), nullable = True)
	Topic_8 = db.Column(db.String(20), nullable = True)
	Topic_9 = db.Column(db.String(20), nullable = True)
	Topic_10 = db.Column(db.String(20), nullable = True)
	CreateDate = db.Column(db.Date, nullable = False)

	@property
	def serialize_short(self):
		return {'ShopName': self.ShopName,
	    'DescrShort': self.DescrShort,
		'Topic_1': self.Topic_1,
		'Topic_2': self.Topic_2,
		'Topic_3': self.Topic_3,
		'Topic_4': self.Topic_4,
		'Topic_5': self.Topic_5,
		'Topic_6': self.Topic_6,
		'Topic_7': self.Topic_7,
		'Topic_8': self.Topic_8}

	@property
	def serialize(self):
		return {'ShopName': self.ShopName,
	    'DescrShort': self.DescrShort,
	    'DescrFull': self.DescrFull,
		'Topic_1': self.Topic_1,
		'Topic_2': self.Topic_2,
		'Topic_3': self.Topic_3,
		'Topic_4': self.Topic_4,
		'Topic_5': self.Topic_5,
		'Topic_6': self.Topic_6,
		'Topic_7': self.Topic_7,
		'Topic_8': self.Topic_8,
		'Topic_9': self.Topic_9,
		'Topic_10': self.Topic_10}

	def __repr__(self):
		return '<Shop %r>' % (self.ShopName)


class Delivery(db.Model):
	DelId = db.Column(db.Integer, nullable = False, primary_key = True)
	MinDaysMKAD = db.Column(db.Integer, nullable = True)
	MinDaysMO = db.Column(db.Integer, nullable = True)
	MinDaysRF = db.Column(db.Integer, nullable = True)
	CostMKAD = db.Column(db.Integer, nullable = True)
	CostMO = db.Column(db.Integer, nullable = True)
	CostRF = db.Column(db.Integer, nullable = True)
	ShopId = db.Column(db.Integer, nullable = False)
	UsLegId = db.Column(db.Integer, nullable = False)
	CreateDate = db.Column(db.Date, nullable = False)
	UpdateDate = db.Column(db.Date, nullable = False)

	def __repr__(self):
		return '<Delivery %r>' % (self.DelId)


class Order(db.Model):
	OrderId= db.Column(db.Integer, nullable = False, primary_key = True)
	CntItems = db.Column(db.Integer, nullable = False)
	SumCost = db.Column(db.Integer, nullable = False)
	DeliveryFlg = db.Column(db.Boolean, nullable = False)
	DeliveryCost = db.Column(db.Integer, nullable = True)
	DeliveryDate = db.Column(db.Date, nullable = True)
	OrderStatusCode = db.Column(db.Integer, nullable = False)
	GetItemWay = db.Column(db.Integer, nullable = False)
	CheckLink = db.Column(db.String(60), nullable = False)
	OrderQRLink = db.Column(db.String(20), nullable = True)
	PostId = db.Column(db.Integer, nullable = False)
	ShopId = db.Column(db.Integer, nullable = False)
	# UsLegId = db.Column(db.Integer, nullable = False) - Мне нужно только название магазина, какое мне дело до ника владельца
	# UsLegNickName = db.Column(db.String(20), nullable = False)
	UsPhId = db.Column(db.Integer, nullable = False)
	BackId = db.Column(db.Integer, nullable = False)
	CreateDate = db.Column(db.Date, nullable = False)
	UpdateStDate = db.Column(db.Date, nullable = False)

	@property
	def serialize(self):
		return {'CntItems': self.CntItems,
	    'SumCost': self.SumCost,
	    'DeliveryFlg': self.DeliveryFlg,
		'DeliveryCost': self.DeliveryCost,
		'DeliveryDate': self.DeliveryDate,
		'OrderStatusCode': self.OrderStatusCode,
		'GetItemWay': self.GetItemWay,
		'CheckLink': self.CheckLink,
		'OrderQRLink': self.OrderQRLink,
		'CreateDate': self.CreateDate,
		'UpdateStDate': self.UpdateStDate}

	def __repr__(self):
		return '<Order %r>' % (self.OrderId)


class OrderArch(db.Model):
	OrderId = db.Column(db.Integer, nullable = False, primary_key = True)
	CntItems = db.Column(db.Integer, nullable = False)
	SumCost = db.Column(db.Integer, nullable = False)
	DeliveryFlg = db.Column(db.Boolean, nullable = False)
	DeliveryCost = db.Column(db.Integer, nullable = True)
	DeliveryDate = db.Column(db.Date, nullable = True)
	OrderStatusCode = db.Column(db.Integer, nullable = False)
	GetItemWay = db.Column(db.Integer, nullable = False)
	PostId = db.Column(db.Integer, nullable = False)
	ShopId = db.Column(db.Integer, nullable = False)
	# UsLegId = db.Column(db.Integer, nullable = False)
	# UsLegNickName = db.Column(db.String(20), nullable = False)
	UsPhId = db.Column(db.Integer, nullable = False)
	BackId = db.Column(db.Integer, nullable = False)
	CreateDate = db.Column(db.Date, nullable = False)
	UpdateStDate = db.Column(db.Date, nullable = False)

	def __repr__(self):
		return '<Archived Order %r>' % (self.OrderId)


class Map_Topic(db.Model):
	TopicId = db.Column(db.Integer, nullable = False, primary_key = True)
	TopicExpl = db.Column(db.String(100), nullable = False)

	def __repr__(self):
		return '<Topic %r>' % (self.TopicExpl)


class Map_Status(db.Model):
	StatusId = db.Column(db.Integer, nullable = False, primary_key = True)
	StatusExpl = db.Column(db.String(100), nullable = False)

	def __repr__(self):
		return '<Status %r>' % (self.StatusExpl)


class Map_GetItemWay(db.Model):
	GiwId = db.Column(db.Integer, nullable = False, primary_key = True)
	GiwExpl = db.Column(db.String(100), nullable = False)

	def __repr__(self):
		return '<Giw %r>' % (self.GiwExpl)


 # = db.Column(db.String(), nullable = False)
 # = db.Column(db.Integer, nullable = False)
 # = db.Column(db.Date, nullable = False)
 # = db.Column(db.Boolean, nullable = False)









































