from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

data_store = {}


@app.route('/')
def home():

    return render_template("index.html")


@app.route('/internships', methods=['POST'])
def internships():

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    qualification = request.form['qualification']
    gender = request.form['gender']
    skill_level = request.form['skill_level']

    skill = request.form['skill']
    domain = request.form['domain']
    company = request.form['company']

    resume = request.files['resume']

    if resume:

        filename = resume.filename.lower()

        allowed_extensions = (
            '.pdf',
            '.doc',
            '.docx'
        )

        if filename.endswith(allowed_extensions):

            resume.save(os.path.join(
                app.config['UPLOAD_FOLDER'],
                resume.filename
            ))

        else:

            return "❌ Only Resume Files Allowed (PDF/DOC/DOCX)"

    data_store['name'] = name
    data_store['email'] = email
    data_store['phone'] = phone

    data_store['qualification'] = qualification
    data_store['gender'] = gender
    data_store['skill_level'] = skill_level

    data_store['skill'] = skill
    data_store['domain'] = domain
    data_store['company'] = company

    return render_template(

        "internships.html",

        name=name,
        email=email,
        phone=phone,

        qualification=qualification,
        gender=gender,
        skill_level=skill_level,

        skill=skill,
        domain=domain,
        company=company
    )


@app.route('/success')
def success():

    skill = data_store.get('skill')

    return render_template(
        "success.html",
        skill=skill
    )


@app.route('/offer-letter')
def offer_letter():

    return render_template(

        "offer_letter.html",

        name=data_store.get('name'),
        qualification=data_store.get('qualification'),
        skill_level=data_store.get('skill_level'),

        skill=data_store.get('skill'),
        domain=data_store.get('domain'),
        company=data_store.get('company')
    )


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)