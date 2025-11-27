# Book App (Flask + SQLite)

A simple Flask web application to manage a list of books. Users can add book details like title, author, and published date, and view them on the homepage.

## Project Structure

```
book_app/
├── data_preprocessing/       # Placeholder for future data tasks
├── database/                 # Contains the SQLite DB
├── website/                 
│   ├── app.py                # Flask web app
│   └── templates/            # HTML templates
│       ├── index.html
│       └── add_book.html
├── requirements.txt          # Python dependencies
└── README.md
```

## Setup

```bash
cd book_app
pip install -r requirements.txt
python website/app.py
```

Then open `http://localhost:5000` in your browser.
