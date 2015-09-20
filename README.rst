Improving our Functional Tests
==============================

In Agile methodologies is the concept of a UserStory.

A UserStory maps almost directly to a functional test.


So what is a UserStory? A UserStory is a description of functionality from the end user's point of view.

A very basic user story looks like this:

 As a user I want a todo list so that I can keep track of my things to do.

The structure of a minimum UserStory should always be

As a <role> I want a <thing> so that I can <outcome or action>

While that does give a basic idea of what the end user wants to do it is much better to provide greater detail.

         Edith has heard about a cool new online to-do app. She goes
         to check out its homepage

         She notices the page title and header mention to-do lists

         She is invited to enter a to-do item straight away

         She types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)

         When she hits enter, the page updates, and now the page lists
         "1: Buy peacock feathers" as an item in a to-do list

         There is still a text box inviting her to add another item. She
         enters "Use peacock feathers to make a fly" (Edith is very methodical)

         The page updates again, and now shows both items on her list

         Edith wonders whether the site will remember her list. Then she sees
         that the site has generated a unique URL for her -- there is some
         explanatory text to that effect.

         She visits that URL - her to-do list is still there.

         Satisfied, she goes back to sleep

This is much richer in detail and much easier to create a test from.