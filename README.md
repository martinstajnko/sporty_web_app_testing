Which dependencies do I need to install to run this project?
- playwright (>=1.55.0,<2.0.0)
- requests (>=2.32.5,<3.0.0)
- pytest-playwright (>=0.7.1,<0.8.0)








# Run all tests against all 3 browsers
poetry run pytest tests/test_demo.py -v

# Run only Chromium
poetry run pytest tests/test_demo.py -v -k chromium

# Run only Firefox
poetry run pytest tests/test_demo.py -v -k firefox

# Run a specific test with all browsers
poetry run pytest tests/test_demo.py::test_search_starcraft_on_twitch -v



Next steps you can take:

Add more test cases
Expand the TwitchPage with additional methods
Create more page objects for different parts of the application
Add test reports and assertions
Set up CI/CD with these commands