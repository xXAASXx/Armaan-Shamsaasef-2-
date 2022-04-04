{% include navigation.html %}

# Create Task

## WishLIST - Paul and Armaan

### Planning
This Create Task Idea will allow the user to add books to a Wishlist by being prompted with different books and choosing which ones they like. By the end, they will have a list of the books they chose.

#### Create Task Requirements:
- [x] Instructions for input: User will be able to select whether or not they would like to add a book to their wishlist. There will be 5 options to choose from that the user will decide on
- [x] Use of at least 1 list: The books that will be prompted will be from a question list. A list will also be created as the user decides on the books that they like.(push-js)
- [x] At least 1 procedure: The procedure will be taking the input from a user and the function will produce a list of books that they wanted to add to their wishlist
- [x] An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure: The function runs through a loop that adds questions to a list and shuffles them. There will be different parts to this and only certain action will occur when  specific conditions are met. Ex: If the user likes the book, the function will add it to a list.
- [x] Calls to your student-developed procedure: the "next" button will switch to different question and allow the user to decide on the next book they want to add
- [x] Instructions for output (tactile, audible, visual, or textual) based on input program functionality: The output will be a textual list of books that the user created

##### Answers to Written Response
#### [Armaan Video](https://youtu.be/gamMwwdtFfI) - Done on the local.

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


#### B Sub-part iii-v
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
#### C Sub-part iii & iv
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
