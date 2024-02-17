Nondeterminism is a useful theoretical concept because it can make designs simpler and more modular. However, our actual devices are deterministic. In this part of the project, you'll choose a language that can be represented using nondeterminism in some interesting way, then illustrate the construction that converts NFA to DFA for this example.

Specifically:

1. Choose an alphabet $\Sigma$ for this entire first task of the project.

    

2. Write a program in Java, Python, JavaScript, C++, or another programming language of your choosing that takes as input a representation of an NFA over this alphabet and outputs a representation of a DFA over this alphabet that recognizes the same language. You get to choose the way NFA and DFA are represented, so long as it is general enough to represent any NFA and any DFA over this alphabet. For simplicity: you can restrict your attention to NFA **without spontaneous moves** (in other words, where the transition function has domain $Q \times \Sigma$ when $Q$ is the set of states of the NFA). Informally, this means that the nondeterminism is coming from there being zero, one, or more arrows coming out of each state for each character in the alphabet and there are no arrows with $\varepsilon$ labels.


    If you would like, you may use aids such as co-pilot or ChatGPT to help you write this program. However, you should test the code that is produced and be able to explain what it is doing. As a header in your code file, include a comment block describing any resources that were used to help generate your code.

    Whenever your program is run, it should display a representation of the input NFA and of the output DFA of the run.

4. To demonstrate your program, design a NFA over $\Sigma$ with three states and with no spontaneous moves where the language of the NFA is neither $\emptyset$ nor $\Sigma^*$ and draw its state diagram. Your NFA should use nondeterminism in some way. In other words, the state diagram you draw can't already be the state diagram of a DFA. Run your program with the NFA you just designed to output a representation of an equivalent DFA and demonstrate its design and the test case on video.

### Checklist for submission

For this task, you will submit a PDF plus a video file.

The PDF should include:

- Clear specification of alphabet and state diagram of chosen three-state NFA.
- Documentation for program converting NFA to DFA: include a description of how NFA and DFA are represented in the program and give instructions for running it.
- Printout of code for program converting NFA to DFA.
- Screen shots of demonstration of running your program on your chosen NFA, including the representation of the output DFA.
- Solution is typed or clearly hand-drawn with precise language and notation for all terms.

Presenting your reasoning and demonstrating it via screenshare are important skills that also show us a lot of your learning. Getting practice with this style of presentation is a good thing for you to learn in general and a rich way for us to assess your skills. To demonstrate your work, you will create a 3-5 minute screencast video with the following components:

- Start with your face and your student ID for a few seconds at the beginning, and introduce yourself audibly while on screen. You don't have to be on camera for the rest of the video, though it's fine if you are. We are looking for a brief confirmation that it's you creating the video and doing the work you submitted.
- Present the NFA you will be working with. Your video should include a clear and precise explanation of why the language of this NFA is not empty and also not the set of all strings over $\Sigma$.
- Show on the screen and explain the code for your program, including the software design choices you made (e.g. which data structures are you using, etc.) and any resources you used. The video should clearly describe which programming language was chosen for the implementation and gives the reasons why.
- Show on the screen and explain the representation of the NFA that you will input to the program.
- Demonstrate running your code on your example input. The video should include screencasts of running the code live. Explain why the output of your program is what you would expect, by connecting the output of the program to a DFA and discussing which strings are accepted / rejected by this DFA.
- Logistics: video needs to load correctly, be between 3 and 5 minutes, show your face and ID, and you introduce yourself audibly while on screen.

**Note**: Clarity and brevity are both important aspects of your video. In previous years, we've seen students speed up their videos to get below the 5 minute upper bound. This is ok so long as it doesn't compromise clarity.


   $\Sigma$:         ${0, 1}$

   Langugage:        Python
   
   Input:            A representation of an NFA
   
   Output:           A representation of a DFA, (Display both representation with diagram)
   
   The way:          May be Ajacency List, Linked List (general)

   Not gonna use simplicity. HA HA ...

   Definitely use ChatGPT. with explanation on head of code file Comment block.

   Video:            Run your program.

       - 


   



