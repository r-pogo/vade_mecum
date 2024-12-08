## Test Planning
### Purpose and Content of Test Plan
A test plan outlines the objectives, resources, and processes for a test project, serving as a key tool for organization and communication.  
Purpose of a Test Plan:  
- Defines the schedule and means to achieve test objectives.  
- Ensures testing aligns with established criteria, policies, and strategies (or explains deviations).  
- Facilitates communication among team members and stakeholders.  
- Helps address future challenges related to risks, schedules, resources, tools, and costs.  

Typical Content of a Test Plan:  
1. Context: Scope, objectives, constraints, and test basis.  
2. Assumptions & Constraints: Factors impacting the project.  
3. Stakeholders: Roles, responsibilities, and training needs.  
4. Communication: Methods, frequency, and documentation templates.  
5. Risk Register: Product and project risks.  
6. Test Approach: Test levels, types, techniques, deliverables, entry/exit criteria, metrics, data, environment needs, and policy deviations.  
7. Budget & Schedule: Resources and timelines.  
The test plan process fosters strategic thinking about the effort needed to achieve testing goals. For more details, refer to the ISO/IEC/IEEE 29119-3 standard.

### Tester's Contribution to Iteration and Release Planning (K1)
In iterative software development, testers contribute to two main planning activities:  

1. Release Planning: Focuses on the product release and the overall backlog. Testers:  
- Write testable user stories and acceptance criteria.  
- Participate in project and quality risk analyses.  
- Estimate test effort for user stories.  
- Define the test approach and plan testing across iterations.  

2. Iteration Planning: Focuses on the iteration backlog for a single cycle. Testers:  
- Conduct detailed risk analysis of user stories.  
- Assess and ensure the testability of user stories.  
- Break down user stories into specific tasks, including testing tasks.  
- Estimate effort for testing tasks.  
- Refine functional and non-functional test aspects.  

Testers play a critical role in ensuring test coverage, risk management, and test readiness at both planning levels.

### Entry Criteria and Exit Criteria 
`Entry Criteria` define the prerequisites for starting an activity, ensuring it is efficient and manageable.
Should be defined for each test level.  
Failing to meet all entry criteria have various negative impacts on an activity.  
Referred to as the `Definition of Ready` in Agile software development.  
Types to know for exam: 
- Availability of resources (e.g., people, tools, data)  
- Availability of testware (e.g., requirements, test cases, cod eor design documents)  
- Initial quality level of the test object (e.g., passing smoke tests, basics check)  

`Exit Criteria` define what must be achieved to complete an activity.  
May act as entry criteria for a subsequent activity.  
Should be defined for each test level.  
Referred to as the `Definition of Done` in Agile software development.  
Types to know for exam:  
- Measures of thoroughness (specified lvl of coverage have been achieved, certain number of unresolved defects or failed TC)  
- Completion Criteria (All planned TC have been executed, all regression test have been automated, all identified risks have a mitigation)
- Running out of time or budget (provided stakeholders accept the associated risks)  

### Estimation Techniques
`Estimation based on Ratio`:  
- Development to test effort  
- Metric-based
- Requires historical project data
- Involves calculating standard ratios

![img.png](img/img_20.png)

`Extrapolation`:  key word is `average` 
In this metrics-based technique, measurements are made as early as possible in the 
current project to gather the data. Having enough observations, the effort required for the remaining work 
can be approximated by extrapolating this data (usually by applying a mathematical model). This method 
is very suitable in iterative SDLCs. For example, the team may extrapolate the test effort in the 
forthcoming iteration as the averaged effort from the last three iterations. 

![img_1.png](img/img_21.png)

`Wideband Delphi`:  
`Planning poker` is a variant of this.
Estimations are based upon the experts past experience:

![img_2.png](img/img_22.png)

The estimation is shared between the experts and each explains why the number.
Once the discussion is finished the experts estimate independently again, and discuss again.  
This process is repeated until the consensus is reached.  

`Three-point estimation`:
In this expert-based technique, three estimations are made by the experts: the 
most optimistic estimation (a), the most likely estimation (m) and the most pessimistic estimation (b). The 
final estimate (E) is their weighted arithmetic mean.  

![img_3.png](img/img_23.png)

Formula:
![img_4.png](img/img_24.png)

![img_5.png](img/img_25.png)

![img_6.png](img/img_26.png)
### Test Case Prioritization
Once test cases and procedures are defined and grouped into test suites, they can be organized in an execution schedule.  
The order of execution can be prioritized using various strategies:  
1. `Risk-Based Prioritization`: Test cases addressing the highest risks (based on risk analysis) are executed first.  
2. `Coverage-Based Prioritization`: Test cases that achieve the highest coverage (e.g., statement coverage) are executed first. In additional coverage prioritization, test cases are executed in the order that maximizes additional coverage, takes also in consideration overlaps between TC.  
3. `Requirements-Based Prioritization`: Test cases related to the most important requirements (as defined by stakeholders) are executed first. Highest to the lowest priority. Dependencies can override priority order.

Test cases should ideally be executed in order of priority, but dependencies between test cases or features may require adjustments.  
Additionally, resource availability (tools, environments, personnel) must be considered when determining the execution schedule.

### Test Pyramid