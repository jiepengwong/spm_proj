from flask import Blueprint, jsonify, request
from ..models import db, Role, Jobrole,Course,Skill,Staff,Learningjourney,Registration

jobrole = Blueprint('jobroleroute', __name__)
# TO CALL API, USE /jobrole/<route>
# Replace and change this. This is just dummy data for you to follow the format
@jobrole.route('/viewall')
def viewAllJobroles():
    course = Jobrole.query.all()
    coursearray = []
    for item in course:
        coursearray.append(
        item.to_dict()
    )
    if course:
        return jsonify(
            {   
                "code": 200,
                "data": coursearray
            }
        ),200
    else:
        return jsonify(
            {   
                "code": 404,
                "data": "Error!"
            }
        ),200

@jobrole.route('/hraddjobrole',methods=['POST'])
def hraddskills():
    print("Hello!")
    data = request.get_json()
    jobrole_name = data['jobrole_name']
    department = data['jobrole_desc']
    jobrole_desc = data['jobrole_desc']
    jobrole_status = data['jobrole_status']


    if Jobrole.query.filter_by(jobrole_name=jobrole_name).first():
        return jsonify({
            "code":404,
            "message": "There exist such a Skill Name in the Database. Please check your input fields."
        })
    jobrolenew = Jobrole( jobrole_name=jobrole_name,department=department,jobrole_desc=jobrole_desc,jobrole_status=jobrole_status)
    try:
        print("adding session")
        db.session.add(jobrolenew)
        db.session.commit()

        return jsonify({
            "code": 200,
            "message": "Job role has been added successfully!"
        })
    except:
        print("Error")
        return jsonify({
            "code":500,
            "message": "There is error with creating a new jobrole."
        })

# Might use this again
# def route1():
#     staff = Jobrole.query.first()
#     #remove when jp push 
#     skill1 = Skill(skill_id=4,skill_name= "Conflict Management Skill Advanced",skill_desc= "Able to handle team and customer conflict effectively.",skill_status=1)
#     skill2 = Skill(skill_id=5,skill_name= "Conflict Management Skill Advanced 2",skill_desc= "Able to handle team and customer conflict effectively.",skill_status=1)
#     # Simulate assigning and adding new skills
#     staff.skills.append(skill1)
#     staff.skills.append(skill2)

    
#     array = []

#     for item in staff.skills:
#         array.append(
#             item.to_dict()
#         )
        

#     return jsonify(
#         {   
#             "jobrole" : staff.to_dict(),
#             "skillassociated": array
#         }
#     )


# @jobrole.route('/jobrole/')
# def route2():
#     jobroles = Jobrole.query.all()
#     return jsonify(
#         {
#             "data": [jobrole.to_dict() for jobrole in jobroles]
#         }
#     )


