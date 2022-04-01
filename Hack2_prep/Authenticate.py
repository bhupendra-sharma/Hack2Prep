from crypt import methods
import datetime
import secrets

# tokens = {}

def signup(role,req,db,Actor):
    req = req.get_json()
    # print(req)
    
    username = req['username']
    password = req['password']
    actor = Actor.query.filter_by(username = username,role = role).count()
    print(actor)
    if actor > 0:
        return {'err_msg':'User with this role already exist'}
    actor = Actor(username = username , password = password , role = role)
    db.session.add(actor)
    db.session.commit()

    return {'info_msg':'Successfully added'}

def login(role,req,Actor):
    req = req.get_json()
    username = req['username']
    password = req['password']
    actor = Actor.query.filter_by(username = username,password = password , role = role).count()
    print(actor)
    if actor == 0:
        return {'err_msg':'User not found'}

    token = secrets.randbits(8)
    actor = Actor.query.filter_by(username = username,password = password , role = role).first()
    return {'token':token,'succ_msg':'Authentication Successfull','username':actor.username}