# Welcome to Dog Eared Books!
By Athazahra Nabila Ruby - 2306173113  
Platform Based Programming KKI 2024/2025

<details>
<Summary><b>Assignment 7</b></summary>

## Step-by-Step Project Implementation
### Create a new Flutter application
1. To initialize a Flutter project, I ran the command:
```
flutter create aina_fnb_mobile.
```
2. I then connected it to this GitHup Repository.
3. Next, I created a new file called menu.dart in the dog_eared_books/lib directory in which I defined 3 widgets: MyHomePage, InfoCard, and ItemCard which was given in the main.dart file.
4. I then changed the main.dart contents to this:
```dart
import 'package:flutter/material.dart';
import 'package:dog_eared_books/menu.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dog Eared Books',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSwatch(
          primarySwatch: Colors.green,
        ).copyWith(secondary: Colors.green[700]),
      ),
      home: MyHomePage(),
    );
  }
}
```
I set the title to 'Dog Eared Books' and the theme to the color green, as per my previous projects' theme.

### Create three simple buttons with icons and texts
5. On menu.dart, I created a new classed named ItemHomepage:
```dart
class ItemHomepage {
  final String name;
  final IconData icon;

  ItemHomepage(this.name, this.icon);
}
```
6. I then created the 3 buttons within the items list in the MyHomePage class:
```dart
class MyHomePage extends StatelessWidget {
  ...
  final List<ItemHomepage> items = [
      ItemHomepage("View Available Books", Icons.list),
      ItemHomepage("Add Books", Icons.add),
      ItemHomepage("Logout", Icons.logout),
  ];
  ...
}
```

### Implement different colors for each button
6. In the GridView.count widget, the buttons are assigned with different colors based on their index:
```dart
class MyHomePage extends StatelessWidget {
  ...
  children: items.asMap().entries.map((entry) {
      int idx = entry.key;
      ItemHomepage item = entry.value;
      Color color;
      switch (idx) {
          case 0:
              color = Colors.green.shade800;
              break;
          case 1:
              color = Colors.green.shade400;
              break;
          case 2:
              color = Colors.green.shade200;
              break;
          default:
              color = Colors.green;
      }
      return ItemCard(item, color: color);
  }).toList(),
  ...
}
```

### Display a Snackbar with specific messages
7. In the ItemCard widget, the onTap callback displays a SnackBar with a specific message for each button:
```dart
class ItemCard extends StatelessWidget {
  ...
  onTap: () {
  // Display the SnackBar message when the card is pressed.
  ScaffoldMessenger.of(context)
  ..hideCurrentSnackBar()
  ..showSnackBar(
  SnackBar(content: Text("You have pressed the ${item.name} button!"))
  );
  },
  ...
}
```

## Explain what are stateless widgets and stateful widgets, and their differences
- Stateless widget: a widget that does not change on its own through actions or internal behaviors. It will only change if it is modified by its parent widget. Therefore, stateless widgets only have final properties defined at construction.
- Stateful widget: a widget that can dynamically change its data or description. It displays data through an initial description defined at the beginning. If there is a change in state, the widget component will re-render to display the new data.
In general, a stateless widget is static and does not change after it is created, making it suitable for elements that do not require data updates. While a stateful widget can change during the app’s runtime because it has a state that can be updated, making it ideal for dynamic or interactive elements.

## Mention the widgets that you have used for this project and its uses.
- MaterialApp: The root widget of the application, setting up the theme and the starting point of the app.
- Scaffold: The basic structure of a page, providing the AppBar, body, and other layout structures.
- AppBar: The top header of the page containing the application title.
- Text: Displays static text on the screen.
- Padding: Adds space around a widget.
- Column: Arranges widgets vertically.
- Row: Arranges widgets horizontally.
- InfoCard (Custom Widget/Component): A custom card widget to display information such as NPM, name, and class.
- SizedBox: Adds empty space or adjusts the size of a widget.
- Center: Positions its child widget in the center.
- GridView.count: Displays widgets in a grid with a fixed number of columns.
- Card: A card widget that can have shadows or borders.
- Container: A flexible widget for holding elements, adjusting size, padding, and background color.
- ItemCard (Custom Widget/Component): A custom card widget for menu items that uses InkWell to detect interactions.
- Material: Adds a material-style visual to a widget.
- InkWell: Adds a splash effect and detects taps for interaction.
- SnackBar: Displays a temporary pop-up message at the bottom of the screen.

## What is the use-case for setState()? Explain the variable that can be affected by setState().
setState() is a function that allows you to dynamically display a component/widget. When the setState() function is called, it notifies Flutter that there has been a change in state that requires a rebuild. When a widget rebuilds, it will be displayed based on the updated state values.

Variables affected by setState() are usually those that need to change when an event occurs. For example, when a counter value changes, this change is typically displayed directly to the user. Not only variables, but properties like the color of a widget may also change, depending on the purpose of the state change.

## Explain the difference between const and final keyword.
Both const and final indicate that a variable cannot be changed, but there are some differences between the two:
- The value of a final variable can be assigned at runtime (when the app is running), whereas the value of a const variable must be known at compile time.
- Variables declared with final are more suitable for values that can only be determined when the app is running, for example, if the variable depends on a condition or calculation. While const variables must be defined in the code beforehand.
- const variables are more optimized compared to final.

</details>

<details>
<Summary><b>Assignment 7</b></summary>

## Step-by-Step Project Implementation
### Implement the registration feature
### Create a login page
### Integrate the Django authentication system
### Create a custom model according to your Django application
### Create a page containing a list of all items available at the JSON endpoint in Django
### Create a detail page for each item listed on the Product list page
### Filter the item list page to display only items associated with the currently logged-in user

## Why we need to create a model to retrieve or send JSON data
A model represents the structure of our data, making it easier to parse and handle JSON objects in a consistent way. Without a model, manually extracting fields increases the risk of errors, especially with complex or nested JSON. While not strictly required, omitting a model may lead to runtime errors due to mismatched field names or missing attributes.

## Function of http library
The http library allows Flutter apps to make HTTP requests to fetch, send, or update data on a server. It provides simple methods like get and post for RESTful communication and handles request headers, body, and responses in an easy-to-use manner.

## Function of cookie request
CookieRequest manages HTTP requests with session cookies, enabling persistent authentication across different components of the app. Sharing the CookieRequest instance ensures that all components use the same session, maintaining user authentication and state across requests (e.g., login, fetch data).

## Mechanism of Data Transmission
Input: User submits data through a form in Flutter.
Transmission: The app sends a request (e.g., POST) with data to a server endpoint via http or CookieRequest.
Backend Processing: The server (Django) processes the request, updates the database, and returns a JSON response.
Display: The app parses the response (using models if needed) and updates the UI dynamically.

## Authentication Mechanism
Login/Register: User inputs account details in Flutter, which are sent to Django via POST requests. Django validates the credentials, creates a session (if valid), and returns a success or error response.
Session Management: CookieRequest stores the session cookie for future requests.
Logout: The session is invalidated by sending a logout request to Django, clearing the cookie in the app. Upon success, the app redirects to the login screen.