### Objective

Welcome to the sennder Coding Challenge! Studio Ghibli is a Japanese movie company. They offer a ​[REST API](https://ghibliapi.herokuapp.com/) ​where one can query information about movies and people (characters). The task is to write a Python application which serves a page on localhost:8000/movies/.

### Brief

This page should contain a plain list of all movies from the Ghibli API. For each movie the people that appear in it should be listed.

Do not use the ​**people** ​field on the ​**/films​** endpoint, since it’s broken. There is a list field called **films** ​on the ​**/people** ​endpoint which you can use to get the relationship between movies and the people appearing in them. You don’t have to worry about the styling of that page.

Since accessing the API is a time-intensive operation, it should not happen on every page load. But on the other hand, movie fans are a very anxious crowd when it comes to new releases, so **make sure that the information on the page is not older than 1 minute** when the page is loaded.

Write **unit tests** for your business logic. Your tests don’t have to be complete, but you should describe how you would extend them if you had the time.

If you have to skip some important work due to time limitations, feel free to add a short description of what you would improve and how if you had the time for it.

### Evaluation Criteria

-   Python best practices
-   Show us your work through your commit history
-   We're looking for you to produce working code, with enough room to demonstrate how to structure components in a small program
-   Completeness: did you complete the features?
-   Correctness: does the functionality act in sensible, thought-out ways?
-   Maintainability: is it written in a clean, maintainable way?
-   Testing: is the system adequately tested?
-   Formating/Code style: Are you following **PEP8** conventions?

### CodeSubmit

Please organize, design, test and document your code as if it were
going into production - then push your changes to the master branch.

Happy Coding ✌️

The sennder Team
