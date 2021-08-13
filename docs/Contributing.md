# Contributing 

We appreciate the efforts by anyone who feels like contributing towards this project. Anyone can contribute by: 

- moderating the documentation
- adding more data
- creating more applications
- or through [Donations](Donations.md)

## Documentation

Documentation can be difficult to intepret based on the readers experience. We have tried as much as possible to simplify this but anyone can add their interesting discoveries as to what they can do with this data for the benefit of others. 

_Keep in mind that not everyone who would wish to use this data is neither a software developer or a GIS software user_ therefore documentatio should be as fluent as possible. 

**Steps** 

1. Fork the [repository](https://github.com/African-Surveyors-Connect/Zimbabwe-COVID-19-Data)

2. Clone the forked version of the repository

    ```
    git clone https://github.com/<your-fork-url>.git
    ```

3. Cd into your local repository 

    ``` 
    cd <name-of-repository>
    ```

4. Check that your fork is the "origin" remote

    Use `git remote -v` to show your current remotes. You should see the URL of your fork next to the word "origin".

    If you don't see an "origin" remote, you can add it using: `git remote add origin URL_OF_FORK`.

5. Add the project repository as the "upstream" remote

    Go to your fork on GitHub, and click the "forked from" link to return to the project repository:
  
    While in the project repository, click the green __Clone or download__ button and then copy the HTTPS URL

    Add the project repository as the "upstream" remote using: `git remote add upstream <URL_OF_PROJECT>`.

    Use `git remote -v` to check that you now have two remotes: an origin that points to your fork, and an upstream that points to the project repository

6. Pull the latest changes from upstream into your local repository

    Use `git pull upstream master` to "pull" any changes from the "master" branch of the "upstream" into your local repository.

    (If the project repository uses "main" instead of "master" for its default branch, then you would use `git pull upstream main` instead.)

7.  Create a new branch 

    Use `git checkout -b <BRANCH_NAME>` to create a new branch and then immediately switch to it.

8. Make changes in your local repository

9. Commit your changes

10. Push changes to your fork

11. Create a Pull Request


## Adding Applications

If you have your Location Intelligent or Data Analysis and Visualization application that you would like us to add onto the project simply send us an Email on: [info@africansurveyors.net](mailto:info@africansurveyors.net) describing the application and the link to the online application. 

Remember everything submitted within our [COVID-19 Hub for Zimbabwe](https://covid19.africansurveyors.net/) is entirely __Open-Source__


## Data Sources

If you have a data source you think might be helpful and will improve this project kindly send through the link of the source to our Email: [info@africansurveyors.net](mailto:info@africansurveyors.net)


