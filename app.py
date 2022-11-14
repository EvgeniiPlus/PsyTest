from flask import Flask, render_template, request, redirect, flash, url_for
import json

app = Flask(__name__)


def counter(file):
    i = 0
    names_list = []
    with open(file, encoding='utf-8') as f:
        questions = json.load(f)
    for key, value in questions.items():
        i += 1
        c = 0
        if questions[key] == "":
            continue
        for v in value[1:]:
            c += 1
            names_list.append(f'{i}-{c}')
    # print(names_list)
    return names_list


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tests')
def tests():
    return render_template('tests.html')


@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        sum = 0
        names_list = counter('static/question.json')
        for i in names_list:
            # print()
            sum += int(request.form[i])
        flash(sum)
        if sum <= 331:
            print(f'Вы набрали {sum} баллов. У Вас адаптивный уровень готовности к профессиональной самореализации')
        elif 332 <= sum <= 497:
            print(f'Вы набрали {sum} баллов. У Вас репродуктивный уровень готовности к профессиональной самореализации')
        elif 498 <= sum <= 748:
            print(f'Вы набрали {sum} баллов. У Вас продуктивный уровень готовности к профессиональной самореализации')
        elif 749 <= sum:
            print(f'Вы набрали {sum} баллов. У Вас рефлексивный (устойчивый) уровень готовности к профессиональной самореализации')
        return redirect('/')
    else:
        with open('static/question.json', encoding='utf-8') as f:
            questions_dict = json.load(f)
        return render_template('test.html', questions=questions_dict)

@app.route('/biblio_list')
def biblio_list():

    return render_template('bibliographic_list.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
