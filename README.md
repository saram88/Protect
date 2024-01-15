![CI logo](/media/readme/protect-logo.png) 
# Welcome to Protect shop
This is my Code Institute student PP5 final project Protect shop readme.
The live link and my GitHUb reprosity you can find here:

## **[Live site](https://saram88-protect-d3535879dbc8.herokuapp.com/)**

## **[GitHub](https://github.com/saram88/Protect)**

The Protect Shop is an online store where clients can purchase a wide range of cybersecurity antivirus. 
Stripe is used as the payment processor. 
Use the test card number 4242 4242 4242 4242 with a future expiration date, a three-digit CVC, and a five-digit postal code to test the payment functionality.


### By [Sara Mentzer](https://www.linkedin.com/in/sara-mentzer-17b9b1170/)

## Table of Contents
* [Introduction](#introduction)
    - [Site Goals](#Site-Goals)
* [Features](#features)
    - [Navigation](#navigation)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [Products Page](#products-page)
    - [Product Details Page](#product-details-page)
    - [Checkout Page](#checkout-page)
    - [Ordersheet Page](#ordersheet-page)
    - [Profile Page](#profile-page)
    . [Wishlist page](#wishlist-page)
    - [Contact Page](#contact-page)
    - [Error 404 Page and 500 error Page](#error-404-page-and-500-error-page)
    - [Forgot Password](#forgot-password)
    - [Register Page](#register-page)
    - [Login](#login)
    - [Review](#review)
* [Future ideas](#future-ideas)
* [Model schema](#model-schema)
* [Agile Development](#agile-development)
    - [Epics and userstorys](#epics-and-userstorys)
* [Technologies Used](#technologies-used)
    - [Language Used](#language-used)
    - [Frameworks Used](#frameworks-used)
    - [Libraries Used](#libraries-used)
    - [Database Used](#database-used)
    - [Stripe](#stripe)
* [E-commerce Business Model](#e-commerce-business-model)
    - [Web Marketing Strategies](#web-marketing-strategies)
    - [Facebook Business Page](#facebook-business-page)
    - [Newsletter Signup & Email Marketing](#newsletter-signup--email-marketing)
    - [SEO](#seo)
    - [Paid Advertising](#paid-advertising)
    - [Links](#links)
    - [Design](#design)
        - [Logo](#logo)
    - [Color](#color)
* [Deployment](#deployment)
* [Bugs](#bugs)
* [Testing](#testing)
    - [Google Lighthouse Testing](#google-lighthouse-testing)
    - [HTML W3 Validation](#html-w3-validation)
    - [CSS Validation](#css-validation)
    - [JS validator](#js-validator)
    - [PyLint Validation](#pylint-validation)
    - [Credits](#credits)
    - [Source code](#source-code)
    - [Images](#images)
* [Contact me](#contact-me)


## Introduction

Protect is a website built in Django using Python, JavaScript, CSS and HTML. 

### Site Goals
- Site owner aim and business model.
    - Site owner can effectively sell their Antivirus program.
    - Site owner add or update their available programs that they sell.
    - Site owner can highlight their products in sale or featured products category.
-  Site User Goals:
    - Can easily find the product that they locking for.
    - Have a great user experience.
    - Can purchase Antivirus program easily. And aslo validate their licens key and download it.


## Features


### Navigation
- The navigation bar on all pages, allows users to access the key pages.
- The navbar uses a hamburger menu toggle on smaller displays and is fully responsive.
- The user can see whether they are logged in from the "My Account" dropdown options, which vary depending on the user role (admin etc). This dropdown has additional choices only available to admin users.
- only logged in users can access the profile or logout pages.
- only logged out users can access login and register page.
- The menu collapses to a toggler on smaller screens, leaving the account, search and ordersheet and burger menu links in the navbar allowing for easy navigation across all device sizes.
![](/media/readme/navigation.png)

### Footer
- Links to the site's social media pages ( Facebook) are provided in the footer.
- The footer also provides navigation to other important parts of the site including the Contact and Privacy Policy.

### Home Page
The home page is divided into different sections.

- A hero image with a link to the All Products page and some text content to boost SEO (Search Engine Optimisation).
![](/media/readme/startsida.png)

- The Recently Added Products section displays the recently added products in the navbar checkout,

### Products Page

![](/media/readme/Products.png)
- The All Products page displays all the products available on the website. 
- The user has the option to sort the products by various categories and price.
- Once the user clicks on the product, they go to the product details page.
- A sale tag is added automatically if product is on sale along with the original price
- Edit, Delete options are displayed on this page when the superuser/admin is logged in.


### Product Details Page

- The product detail page provides additional information about the products
- The user can choose the units of the product they wish to purchase
- If an item is added for a certain duration of years, and the same item added for a different duration of years, they now appear as two separate cart items.
For example, if you buy 1 item and choose 2 years, you can only add more products with 2 years of subscription. For example, if you want to add 1 item but change it to 3 years of subscription, you have to go back to the product page and add a new product with the number of selected years that you want and remove the first choice that you no longer want from the shopping cart.

- Edit, Delete options are displayed on this page when the superuser/admin is logged in.

![](/media/readme/Product_detail.png)


### Checkout Page
- The checkout page is intended to make it easy for a user to make purchase.
- Only registered users can save their info for future purchase.
- It also shows the summary of the products so that the user knows what they are purchasing before making the payment.
- The page gives the buyer an option to create an account if they wish to save their details for future.


 ![](/media/readme/checkout.png)

### Ordersheet Page

- When the order has been complited the user land on ordersheet page.
- The Ordersheet page provides a summary of the items in the ordersheet and total prices.
- The page calculates prices of items automatically if an item is on sale.
- The user may easily make their final purchasing decisions because they have the opportunity to update or remove goods from the ordersheet.

    ![](/media/readme/ordersheet.png)


### Wishlist Page

- From product detal page, user can add an product to its personal wishlist. Applys only when user are logged in.
- In the top menu, user can access its own wishlist by clicking on the heart icon
    ![](/media/readme/wishlist.png)


### Profile Page
- A registered user can easily access their order history and modify their default shipping information on their profile page.
- User can also update their information.
- The user can view their purchased product license. 
    ![](/media/readme/profile.png)

### Contact Page
- The Contact page displays the imaginary address of the company office and its location on the map.
- It also gives users the option to click on the botton to contact us.

- When you go to "Contact us" the form is updated. Everything that is sent is stored in the database as well, under the Contact model

    ![](/media/readme/protect-contact-form.png)

### Error 404 Page and 500 error Page

- A 404 error page gives the user a helpful message if a link is used incorrectly.
- It also gives the user a way to get back to the home page with a link.
- The 500 error page also provides response if something goes wrong in the code on the server, with a way to recover, without debug messaging.


### Forgot Password
- If a user forgets their password they can reset it. 
- They will be asked to enter their email, and the site will send them an email with a link to reset their password.
- User will be asked to enter their new password twice for confirmation.
- password reset form
 
### Register Page
 Users can register on this page. 
If they are already registered, the page gives them a link to the Login page.

### Login

Users can log in on this page. 
If they are not registered, there is a link to the register page.

### Contact Page

Users can view company details and they can fill up the form contact us.
![]()

### Review

Users can add reviews on individual products. Only logged-in users can add reviews. A created review cannot be modified or deleted by users.
Only superuser users can delete reviews.
![](/media/readme/protect-adding-product-review.png)

## Future ideas

- Devolope a antivirus software program
- Add more product for security
- Could enable Site admin to respond to a message on the site

## Model Schema

Two relational databases were used to create the site. 
The builtin Django SQLite database was used for development and then Elephant SQL Postgres for the deployed version. 
The site is based around a number of models separated into the following main groups.

![](/media/readme/protect-db-diagram.png)


**Product model**
 
*Category* - stores the details of a product category.

*Product* - stores all the details about a product for sale. Connected to the featured product, recently added products and Category objects via foreign key relationships.

**User model**

 *User* - the Django Allauth user model containing information such as username and password.

 *Profile* - stores a users default delivery information and is connected to the User via a one to one relationship.

**Order Models**

 *Order* - a foreign key relationship connects the user profile to the storage of the complete order data.

 *OrderLineItem* - stores the product information for a single product purchased on an order. Foreign key relationships connect the product and order.

## Agile Development

This project was started with my GitHub Projects [Page](https://github.com/saram88/Protect) to track and manage the [issues](https://github.com/saram88/Protect/issues) such as user stories, milestones and other work and sprints involved.
The purpose of Agile Development is to plan and measure progress for expected work and tasks, by listing the epics and then break them down into user stories or smaller tasks to ultimately finish the site in the allocated time.

At the initial stages I decided on core requirements ('must have' issues) for the project and some 'could have' issues but not critical requirements.

From these I added the associated user stories, acceptance criteria and the tasks so I can track my work effectively.


Once I completed a task I note the item as completed and if all parts of this story were completed I would move it from **In Progress** to **Done** on the board. Acceptance criteria would also be noted where appropriate.

### Epics and userstorys

To view details of the user stories please click on a user story below.
See the project page for the full [list of issues](https://github.com/saram88/Protect/issues) to see the details and comments.

## Technologies Used

### Language Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks Used
- [Django](https://www.djangoproject.com/) - A high-level Python web framework for rapid development with clean, pragmatic design.
- [Bootstrap](https://getbootstrap.com/) - A framework for building responsive, mobile-first sites.

### Libraries Used
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

### Database Used

[ElephantSQL](https://www.elephantsql.com/) for deployment to heroku.

### Stripe
[Stripe](https://stripe.com/gb) has been used for the payment for this website.

The developer mode in Stripe allows us to use and process test payments.

Type | card No | Expiry | CVC | ZIP
--- | --- | --- | --- | ---
Success | **4242 4242 4242 4242** | A date in the future | Any 3 digits| Any 3 digits
Require authorisation | **4000 0027 6000 3184** | A date in the future | Any 3 digits| Any 5 digits

## E-commerce Business Model

### Web Marketing Strategies
- The following strategies for Test a Virus and VPN have been considered and a combination of strategies can be implemented as the company grows.
- For an online service, word of mouth will be the strongest tool alongside online support as described below. Whit person that work in company and talk to college in other company.

### Facebook Business Page

![](/media/readme/facebook%20protect.png)


- The Facebook Business page for Test a Protect will be set up as an initial entry into the social media marketing space. 
- It would be beneficial to set up an Instagram page that can link with Facebook and allow for more engagement with the target market.
- The content would be focused on professional things that support why the user should have Virus security. 
- It can also drive traffic to the newsletter to share more long-form content. 
- Brand campaigns can be developed e.g. interviewing customers and getting testimonials.
- Paid Instagram and Facebook ads can be used as a driver to the website.
  
### Newsletter Signup & Email Marketing

![](/media/readme/Mailshimp.png)

- The newsletter can allow more detail and article-type content to be delivered to those who opt-in. 
- This can begin as a monthly update and can increase to weekly once a larger audience is established.
- The social media pages can be used as a guide to what content is interesting to followers. 
- Testing of approaches can be easily done to see which content generates referrals and sales. 
- If there are competitions, offers, or information accouterments this channel can assist in information sharing with customers.

### SEO
- The content of the website was written inspired by real-business operating sites with similar content without the use of keyword stuffing as a bad practice.
- The website was designed to extend additional meta descriptions and keywords as the site grows.
- For now, the home and services page are SEO optimised which can be reworked if Google Adwords are implemented at a later stage.
- There is a [robots.txt](https://github.com/saram88/Protect/blob/df4c99365800fe04c38297b4a6959b65bd38fd8a/robots.txt) and [site-map.xml](https://github.com/saram88/Protect/blob/df4c99365800fe04c38297b4a6959b65bd38fd8a/sitemap.xml) for search engine crawlers and proper indexing.   

### Paid Advertising
- For the size of this business, it would be beneficial to look at how social media advertising can drive traffic to the website with engaging content that is relatable to the customer.

### Links
- social links and other links that go outside the domain have `rel="nofollower"` to signal to search engines that those links are not associated with our specific domain

### Design
The website is created to look good and be easy to use, and also making it possible for a customer to browse and buy products of interest quickly and easily.
For desktop, tablet, and mobile devices, where produced and only few colors were used to maintain the ARIA accessibility of the website.

### Logo ###
For this project i create my own logo in Canva desgin. The logo also stand for all products but then whit different colors. The logo have something in it that make you think about protection and make the user to feel secure and get a good impression of the Company.   

![](/media/readme/readmelogo.png)

### Color 

The color palette for this project was kept as simple as possible in order to maintain the contrast between the background and the foreground.

**[Homepage to Coolers](https://coolors.co/)**

![](/media/readme/Coolers.png)


## Deployment

The site has been deployed to Heroku at [Here](https://saram88-protect-d3535879dbc8.herokuapp.com)

To se specifide detail about the deplyment, see deployment.md file

## Bugs

- No bugs detacted after last update of site
## Testing

### Manually function testing ###

#### Account Registration test #### 
User | Function | Description | Result 
--- | --- | --- | --- 
|Site user | User can create account | the sign up page creates a new user when correctly completed | OK |
|Site user | User can log into account| the new user can sign in and their name appears in the main page and subsequent orders made | OK|
|Site user | User can log out of account| the logout option returns to the main non logged in page with the register and login options| OK|


#### Navigation test #### 
User | Function | Description | Result 
--- | --- | --- | --- 
|Site user|User can navigate to Product Details | Product details are displayed when product clicked in list | OK |
|Site user|User can access menu items| Menu items are appropriate to state and appear in dropdow for CRUD | OK|
|Site admin|Admin can access admin panel| Admin user menu item appears and goes to Admin page |OK|

#### Security test ####
User | Function | Description | Result 
--- | --- | --- | --- 
|All user|Not logged in user cannot add a product | Not logged in User cannot create a product (cut and paste create link) and returns to the login page |OK |
|All user|Not logged in user cannot edit a product | Not logged in User cannot edit a product (cut and paste edit link) and returns to login page | OK|
|Site user|Non superuser cannot access admin panel | User not logged in trying to get to admin link fails and goes to admin login page | OK|

#### View and purchase test #### 
User | Function | Description | Result 
--- | --- | --- | --- 
|Logged in user|User can save a profile or order when all required fields are completed | if fields are missing, informative errors are flagged, and completes successfully when form is complete | OK |
|Logged in user|User can save a profile or order when all required fields are completed | user has the option to complete the profile/order | OK |
|Logged in user|User can save a profile or order when all required fields are completed | user has the option to draft save a profile or order which then needs to be edited to be completed | OK |
|Logged in user|User tries to submit a profile or order with empty form is not possible | if form is blank the profile or order does not submit |OK|
|Logged in user|User can view their profile or order | user can see the profile or order page when submitted |OK|
|Logged in user|User can edit the profile or order| user can only see the edit button on their profile or order detail |OK|
|Logged in|Edit button does not present on other users profile or order| User only gets edit button on their profile or orer |OK|

#### Account test ####
User | Function | Description | Result 
--- | --- | --- | --- 
|All user|User cannot register username to the same as another user| trying an existing username fails if it already exists |OK|
|All user|User cannot register their email to the same as another user | trying an existing email fails if it is already recorded |OK|

#### Admin test ####
User | Function | Description | Result 
--- | --- | --- | --- 
|Admin user|Admin can add products to site| Admin panel has the option to add products and products appear when published  |OK|
|Admin can edit products on site| Admin panel can edit products and updates show on products |OK|
|Admin user|Admin can delete products on site| Admin panel has delete option and products disappear when deleted |OK|
|Admin user|Products changed by the admin display correctly on main site when updated / added| Changes appear when main site is viewed |OK|

### Automatic testing ###

#### Google Lighthouse Testing ####

The lighthouse results do vary depending on Internet contention and time of day, affecting the load times for linked resources such as bootstrap, fonts, css and js.
The necessary bootstrap modules, particularly for Popper dropdown menus and Stripe functionality do add siginificant load, but are essential.
Even with preload statements they still take time to load, so the Lighthouse performance stat is as good as it can be at this time.
I did also try using Cloudinary responsive image features, but found it added further load.
So I managed to get good results by using WEBP file type for images, especially now that Apple IoS supports webp.

I try to follow this manual, if you want to read more [Here](https://developer.chrome.com/docs/lighthouse/performance/uses-webp-images/?utm_source=lighthouse&utm_medium=devtools)

![](/media/readme/testchrome.jpg)

#### HTML W3 Validation ####

![HTML ✅ ](/media/readme/htmlchecker.jpg)
Result: Pass - No Errors

#### CSS Validation ####

Here is a link to the validate result that you also can use for future if i want to validate it again if i chnage something. [Here](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fsaram88-protect-d3535879dbc8.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv)  

Result: Pass - No Errors

![W3 Validation checker](/media/readme/testcss.jpg)

#### JS validator ####

![jshint.com](/media/readme/testjs.png)
Result: Pass - No Errors

#### PyLint Validation ####
![https://pep8ci.herokuapp.com](/media/readme/testpy.jpg)
Result: Pass - No Errors

## Credits
- The Code Institute 'Boutique Ado' walkthrough project assisted and guided in the setup and basic structure of this project.
- https://www.geeksforgeeks.org/ - code solutions
- https://www.w3schools.com/ - code solutions
- https://github.com/Code-Institute-Org/gitpod-full-template - Code Institute Template
- https://pep8ci.herokuapp.com/ - code validation tool
- Mailchimp - subscription tool
- Stripe - payment tool
- AWS & ElephantSQL - databases
- Heroku - hosting
- GitPod - IDE
- https://www.privacypolicygenerator.info/( for pravicy policys)
- https://www.wordtracker.com/ ( keywords SEO)
- https://stackoverflow.com ( for different code issues)


## Source code

- Code Institute Django course material, tutors, mentors and colleagues in Slack channels.
- Bootstrap documentation https://getbootstrap.com/docs/5.3/getting-started/introduction/ 

    
## Images
- Product images https://www.pexels.com/ 
- favicon.ico generation https://favicon.io/favicon-generator/
- Colors from [Coolors](https://coolors.co/)

# Contact me

- Sara Mentzer [LinkedIn](https://www.linkedin.com/in/sara-mentzer-17b9b1170/)
- Sara Mentzer [GitHub](https://github.com/saram88)

[def]: #login