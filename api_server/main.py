
from xestore.api.app import make_app

app = make_app()

if __name__ == '__main__':
    from xestore.api.app import make_local_app
    app = make_app()
    app.run(host="localhost", debug=True, ) #ssl_context="adhoc"
    