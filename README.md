# python-challenge
third week's assignment

Hana Wasif
Instructor Anish Talsania
Data Analytics
8 August 2024



My approach to PyBank's instructions was to take them, step-by-step.

    I knew that they involved budget_data.csv, so I set my sights on importing it to main.py and opening it as a reading file in order to analyze it with my script.

    After doing so, I decided on looping through budget_data.csv's rows, as the first direction to calculate totalmonths required it. Seeing the format of budget_data.csv, I figured that totalmonths would be the same as the amount of lines in file since each line contained a unique month; thus, totalmonths = totalmonths + 1 was born in my script's loop.

    Then, I arrived at the second direction, asking for me to calculate total. The process to calculate total was similar to the process to calculate totalmonths, with the exception of the "+ 1" at the end of the previous formula. In stead of "+ 1", I used "+ int(row[1])" because I was not counting the line: I was counting the /value/ in the line.

    While the prior calculations were relatively unchallenging, approaching the calculation to averagechange was difficult to fathom. Consequently, I chose to write what I knew: averagechange = sum(changes) / len(changes). Still, there was a gaping hole in my logic...How would I calculate every single change between every single line? Consulting Xpert and reviewing Python's basics on Monday's slides truly helped. I pursued the concept of lists, and it worked out. Smooth sailing followed, with a few hiccups pertaining the placement of previousvalue's variable in the loop yet out of the condiitonal.

    When I finished with calculating total, I directed my attention to giip and gdip. I had an idea that their calculations would be quite similar, and their only major difference would amount to selecting between < and >. As a result, conditionals seemed to be my best bet.



My approach to PyPoll's instuctions was much of the same, going little by little.

    Before I even managed to complete Pybank's instructions, I calculated totalvotes as soon as I figured out how to calculate the aforementioned totalmonths. All that I had to do was count the amount of Ballot IDs -- which was very easy, due to the fact that each line had a unique Ballot ID, meaning that I could simply count the rows as I had done above.

    In regards to storing each candidate in a variable, I -- again -- did as I had done above: Essentially, lists were my best friend. After filling the list for all of the candidates, I did /not/ calculate their percentages before calculating their total votes as PyPoll's instructions suggest for us to do. On the contrary, I calculated their total votes, first. The way that I learned to calculate percentages (their percentages = their total votes / totalvotes) requires me to know their total votes as a prerequisite.

    The winner would depend on which candidate had the most votes, but there were 3 candidates to consider. Again, a conditional seemed to be my best bet.
