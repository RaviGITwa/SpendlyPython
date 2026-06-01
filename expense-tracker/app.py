from flask import Flask, render_template, session, redirect, url_for
from database.db import get_db, init_db, seed_db

app = Flask(__name__)
app.secret_key = "dev-secret"

with app.app_context():
    init_db()
    seed_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    return "Logout — coming in Step 3"


@app.route("/profile")
def profile():
    if not session.get("user_id"):
        return redirect(url_for("login"))

    user = {
        "name": "Alex Johnson",
        "email": "alex.johnson@example.com",
        "initials": "AJ",
        "member_since": "January 2024",
    }
    stats = {
        "total_spent": "₹24,850",
        "transaction_count": 12,
        "top_category": "Food & Dining",
    }
    transactions = [
        {"date": "2024-05-28", "description": "Swiggy Order",         "category": "Food & Dining",  "amount": "₹450"},
        {"date": "2024-05-26", "description": "Monthly Rent",          "category": "Housing",        "amount": "₹12,000"},
        {"date": "2024-05-24", "description": "Metro Card Recharge",   "category": "Transport",      "amount": "₹500"},
        {"date": "2024-05-20", "description": "Groceries — DMart",     "category": "Food & Dining",  "amount": "₹1,850"},
        {"date": "2024-05-15", "description": "Netflix Subscription",  "category": "Entertainment",  "amount": "₹649"},
    ]
    categories = [
        {"name": "Housing",       "amount": "₹12,000", "pct": 48},
        {"name": "Food & Dining", "amount": "₹6,300",  "pct": 25},
        {"name": "Transport",     "amount": "₹2,500",  "pct": 10},
        {"name": "Entertainment", "amount": "₹1,800",  "pct": 7},
        {"name": "Other",         "amount": "₹2,250",  "pct": 10},
    ]
    return render_template(
        "profile.html",
        user=user,
        stats=stats,
        transactions=transactions,
        categories=categories,
    )


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
