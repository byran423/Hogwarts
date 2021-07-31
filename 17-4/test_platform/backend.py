import sqlalchemy
from flask import Flask, json, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello():
    return "Hogwarts"


@app.route("/login", methods=["GET", "POST"])
def hello_name():
    if request.method == "GET":
        return f'hello, get from {request.args.get("name","hogwarts")}'
    elif request.method == "POST":
        return f'hello, post from {request.args.get("name","hogwarts")}'


testcases = []


class TestCaseList:
    def __init__(self, name, description, steps):
        self.name = name
        self.description = description
        self.steps = steps

    def as_dict(self):
        return {"name": self.name, "description": self.description, "steps": self.steps}


class TestCaseServier(Resource):
    def get(self):
        app.logger.info(request.args)
        return testcases

    def post(self):
        app.logger.info(request.args)
        app.logger.info(request.json)
        testcase = TestCaseList(**request.json)
        testcase.steps = json.dumps(request.json.get("steps"))
        app.logger.info(testcase.as_dict())
        testcases.append(testcase.as_dict())
        return {"error": 0, "msg": "OK"}


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    steps = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return "<TestCase %r>" % self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TestCaseServierOrm(Resource):
    def get(self):
        app.logger.info(request.args)
        case_id = request.args.get("id")
        if case_id:
            case_data = TestCase.query.filter_by(id=case_id).first()
            testcases = [case_data.as_dict()]
        else:
            case_data = TestCase.query.all()
            testcases = [i.as_dict() for i in case_data]
        return testcases

    def post(self):
        app.logger.info(request.args)
        app.logger.info(request.json)
        app.logger.info(json.dumps(request.json.get("steps")))
        try:
            testcase = TestCase(**request.json)
            testcase.steps = json.dumps(request.json.get("steps"))
            app.logger.info(testcase)
            db.session.add(testcase)
            db.session.commit()
            db.session.close()
            return {"error": 0, "msg": "OK"}
        except:
            return {"error": 1, "msg": "server failed"}


api.add_resource(TestCaseServier, "/testcase")
api.add_resource(TestCaseServierOrm, "/testcase_orm")


if __name__ == "__main__":
    # db.drop_all()
    db.create_all()
    app.run(debug=True, use_reloader=True)
