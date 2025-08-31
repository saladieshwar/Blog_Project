# Django Blog_Website

A simple yet powerful Blog Website built with the Django Framework.
This project demonstrates the fundamentals of user authentication and content management with a clean and minimal design.

✨ Features

🔹 User Authentication

   Register a new account

   Login securely

   Logout anytime

🔹 Blog Management

  Create and publish new blog posts

Each post contains:

  ✍️ Author name

  📅 Date & time of publishing

  🏷️ Title of the blog

  📖 Description/content of the blog

🔹 User-Friendly Experience

  Only registered users can create posts

  Simple and clean UI for easy navigation

🛠️ Tech Stack

  Backend: Django (Python) 🐍

  Frontend: HTML, CSS (Bootstrap/Custom styles) 🎨

  Database: SQLite (default Django DB) 🗄️

  Authentication: Django built-in auth system 🔐

🚀 How to Run

1.Clone the repository

    git clone https://github.com/your-username/your-blog-repo.git
    cd your-blog-repo


2.Create a virtual environment & activate it

    python -m venv venv
    venv\Scripts\activate  #On Windows 


3.Install dependencies

    pip install -r requirements.txt


4.Run migrations

    python manage.py migrate


5.Start the development server

    python manage.py runserver


6.Open in browser:

    http://127.0.0.1:8000/


📸 Screenshots


![registerpage](https://github.com/user-attachments/assets/8a910cf3-b03f-44df-85f5-19cccbd2646b)

![loginpage](https://github.com/user-attachments/assets/c30fe171-a970-4f75-b221-a5377f5bf789)

![homepage](https://github.com/user-attachments/assets/af931ce9-d12c-4cca-874e-89fea219d228)

![Post Blog](https://github.com/user-attachments/assets/99369213-77e8-4a71-9d24-80dc978a2cec)

🌟 Future Improvements

  Add categories/tags for blogs

  Allow image uploads in posts

  Comment system for readers

  Pagination for blog list

