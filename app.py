import os

from flask import Flask, redirect, render_template, request, url_for

from lend.catalog import CatalogError, ToolIsOut, ToolNotFound, add_tool, list_tools, retire_tool
from lend.db import connect, database_summary, init_db
from lend.loans import (
    LoanError,
    LoanNotFound,
    MemberNotFound,
    ToolUnavailable,
    add_member,
    borrow_tool,
    list_available_tools,
    list_members,
    list_open_loans,
    return_tool,
)


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template("home.html", summary=database_summary())

    @app.get("/tools")
    def tools():
        connection = connect()
        try:
            items = list_tools(connection)
        finally:
            connection.close()
        return render_template("tools.html", tools=items, error=request.args.get("error"))

    @app.post("/tools")
    def create_tool():
        connection = connect()
        try:
            add_tool(connection, request.form.get("name", ""), request.form.get("category", ""))
        except CatalogError as error:
            items = list_tools(connection)
            return render_template("tools.html", tools=items, error=str(error))
        finally:
            connection.close()
        return redirect(url_for("tools"))

    @app.post("/tools/<int:tool_id>/retire")
    def retire(tool_id):
        connection = connect()
        try:
            retire_tool(connection, tool_id)
        except ToolNotFound as error:
            return redirect(url_for("tools", error=str(error)))
        except ToolIsOut as error:
            return redirect(url_for("tools", error=str(error)))
        finally:
            connection.close()
        return redirect(url_for("tools"))

    @app.get("/loans")
    def loans():
        connection = connect()
        try:
            return render_template(
                "loans.html",
                members=list_members(connection),
                tools=list_available_tools(connection),
                loans=list_open_loans(connection),
                error=request.args.get("error"),
            )
        finally:
            connection.close()

    @app.post("/members")
    def create_member():
        connection = connect()
        try:
            add_member(connection, request.form.get("name", ""), request.form.get("email", ""))
        except LoanError as error:
            return redirect(url_for("loans", error=str(error)))
        finally:
            connection.close()
        return redirect(url_for("loans"))

    @app.post("/loans")
    def create_loan():
        connection = connect()
        try:
            borrow_tool(
                connection,
                int(request.form.get("tool_id", "0")),
                int(request.form.get("member_id", "0")),
            )
        except ValueError:
            return redirect(url_for("loans", error="Choose a member and an available tool."))
        except (MemberNotFound, ToolUnavailable) as error:
            return redirect(url_for("loans", error=str(error)))
        finally:
            connection.close()
        return redirect(url_for("loans"))

    @app.post("/loans/<int:loan_id>/return")
    def return_loan(loan_id):
        connection = connect()
        try:
            return_tool(connection, loan_id)
        except LoanNotFound as error:
            return redirect(url_for("loans", error=str(error)))
        finally:
            connection.close()
        return redirect(url_for("loans"))

    return app


def main():
    init_db()
    port = int(os.environ.get("PORT", "5000"))
    app = create_app()
    # use_reloader=False keeps this to one process. The reloader would spawn a second one.
    app.run(host="0.0.0.0", port=port, use_reloader=False)


if __name__ == "__main__":
    main()
