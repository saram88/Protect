
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome to Protect shop

This is my Code Institute student PP5 final project Protect shop readme.
The live link you can find here:

## **[Live site](LÄGG IN)**

The Protect Shop is an online store where clients can purchase a wide range of cybersecurity antivirus. 
Stripe is used as the payment processor. 
Use the test card number 4242 4242 4242 4242 with a future expiration date, a three-digit CVC, and a five-digit postal code to test the payment functionality.


### By [Sara Mentzer](https://www.linkedin.com/in/sara-mentzer-17b9b1170/)

---

## Introduction

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#Protect) 

Protect is a website built in Django using Python, JavaScript, CSS and HTML. 


### Site Goals
- Site owner aim and business model.
    - Site owner can effectively sell their Antivirus program.
    - Site owner add or update their available programs that they sell.
    - Site owner can highlight their products in sale or featured products category.
-  Site User Goals:
    - Can easily find the product that they locking for.
    - Have a great user experience.
    - Can purchase Antivirus program easily.


## Table of Contents
* [Features](#features)
     - [Future Enhancements](#future-enhancements)
     - [Web Marketing](#web-marketing)
* [Design/UX](#design)
     - [Wireframes](#wireframes)
     - [Model Schema](#model-schema)
* [Technologies Used](#technologies-used)
* [Agile Development](#agile-development)
* [Testing](#testing)
* [Deployment](#deployment)
* [Release History](#release-history)
* [Credits](#credits)


## Features

### Existing Features

### Navigation
- The navigation bar on all pages, allows users to access the key pages.
- The navbar uses a hamburger menu toggle on smaller displays and is fully responsive.
- The user can see whether they are logged in from the "My Account" dropdown options, which vary depending on the user role (admin etc). This dropdown has additional choices only available to admin users.
- only logged in users can access the profile or logout pages.
- only logged out users can access login and register page.
- The menu collapses to a toggler on smaller screens, leaving the account, search and ordersheet and burger menu links in the navbar allowing for easy navigation across all device sizes.

- Navigation on large screen

    ![]()

- Navigation on smaller screen
 
    ![]()

### Footer
- Links to the site's social media pages are provided in the footer.
- The footer also provides navigation to other important parts of the site including the Contact, FAQ page and Privacy.
![]()

### Home Page
The home page is divided into different sections.

- A hero image with a link to the All Products page and some text content to boost SEO (Search Engine Optimisation).
![]()

- The Recently Added Products section displays the most recently added eight products. 
![]()

- The comments section displays bootstrap carousel reviews. 

    It shows the product image, who reviewed it and the review details.

![](Rewiev screenshot here)


### Products Page
- The All Products page displays all the products available on the website. 
- The user has the option to sort the products by various categories. JA ELLER NEJ?
- Once the user clicks on the product, they go to the product details page.
- A sale tag is added automatically if product is on sale along with the original price

- Edit, Delete options are displayed on this page when the superuser/admin is logged in.
![](Screenshot här)

### Search Page
- The search page searches for the products and displays on the page.

    ![](docs/screenshot/features/search.png)

### Product Details Page

- The product detail page provides additional information about the products
- The user can choose the units of the product they wish to purchase
- A comment form is displayed in the review section for registered users to leave a comment.
- Review of the product is displayed if there is a review available on that product.

    ![](docs/screenshot/features/product-detail.png)

### Ordersheet Page

- The Ordersheet page provides a summary of the items in the ordersheet and total prices.
- The page calculates prices of items automatically if an item is on sale.
- The user may easily make their final purchasing decisions because they have the opportunity to update or remove goods from the ordersheet.

    ![](docs/screenshot/features/ordersheet.png)

### Checkout Page
- The checkout page is intended to make it easy for a user to make purchase.
- Only registered users can save their info for future purchase.
- It also shows the summary of the products so that the user knows what they are purchasing before making the payment.
- The page gives the buyer an option to create an account if they wish to save their details for future.

    ![](docs/screenshot/features/checkout.png)

### Checkout Success Page
- Once the order has been processed, a checkout success page is loaded to let the customer know whether or not their purchase was successful.
- An email of the order confirmation is also sent to the user.

    ![](docs/screenshot/features/checkout-success.png)

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#policyshop) 


### Profile Page
- A registered user can easily access their order history and modify their default shipping information on their profile page.
- User can also update their information.
    ![](docs/screenshot/features/profile.png)


### Contact Page
- The Contact page displays the imaginary address of the company office and its location on the map.
- It also gives users the option to send a quick message about their queries.
- The admin can view the message in the admin panel. 
- The admin does not have option to reply back to the message but that can be added in the future feature

    ![](Screenshot på kontaktdelen)

### Error 404 Page and 500 error Page

- A 404 error page gives the user a helpful message if a link is used incorrectly.
- It also gives the user a way to get back to the home page with a link.
- The 500 error page also provides response if something goes wrong in the code on the server, with a way to recover, without debug messaging.

    ![]()

### Forgot Password
- If a user forgets their password they can reset it. 
- They will be asked to enter their email, and the site will send them an email with a link to reset their password.
- User will be asked to enter their password twice for confirmation.

- password reset form
    ![](docs/screenshot/features/forgotpw1.png)

- password reset confirmed form
    ![](docs/screenshot/features/forgotpw2.png)

- email received to reset password
    ![](docs/screenshot/features/forgotpw3.png)

- page to reset password
    ![](docs/screenshot/features/forgotpw4.png)

## Future Enhancements


Future Enhancements user stories [here](länk till vad jag vill erbjuda i framtiden. tex kunna boka en tid direkt, och kunna följa när ordrar skickas osv)

### Other future features
- Could add product consulting availability hours and displays next date work can be started and completed.
- Could add an order tracking page with ordersheet linked to multiple delivery options to allow clients to monitor order delivery and scheduling.
- Could add a 'Favourite' button where clients can save services to their favourites for later use. 
- Could enable Site admin to respond to a message on the site
- Could enable Site admin to respond to and/or delete a comment on the site
- The example app used sizes for products i.e. XS, S, M, L, XL. I don't use product sizes for consulting services and time, but am considering changing to hours, days, weeks etc in a future version.

### Web Marketing
The use of social media marketing is very important for bringing in customers and increasing visibility of the site. 
The approved way to generate interest is an organic approach as the marketing budget will be small initially.

Facebook marketing is often more important than any other platform, we are using it for this project. 

I started with the CI planning template [below](screenshot på facebook), 

and created a page which may still be visible [here](länk till facebook)


### Search Engine Optimization
The meta keywords and description in base.html have been amended to the researched keywords. 
On significant pages like the index and product pages, the site title has the name Protect and also has keywords.

The homepage has also been designed with SEO in mind. 

For SEO purposes, we have also added a sitemap.xml and robots.txt file to the website's root directory for search engines to crawl the site. 

A sitemap is a method of classifying a website, indicating the URLs and the information contained within each section.
The URLs on your website that a search engine crawler is permitted to visit are specified in a robots.txt file.

![](docs/screenshot/others/SEO-keywords.png)

## Design
The website is created to look good and be easy to use, and also making it possible for a customer to browse and buy products and services of interest quickly and easily.
Wireframes for desktop, tablet, and mobile views were produced and only few colors were used to maintain the ARIA accessibility of the website.

- ## Wireframes
wireframes for the project were created using [Balsamiq](https://balsamiq.com/)SKA JAG ANVÄNDA DEN ELLER KÖRA ANNAT

* [Back to table of contents]() 
* [Back to top of README.md]() 

- Home Page 

    ![]()

- Product Page

    Product page displays all the products available in the store.
![]()

- Product Details Page

    Displays the details of the product. Users can add products to their ordersheet. 
    They can also +/- the amount of products and update the bag from here.
    
![]()

- Register Page

    Users can register on this page. 
    If they are already registered, the page gives them a link to the Login page.
    ![]()

- Login

    Users can log in on this page. 
    If they are not registered, there is a link to the register page.
    
    ![]()

- Ordersheet

    Users can add items to their ordersheet. 
    This page gives them options to increment or decrement their products as well as to remove them.
    
    ![]()

- Checkout Page

    Users can enter their shipping and card details to make a purchase. 
    The user must create an account to save their details for future use.
    
    ![]()

- Checkout Success Page

    Once the checkout is complete, the user is redirected to checkout success page, where they can see their order details and shipping details.
    
    ![]()

- Contact Page

    Users can view company details and they can fill up the form contact us.
    
    ![]()

- ## Color Schema

The color palette for this project was kept as simple as possible in order to maintain the contrast between the background and the foreground.

**[Homepage to Coolers](https://coolors.co/)**

![](screenshot)

- ## Model Schema

Two relational databases were used to create the site. 
The builtin Django SQLite database was used for development and then Elephant SQL Postgres for the deployed version. 

LÄNKA TILL VAR OCH HUR DET SER UT I MODELSCHEMA

The site is based around a number of models separated into the following main groups.

**Product Models**

![]()

**Category** - stores the details of a product category.

- **Product** - stores all the details about a product for sale. Connected to the featured product, recently added products and Category objects via foreign key relationships.

![]()

- **Review / Comments** - stores a user review of a product and is connected to the Product and by foreign key relationships.

![]()

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#policyshop) 


**User Models**

- **User** - the Django Allauth user model containing information such as username and password.
- **Profile** - stores a users default delivery information and is connected to the User via a one to one relationship.

![]()


**Order Models**

- **Order** - a foreign key relationship connects the user profile to the storage of the complete order data.
- **OrderLineItem** - stores the product information for a single product purchased on an order. Foreign key relationships connect the product and order.

![]()


## Agile Development


To see the list of [issues]() click [here]()

This project was started with my GitHub Projects [Page]() to track and manage the [issues]() such as expected epics, user stories, milestones and other work and sprints involved.
The purpose of Agile Development is to plan and measure progress for expected work and tasks, by listing the epics and then break them down into user stories or smaller tasks to ultimately finish the site in the allocated time.

At the initial stages I decided on core requirements ('must have' issues) for the project and some 'could have' issues but not critical requirements.

From these I added the associated Epics, user stories, acceptance criteria and the tasks so I can track my work effectively.
I did also use [milestones]() as another way to visualise Epic completion status.

Once I completed a task I note the item as completed and if all parts of this story were completed I would move it from **In Progress** to **Done** on the board. Acceptance criteria would also be noted where appropriate.

At the end of a coding session I would update the user stories with a comment of:

 - What was done
 - What is left to be done
 - Reminders to track where I finished so subsequent work would follow.

#### Epics

##### Completed Epics

1. [EPIC: Initial Project Setup]()
2. [EPIC: The Home Page]()
3. [EPIC: Setup Services and Products]()
4. [EPIC: Order Processing]()
5. [EPIC: User profiles]()
6. [EPIC: Site and Product Admin]()
7. [EPIC: Additional Features]()
8. [EPIC: SEO and Web Marketing]()
9. [EPIC: Testing]()
10. [EPIC: User CRUD for orders (and profiles)]()

#### User stories

#####  Completed User Stories

To view details of the user stories please click on a user story below.
See the project page for the full [list of issues]() to see the details and comments.
See the page [here]()

 1. [USER STORY: Setup Authentication]
 2. [USER STORY: Setup Base Page]
 3. [USER STORY: Setup Home Page (index.html)]
 4. [USER STORY: Product and services setup]
 5. [USER STORY: Product Filtering]
 6. [USER STORY: Product Searching]
 7. [USER STORY: Product Sorting]
 8. [USER STORY: Order Processing Setup]
 9. [USER STORY: Adding Products]
 10. [USER STORY: Adjusting and Deleting Products]
 11. [USER STORY: Checkout]
 12. [USER STORY: Purchasing with Stripe]
 13. [USER STORY: NOtifications, Messages, Toasts]
 14. [USER STORY: Setup User profiles]
 15. [USER STORY: Adding Users with Profiles]
 16. [USER STORY: Adjust allauth default pages]
 17. [USER STORY: Adjusting user profile and default delivery info]issues/22)
 18. [USER STORY: Adding Order History to User Profile]
 19. [USER STORY: Stripe Webhooks to catch delays/errors]
 20. [USER STORY: Notifications from Profile info]
 21. [USER STORY: Adding Products to catalog as Admin]
 22. [USER STORY: Editing Products as Admin]
 23. [USER STORY: Deleting Products as Admin]
 24. [USER STORY: Adjusting admin+allauth forms format]
 25. [USER STORY: Adjust models for new PP5 data/features]
 26. [USER STORY: FAQ app/model]
 27. [USER STORY: Contact app/model]
 28. [USER STORY: Privacy app/model]
 29. [USER STORY: SEO Features]
 30. [USER STORY: Web marketing and FB]
 31. [USER STORY: e-commerce business model]
 32. [USER STORY: Testing]
 33. [USER STORY: account registration]
 34. [USER STORY: Create order for me only]
 35. [USER STORY: Update order for me only]
 36. [USER STORY: Delete my orders only]
 37. [USER STORY: Setup CSS]
 38. [USER STORY: Site Menu]


The following User stories were not completed as they are possible future features:

 ##### Future Feature User stories

 39. [USER STORY: Consulting Service Bookings]()
 40. [USER STORY: Social Media Login]()

I decided against implementing some future features at this time due to deadlines and because the core requirements of the project have been satisfied elsewhere.


## Testing

Testing is in different sections and individually tested with test cases developed for each function.

Details of the [testing]() procedures and methodology can be found in the testing.md file [here](/docs/testing/TESTING.md)

I got automated testing to work for most of the models, with up to % coverage overall, according to the coverage [report](/report.txt)

Details of the [testing](/docs/testing/TESTING.md) procedures and methodology can be found in the testing.md file [here](/docs/testing/TESTING.md)

The site was also tested for responsiveness here https://www.browserstack.com/responsive and here https://ui.dev/amiresponsive


> Responsive Examples of Live Site

![Responsive Site examples](docs/testing/responsive.png)

 - The site is fully responsive across multiple screen sizes and devices. 

 I had to carry out significant security research, updates and testing to get this test to work.



### Bugs of note



### Development bugs: 

#### fixed 



## Technologies Used


- ## Language Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- ## Frameworks Used
- [Django](https://www.djangoproject.com/) - A high-level Python web framework for rapid development with clean, pragmatic design.

- [Bootstrap](https://getbootstrap.com/) - A framework for building responsive, mobile-first sites.

- # Libraries Used
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - is used for user authentication, registration & account management to the site.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - is used to add bootstrap styling to the forms used.
- [Django Countries](https://pypi.org/project/django-countries/) - is used for the country CountryField in the checkout page.
- [jQuery](https://jquery.com/) - is used for styling components and also in some of the custom JS used throughout the site.
- [Google Fonts](https://fonts.google.com/) - is used for websites font
- [Font Awesome](https://fontawesome.com/) - is used for all the icons on the site.
- [Mailchimp](https://mailchimp.com/) - is used to create the newsletter signup form.
- [Facebook Pages](https://www.facebook.com/)
- [Stripe](https://stripe.com/gb) - is used for the processing of payments.
- [Heroku](https://dashboard.heroku.com/apps) - is used to deploy the site.
- [Gunicorn](https://gunicorn.org/) - is used as the server to run Django on Heroku.
- [Amazon AWS](https://aws.amazon.com/) - is used store the static and media files for the site.
- [PostgresSQL](https://www.postgresql.org/) - is used as the database for the site.
- [Git](https://git-scm.com/) - is used as version control 
- [Github](https://github.com/) - is used to store the project's code.
- [pillow](https://pypi.org/project/Pillow/) - Python imaging library
- [psycopg2](https://pypi.org/project/psycopg2/) - database adapter which allow us to connect with a postgres database
- [boto3](https://pypi.org/project/boto3/) - Allows connection to AWS S3 bucket


- ## Database Used

[ElephantSQL](https://www.elephantsql.com/) for deployment to heroku.

- ## Stripe
[Stripe](https://stripe.com/gb) has been used for the payment for this website.

The developer mode in Stripe allows us to use and process test payments.

Type | card No | Expiry | CVC | ZIP
--- | --- | --- | --- | ---
Success | **4242 4242 4242 4242** | A date in the future | Any 3 digits| Any 3 digits
Require authorisation | **4000 0027 6000 3184** | A date in the future | Any 3 digits| Any 5 digits


## Deployment


The site has been deployed to Heroku at [https://ib-pp5-polshop.herokuapp.com/]()

## Credits
* [Back to table of contents]() 
* [Back to top of README.md]() 

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

-   ### Source code

    - Code Institute Django course material, tutors, mentors and colleagues in Slack channels.
    - Bootstrap documentation https://getbootstrap.com/docs/5.3/getting-started/introduction/ 
    
-   ### Images
    - Product images https://www.pexels.com/ 
    - favicon.ico generation https://favicon.io/favicon-generator/
    - Colors from [Coolors](https://coolors.co/)

    ### Contact me

     - Sara Mentzer [LinkedIn](https://www.linkedin.com/in/sara-mentzer-17b9b1170/)
     Sara Mentzer [GitHub]()https://github.com/saram88