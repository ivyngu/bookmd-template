# bookmd-template

A short python script to create a markdown file containing book details. 

To run the script, first make sure you have python3 on your machine. Download the code and place it into your desired directory. Then, open the terminal and cd into that folder. Run the script by writing the command: 
  python3 bsmd.py

The script prompts you to choose between a fiction & non-fiction book template. Then, it prompts you for a GoodReads link to scrape for the book title & author. It will create a markdown file in the current working directory.

The created markdown file contains the book title, book author, and a template for you to fill out.
Both templates include:
- Date Started
- Date Finished
- Rating

The non-fiction template includes these prompts:
- the book in 3 sentences
- impressions
- who should read it?
- how the book changed me
- my top 3 quotes
- summary + notes

The fiction template includes these prompts:
- summary
- how i discovered it
- thoughts
- who would like it?

One can modify the script to add/remove prompts from the template to their own preferences. Simply change what is stored in nf_str for non-fiction and f_str for fiction.
Hope this helps with book tracking!
