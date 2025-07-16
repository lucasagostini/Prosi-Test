# Prosi-Test

This a simple repository built for Prosigliere technical test.

It is a Django-based project, that consists on two data models, BlogPost and Comment.

It has 4 endpoints:

- GET /api/posts
- POST /api/posts
- GET /api/posts/{id}
- POST /api/posts/{id}/comments

I built a very simple frontend, but since the requirement specified I should not spend more than 4 hours working on it, I stopped when the clock hit the time, and we have a functional home page when you access your localhost:8000/

I tried to do this project using TDD, so I started by building the tests, then moved into the code itself.

To run this project, simply clone the repository and run
`pip install -r requirements.txt -r test-requirements.txt`

Then run the command below to start the server:
`python manage.py runserver`

Or if you just want to install dependencies and run tests, you can use tox, by using the command:
`tox -e py`



# Next steps

If I had more time, I would work on building a frontend that is functional across all pages.
Also add security, like token or session based access.
Another option would be to add pagination, and maybe also filtering and search.
Then I could also create some tests using frontend testing libraries.
If we consider a lot more time, we could even talk about using docker, building CI/CD pipelines to run tox, etc.
We could use django i18n as well to translate pages to other languages. 