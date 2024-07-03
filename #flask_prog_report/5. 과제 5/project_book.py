from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_book import Base, BookStore, BookItem

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:root@localhost/bookstore')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# 1. JSON return 함수 구현 할 것
@app.route('/bookstores/<int:bookstore_id>/booklist/JSON')
def bookListJSON(bookstore_id):
    store=session.query(BookStore).filter_by(id=bookstore_id).one() # bookstore 클래스에서 param값과 일치하는 store READ
    # 해당 북스토어의 책들을 '전부' READ한다.
    lists=session.query(BookItem).filter_by(
        bookstore_id=bookstore_id).all()
    return jsonify(booklist=[i.serialize for i in lists])
#jsonify 함수로 serialize해서 넘겨준다.


# 2. bookList 함수 구현 할 것 (booklist.html template 구축해야 함)
@app.route('/')
@app.route('/bookstores/<int:bookstore_id>/booklist')
def bookList(bookstore_id=None):
    if bookstore_id == None:
        bookstore_id = 1 # bookstore id initialization
    store=session.query(BookStore).filter_by(id=bookstore_id).one() # 입력 url값과 같은 bookstore를 하나 READ하고 해당 store의 책들을 READ한다.
    lists=session.query(BookItem).filter_by(bookstore_id=bookstore_id)
    return render_template(
        'booklist.html',store=store,lists=lists,bookstore_id=bookstore_id)
#rendering template 함수로 html파일에 인자를 전달

# 3. newBookItem 함수 구현 할 것 (newbook.html template 구축해야 함)
@app.route('/bookstores/<int:bookstore_id>/new', methods=['GET', 'POST'])
def newBookItem(bookstore_id):
    if request.method == 'POST':
        newBook = BookItem(name=request.form['name'],price=request.form['price'],bookstore_id=bookstore_id)
        session.add(newBook)
        session.commit()
        #POST방식일 때, 새로운 책 obj를 생성해주고, add(INSERT)한 후 HDD에 commit까지 해준다.
        return redirect(url_for('bookList',bookstore_id=bookstore_id))
        #redirection으로 list 확인
    else:
        # 다른 METHOD 방식일 떄 html load
        return render_template('newbook.html',bookstore_id=bookstore_id)


# 4. editBookItem 함수 구현 할 것 (editbook.html template 구축해야 함)
@app.route('/bookstores/<int:bookstore_id>/<int:book_id>/edit',
           methods=['GET', 'POST'])
def editBookItem(bookstore_id, book_id):
    editedBook=session.query(BookItem).filter_by(id=book_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedBook.name=request.form['name']
        if request.form['price']:
            editedBook.price=request.form['price']
        # request에 맞게 아이템을 수정해주고 UPDATE까지 완료한다.
        session.add(editedBook)
        session.commit()
        # INSERT와 COMMIT까지 완료
        return redirect(url_for('bookList',bookstore_id=bookstore_id))
        # redirect로 UPDATE 확인
    else:
        # GET 방식일경우 HTML로 LOAD
        return render_template(
            'editbook.html',bookstore_id=bookstore_id,book_id=book_id,book=editedBook)
        


# 5. deleteBookItem 함수 구현 할 것 (deletebook.html template 구축해야 함)
@app.route('/bookstores/<int:bookstore_id>/<int:book_id>/delete',
           methods=['GET', 'POST'])
def deleteBookItem(bookstore_id, book_id):
    bookToDel = session.query(BookItem).filter_by(id=book_id).one()
    # 삭제할 책 READ
    if request.method =='POST':
        session.delete(bookToDel)
        # DELETE
        # 이후 진행은 이전 방식들과 동일함
        session.commit()
        return redirect(url_for('bookList',bookstore_id=bookstore_id))
    else:

        return render_template('deletebook.html',book=bookToDel)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
