# Podstawy Testowania
ISO/ICE/IEE 29119-1: info about software testing concepts  
ISO/ICE/IEE 29119-2: info about test processes
## What is testing
Software testing is a comprehensive set of activities aimed at identifying defects and assessing the quality of software artifacts. These artifacts, during the testing process, are referred to as 'test objects'.  
Testing is not limited to the execution of test cases; it also encompasses other activities aligned with the Software Development Life Cycle (SDLC).  

There are two main aspects of testing:

`Verification`: This process checks whether the system has been built correctly and adheres to specified requirements. In other words, it answers the question: Is the product being developed as expected?  
`Validation`: This step ensures that the system meets the actual needs of users and other stakeholders in its intended operational environment. It addresses the question: Is the right product being built?  

Testing is not solely a technical endeavor; it also requires proper planning, management, estimation, monitoring, and control to be effective.  
Furthermore, testing is predominantly an intellectual activity, requiring testers to possess specialized knowledge, apply analytical skills, and engage in critical and systems thinking.  

In essence, software testing provides valuable insights into the quality of the product being tested.

Testing can take two forms:  

`Dynamic testing`, where the system or module is executed to assess its behavior.  
`Static testing`, which involves reviewing documentation and code without execution.

### Cele testowania K1 (Identify typical test objectives)
The typical test objectives are:  
• Evaluating work products such as requirements, user stories, designs, and code  
• Triggering failures and finding defects  
• Ensuring required coverage of a test object  
• Reducing the level of risk of inadequate software quality  
• Verifying whether specified requirements have been fulfilled  
• Verifying that a test object complies with contractual, legal, and regulatory requirements  
• Providing information to stakeholders to allow them to make informed decisions  
• Building confidence in the quality of the test object  
• Validating whether the test object is complete and works as expected by the stakeholders  

### Testing and Debugging
`Testowanie (ujawnia awarię)`: triggers failures that are caused by defects in
the software (dynamic testing) or can directly find defects in the test object (static testing). 

`Debugowanie (szuka przyczyny)`: debugging is concerned with finding causes of
this failure (defects), analyzing these causes, and eliminating them.

Debugging process:
- Reproducing failure
- Diagnosis (finding root cause)
- Fixing the cause

Static testing identifies a defect, debugging here is concerned with removing it.
Static testing directly finds defects, and cannot cause failures.
___
### Why is Testing Necessary?

Testing provides a cost-effective means of detecting defects. These defects can then be removed (by
debugging – a non-testing activity), so testing indirectly contributes to higher quality test objects.

Testing provides a means of directly evaluating the quality of a test object at various stages in the SDLC.

Testers ensure that their understanding of users’ needs are considered throughout the development lifecycle.

Testing may also be required to meet contractual or legal requirements, or to comply with regulatory
standards

### QM/QA/TQC/testing K1 (Recall the relation between testing and quality assurance)
`Quality assurance` (zapewnianie jakości) jest często utożsamiane z testowaniem.
Są to dwa oddzielne procesy, które zawierają się w szerszym pojęciu `Quality management` (zarządzanie jakościa).  
`QM` obejmuje wszystkie czynności mające na celu kierowanie organizacji w dziedzinie  
jakości i ich nadzorowanie.

![img.png](img/img.png)

Testing is a form of quality control.

![img_1.png](img/img_1.png)

`QC`: `product-oriented`, corrective approach that focuses on those activities supporting the achievement 
of appropriate levels of quality. QC results are used to fix defects.

`QA`: `process-oriented`, preventive approach that focuses on the implementation and improvement of 
processes. It works on the basis that if a good process is followed correctly, then it will generate a good 
product. QA results provide feedback on how well the development and test processes are performing.

### Errors, Defects, Failures, Root Causes
- `Pomyłka/Error (błąd)`: działanie człowieka powodujące powstanie nieprawidłowego rezultatu (programista zle NAPISAŁ funkcje, w której pomylił znak + z *)
- `Defekt/Defect (bug, usterka)`: niedoskonałość, wada produktu pracy, polegająca na niespełnianiu wymagań (bug w kodzie czyli * zamiast +)
- `Awaria/Failure`: zdarzenie, w którym moduł/system nie wykonuje wymaganej funkcji w określonym zakresie. (kiedy użytkownik chce dodać to produk mnoży i bęc jest awaria)
- `Podstawowa przyczyna defektu/Root Cause`: fundamental reason for the occurrence of a problem

Errors and defects are not the only cause of failures. Failures can also be caused by environmental 
conditions, such as when radiation or electromagnetic field cause defects in firmware.

![img_2.png](img/img_2.png)

### Wyniki fałszywie pozytywne/negatywne

- `Fałszywie pozytywny`: raportowany jako defekt którego właściwie nie ma
- `Fałszywie negatywny`: nie wykrywają defektu który powinien zostać wykryty

Dlatego kluczowa jest analiza podstawowej przyczyny defektu.

### 7 testing principles
1. Testing shows the presence, not the absence of defects.
2. Exhaustive testing is impossible.
3. Early testing saves time and money.
4. Defects cluster together.
5. Paradoks pestycydów/Tests wear out.
6. Testing is context dependent. 
7. Przekonanie o braku błędów jest błędem/Absence-of-defects fallacy.

![img_3.png](img/img_3.png)
___
### Test Activities, Testware and Test Roles
Testing is highly context-dependent, influenced by various factors that shape testing decisions.  

`External factors` include stakeholder interests, relevant laws, the domain you're working in, and the standards that apply to that domain.

`Internal factors` involve aspects like the software development lifecycle model in use, available budgets, resources, time constraints, and the system's overall complexity, all of which impact your testing process.

`Testware` refers to the output produced from test activities, such as test plans, scripts, and data.

Testing activities can be broadly categorized into test planning, monitoring and control, analysis, design, implementation, execution, and completion. While these activities may seem to follow a logical sequence, they don't have to be strictly linear. In practice, especially in agile or agile-like environments, you might perform test planning, analysis, design, and execution in smaller, iterative cycles. This approach allows you to plan, analyze, test, and report in short, repeated steps, adjusting based on ongoing results. The overall workflow dynamics depend on how the team works together, requiring flexibility and adaptation.

`Test Planning` involves defining clear test objectives and selecting an approach that effectively meets those objectives, considering the constraints and context surrounding the project. It’s important to note that a test plan is not rigid—it can evolve as the project progresses.

`Test planning work products` include the test plan, test schedule, risk register, and entry/exit criteria. The **risk register** is a document that outlines potential risks, their likelihood and impact, and strategies for mitigating each risk.

`Test Monitoring and Control` involves continuously tracking all test activities and comparing actual progress against the plan. The key questions are: Are we doing what we planned to do? If not, why? Are we on track to meet deadlines, and if not, what can be done to get back on track? Test control focuses on taking the necessary actions to ensure the testing objectives are met.

To effectively monitor and control testing, it is essential to maintain traceability throughout the process, linking test basis elements (such as requirements or design documents) with testware (like test cases, conditions, and risks), test results, and detected defects. This traceability ensures that testing is aligned with the project’s goals and supports the evaluation of coverage.

**Coverage evaluation** is more effective when measurable coverage criteria are defined in the test basis. These criteria can serve as key performance indicators, helping track progress towards test objectives. For example:
- **Traceability of test cases to requirements** ensures that all requirements are covered by test cases.
- **Traceability of test results to risks** allows assessment of residual risks in the test object.

In addition to evaluating coverage, good traceability helps determine the impact of changes, facilitates audits, and ensures compliance with IT governance standards. It also makes test progress and completion reports clearer by including the status of test basis elements, which aids in communicating technical aspects to stakeholders in an understandable way. Traceability provides valuable insights into product quality, process efficiency, and progress toward business objectives.

**Test monitoring and control work products** include test progress reports, control directives, and risk documentation. These reports provide visibility into the status of testing activities—such as who is working on what tasks—and help in making informed decisions throughout the testing process.

`Test Analysis (What to Test?)`: Test analysis involves examining the test basis to identify which features are testable and defining the associated test conditions. It also includes prioritizing these conditions, evaluating related risks, and determining their risk levels. During this process, the test basis and test objects are assessed for defects and testability. Test analysis is often supported by various test techniques and aims to answer the question **“What to test?”** through measurable coverage criteria.

The better you understand the system, the more effective your tests—and overall work—will be. But what exactly should you analyze? Start with key documents like business requirements, functional and non-functional requirements. Architectural diagrams, UML diagrams, and any technical documentation created by the system’s designers are essential as well. Additional resources such as the actual code, metadata, and system interface documentation can provide valuable insights. If available, include risk analysis reports in your test basis too.

Essentially, anything that can inform your understanding of the system is fair game for analysis. But what does "analyzing" really mean? It’s more than just reading through documents. You need to critically examine them to identify potential defects—such as ambiguities, omissions, inconsistencies, inaccuracies, contradictions, or unnecessary statements. These defects in the documentation can easily translate into software defects and, ultimately, system failures. This is why early testing is emphasized in the testing principles—it helps save both time and money.

`Test Analysis Work Products Include`: Prioritized test conditions (e.g., acceptance criteria) and defect reports related to issues found in the test basis (if not directly fixed).

**So, what exactly are test conditions?** In simple terms, they are the testable aspects of a component or system, identified during analysis. You can break down requirements into logical components, map those components to test conditions with clear, limited scope, and use these conditions to design individual test cases.


Here’s a refined version of your text that is more concise, clearer, and flows better:

`Test Design and Implementation`: After thoroughly analyzing what to test, the next step is to determine **how to test it**. Test design involves several key activities: designing and prioritizing test cases and test sets, identifying the required test data to support test conditions and cases, preparing or evaluating the test environment, determining necessary infrastructure and tools, and establishing bi-directional traceability between the test basis, test conditions, and test cases.

In the design process, you create multiple test cases, documenting the steps, expected results, and required input data for each. These test cases are then typically grouped into test sets, test suites, or test packs—terms that are often used interchangeably. Additionally, you document all the resources needed for testing, including testing tools, test conditions, and the test environment (such as browser versions, operating systems, and specific software).

Next, all of this information is mapped to the corresponding requirements. Since requirements can be large and complex, this often results in hundreds of test cases grouped into multiple test sets, each mapping to different subsections of the overall requirements. In this case, you might create intermediate test conditions that correspond to specific sections of the requirements.

Regardless of the approach, it's crucial to establish requirements-to-test mapping, also known as traceability. This ensures that there’s a clear link between the requirements, the test basis, and the test work products, such as the test cases. In summary, test design answers the question, **how to test.**

`Test Design (How to Test)`: involves transforming test conditions into detailed test cases and other testware, such as test charters. This process often includes identifying coverage items, which help specify the necessary test case inputs.

Test design also encompasses defining the required test data, designing the test environment, and identifying any other necessary infrastructure and tools to support the testing process.

The main activities in test design include:

- Designing and prioritizing test cases and test case sets.  
- Identifying the test data needed to support test conditions and cases.  
- Designing, preparing, and evaluating the test environment.  
- Identifying any required infrastructure or tools.  

Additionally, test design involves ensuring bi-directional traceability between the test basis, test conditions, and test cases.  
`Test design work products` include prioritized test cases, test charters, coverage items, test data requirements, and test environment requirements.

![img.png](img/img_4.png)

`Test Implementation (Do we have everything in place to run the tests?)`: involves creating or acquiring the necessary testware to execute the tests, such as test data. Test cases are organized into test procedures and often grouped into test suites. Both manual and automated test scripts are developed. Test procedures are prioritized and arranged within a test execution schedule to ensure efficient execution. The test environment is set up and verified to be properly configured.

Key activities in test implementation include:

- Developing test procedures and, if needed, creating automated test scripts.  
- Setting up the test environment, which may involve tools like test harnesses, service virtualization, simulators, and other infrastructure.  
- Preparing the required test data and ensuring it is correctly loaded into the test environment (as identified in the earlier design phase).  
- Verifying and maintaining bi-directional traceability between the test basis, test conditions, test cases, and other related elements.  

`Test implementation work products`: include test procedures, automated test scripts, test suites, test data, test execution schedules, and test environment components. Examples of test environment components include stubs, drivers, simulators, and service virtualizations.

`Test Execution`: involves running tests according to the test execution schedule (test runs). Test execution can be performed manually or through automation and may take various forms, such as continuous testing or pair testing sessions. During execution, actual test results are compared to expected outcomes. Test results are logged, and any anomalies are analyzed to determine their likely causes. This analysis helps in reporting the anomalies based on the observed failures.

`Test execution work products`: include test logs and defect reports.

`Test Completion` activities typically occur at project milestones (e.g., release, end of iteration, or test level completion) and focus on addressing unresolved defects, change requests, or product backlog items. Testware that may be useful in the future is identified, archived, or handed over to the appropriate teams. The test environment is returned to an agreed state, and test activities are reviewed to identify lessons learned and areas for improvement in future iterations, releases, or projects. A test completion report is then created and communicated to stakeholders.

This phase usually occurs when a major software version is released, a test project is completed, or an agile iteration concludes. In essence, it serves as a retrospective at the end of a milestone. Test completion includes ensuring that all defect reports are closed—this is crucial to verify that no issues were overlooked—creating a test summary report for stakeholders, finalizing and archiving testware (such as test cases, test data, and other resources), and ensuring the necessary storage of test evidence for regulatory compliance, which may be required for audits.

Additionally, the completion phase involves analyzing lessons learned from the completed testing activities to identify improvements for future work, helping to refine processes and avoid past mistakes.

`Test completion work products` include the test completion report, action items for improvement in subsequent projects or iterations, documented lessons learned, and change requests (such as product backlog items).


![img_1.png](img/img_5.png)

![img_2.png](img/img_6.png)


Testing is not performed in isolation. Test activities are an integral part of the development processes 
carried out within an organization. Testing is also funded by stakeholders and its final goal is to help fulfill 
the stakeholders’ business needs. Therefore, the way the testing is carried out will depend on a number 
of contextual factors including: 
• Stakeholders (needs, expectations, requirements, willingness to cooperate, etc.) 
• Team members (skills, knowledge, level of experience, availability, training needs, etc.) 
• Business domain (criticality of the test object, identified risks, market needs, specific legal 
regulations, etc.) 
• Technical factors (type of software, product architecture, technology used, etc.) 
• Project constraints (scope, time, budget, resources, etc.) 
• Organizational factors (organizational structure, existing policies, practices used, etc.) 
• Software development lifecycle (engineering practices, development methods, etc.) 
• Tools (availability, usability, compliance, etc.) 
These factors will have an impact on many test-related issues, including: test strategy, test techniques 
used, degree of test automation, required level of coverage, level of detail of test documentation, 
reporting, etc.

### Role in testing
`test management`: takes overall responsibility for the test process, test team and leadership of the 
test activities. The test management role is mainly focused on the activities of test planning, test 
monitoring and control and test completion

`testing role`: takes overall responsibility for the engineering (technical) aspect of testing. The testing 
role is mainly focused on the activities of test analysis, test design, test implementation and test 
execution.

## Essential Skills and Good Practices in Testing

 - Testing knowledge (to increase effectiveness of testing, e.g., by using test techniques) 
 - Thoroughness, carefulness, curiosity, attention to details, being methodical (to identify defects, 
especially the ones that are difficult to find) 
 - Good communication skills, active listening, being a team player (to interact effectively with all 
stakeholders, to convey information to others, to be understood, and to report and discuss 
defects) 
 - Analytical thinking, critical thinking, creativity (to increase effectiveness of testing) 
 - Technical knowledge (to increase efficiency of testing, e.g., by using appropriate test tools) 
 - Domain knowledge (to be able to understand and to communicate with end users/business 
representatives)

## Whole Team Approach K1 (Recall the advantage of the whole team approach)

The "whole-team approach" in testing, rooted in Extreme Programming, emphasizes 
collaboration where all team members share responsibility for quality.  
In this model, any team member with the required skills can handle any task,  
creating a cohesive and dynamic environment. Co-location (physical or virtual) supports effective  
communication, and the diverse skills within the team are utilized to enhance project outcomes.  
Testers collaborate closely with business representatives and developers to establish acceptance tests,  
test strategy, and automation. However, in specific contexts like safety-critical projects, a high 
degree of test independence may be required, limiting the use of the whole-team approach.

## Independence of Testing
Independence in testing can enhance effectiveness by reducing cognitive biases  
between the author and tester, though it doesn't replace the need for familiarity with the product. 

Work products can be tested by their author (no independence), by the author's peers from the same 
team (some independence), by testers from outside the author's team but within the organization (high 
independence), or by testers from outside the organization (very high independence).
A mixed approach is often ideal, where developers, test teams, and business representatives handle different testing stages.

The main benefit of independence of testing is that independent testers are likely to recognize different 
kinds of failures and defects compared to developers because of their different backgrounds, technical 
perspectives, and biases. Moreover, an independent tester can verify, challenge, or disprove 
assumptions made by stakeholders during specification and implementation of the system. 

However, drawbacks include potential isolation from developers, communication issues,  
strained team dynamics, and the risk of developers disengaging from quality ownership,  
with independent testers possibly being blamed for delays.
___
## Sources
- A. Doronins, ISTQB® Foundation: Getting Started, https://app.pluralsight.com/
- A. Roman, L. Stapp, Certifikowany tester ISTQB Poziom Podstawowy, Helion SA 2020
- Certified Tester Foundation Level Syllabus v4.0


