import os

from flask import Flask

from lend.db import init_db


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return "Lend is running."

    return app


def main():
    init_db()
    port = int(os.environ.get("PORT", "5000"))
    app = create_app()
    # use_reloader=False keeps this to one process. The reloader would spawn a second one.
    app.run(host="0.0.0.0", port=port, use_reloader=False)


if __name__ == "__main__":
    main()