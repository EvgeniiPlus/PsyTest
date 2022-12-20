from flask import Flask, render_template, request, redirect, flash, url_for
import json
from db import app, db, Value


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
    print(names_list)
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
            print(
                f'Вы набрали {sum} баллов. У Вас рефлексивный (устойчивый) уровень готовности к профессиональной самореализации')
        return redirect('/')
    else:
        with open('static/question.json', encoding='utf-8') as f:
            questions_dict = json.load(f)
        return render_template('test.html', questions=questions_dict)


@app.route('/biblio_list')
def biblio_list():
    return render_template('bibliographic_list.html')


@app.route('/inventory')
def inventory():
    values = db.session.query(Value)
    return render_template('inventory.html', values=values)

@app.route('/inventory/add', methods=['GET', 'POST'])
def add_inventory():
    if request.method == 'POST':
        newValue= Value(
            inventory_number=request.form['inventory_number'],
            name=request.form['name'],
            unit = request.form['unit'],
            quantity = request.form['quantity'],
            cost = request.form['cost'],
            employee = request.form['employee'],
            room = request.form['room'],
            fin_account = request.form['fin_account'],
            financial_source = request.form['financial_source'],

        )
        db.session.add(newValue)
        db.session.commit()
        return redirect(url_for('inventory'))
    else:
        return render_template('add_inventory.html')

@app.route('/inventory/edit/<value_id>', methods=['GET', 'POST'])
def editValue(value_id):
    editedValue = db.session.query(Value).filter_by(id=value_id).one()
    if request.method == 'POST':
        editedValue.inventory_number = request.form['inventory_number']
        editedValue.name = request.form['name']
        editedValue.unit = request.form['unit']
        editedValue.quantity = request.form['quantity']
        editedValue.cost = request.form['cost']
        editedValue.employee = request.form['employee']
        editedValue.room = request.form['room']
        editedValue.fin_account = request.form['fin_account']
        editedValue.financial_source = request.form['financial_source']
        db.session.add(editedValue)
        db.session.commit()
        return redirect(url_for('inventory'))
    else:
        return render_template('editValue.html', value=editedValue)

@app.route('/inventory/delete/<value_id>', methods=['GET', 'POST'])
def deleteValue(value_id):
    deletedValue = db.session.query(Value).filter_by(id=value_id).one()
    if request.method == 'POST':
        db.session.delete(deletedValue)
        db.session.commit()
        return redirect(url_for('inventory'))
    else:
        return render_template('deleteValue.html', value=deletedValue)

@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

