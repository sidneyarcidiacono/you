"""Import from our you_app package and run app."""
from you_app import app, db

if __name__ == "__main__":
    app.run(debug=True)
