![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220607%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220607T225901Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3811149efc22f90c0a39c509b3e1def1f843f3067029057a5942ba01c942630a)

# 0x1A. Application server

------------

## General

- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments

------------

## List of poinst.

|  Point | What is done at this point? | level |
| ------------ | ------------ | ------------ | 
| README.md | Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production. | Mandatory | 
| 0x1A-application_server | Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000. You’ll need to install Gunicorn and any libraries required by your application. Your Flask application object will serve as a WSGI entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments. | Mandatory |
| 2-app_server-nginx_config | Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/ | Mandatory |
| 3-app_server-nginx_config | Building on what you did in the previous tasks, let’s expand our web application by adding another service for Gunicorn to handle. In AirBnB_clone_v2/web_flask/6-number_odd_or_even, the route /number_odd_or_even/<int:n> should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure Nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001. The key to this exercise is getting Nginx configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of Gunicorn without having multiple terminals open, see tips below. | Mandatory |
| 4-app_server-nginx_config | Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01. | Mandatory |
| 5-app_server-nginx_config | Let’s serve what you built for AirBnB clone - Web dynamic on web-01. | Mandatory |

------------

# Resources

- https://intranet.hbtn.io/concepts/17
- https://intranet.hbtn.io/concepts/67
- https://intranet.hbtn.io/concepts/68
- https://www.nginx.com/resources/glossary/application-server-vs-web-server/
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04
- https://docs.gunicorn.org/en/latest/run.html
- https://werkzeug.palletsprojects.com/en/0.14.x/routing/
- https://upstart.ubuntu.com/cookbook/
- https://gist.github.com/soheilhy/8b94347ff8336d971ad0

------------

# Author

## Juan Sebastian Avendaño Gonzalez:
- Git: https://github.com/AvendanoisPepe
- Twitter: https://twitter.com/Sebastian_Aven
- Linkedin: https://www.linkedin.com/in/juan-sebastian-avenda%C3%B1o-gonz%C3%A1lez-8b1185200/

------------


![](https://i.imgur.com/HPJ8Qn8.jpg)