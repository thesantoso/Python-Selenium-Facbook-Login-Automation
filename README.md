# Python-Selenium-Facebook-Login-Automation

The program is an automation script that utilizes Selenium WebDriver to perform a login test on the Facebook website.

The program starts by initializing the Chrome driver using the appropriate Chromedriver file path. Then, it opens the Facebook page using the `get()` method.

Once the page is open, the program locates the email input element and enters the specified email using the `send_keys()` method. It then finds the password input element and enters the specified password.

Next, the program waits for the "Login" button to become interactive using `WebDriverWait` and `expected_conditions`. Once the button is clickable, the program clicks on it using the `click()` method.

After clicking the "Login" button, the program waits for 20 seconds using `time.sleep()` to allow time for the login process before terminating. Finally, the program closes the Chrome browser by calling the `quit()` method on the driver object.

This program is useful for automating the login process on Facebook, enabling automated testing or other tasks that require logging into a Facebook account.
