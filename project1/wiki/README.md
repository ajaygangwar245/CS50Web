# Wiki: A Wikipedia-like Online Encyclopedia

## Video Demo
`URL` : [Youtube](https://youtu.be/a1mqkEr1m2s)

## Overview

Wiki is a lightweight online encyclopedia that allows users to create, edit, search, and browse encyclopedia entries. Entries are stored in Markdown for easy editing and converted to HTML for viewing. The project is built using the Django framework.

---

## Features

1. **Entry Page**  
   - Visiting `/wiki/TITLE` displays the content of an encyclopedia entry with the title `TITLE`.
   - If the entry does not exist, the user sees an error page.

2. **Index Page**  
   - Displays a list of all available encyclopedia entries.
   - Each entry name is clickable and redirects to its corresponding page.

3. **Search**  
   - Users can search for entries using a search bar.
   - If the search query matches an entry, the user is redirected to that entry's page.
   - If the query is a substring of any entry, a list of matching entries is displayed.

4. **Create New Page**  
   - Users can create new encyclopedia entries by providing a title and Markdown content.
   - If an entry with the same title exists, the user is shown an error message.

5. **Edit Page**  
   - Users can edit existing entries using a pre-populated form with the current Markdown content.
   - Edited content is saved, and the user is redirected to the updated entry.

6. **Random Page**  
   - A "Random Page" link allows users to visit a random entry.

7. **Markdown to HTML Conversion**  
   - Markdown content is converted to HTML for rendering on entry pages.
   - The `markdown2` library is used for this purpose (install with `pip3 install markdown2`).

---

## Getting Started

### Prerequisites
- Python 3.8+
- Django 3.0+
- `markdown2` library (`pip3 install markdown2`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ajaygangwar245/project1/wiki.git

2. Navigate to the project directory:
   ```bash
   cd wiki

3. Install dependencies:
   ```bash
   pip3 install markdown2

4. Run the development server:
   ```bash
   python manage.py runserver

### Accessing the Application
Visit http://127.0.0.1:8000 in your browser to start using the application.

### File Structure
- `encyclopedia/urls.py`: URL routing for the application.
- `encyclopedia/util.py`: Utility functions for interacting with entries.
   - `list_entries()`: Returns a list of all entry names.
   - `save_entry(title, content)`: Saves an entry with a title and Markdown content.
   - `get_entry(title)`: Retrieves an entry's Markdown content or None if it does not exist.
- `entries/`: Directory where all encyclopedia entries are stored as Markdown files.
- `templates/`: HTML templates for pages.
- `static/`: CSS and static files for the application.

### Application Structure
`Index Page`: Dynamically generates a list of all entries on homepage.

`Entry Page`: Displays each Markdown file entry as HTML content page.

`Error Page`: Displays error as HTML page, if occurs.

`Search`: Implements substring search and redirects to search results or entry pages.

`New Page`: Creates new page and validates title uniqueness before saving.

`Edit Page`: Pre-populates a form with the current Markdown content and allows to edit that.

`Random Page`: Selects and redirects to a random entry page.

## Acknowledgments
- CS50’s Web Programming with Python & JavaScript Course for the project idea.
- Google for inspiration and reference.