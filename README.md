# Welcome to Dog Eared Books!
Link to PWS deployement: [Dog Eared Books](http://athazahra-nabila-dogearedbooks.pbp.cs.ui.ac.id/)  
By Athazahra Nabila Ruby - 2306173113  
Platform Based Programming KKI 2024/2025

<details>
<Summary><b>Assignment 2</b></summary>

## Step-by-Step Project Implementation
A breakdown of what I did to execute this project:
### Creating the Django project
1. I made a new directory "dog-eared-books" to store the contents of this project
2. I installed a virtual inviroment in the "book_store" directory by running this command on the terminal:
    ```
   python3 -m venv env
   ```
3. Then I activated it with the command:
    ```
   source env/bin/activate
   ```
4. I created the file "requirement.txt" and edited it by using VS Code to add the required the dependencies:
   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
5. Then I installed the dependencies with the command:
    ```
    pip install -r requirements.txt
    ```
6. I created a new Django project named "book_store" with the command 
    ```
    django-admin startproject book_store .
    ```
7. After the project was installed, I added "localhost" and "127.0.0.1" to the ALLOWED_HOSTS in the settings.py file.

### Creating an application with the name main in the project.
8. I created a new application named main with the command:
    ```
    python manage.py startapp main
    ```
9. After the main application was installed, I added 'main' to the INSTALLED_APPS list in the settings.py file to signify the presence of the main application.

### Creating a Template
10. To create a template, I created a templates directory (within the main directory) and added a main.html file that would serve as the template.
11. I filled the template with the necessary components (application name, name, class)

### Creating Models
12. I added a model in the models.py file called Product, which has the necessary attributes name, price, and description, and i also added other attributes that relate to my shop, namely release_date and genre.
13. I then performed migrations to apply my model with the commands:
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

### Connecting View with Template
14. I filled the views.py file with a function called show_main that will "send" data to the template if a request is made from the template, which includes app_name, name, and class.

### Configuring URLs
15. I created a urls.py file in the main application and added the following code to configure the routing in the application:
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
16. Then, I edited the urls.py in the book_store project for overall project with:
    ```
    from django.urls import path, include

    urlpatterns = [
        path('', include('main.urls')),
    ]
    ```

### Git and PWS Deployment
17. I created a new repository on GitHub and connected it to the local repository by runnning git init.
18. After the connection was established, I performed add, commit, and push actions to the remote GitHub repository.
19. To deploy to PWS, I created a new project titled 'dogearedbooks' on the PWS website then added my PWS deployement URL to the ALLOWED_HOSTS list in settings.py.
20. Finally, I connected the repository to PWS and pushed it to the PWS repository for deployment.
21. I'm finished!


## Diagram
![Diagram](images/pbp_diagram.jpg)

## The use of git in software development
Git is a version control system that helps developers track changes in their codebase, making it easier to manage and collaborate on projects. It allows multiple developers to work on the same project simultaneously, supports branching and merging, and provides a history of all changes, enabling easy rollback to previous versions if needed.


## Why Django?
I believe that one of the reasons Django was chosen is because it uses Python, a language we have been studying since the first semester. This allows students to focus directly on platform-based programming concepts without having to learn a new syntax, as they are already familiar with Python.

## Why are Django Models Called ORMs?
Django models are called ORMs (Object Relational Mapping) because of their nature of directly converting data into tables. As a result, developers don't need to interact directly with data tables like in SQL but can create and access data directly from the model.

</details>

<details>
<Summary><b>Assignment 3</b></summary>

## Step-by-Step Project Implementation

### Setting up template
1. Firstly, I created a new templates folder in the root directory and added base.html that functions as a base view to ensure a consistent design throughout the website and minimize code duplication.
2. To adjust to the changes, I added BASE_DIR / 'templates' in settings.py to the DjangoTemplates DIR field.
3. Then I adjusted my main.html file to use base.html as the main template.

### Creating an input form
4. First, I added an UUID to correctly identify each book and did a model migration.
```
class BookEntry(modelsModel):
    ...
   id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
   ...
``` 
5. Then, I created the file forms.py which is used to create the structure of the form that can accept entries or new item data. It contains:
```
from django.forms import ModelForm
from main.models import BookEntry

class BookEntryForm(ModelForm):
    class Meta:
        model = BookEntry
        fields = ["title", "author", "price", "genre", "summary"]
```
6. On views.py, I imported redirect and created a new function which implemented the form and validates the inputs.
```
def create_book_entry(request):
    form = BookEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_book_entry.html", context)
```
7. I modified the show_main function so that it stores all of the entries.
```
def show_main(request):
    book_entries = BookEntry.objects.all()

    context = {
        'application_name': 'dog-eared-books',
        'class': 'PBP KKI',
        'name': 'Athazahra Nabila Ruby',
        'book_entries': book_entries
    }

    return render(request, "main.html", context)
```
8. I then imported the create_book_entry function to urls.py and implemented its URL routing by adding:
```
urlpatterns = [
   ...
   path('create-book-entry', create_book_entry, name='create_book_entry')
]
```
9. I created create_book_entry.html to add a HTML page on submitting the entries, it contains:
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Book Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Book Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
10. Then I modified my main.html to add a button that redirects to the entry submission and displays said entries as a table:
```
...
{% if not book_entries %}
<p>Sorry, there are no books available!</p>
{% else %}
<table>
  <tr>
    <th>Title</th>
    <th>Author</th>
    <th>Price</th>
    <th>Genre</th>
    <th>Summary</th>
  </tr>

  {% comment %} This is how to display book data
  {% endcomment %} 
  {% for book_entry in book_entries %}
  <tr>
    <td>{{book_entry.title}}</td>
    <td>{{book_entry.author}}</td>
    <td>{{book_entry.price}}</td>
    <td>{{book_entry.genre}}</td>
    <td>{{book_entry.summary}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_book_entry' %}">
  <button>Add New book Entry</button>
</a>
{% endblock content %}
```

### Adding views
11. I added 4 functions to views.py to access data in the form of XML, JSON, and both by IDs
```
def show_xml(request):
    data = BookEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BookEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = BookEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = BookEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Creating URL routing to each view
12. I then imported those 4 functions to urls.py then implemented their URL routing by adding:
```
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
13. Lastly, I deployed the changes I made to PWS and Github.
14. I'm done!

## Why do we need data delivery in implementing a platform?
In the process of implementing a platform, data delivery is important because it facilitates communication between clients, servers, and other systems. This process ensures that information can be sent quickly, securely, and efficiently. Without proper data delivery, the platform would feel slow and inefficient, which could reduce user interest.

## Which is better, XML or JSON? Why is JSON more popular than XML?
In my opinion, JSON is better and more popular than XML because JSON has a simpler structure and appearance, making it easier for humans to read. Moreover, JSON processing tends to be faster and more efficient for data exchange due to its lower complexity compared to XML.

## What is the usage of is_valid() in Django forms? Why do we need the method in forms?
The is_valid() method in Django forms is used to check the validity of the data entered. If the data entered meets the form's requirements (such as data type, data length), then is_valid() will return True, otherwise, it will return False. This method is needed because it verifies and ensures that the data to be entered into the database is correct. Additionally, this method simplifies management in case there are errors when the entered data is not valid.

## Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?
The csrf_token is important to protect web applications from Cross-Site Request Forgery (CSRF) attacks, where an attacker can trick an authenticated user into sending malicious requests to the server without their knowledge. Without a csrf_token, the server cannot differentiate between a legitimate request and a malicious one, allowing attackers to abuse the user’s session to perform unintended actions. Therefore, the csrf_token ensures that every request originates from a legitimate and secure source.

## Postman Screenshots
XML
![XML](images/pbp_xml.jpg)

XML by ID
![XMLID](images/pbp_xmlid.jpg)

JSON
![JSON](images/pbp_json.jpg)

SON by ID
![JSONID](images/pbp_jsonid.jpg)

</details>


<details>
<Summary><b>Assignment 4</b></summary>

## Step-by-Step Project Implementation

### Implement the register, login, and logout functions & using data from cookies
1. I first activated the virtual enviroment by running:
```
source env/bin/activate
```
2. In views.py, I imported:
- UserCreationForm to implement the register function
- AuthenticationForms, authenticate, and login to implement the login function
- logout to implement the logout functions 
- datetime, HttpResponseRedirect, and reverse to use cookies. 
I then added those three functions (register, login, logout) to the file:
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
3. To use cookies for the login, I modified show_main:
```
def show_main(request):
...
                'last_login': request.COOKIES['last_login'],
        }
        return render(request, "main.html", context)  
...
```

4. I created an HTML file called "register.html" to display the register page.
```
{% extends 'base.html' %} {% block meta %}
<title>Register</title>
{% endblock meta %} {% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Register" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
5. I created an HTML file called "login.html" to display the login page.
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
6. I also created a "logout" button and displayed the last login data on the main page by adding this to main.html:
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>

<h5>Last login session: {{ last_login }}</h5>
```
7. Next, I performed URL routing by importing the register, login, and logout functions to urls.py then added these paths to urlpatterns:
```
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```
8. To force users to login before accessing the site, I imported login_required to views.py then added the restriction to the show_main function:
```
@login_required(login_url='/login')
```

### Make two user accounts with three dummy data each
9. I created two acounts on my page, namely "voicemail337" and "dogears" and I added some book entries.  
voicemail337:
![voicemail337](images/voicemail337.jpg)
dogears:
![dogears](images/dogears.jpg)

### Connect the models Product (BookEntry) and User
10. In models.py, I imported User then modified my BookEntry class by adding:
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
11. In views.py, I modified show_main so that only authorized users can view their Product models. I also modified create_book_entry to modify the user field before saving it to the database
```
def show_main(request):
    book_entries = BookEntry.objects.filter(user=request.user)

    context = {
        ...
        'name': request.user.username,
        ...
    }

def create_book_entry(request):
    form = BookEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        book_entry = form.save(commit=False)
        book_entry.user = request.user
        book_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_book_entry.html", context)
```
12. Lastly, I did model migrations by running
```
python manage.py makemigrations
python manage.py migrate
```

## What is the difference between HttpResponseRedirect() and redirect()?
The difference between HttpResponseRedirect() and redirect() lies in how they are used to perform URL redirects and the level of control they offer.

- HttpResponseRedirect(): Returns an HTTP 302 response to redirect to a specified URL. It’s useful when you need more control over the response before returning it, such as redirecting to an external site.
- redirect(): Internally uses HttpResponseRedirect(). It is more practical and flexible because it can accept different types of parameters, such as URLs, named URL patterns, or model instances.

In short, redirect() is simpler and more flexible, making it easier to use for various scenarios. HttpResponseRedirect(), on the other hand, is better when more control over the response is needed.

## How the BookEntry model is linked with User
The BookEntry model is linked to the User model through a foreign key (on models.py):
```
class BookEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
When a BookEntry is created using the create_book_entry function (on views.py), it is linked to the corresponding User.
```
def create_book_entry(request):
    form = BookEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        book_entry = form.save(commit=False)
        book_entry.user = request.user
```

## What is the difference between authentication and authorization, and what happens when a user logs in?
Authentication is the process of verifying a user's identity to ensure they are who they claim to be. For example, entering a username, password, or OTP during login. In Django, authentication is handled by the authenticate() and login() functions. 

Authorization is about determining what actions or resources a user is allowed to access after they have been authenticated. In Django, authorization is managed using permissions and groups, and decorators like @login_required and @permission_required help control access to views.

When a user logs in:
1. Provide Credentials: User submits username and password
2. Authentication: The system verifies if the credentials match stored data using Django's authenticate() function
3. Session Creation: If authenticated, Django creates a session for the user, storing the session ID as a cookie in the browser
4. Authorization: The system checks the user's permissions and roles to determine accessible resources
5. Redirect: If successful, the user is redirected to a target page

## How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.
Django remembers logged-in users through sessions stored in cookies. When a user logs in, Django creates a session, stores the session data on the server, and assigns a unique session ID to the user. This session ID is sent to the user's browser as a cookie called sessionid. Every time the user makes a new request, the browser sends the sessionid cookie back to the server, allowing Django to identify the user.

Cookies can also be used for storing user preferences, tracking, shopping carts in e-commerce, and security tokens. However, not all cookies are safe to use. There are key concerns regarding their security and privacy. Cookies can be vulnerable to attacks such as Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF) if they are not properly managed. Additionally, tracking cookies can raise significant privacy issues, as they often collect data on user behavior without explicit consent.

