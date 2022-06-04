# **Cartwright's Jewellery & Goldsmiths**

Cartwright's Jewellery & Goldsmiths, is the final Milestone project, specifically built for the Django modules of the Code Institute's - Full Stack Software Development Diploma. The scope and idea for this project, were to plan, design and build an e-commerce website, that gives users all of the same functionality of any other general e-commerce based website. The project is built around an idea for an online Jewellery store, with a view to possibly being used as a full production site for a family member, when the course has been completed.

[View the live project on Heroku](https://cartwrights-jewellery.herokuapp.com/)

![Am I responsive image]()

---
## **Contents**

- [UX Design](#ux-design)
- [UI Design](#ux-design)
- [Wireframes](#wireframes)
- [Data Structure](#data-structure) 
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---

## **UX Design**

### **User Persona**

The website is targeted at users who may be interested in purchasing ready made Jewellery, or accessing bespoke design and production services. The primary focus of the site is to ensure users are faced with a site that is easy to navigate, offers the user the options to browse the site, purchase items, or make contact for bespoke design services.


### **User Goals**

- Be able to view all products available on the site
- Be able to view featured products of deals.
- Be able to be able to vies the contact details for the store and it's bespoke services.
- Be able to use the application on Mobile, Tablet or Desktop devices. 

### **Site Owners Goals**

- Provide a positive experience for all users, looking to access the site and make purchases.
- Ensure that the sites purchasing functionality is as clear and seamless as possible, increasing the number of conversions and reducing cart abandonment.
- Be a "go-to" store, for users looking to purchase jewellery products.
- Make it easy for any potential customer to contact or find the store and ask any questions. 


### **User Requirements and Expectations**
#### Requirements 

- Easily identifiable navigation.
- Clean and structured layout with rlevant links to different product categories.
- Visually appealing elements
- Easy way to search, sort and filter products for quick and easy viewing and purcahsing.
- Be notified of order confirmation via email.

#### Expectations

- When using the main navigational links, the user should be directed to each part of the application without issue.
- Links clicked on in the user resources, should open in a new page and not overwrite the current page that the user is on.
- The ability to purchase a product safely and securely, with a clear process and confirmation of the purchase.
- To be able to register for an account with the store, where I can see previous purchases and re-order if required..

### **User Stories**

#### *New Visitor*
1. As a first time visitor, I want the main purpose of the site to be immediately clear.
2. As a first time visitor, I want the look of the site to be visually appealing.
3. As a first time visitor, I want the layout of the site to be well structured.
4. As a first time visitor, I want to be able to easily navigate the site and see the different product categories that are available.
5. As a first time visitor, I want to be able to easily find the main products page.
7. As a first time visitor, I want to be able to navigate directly to pages for specific product categories.
8. As a first time visitor, I want to be able to sort or filter product categories, to more relevant product views.
9. As a first time visitor, I want to be able to conduct a more specific search for a product, via an easily accessible search function.
10. As a first time visitor, I want to be able to closely view product details in their own page.
11. As a first time visitor, I want to be able to have full control over the amounts of a product that can be purchased.
12. As a first time visitor, I want to be able to add the chosen products to a shopping basket where the basket total can be seen.
13. As a first time visitor, I want to be able to access the shopping basket at any time and update or remove the chosen products, seeing an update to the overall shopping basket total.
14. As a first time visitor, I want to be able to preview the order details before continuing to make a purchase.
15. As a first time visitor, I want to be able to follow a simple payment process which feels secure.
16. As a first time visitor, I want to be able to see notifications appear, instructing of confirmed or failed purchases, with feedback on the reasons for failed purchases.
17. As a first time visitor, I want to be able to register as a user either before purchasing products or after purchasing products.
18. As a first time visitor, I want to be able to find contact details for the site owners, and possibly submit an online enquiry regarding bespoke jewellery design. 
19. As a first time visitor, I want to be able to connect with the store on social media platforms where I can see additional information.

#### *Registered User*

As a regitered user, I would want all of the same functionality of that of a guest user, as well as:

1. As a registered user, I want to be able to login with a set of registered credentials.
2. As a registered user, I want to be able to logout of my account.
3. As a registered user, I want to be able to change my user credentials should they be forgotten.
4. As a registered user, I want to be able to add and store my personal details for future use on the site.
5. As a registered user, I want to be able to edit or delete my personal details, should circumstances require it.
6. As a registered user, I want to be able to see a profile page where I can view my previous orders.

#### *Site Administrator*

As a site administrator, I would want all of the same functionality of that of a guest/registered user, as well as:

1. As a site Administrator, I would want to be able to control the main functionality of the site, including adding new categories and products.
2. As a site Administrator, I would want to be able to edit or delete categories and products as required.
3. As a site Administrator, I would want to be able to view all current and existing purchases made by users for accessing should a purchase query arise.
4. As a site Administrator, I would want to be able to add new users or delete users who have issues with registration or account deletion functionality.

---

## **UI Design**

### Fonts
- The project uses Google Fonts for the delivery of the main font styling.
- The main font used for body text, is the Source Sans Pro font.
- The font used for the main logo and nav links in the header is Playfair Display.

### Colour Scheme
- The colour scheme was chosen to make the site look as visually appealing, using a minimal amount of colours.

The overall colour palette was designed from a website called [Coolors](https://coolors.co/) and was selected, becasue of the broad spectrum of colour options available. However, not all colours in the palette are used. 
![Colour Palette](/documentation/images/general-images/MS4-palette.png)

- The Davy's Grey color was used for the general font color of the site, so that it stands out against the background colour.
- The Vivid Sky Blue colour is used for the bacground colour of the navigation bar and for the footer   
- The Gainsborough colour has been used as the general background colour for all pages.
- The Vivid Sky Blue colour has been used for the buttons, with the Cerulean Blue colour being used to accent the button colours with the hover feature.

### Icons

Where required, icons used have been incorporated using Font Awesome

---

## **Wireframes**

### **Low Fidelity Wireframes**

Low fidelity wireframes were created with Balsamiq, and bring to life the basic prototyping structure of how the site may initially be designed to look.

- [Home Page](/documentation/wireframes/home-page.png)
- [Products Page](/documentation/wireframes/products-page.png)
- [Product Details](/documentation/wireframes/product-details.png)
- [Shopping Basket](/documentation/wireframes/shopping-basket.png)
- [Checkout Page](/documentation/wireframes/checkout-page.png)
- [User Reviews](/documentation/wireframes/user-reviews.png)

---
## **Features**

**Implemented**

*Generic*
* Responsive design on the vast majority of devices
* Delivery banner which displays the purchase requirement for free delivery and also product information.
* Navigation bar, including logo and link to the home page, a search box, an account icon and shopping basket icon which also displays the number of items currently in the basket.
* Links in the navigation bar collapse to a hamburger button on smaller devices such as smartphones and tablets.
* Toast messages giving users meaningful feedback to their actions on the website.
* Footer with navigation links to all pages, contact details, social media links and copyright information.
* 'Back to top' button where applicable.

*Homepage*
* Hero image with call to action button to encourage people to make a purchase.
* An About-Us section detailing the business, its locations and it's history.
* A bespoke design section highlighting the option for customer to purchase bespoke design creations services from the buisness, with images to show previously designed jewellery.

*Product Pages*
* Clear pictures of the products.
* Ability to sort products by name and price.
* Gives store admin access to edit/delete options.

*Product Details Page*
* The product detail page gives a larger image.
* Also gives users the ability to select a quantity to add to the basket.
* Gives store admin access to edit/delete options.


*Add & Edit Product Pages*
* These pages give the store admin the ability to add new products and edit existing ones.

*Basket Page*
* Shows all the products in the basket.
* The ability to amend items in the basket.
* Also shows the total amount due, delivery costs and any applicable discount.

*Checkout Page*
* Users can enter delivery and payment information for their purchase.
* This information is pre-filled if the user already has logged in to their saved profile.
* Webhooks were employed to ensure smooth and secure transactions.

*User Review Page*
* A user review page where visitors to the site can view reviews of the jewellery purchased by customers.
* Ability to add Images to the review with the main review title being a link to the full review.
* Details of the author and date published.
* Ability for people to comment on the review posts.

*News (Blog) Detail*
* Comment section allowing users to comment on posts that have been published.
* Each review shows all comments left by visitors to the site.
* A form where people can leave comments on a review (this includes a call to action to be the first to comment).
* The ability to edit or delete a news post (admin logins only).

*User Profile Page*
* User can edit their contact and delivery information held on the system.
* User can also see their order history.

**Future Features to Implement**
* The ability to login using a social media account.
* A wish list feature.
* Inventory tracking so stock availability can be shown on website.
* 'Track my order' functionality so that customers can see the status of their order.
* Skip navigation links for visitors to the site with certain disabilities to enhance their UX.
* The ability to accept or edit cookies.
* Marketing opt-in options on the registration page.

---

## **Testing**

Testing information can be found in the separate [TESTING.md file](readme/testing/TESTING.md)

---

## **Technologies Used**

*IDE*
* Gitpod

*Languages*
* Python
* HTML
* CSS
* JavaScript

*Frameworks, Templates & Libraries*
* Django
* JQuery
* Jinja
* Bootstrap
* Font Awesome
* Google Fonts

*Storage & Hosting*
* Heroku
* Github
* Amazon Web Services

*Databases*
* SQLite3 for development
* PostgresSQL for the deployed site

*Payment Service*
* Stripe

*Other Tools*
* Google Dev Tools (including Lighthouse)
* Pep8online.com (to check Python code for PEP 8 requirements)
* W3C Validator (to check validity of HTML and CSS)
* JSHint.com (to check JavaScript)
* dbdiagram.io (to produce the MongoDB ERD)

---
## **Deployment**

As with testing, due to the amount of information regarding deployment, it has been detailed in the following separate [file](readme/deployment/Deployment.md).

---

## **Credits**