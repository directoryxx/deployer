from app import app, db

from app.models import Instruction, WhiteList
from app.schema import instruction_schema,instruction_schemas
from flask import request, jsonify, make_response
from middleware import Middleware
from services.slack import Slack
from config import Config
from services.google import Google
from services.ssh import SSH

# app.wsgi_app = Middleware(app.wsgi_app)

# endpoint to CREATE instruction
@app.route("/instruction", methods=["POST"])
def create_instruction():
    try:
        user = request.json['user']

        if 'short_desc' in request.json:
            short_desc = request.json['short_desc']
        else:
            short_desc = ""
        
        step = request.json['step']
        command = request.json['command']
        tag = request.json['tag']
        target = request.json['target']

        new_category = Instruction(user, step, command, tag, short_desc,target)

        db.session.add(new_category)
        db.session.commit()

        result = instruction_schema.dump(new_category)

        data = {
            'message': 'New Instruction Created!',
            'status': 201,
            'data': result
        }
        return make_response(jsonify(data))
    except:
        data = {
            'message': 'Error!',
            'status': 500,
        }
        return make_response(jsonify(data),500)

@app.route("/instruction", methods=["GET"])
def get_instruction():
    try:
        args = request.args
        tag = args.get("tag")
        getInstruction = Instruction.query.filter_by(tag=tag).all()
        result = instruction_schemas.dump(getInstruction)

        slack = Slack()
        slack.send_message(Config.SUNNY,"Test")

        data = {
            'message': 'Get Specified Tag!',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data))
    except (KeyError):
        data = {
            'message': 'Error!',
            'status': 500,
        }
        return make_response(jsonify(data),500)


@app.route("/deploy", methods=["POST"])
def execute_deploy():
    try:
        tag = request.json['tag']

        google = Google()

        slack = Slack()
        slack.send_message(Config.RAIN,"Getting Information",tag)

        target = google.get_instance_ip(tag)

        slack.send_message(Config.SUNNY,"Get "+str(len(target))+" IPs",tag)

        slack.send_message(Config.RAIN,"Starting Deploy",tag)

        getInstruction = Instruction.query.filter_by(tag=tag).all()
        result = instruction_schemas.dump(getInstruction)
        counter = 0

        for ip in target:
            counter += 1
            for data in result:
                slack.send_message(Config.RAIN,data['short_desc']+"("+str(counter)+"/"+str(len(target))+")",tag)
                external = SSH()
                external.connect(data['user'], ip, data['command'])

        slack.send_message(Config.SUNNY,"Deployed Complete",tag)


        result = "ok"
        
        data = {
            'message': 'Deployed '+tag,
            'status': 201,
            'data': result
        }
        return make_response(jsonify(data))
    except:
        data = {
            'message': 'Error!',
            'status': 500,
        }
        return make_response(jsonify(data),500)