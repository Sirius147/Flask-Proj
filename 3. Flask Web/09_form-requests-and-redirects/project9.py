from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:root@localhost/restaurant')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    if restaurant_id == None:
        restaurant_id = 1
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

# Task 1: Create route for newMenuItem function here


@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
# 실행 순서 : 1) else문의 newmenuitem.html 실행,
#            2) create button click하면 form tag의 action에 있는 url 실행 (if문 실행)
#            3) if문의 마지막 함수인 redirect를 부르면 restaurantMenu 함수를 실행
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(
            # request.form['name'] : form tag의 name에 들어가 있는 string
            name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        # redirect : 다른 url로 이동
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:   # request.method == 'GET'
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# Task 2: Create route for editMenuItem function here


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
