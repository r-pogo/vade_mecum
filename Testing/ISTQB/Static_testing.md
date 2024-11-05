# Static Testing 
ISO/IEC 20246 standard defines a generic review process.

In static testing the software tested doesn't need to be executed, is a "manual" examination like reading (```reviews```)
or performed with a help of a tool like a linter for code or spellchecker (```static analysis```), 
in static testing the software under test does not need to be executed. 

Test objectives are same as in "normal" testing.

Can be applied for both verification and validation.
E.g:
1. Review techniques can be applied  to ensure user stories are complete and understandable and include  
testable acceptance criteria. By asking the right questions, testers explore, challenge and help improve  
the proposed user stories.
2. Static analysis is often incorporated into CI frameworks. While largely used to  
detect specific code defects, static analysis is also used to evaluate maintainability and security.  
Spelling checkers and readability tools are other examples of static analysis tools.  
___
## Work Products Examinable by Static Testing (K1)
Almost any work product can be examined using static testing. Examples include requirement 
specification documents, source code, test plans, test cases, product backlog items, test charters, project 
documentation, contracts and models. 
Any work product that can be read and understood can be the subject of a review. However, for static 
analysis, work products need a structure against which they can be checked (e.g., models, code or text 
with a formal syntax).  
Work products that are not appropriate for static testing include those that are difficult to interpret by 
human beings and that should not be analyzed by tools (e.g., 3rd party executable code due to legal 
reasons). 
___
## Value of Static Testing 
1. Static testing can detect defects in the earliest phases of the SDLC, fulfilling the principle of ```early testing``` 
2. It can  identify ```defects which cannot be detected by dynamic testing``` (e.g., 
unreachable code, design patterns not implemented as desired, defects in non-executable work 
products).  
3. Static testing provides the ability to evaluate the quality of, and to build confidence in work products. By 
verifying the documented requirements, the stakeholders can also make sure that these requirements 
describe their ```actual needs```. Since static testing can be performed early in the SDLC, a shared 
understanding can be created among the involved stakeholders. Communication will also be improved 
between the involved stakeholders. For this reason, it is recommended to involve a wide variety of 
stakeholders in static testing.  

Even though reviews can be costly to implement, the overall project costs are usually much lower than 
when no reviews are performed because less time and effort needs to be spent on fixing defects later in 
the project. 
___
## Differences between Static Testing and Dynamic Testing 
Static testing and dynamic testing practices complement each other. They have similar objectives, such 
as supporting the detection of defects in work products, but there are also some 
differences, such as: 
• Static and dynamic testing (with analysis of failures) can both lead to the detection of defects, 
however there are ```some defect types that can only be found by either static or dynamic testing```.  
• ```Static testing finds defects directly```, while dynamic testing causes failures from which the 
associated defects are determined through subsequent analysis 
• Static testing may more easily detect defects that lay on ```paths through the code that are rarely 
executed or hard to reach``` using dynamic testing 
• Static testing can be applied to ```non-executable work products```, while dynamic testing can only be 
applied to executable work products 
• Static testing can be used to measure quality characteristics that are not dependent on executing 
code (e.g., ```maintainability```), while dynamic testing can be used to measure quality characteristics  
that are dependent on executing code (e.g., performance efficiency) 
Typical defects that are easier and/or cheaper to find through static testing include: 
• Defects in requirements (e.g., inconsistencies, ambiguities, contradictions, omissions, 
inaccuracies, duplications) 
• Design defects (e.g., inefficient database structures, poor modularization) 
• Certain types of coding defects (e.g., variables with undefined values, undeclared variables, 
unreachable or duplicated code, excessive code complexity) 
• Deviations from standards (e.g., lack of adherence to naming conventions in coding standards) 
• Incorrect interface specifications (e.g., mismatched number, type or order of parameters) 
• Specific types of security vulnerabilities (e.g., buffer overflows) 
• Gaps or inaccuracies in test basis coverage (e.g., missing tests for an acceptance criterion)

## Benefits of Early and Frequent Stakeholder Feedback (K1)
```VALIDATION!```

Early and frequent feedback allows for the early communication of potential quality problems. If there is 
little stakeholder involvement during the SDLC, the product being developed might not meet the 
stakeholder’s original or current vision. A failure to deliver what the stakeholder wants can result in costly 
rework, missed deadlines, blame games, and might even lead to complete project failure.  
```Frequent stakeholder feedback throughout the SDLC can prevent misunderstandings about requirements```
```and ensure that changes to requirements are understood and implemented earlier```. This helps the 
development team to improve their understanding of what they are building. It allows them to focus on 
those features that deliver the most value to the stakeholders and that have the most positive impact on 
identified risks. 

## Review Process Activities 
The ISO/IEC 20246 standard defines a generic review process that provides a structured but flexible 
framework from which a specific review process may be tailored to a particular situation. 

The activities in the review process are: 
• ```Planning.``` During the planning phase, the scope of the review, which comprises the purpose, the 
work product to be reviewed, quality characteristics to be evaluated, areas to focus on, exit 
criteria, supporting information such as standards, effort and the timeframes for the review, shall 
be defined. 
• ```Review initiation.``` During review initiation, the goal is to make sure that everyone and everything 
involved is prepared to start the review. This includes making sure that every participant has 
access to the work product under review, understands their role and responsibilities and receives 
everything needed to perform the review. 
• ```Individual review.``` Every reviewer performs an individual review to assess the quality of the work 
product under review, and to identify anomalies, recommendations, and questions by applying 
one or more review techniques (e.g., checklist-based reviewing, scenario-based reviewing). The 
ISO/IEC 20246 standard provides more depth on different review techniques. The reviewers log 
all their identified anomalies, recommendations, and questions.  
• ```Communication and analysis.``` Since the anomalies identified during a review are not 
necessarily defects, all these anomalies need to be analyzed and discussed. For every anomaly, 
the decision should be made on its status, ownership and required actions. This is typically done 
in a review meeting, during which the participants also decide what the quality level of reviewed 
work product is and what follow-up actions are required. A follow-up review may be required to 
complete actions.  
• ```Fixing and reporting.``` For every defect, a defect report should be created so that corrective 
actions can be followed-up. Once the exit criteria are reached, the work product can be accepted. 
The review results are reported. 

## Roles and Responsibilities in Reviews  (K1)
• ```Manager``` – decides what is to be reviewed and provides resources, such as staff and time for the 
review 
• ```Author``` – creates and fixes the work product under review
• ```Moderator (also known as the facilitator)``` – ensures the effective running of review meetings, 
including mediation, time management, and a safe review environment in which everyone can 
speak freely 
• ```Scribe (also known as recorder)``` – collates anomalies from reviewers and records review 
information, such as decisions and new anomalies found during the review meeting 
• ```Reviewer``` – performs reviews. A reviewer may be someone working on the project, a subject 
matter expert, or any other stakeholder 
• ```Review leader``` – takes overall responsibility for the review such as deciding who will be involved, 
and organizing when and where the review will take place 
Other, more detailed roles are possible, as described in the ISO/IEC 20246 standard. 

## Review Types 
Some commonly used review types are: 
• ```Informal review```. Informal reviews do not follow a defined process and do not require a formal 
documented output. The main objective is detecting anomalies. 
• ```Walkthrough```. A walkthrough, which is led by the author, can serve many objectives, such as 
evaluating quality and building confidence in the work product, educating reviewers, gaining 
consensus, generating new ideas, motivating and enabling authors to improve and detecting 
anomalies. Reviewers might perform an individual review before the walkthrough, but this is not 
required. 
• ```Technical Review```. A technical review is performed by technically qualified reviewers and led by 
a moderator. The objectives of a technical review are to gain consensus and make decisions 
regarding a technical problem, but also to detect anomalies, evaluate quality and build confidence 
in the work product, generate new ideas, and to motivate and enable authors to improve. 
• ```Inspection```. As inspections are the most formal type of review, they follow the complete generic 
process. The main objective is to find the maximum number of anomalies. 
Other objectives are to evaluate quality, build confidence in the work product, and to motivate and 
enable authors to improve. Metrics are collected and used to improve the SDLC, including the 
inspection process. In inspections, the author cannot act as the review leader or scribe.

Comparison:

| Review Type | Prep Required | Review Meeting | Author Led | Gather Metrics |
|-------------|---------------|----------------|------------|----------------|
| Informal Review | No | No | Can be | No |
| Walkthrough | No | Yes | Yes | No |
| Technical Review | Yes | Optional | No | Some |
| Inspection | Yes | Yes | No | Yes
___
## Review Techniques
- Ad-Hoc
- Checklist-based
- Scenarios
- Role-based: Recenzenci oceniają produkt pracy z perspektywy poszczególnych ról interesariuszy, lub określone role w organizacji.
Np.: doświadczony użytkownik, niedoświadczony, starszy, dzieci, administrator, pracownik itp.
- Perspective-based: Różni przeglądający przyjmują podczas przeglądania produktu pracy różne punkty widzenia interesariuszy i przeglądają produkt właśnie pod tym kątem.
Typowe perspektywy: użytkownik, analityk biznesowy, projektant, tester, operator systemu itp.
Różnica pomiędzy tym a role-based jest taka, że w przeglądzie opartym na rolach zmieniają się rodzaje użytkowników, ale zadania do wykonania pozostają te same, 
w perspektywie zmieniają się właśnie perspektywy interesariuszy.
___
## Success Factors for Reviews (K1)
There are several factors that determine the success of reviews, which include: 
• Defining clear objectives and measurable exit criteria. Evaluation of participants should never be 
an objective 
• Choosing the appropriate review type to achieve the given objectives, and to suit the type of work 
product, the review participants, the project needs and context 
• Conducting reviews on small chunks, so that reviewers do not lose concentration during an 
individual review and/or the review meeting (when held)  
• Providing feedback from reviews to stakeholders and authors so they can improve the product 
and their activities
• Providing adequate time to participants to prepare for the review 
• Support from management for the review process 
• Making reviews part of the organization’s culture, to promote learning and process improvement 
• Providing adequate training for all participants so they know how to fulfil their role 
• Facilitating meetings
___
## Sources
- A. Roman, L. Stapp, Certifikowany tester ISTQB Poziom Podstawowy, Helion SA 2020
- Certified Tester Foundation Level Syllabus v4.0