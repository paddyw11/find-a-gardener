# LUDIDO Activity database

![Am I Responsive](documentation/readme/amiresponsive.png)

(Developer: Martyna Nowak)

[Live Webpage](https://ludido-ba4a496efb9b.herokuapp.com/)

This is the testing documentation for the LUDIDO website. For the README file, [click here](https://github.com/mmnowak/mp3_ludido/blob/main/README.md)

## Table of Contents

1. [Validation](#validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Python Linting](#python-linting)
    4. [Accessibility Testing](#accessibility-testing)
    5. [Performance Testing](#performance-testing)
2. [Manual Testing](#manual-testing)
    1. [Device Testing](#device-testing)
    2. [Browser compatibility](#browser-compatibility)
    3. [Testing User Stories](#testing-user-stories)
    4. [Feature Testing](#feature-testing)
3. [Bugs](#bugs)
    1. [Resolved](#resolved)
    2. [Unresolved](#unresolved)


## Validation

### HTML Validator

The W3C Markup Validation Service was used to validate the HTML of the website. All errors found were corrected, currently there are no errors.

[Home Page](https://validator.w3.org/nu/?doc=https%3A%2F%2F8080-paddyw11-findagardener-kmry0yh0br8.ws-eu110.gitpod.io%2F)

[All Gardeners](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffind-a-gardener-2f0e9afaf839.herokuapp.com%2Fgardeners)

[Gardener Profile Page](https://find-a-gardener-2f0e9afaf839.herokuapp.com/full_profile/Alan%20Titchmarsh)

[Services Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffind-a-gardener-2f0e9afaf839.herokuapp.com%2Fservices)

[Search By Services](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffind-a-gardener-2f0e9afaf839.herokuapp.com%2Fgardeners_by_service%2F4)

[Regions Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffind-a-gardener-2f0e9afaf839.herokuapp.com%2Fregion)

[Search by Regions](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffind-a-gardener-2f0e9afaf839.herokuapp.com%2Fgardeners_by_region%2F7)

[Add Gardener Profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffind-a-gardener-2f0e9afaf839.herokuapp.com%2Fadd_gardener)

[Register Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffind-a-gardener-2f0e9afaf839.herokuapp.com%2Fregister)

[Login Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffind-a-gardener-2f0e9afaf839.herokuapp.com%2Flogin)


### CSS validation

The W3C Jigsaw CSS Validation Service was used to validate the css file for the website via file upload. No errors were found.

![CSS Jigsaw score](/documentation/readme/css-validator.png)

### Python Linting

All python files were run through the [Python linter](https://pep8ci.herokuapp.com/). There were a number of errors coming from either the lines being too long, over/under indentation and whitespace. The errors have since been corrected.

**routes.py file:**

![Python linter results](/documentation/readme/python_linter.png)

**models.py file:**

![Python linter results](/documentation/readme/python_linter_models.png)


### Accessibility Testing

The pages were run through the [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/).
There were no errors. The alerts mostly related to skipped heading levels. 

See results:

[Home Page](https://wave.webaim.org/report#/https://find-a-gardener-2f0e9afaf839.herokuapp.com/)

[All Gardeners](https://wave.webaim.org/report#/https://find-a-gardener-2f0e9afaf839.herokuapp.com/gardeners)

[Services Page](https://wave.webaim.org/report#/https://find-a-gardener-2f0e9afaf839.herokuapp.com/services)

[Search By Services](https://wave.webaim.org/report#/https://find-a-gardener-2f0e9afaf839.herokuapp.com/gardeners_by_service/3)

[Regions Page](https://wave.webaim.org/report#/https://find-a-gardener-2f0e9afaf839.herokuapp.com/region)

[Search by Regions](https://wave.webaim.org/report#/https://find-a-gardener-2f0e9afaf839.herokuapp.com/gardeners_by_region/7)

[Add Gardener Profile](https://wave.webaim.org/report#/https://find-a-gardener-2f0e9afaf839.herokuapp.com/add_gardener)

[Register Page](https://wave.webaim.org/report#/https://find-a-gardener-2f0e9afaf839.herokuapp.com/register)

[Login Page](https://wave.webaim.org/report#/https://find-a-gardener-2f0e9afaf839.herokuapp.com/login)

### Performance Testing

#### Home
![Home Page](/documentation/readme/lighthouse-home.png)

#### All Gardeners
![All Gardeners](/documentation/readme/lighthouse-all-gardeners.png)

#### Services Page
![Services Page](/documentation/readme/lighthouse-services.png)

#### Search By Services
![Search By Services](/documentation/readme/lighthouse-search-by-service.png)

#### Regions Page
![Regions Page](/documentation/readme/lighthouse-region.png)

#### Search By Regions
![Search by Regions](/documentation/readme/lighthouse-search-by-region.png)

#### Register Page
![Register Page](/documentation/readme/lighthouse-register.png)

#### Login Page
![Login Page](/documentation/readme/lighthouse-login.png)

## User Story Testing

## Evidence Of CRUD

## Browser Compatibility

### Home Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Text paragraph | Pass | Pass | Pass |
| Image | Pass | Pass | Pass |
| Navigtion Buttons | Pass | Pass | Pass | 

### Gardeners Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Gardener Cards | Pass | Pass | Pass |
| Add Gardener Button | Pass | Pass | Pass |
| View Profile Button | Pass | Pass | Pass |
| Edit Gardener Button | Pass | Pass | Pass | 
| Delete Gardener Button | Pass | Pass | Pass |
| Delete Modal | Pass | Pass | Pass |

### Add Gardener Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Add gardener Form | Pass | Pass | Pass |
| Add Gardener Button | Pass | Pass | Pass | 

### Edit Gardener Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Add gardener Form | Pass | Pass | Pass |
| Add Gardener Button | Pass | Pass | Pass |

### Delete Gardener Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Text paragraph | Pass | Pass | Pass |
| Action buttons | Pass | Pass | Pass | 
| Features section images | Pass | Pass | Pass |
| Features section links | Pass | Pass | Pass |

### Services Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Service Cards | Pass | Pass | Pass |
| Add Service Button | Pass | Pass | Pass |
| Edit Service Button | Pass | Pass | Pass | 
| Delete Service Button | Pass | Pass | Pass |
| Delete Modal | Pass | Pass | Pass |

### Add Service Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Add Service Form | Pass | Pass | Pass |
| Add Service Button | Pass | Pass | Pass |

### Edit Service Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Edit Service Form | Pass | Pass | Pass |
| Edit Service Button | Pass | Pass | Pass |

### Regions Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Region Cards | Pass | Pass | Pass |
| Add Region Button | Pass | Pass | Pass |
| Edit Region Button | Pass | Pass | Pass | 
| Delete Region Button | Pass | Pass | Pass |
| Delete Modal | Pass | Pass | Pass |

### Add Region

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Add Region Form | Pass | Pass | Pass |
| Add Region Button | Pass | Pass | Pass |

### Edit Region Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Add Region Form | Pass | Pass | Pass |
| Add Region Button | Pass | Pass | Pass |


### Login Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Login Form | Pass | Pass | Pass |
| Login Button | Pass | Pass | Pass |

### Register Page

| Feature | Google Chrome | Microsoft Edge | Mozilla Firefox |
| ------- |:-------------:| :-------------:| :-------------: |
| Register Form | Pass | Pass | Pass |
| Register Button | Pass | Pass | Pass |

## Issues

Region error in post add_gargener form. I realised form posts were not adding tot he database for the garderner base. I added some print statements to test how the form was functioning. Some print statemnts identified an issues at the point of identifying the selected region on the form. 
