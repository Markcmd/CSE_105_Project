# ProjectCSE105W24: Project

**Due**: February 22 at 5pm (no penalty late submission until 8am next day)

The CSE 105 project is designed for you to go deeper and extend your work on assignments and to explore an application of your choosing. The project is an individual assignment and has two tasks:

- **Task 1**: Implementing the construction that converts NFA to DFA, and
- **Task 2**: Illustrating the theorem that every regular language is decidable

## What resources can you use?

This project must be completed individually, without any help from other people, including the course staff (other than logistics support if you get stuck with screencast). You can use any of this quarter's CSE 105 offering (notes, readings, class videos, homework feedback). Tools for drawing state diagrams (like Flap.js and JFLAP) can be used to help draw the diagrams in the project too. These resources should be more than enough. If you are struggling to get started and want to look elsewhere online, you must acknowledge this by listing and citing any resources you consult (even if you do not explicitly quote them), including any large-language model style resources. Link directly to them and include the name of the author / video creator, any search strings or prompts you used, and the reason you consulted this reference.

The work you submit for the project needs to be your own. Again, you shouldn't need to look anywhere other than this quarter's material and doing so may result in definitions or notations that conflict with our norms in this class so think carefully before you go down this path.

If you get stuck on any part of the project, we encourage you to focus on communicating what you think the question might mean, including bringing an example from class or homework you think might be relevant, and include any submission any aspect where you're unsure. Clear communication about these theoretical ideas and their applications is one of the main goals of the project.

**Submitting the project**: You will submit a PDF plus a video file for the first task and a PDF for the second task. All file submissions will be in Gradescope.

## Task 1: Implementing a construction

Nondeterminism is a useful theoretical concept because it can make designs simpler and more modular. However, our actual devices are deterministic. In this part of the project, you'll choose a language that can be represented using nondeterminism in some interesting way, then illustrate the construction that converts NFA to DFA for this example.

Specifically:

1. Choose an alphabet $\Sigma$ for this entire first task of the project.
2. Write a program in Java, Python, JavaScript, C++, or another programming language of your choosing that takes as input a representation of an NFA over this alphabet and outputs a representation of a DFA over this alphabet that recognizes the same language. You get to choose the way NFA and DFA are represented, so long as it is general enough to represent any NFA and any DFA over this alphabet. For simplicity: you can restrict your attention to NFA **without spontaneous moves** (in other words, where the transition function has domain $Q \times \Sigma$ when $Q$ is the set of states of the NFA). Informally, this means that the nondeterminism is coming from there being zero, one, or more arrows coming out of each state for each character in the alphabet and there are no arrows with $\varepsilon$ labels.

    If you would like, you may use aids such as co-pilot or ChatGPT to help you write this program. However, you should test the code that is produced and be able to explain what it is doing. As a header in your code file, include a comment block describing any resources that were used to help generate your code.

    Whenever your program is run, it should display a representation of the input NFA and of the output DFA of the run.

3. To demonstrate your program, design a NFA over $\Sigma$ with three states and with no spontaneous moves where the language of the NFA is neither $\emptyset$ nor $\Sigma^*$ and draw its state diagram. Your NFA should use nondeterminism in some way. In other words, the state diagram you draw can't already be the state diagram of a DFA. Run your program with the NFA you just designed to output a representation of an equivalent DFA and demonstrate its design and the test case on video.

### Checklist for submission

For this task, you will submit a PDF plus a video file.

The PDF should include:

- Clear specification of alphabet and state diagram of chosen three-state NFA.
- Documentation for program converting NFA to DFA: include
