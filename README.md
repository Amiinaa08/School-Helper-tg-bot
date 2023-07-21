# School-Helper-tg-bot

The School Helper Telegram Bot is a Python-based bot designed to assist with
various school-related questions. It provides help in subjects such as physics,
geography, astronomy, math, and philology, as well as general questions.

## Adding a new theme

To add a new theme, follow these steps:

1. Create a new folder under the `categories` directory to represent the new theme.

2. Inside the new category folder, create new bot functions. You can refer to the
   examples in any of the existing categories.

3. Create an `__init__.py` file within the category folder and import the newly
   created functions.

4. Add the new category to the hierarchy in the `constants.py` file.

   - Begin by importing the category using the following syntax:

   ```python
   import categories.your_category as your_category_functions
   ```

   - Next, add the category to the APP_HIERARCHY constant. Specify the category name,
     its subcategories, and the associated function names. You can use the existing
     categories and functions as a reference.

By following these steps, you can easily add a new theme to the School Helper Telegram Bot
and extend its functionality.

Feel free to use the bot and get the best grades! :>
