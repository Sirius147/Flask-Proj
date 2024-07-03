from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:root@localhost/restaurant')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# url : http://localhost/restaurants/1/
@app.route('/restaurants/<int:restaurant_id>/')
# restaurant_id 변수에 값이 1이 들어옴
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
