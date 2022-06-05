# **Cartwright's Jewellery & Goldsmiths - Site Testing**

[Main README.md file](/README.md)

[View the live project on Heroku](https://cartwrights-jewellery.herokuapp.com/)

## Table of Contents 
* [Test User Stories](#test-user-stories)
* [Testing and Validation](#testing-and-validation) 
* [Manual testing](#manual-testing)
* [Bugs and Fixes](#bugs-and-fixes)
* [Further testing](#further-testing)

---
<br>

## **Test User Stories**
Testing user stories from the UX section with the corresponding features and content.

<details>
<summary>New Visitor</summary>

![New Visitor](/documentation/images/test-images/test_user_stories_guest.png)
</details>
<br>
<details>
<summary>Registered User</summary>

![Registered User](/documentation/images/test-images/test_user_stories_registered.png)
</details>
<br>
<details>
<summary>Admin User</summary>

![Admin User](/documentation/images/test-images/test_user_stories_Admin.png)
</details>
<br>

### User story images:

<details>
<summary>Home</summary>

![Home](/documentation/images/test-images/landing_home.png)
</details>

<details>
<summary>Footer</summary>

![Footer](/documentation/images/test-images/footer.png)
</details>

<details>
<summary>Shop: Product filter, sort and search</summary>

![Shop: Products](/documentation/images/test-images/product_filter_sort_search.png)
</details>

<details>
<summary>Product Detail</summary>

![Product Detail](/documentation/images/test-images/product_detail.png)
</details>

<details>
<summary>Baseket: Empty</summary>

![Basket: Empty](/documentation/images/test-images/basket_empty.png)
</details>

<details>
<summary>Basket: With Products</summary>

![Baskett: With Products](/documentation/images/test-images/basket_with_products.png)
</details>

<details>
<summary>Checkout</summary>

![Checkout](/documentation/images/test-images/checkout.png)
</details>

<details>
<summary>Checkout Success</summary>

![Checkout Success](/documentation/images/test-images/checkout_success.png)
</details>

<details>
<summary>Profile</summary>

![Profile](/documentation/images/test-images/profile.png)
</details>

<details>
<summary>Login</summary>

![Login](/documentation/images/test-images/login.png)
</details>

<details>
<summary>Register</summary>

![Register](/documentation/images/test-images/register.png)
</details>

<details>
<summary>User Reviews</summary>

![User Reviews](/documentation/images/test-images/user_reviews.png)
</details>

---
<br>

## **Testing and Validation**

### [Link Checker](https://validator.w3.org/checklink)
- To check that all links are working and not broken. 
- The report did not have any issues in final testing.

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- To validate the HTML code of the project by pasting code in by direct input method. Note the W3C Validator for HTML does not understand the Jinja templating syntax therefore if there are warnings related to this, this can be safely ignored.
- All issues were resolved except for 2 errors relating to Django crispy forms (see image below for more detail)
<details>

<summary>Checklist for checking all HTMl pages</summary>

![Checklist for checking all HTMl pages](/documentation/images/test-images/html-validation-table.png)
</details>
<br>

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- To validate the CSS code of the project pasting code in by direct input method.
- All issues were resolved

<details>
<summary>CSS Validation</summary>

![CSS Validation](/documentation/images/test-images/css_validation.png)
</details>

### [JavaScript: JSHint](https://jshint.com/)
- JSHint was used to test javascript code in this project. 
- All issues were resolved except the below:
   - Final version - addressing errors and warnings: 
      - Warning for ''let' is available in ES6 (use 'esversion: 6'). Can be safely ignored. If add /*jshint esversion: 6 */ at top of code so that JSHint does not raise unnecessary warnings for ECMAScript 6 features.
      - JSHint flags Jquery $ symbol as an undefined variable - safely ignored.
---

## **Manual testing**
<details>
<summary>Manual testing for features</summary>

![Manual testing for features](/documentation/images/test-images/manual-testing.png)
</details>
<br>
All features of the site have been tested. Test purchases have been made to check the order confirmation emails and these are delivered correctly, with the correct information. 

---

### Lighthouse (Google Dev Tools)

- The Lighthouse Report for the site's main home page on Mobile was as follows:
   - [Desktop Lighthouse Report](/documentation/images/test-images/lighthouse-desktop-home.png)

- The Lighthouse Report for the site's main home page on Desktop was as follows:
   - [Mobile Lighthouse Report](/documentation/images/test-images/lighthouse-mobile-home.png)
<br>
- Lighthouse testing was conducted, to test the accessibility and performance of the website. 
- After testing the site on Lighthouse, there were minor changes that needed to be made, for example, some buttons did not have aria labels, which was added. Another aspect that was fixed was link text styling, the colour needed to be changed to make it more accessible. Lastly, some heading tags were not in order, which was changed as well. 
- After the above changes were made, the overall performance and accessibility have increased. 
- Additional future changes can be made in optimising images in next-generation formats.

## **Deployment**
- Ensured deployed page on Heroku loads up correctly.
- Ensured Debug variable is set to False.
- Confirmed that there is no difference between the deployed version and the development version.