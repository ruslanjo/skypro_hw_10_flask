import json
from flask import Flask

with open('candidates.json', 'r', encoding='utf-8') as candidates_json:
    candidates = json.load(candidates_json)

app = Flask(__name__)


@app.route("/")
def page_index():
    index_page = '<pre>'
    for candidate in candidates:
        name = candidate.get('name')
        desired_position = candidate.get('position')
        skills = candidate.get('skills')

        index_page += f'Имя кандидата - {name}<br>' \
                      f'Позиция кандидата - {desired_position}<br>' \
                      f'Навыки: {skills}<br><br>'
    index_page += '<pre>'
    return index_page


@app.route("/candidates/<uid>")
def candidates_page(uid):
    candidate = candidates[int(uid) - 1]
    return f'<img src="{candidate.get("picture")}"<br>' \
           f'<pre>' \
           f'Имя кандидата - {candidate.get("name")}<br>' \
           f'Позиция кандидата - {candidate.get("position")}<br>' \
           f'Навыки: {candidate.get("skills")}<br>' \
           f'<pre>'


@app.route("/skills/<skill>")
def skills_page(skill):
    skills_page = '<pre>'
    for candidate in candidates:
        skills = candidate.get("skills").split(', ')
        skills = [skill.lower() for skill in skills]

        if skill.lower() in skills:
            skills_page += f'Имя кандидата - {candidate.get("name")}<br>' \
                           f'Позиция кандидата - {candidate.get("position")}<br>' \
                           f'Навыки: {candidate.get("skills")}<br><br>'
    skills_page += '<pre>'
    return skills_page


app.run(port=2406)
