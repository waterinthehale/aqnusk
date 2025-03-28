一个使用flask开发的cms,正在重置部分代码中。预计结构



————
__
cms_project/
│── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── team.py
│   │   ├── service.py
│   │   ├── gallery.py
│   │   ├── contact.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── main.py
│   │   ├── admin.py
│   ├── forms/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── contact.py
│   │   ├── admin.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── admin/
│   │   │   ├── dashboard.html
│   │   │   ├── team.html
│   │   │   ├── services.html
│   │   │   ├── gallery.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   ├── extensions.py
│   ├── config.py
│   ├── utils.py
│── migrations/
│── tests/
│── instance/
│── run.py
│── requirements.txt
│── .env
│── README.md
