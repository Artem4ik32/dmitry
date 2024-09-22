from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    endpoints = [rule.endpoint for rule in app.url_map.iter_rules()]
    return render_template('index.html')

@app.get('/menu')
def menu():
    sort_order = request.args.get('sort', 'asc')
    pizzas = [
        {"name": "Маргарита", "ingredients": "Томатний соус, моцарела, базилік", "price": 190},
        {"name": "Гавайська", "ingredients": "Соус, моцарела, ананаси", "price": 300},
        {"name": "Карбонара", "ingredients": "Сливочный соус, пармезан, моцарела, бекон", "price": 290},
    ]
    
    if sort_order == 'asc':
        pizzas = sorted(pizzas, key=lambda x: x['price'])
    elif sort_order == 'desc':
        pizzas = sorted(pizzas, key=lambda x: x['price'], reverse=True)
    
    return render_template('menu.html', menu_items=pizzas)

if __name__ == '__main__':
    app.run(debug=True)
