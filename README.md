<h1>My Amazing Perfect Bug-free* Anki Project</h1>
<h6>*May not be bug-free</h6>

<h2>Greetings Sigma Labs trainees!</h2>

Are you tired of the sleepless nights having to revise for the Mastery Quizzes? 
Have you ever thought to yourself "There has to be a better way?".

<h3>Then look no further!</h3>

This repo contains a script that helps automatically generate Anki flashcards for questions that you have gotten wrong in the Mastery Quizzes. It support html tags as well, so questions containing code are also nice and readable! 

Unforunately, this script only makes basic flashcards for now, so no cloze or image occlusion

Note, this does **not** teach you how to use Anki. For more information on that, please see <a href="https://www.youtube.com/watch?v=WmPx333n5UQ">this</a> YouTube tutorial.
<h2>How does it work?</h2>
The script works by pulling data from the Airtable API regarding questions you have gotten wrong in the Mastery Quizzes. It uses a PAT to access the Airtable data.

<br> **For security reasons, this token is not uploaded to the repo. Please speak to your tech coaches in your careers channel for assistance with this.** </br>

<h2>Usage</h2>
<ol>
  <li>Using the script</li>
  <li>Making flashcards in Anki</li>
</ol> 

<h2>Using the script</h2>

As mentioned above, the PAT required for the script to work is not in the repo. Please ask in your **#careers** channels for the PAT and for further assistance. When you have your PAT, you need to tell the script how to use it. Here's how...

<ol>
  <li>Create a folder to store the anki.py file and its outputs</li>
  <li>In this same folder, create a .env file</li>
  <li>In this .env file, insert the following: token={your token here}</li>
  <li>Run the anki.py script</li> 
</ol> 

Following these steps should create an _anki_cards.txt_ file in a folder called _/trainee_data_ located in the same folder made in step 1. 

With this _.txt_ file, move onto the next part - making the cards.

<h2>Making flashcards in Anki</h2>

Once you have the <em>anki_cards.txt</em> file, you need to tell Anki to make flashcards with them.
<ol>
  <li>Open up Anki</li>
  <li>Select the profile you want to add the cards to</li>
  <li>Go to File>Import</li>
  <li>Select the <em>anki_cards.txt</em> file</li>
  <li>In the top-right, select the 'Import' button.</li>
</ol>
  
<h2>That's it!</h2>

The flash cards have now been added to your Anki profile. Have fun!
<br></br>
<h3>(Bugs are welcome! If you find any, let me know and I will try to fix them.)</h3>
