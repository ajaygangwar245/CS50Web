from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util

# displays homepage
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# converts markdown content to HTML
def md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    # checks if entry exists or not
    if content == None:
        return None
    else:
        return markdowner.convert(content)          # if entry exists convert content MD to HTML

# display each entry page
def entry(request, title):
    html_content = md_to_html(title)
    # if html page doesn't exists
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Requested page does not exists."                # error message
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,                                             # title of page
            "content": html_content                                     # html content of page
        })

# search among existing pages
def search(request):
    if request.method == 'POST':
        entry_search = request.POST['q']                                # entry searched by user
        html_content = md_to_html(entry_search)                         # get content of searched query
        if html_content is not None:                                    # when query matches with entry in system
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
        else:                                                           # if query doesn't matches entry
            all_entries = util.list_entries()                           # list of all stored entries 
            recommendations = []
            for entry in all_entries:                               
                if entry_search.lower() in entry.lower():               # check if search query is substring of any entry 
                    recommendations.append(entry)                       # add it new list
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendations                       # render new list on search page 
            })
        
# to create a new page
def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title) is not None:                           # if title entered by user already exists
            return render(request, "encyclopedia/error.html", {
                "message": "This page already exists."
            })
        else:
            util.save_entry(title, content)                             # if title does not exist then save page as entry
            html_content = md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })
        

# edit any page
def edit(request):
    if request.method == "POST":
        title = request.POST['page_title']                              # fetch title from the page 
        content = util.get_entry(title)                                 # fetch content using same title
        return render(request, "encyclopedia/edit.html", {              # takes user to edit page
            "title": title,
            "content": content
        })
    
# to save edited page
def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
    
# takes user to random entry page
def random_page(request):
    all_entries = util.list_entries()
    title = random.choice(all_entries)
    html_content = md_to_html(title)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })
