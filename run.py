from application import init_app

app = init_app()

if __name__ == "__main__":
    app.run(host="127.0.0.0",port=9566,debug = True)