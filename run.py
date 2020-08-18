import flask_toy.app as ap

if __name__ == "__main__":

    app = ap.create_app(1)
    app.run()