# Armaan Shamsaasef Repo 

# Notes 5.1 5.2 5.3 5.4 5.5, Quiz Scores, and Github Actions

<img width="1152" alt="Screen Shot 2022-02-18 at 11 49 18 AM" src="https://user-images.githubusercontent.com/89277945/154751954-bb725c9d-3dd3-45fd-b396-1598c894acc5.png">

### 5.1 Notes
- Creating Innovation designed with grouping
- Single effects can be viewed as beneficial and harmful by different or same people
### 5.2 Notes
- A decidable problem is a decision problem for which an algorithm can be written to produce a correct output for all inputs
- An undecidable problem is one for which no algorithm can be constructed that is always capable of providing a correct yes-or-no answer.
- An undecidable problem may have some instances that have an algorithmic solution, but there is no algorithmic solution that could solve all instances of the problem

### 5.3 Notes
- Sequential computing is a computational model in which operations are performed in order one at a time
- Parallel computing is a computational model where the program is broken into multiple smaller sequential computing operations, some of which are performed simultaneously.
- Distributed computing is a computational model in which multiple devices are used to run a program
- Comparing efficiency of solutions can be done by comparing the time it takes to perform the same task
- A sequential solution takes as long as the sum of all of its steps
- A parallel computing solution takes as long as its sequential tasks plus the longest of its parallel tasks.
- The “speedup” of a parallel solution is measured in the time it took to complete the task sequentially divided by the time it took to complete the task when done in parallel
### 5.4 Notes/ Corrections
- I accidentally got this wrong because I did not read the answer fully and went with the first answer that I thought looked correct. The correct answer is D and not A because crowdsourcing is the practice of obtaining input or information from a large number of people via the Internet. Therefore, this application would benefit from the use of crowdsourcing the most, as the application could allow users to contribute descriptions and photographs of landmarks.
### 5.5 Notes
- Plagirism and copying
- Use of material by others creates legal concerns
- NOT GOOD TO DO!!!
### 5.6 Notes 
- Information on the Internet is hard to delete
- Also used for other purposes

## 5.1 Github Actions
Come up with three of your own Beneficial and corresponding Harmful Effects of Computing
Beneficial: Firstly, computers can store endless amounts of information and can help reduce the wastage of natural resources that goes into the production of paper, books, supplies. Secondly, computing connects users with millions of people across the internet through messages, social media, and more. This used to not be possible without the development of technology and computer automation. Thirdly,

Harmful: Firstly, too much use of technology can make you addicted to unrealistic things without experiencing proper social interactions that are crucial. Secondly, computing and the distribution of private information online is a prominent issue in our world and is very hard to prevent. Lastly, a heavy reliance on technology and computing can remove the need to do things individually as we now rely on something other than ourselves.

Talk about dopamine issues above. Real? Parent conspiracy? Anything that is impacting your personal study and success in High School?
Answer: Dopamine issues are where you are too addicted to doing something to the point where you rely on the pleasure it gives rather than its harmful consequences. For example, I have fallen into the trap of playing video games and watching YouTube instead of preparing for school because of the pleasure I received in the moment from the release of dopamine. It can effect school and physical performance if that is the only thing you focus on.

## 5.2 Github Actions
How does someone empower themself in a digital world?
- You can empower yourself in a digital world by staying informed about technologies and using them in your daily life. Being educated and provided with tech will help empower people in a digital environment.

How does someone that is empowered help someone that is not empowered? Describe something you could do at Del Norte HS
- Someone that is empowered can help someone that may not be empowered by providing them with a secure network or their devices with them. For example, at Del Norte, I could give my hotspot to people that may not have strong access to the internet so that they could use online services or I can share a device with them.

Is paper or red tape blocking digital empowerment? Are there such barriers at Del Norte? Elsewhere?
- Redtaping is blocking digital empowerment because it makes people have to follow additional steps in order to access information or technologies. We see this type of thing occurring in many circumstances, not necessarily in just tech. We have similar barriers at Del Norte when we try to connect ourselves to web services through a universal network for students. This field requires a password and other information in order to gain access.



# Create Task
# WishLIST - Paul and Armaan
### Planning
This Create Task Idea will allow the user to add books to a Wishlist by being prompted with different books and choosing which ones they like. By the end, they will have a list of the books they chose.

## Create Task Requirements:
- [x] Instructions for input: User will be able to select whether or not they would like to add a book to their wishlist. There will be 5 options to choose from that the user will decide on
- [x] Use of at least 1 list: The books that will be prompted will be from a question list. A list will also be created as the user decides on the books that they like.(push-js)
- [x] At least 1 procedure: The procedure will be taking the input from a user and the function will produce a list of books that they wanted to add to their wishlist
- [x] An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure: The function runs through a loop that adds questions to a list and shuffles them. There will be different parts to this and only certain action will occur when  specific conditions are met. Ex: If the user likes the book, the function will add it to a list.
- [x] Calls to your student-developed procedure: the "next" button will switch to different question and allow the user to decide on the next book they want to add
- [x] Instructions for output (tactile, audible, visual, or textual) based on input program functionality: The output will be a textual list of books that the user created
## Answers to Written Response
### [Armaan Video](https://youtu.be/gamMwwdtFfI) - Done on the local.

Part A:
Sub-Part | Question | Answer | 
--- | -------- | --------- |
i | Describe the overall purpose of the program | The purpose of WishLIST is to produce a list for the user who chooses the book that they like. This list can be used as a reference to find books they like. |
ii | Describe what part of the program is being shown in the video | The video shows where the input is taken and goes into whatever route it follows. It shows the conditions that have to be met for the program to go certain routes to produce an output. It is the full WishLIST running at its finest point. |
iii | Describes the input and output of the program demonstrated in the video | Input: shown is where the user chooses to either add the book to a list or not. After 5 books have been prompted, Output: shows the list created of the liked books the user chooses. If the user doesn't like any of the books there are more genres to choose from and the output will have nothing on the WishLIST. |

Part B:
Sub-Part | Question | Answer | 
--- | -------- | --------- |
i | The first program code segment must show how data have been stored in the list. | The list for Science-Fiction books ```sfbooks = ["Dune", "The Time Machine", "Brave New World", "The Fountain Trilogy", "Eyes of the Void"]```|
ii | The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. | Example Down Below |
```
            function mixQuestions(clist) {
                while (shuffledQ.length <= 4) {
                    const random = clist[Math.floor(Math.random() * clist.length)]
                    if (!shuffledQ.includes(random)) {
                        shuffledQ.push(random)
                    }
                }
            }
```


### B Sub-part iii-v
Sub-Part | Question | Answer | 
--- | -------- | --------- |
iii | Identifies the name of the list being used in this response | ```clist``` is a parameter in the function that takes a list made and uses it to create a random (shuffled) arrangement of the book category. |
iv | Describes what the data contained in the list represent in your program | The data in the list represents the books being prompted to the user. It is also used to create an output of what the user has selected. |
v | Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list | The lists manage the complexity of the program because it stores all the data easily without having to get it from somewhere else. An API could also do this but it would make categorizing the genres much more difficult. |

Part C:
Sub-Part | Question | Answer | 
--- | -------- | --------- |
i | The first program code segment must be a student-developed procedure that: Defines the procedure’s name and return type (if necessary), contains and uses one or more parameters that have an effect on the functionality of the procedure, and implements an algorithm that includes sequencing, selection and iteration | ![image](https://cdn.discordapp.com/attachments/749509501773807677/945741909127753758/Screen_Shot_2022-02-22_at_9.58.09_AM.png) |
ii | The second program code segment must show where your student-developed procedure is being called in your program | Runs the function with its own specific parameter! Example Down Below |
```
function chosens() {
                document.getElementById("type").innerHTML = "Sci-Fi"
                document.getElementById('quiz').style.display = '';
                button1.disabled = true;
                button2.disabled = true;
                CurrQuestion(0, questions3)
            }
```
### C Sub-part iii & iv
Sub-Part | Question | Answer | 
--- | -------- | --------- |
iii |  Describes in general what the identified procedure does and how it contributes to the overall functionality of the program| This procedure basically prompts the user with a book and the option to add it to the list or not. It starts of by taking the parameter that is chosen by the user and uses it to shuffle the books to prompt the user. It then creates the first question ```currentQuestion```. It also decides what the button "next" will display. |
iv | Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it. | A genre is chosen in the beginning that a certain function. When this runs, it calls this other procedure that has a list for its parameter along with the starting index. While the procedure is running, taking the chosen genre list and shuffling it creates a new list (More WishLIST). Once the chosen list has been shuffled, the procedure will display the first question in the shuffled list. This allows the user to interact with the prompt. Once a button is clicked to go to the next question, The procedure runs again although this time with a different index. This chosen index will choose the next question for the user. The way that this index is changed is shown in the next part more. |

Part D:
Sub-Part | Question | Answer | 
--- | -------- | --------- |
i | Describes two calls to the procedure identified in written response3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. | ![image](https://cdn.discordapp.com/attachments/749509501773807677/945741908720894042/Screen_Shot_2022-02-22_at_12.52.12_AM.png) |
ii |  Describes what condition(s) is being tested by each call to the procedure | Condition #1: One of the options have to be selected and it the option has to be the right answer(add to wishlist); 
Condition #2: One of the options have to be selected and the answer cannot be "yes"|
ii | Identifies the result of each call | Result #1: If the conditions are met, the question/book will be added to the wishlist. The index of the questions will be added by 1 ; 
Result #2 Just the index of the questions will be added by 1.|


Final Idea: Site that gives Coding questions, with rewards and surprises for each correct answer (Level System).

Our project is dedicated to the learning, improvement, and utmost enjoyment of coding! We aspire to help beginners improve their coding ability by implementing a series of levels that increase difficulty as they complete the tasks. By the end, they should see themselves as better programmers than before while also having enjoyed the journey. We are Team Siuuuu and are sponsored by Hackclub, a group of coders hoping to teach beginner coders.

[Replit](https://replit.com/@RitvikKeerthi/Data-Structures-Project#index.html)

Code for Level 1
Code Snippets for Key Learnings:

How Questions are Created (hoping to shift to a const of questions in the future): image

Response to User Input: image

Key Features that are in Progress: Scoring system to reward players if answer is correct Key Features that are in Progress: Link to replit for harder levels if code is > 1 line (so that we don't run into errors with the .value call)



