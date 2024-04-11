 am i responisve img 


on entering do cmd - pip3 install 'Flask-SQLAlchemy<3' psycopg2 sqlalchemy==1.4.46


to add db - cmd - set_pg
                - psql
                - CREATE DATABASE 'name of database'
                - \c 'name of database'
                - \q

                - python3 
                - from findagardener import db
                - db.create_all()

 you can check by using following cmds
                - psql -d findagardener
                - \dt
                - SELECT * FROM 'name of table'
                - \q - to exit

 dont forget to add - app.app_context().push() underneath app.confi in init file





# [Find a Gardener](https://find-a-gardener-2f0e9afaf839.herokuapp.com/)

![Am I Responsive](documentation/readme/amiresponsive.png)

Find a Gardener is a website that will provide a list of available gardeners and their respective services. 

The users of the website will be able to find gardeners in their area and find more information about them.

The other user of the website will be ther garndener themselves who can create a profile to login to and can add, update or delete their information profile.

### Live project

Find the live project [here](https://find-a-gardener-2f0e9afaf839.herokuapp.com/)

---

## Table of Contents
1. [**UX**](#ux)
    - [**Strategy Plane](#strategy-plane)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Color Scheme**](#color-scheme)
        - [**Imagery**](#imagery)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)
    - [**Database Design**](#database-design)
2. [**Features**](#features)
    - [**Current Features**](#current-features)
    - [**Planned Features**](#planned-features)
3. [**Technologies Used**](#technologies-used)
    - [**Development Technologies**](#development-technologies)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)
    - [**Python Modules**](#python-modules)
4. [**Testing**](#testing)
    - [**Validation**](#validation)
    - [**User Story Testing**](#user-story-testing)
    - [**Evidence Of CRUD**](#evidence-of-crud)
    - [**Compatibility**](#compatibility)
    - [**Issues**](#issues)
5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)
6. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Tools And Software**](#tools-and-software)
---


# UX

## Strategy Plane

Target Audience

The target audience of this website are people looking for a gardener.

User Requirements and Expectations

All users of the site will expect:
- Links and buttons to work logically.
- A simple and intuitive navigation system.
- Interactive feedback and notifications.
- Information presented in a clear and concise manner.
- A visually appealing design.
- A simple way to create an account.
- A simple way to log in for existing users.
- The ability to add, edit or delete own data.
- Accessibility.


User Stories

As any user:
1. I want to undertand the purpose of the site on first en.
2. I want to be able to navigate the site easily and intuitively.
3. I want to be able to view the website on any device.
4. I want to be able to return to the page without using browser buttons if I encounter an error.
5. I want to view a list of available gardeners.
6. I want to search for gardeners by region or by services offered.

As a logged out user:

7. I want to be able to easily register a new account.
8. I want to be able to locate a log in page easily.

As a logged in user:

9. I want to be able to see my profile.
10. I want to be able to add, edit or delete my own profile.
11. I want to receive feedback when i've completed an action. 


As a logged in admin User:

12. I want to be able to add, edit or delete regions.
13. I want to be able to add, edit or delete services offered.
14. I want to receive feedback when i've completed an action.

Features Planned

- All Users
1. Responsive design
2. Postgres database to store gardeners, regions, services and users
3. Pages displaying gardeners filtered by either region or services offered

- Logged out users

Structure Plane

#### Color Scheme

I chose a colour scheme that closely resembles the industry that the website is catagorised in, nature and gardens. Synonymous with eco and nature, green was a colour that would dominate on this website. The complimentary color to green, red, i have used to style any danger buttons for example delete. 

![Colour Palette](documentation/readme/color-palette.png)

#### Imagery

#### Typography

### Wireframes
---


To follow best practice, wireframes have been developed to guide the project throught it's development. Device sizes for desktop, tablet and mobile have been created for the core pages using [Balsamiq](https)

<details>
<summary>Home Page</summary>

* Home Page ![screenshot of home page](documentation/readme/wireframes/home-page.png)

</details>

---

<details>
<summary>Register Form</summary>

* Register Form ![screenshot of home page](documentation/readme/wireframes/register.png)

</details>

---

<details>
<summary>Login Page</summary>

* Login Page ![screenshot of home page](documentation/readme/wireframes/login.png)

</details>

---

<details>
<summary>All Gardeners Page</summary>

* All Gardeners Page ![screenshot of home page](documentation/readme/wireframes/all-gardeners.png)

</details>

---

<details>
<summary>Add profile</summary>

* Add Profile Page ![screenshot of home page](documentation/readme/wireframes/add-profile.png)

</details>

---

<details>
<summary>Regions</summary>

* Regions List Page ![screenshot of home page](documentation/readme/wireframes/region.png)

</details>

---

<details>
<summary>Search By Region</summary>

* Search By Region Page ![screenshot of home page](documentation/readme/wireframes/search-by-region.png)

</details>

---

<details>
<summary>Services</summary>

* Services List Page ![screenshot of home page](documentation/readme/wireframes/services.png)

</details>


### Database Design

# Features

## Current Features

## Planned Features

# Technologies Used

## Development Technologies

## Front-End Technologies

## Back-End Technologies

## Python Modules

# Testing

For More information on tersting [see here]{https://github.com/paddyw11/find-a-gardener/blob/main/TESTING.md}




## Local Deployment

## Remote Deployment

# Credits

## Images

- Pexels - Home Page Image [Magic K Photography](https://www.pexels.com/@magic-k-24827758/)

## Code

- Code Pen - Grass Footer [@Tillberger](https://codepen.io/tillberger/pen/MWqbWZJ)


## Tools And Software
