from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def MainStore():
    context={
        'title':"Одежда"
    }
    return render_template("MainStore.html",**context)
@app.route('/Footwear/')
def FootwearStore():
    context = {
        'title': "Обувь"
    }
    return render_template("Footwear.html", **context)
@app.route('/Jacket/')
def JacketStore():
    context = {
        'title': "Куртки"
    }
    return render_template("Jacket.html", **context)
if __name__=="__main__":
    app.run(debug=True)