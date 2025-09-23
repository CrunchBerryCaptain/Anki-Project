<h1>My Amazing Perfect Bug-free* Anki Project</h1>
<h6>*May not be bug-free</h6>

<h2>Greetings Sigma Labs trainees!</h2>

Are you tired of the sleepless nights having to revise for the Mastery Quizzes? 
Have you ever thought to yourself "There has to be a better way?".

<h3>Then look no further!</h3>

This repo contains a script that helps automatically generate Anki flashcards for questions that you have gotten wrong in the Mastery Quizzes. It support html tags as well, so questions containing code are also nice and readable!

Note, this does **not** teach you how to use Anki. For more information on that, please consult your nearest YouTube tutorial.

<h2>How does it work?</h2>
The script works by pulling data from the Airtable API regarding questions you have gotten wrong in the Mastery Quizzes. It uses a PAT to access the Airtable data.

**For security reasons, this token is not uploaded to the repo. Please speak to your tech coaches in your careers channel for assistance with this.**

<h2>Usage</h2>
<ol>
  <li>Using the script</li>
  <li>Making flashcards in Anki</li>
</ol> 

<h2>Using the script</h2>

As mentioned above, the PAT required for the script to work is not in the repo. Please ask in your **#careers** channels for the PAT and for further assistance.

When that is complete, running the file with python3 will create an _anki_cards.txt_ file in a folder called _/trainee_data_ located in the same folder the script was ran from. With this _.txt_ file, move onto Step 2 - making the cards.

<h2>Making flashcards in Anki</h2>

Once you have the _anki_cards.txt_ file, navigate to Anki. Go to File>Import then select the _anki_cards.txt_ file. You should be prompted with a pop-up. In the top-right, please select the **Import** button.

<h2>That's it!</h2>

The flash cards have now been added to your Anki profile. Have fun!
