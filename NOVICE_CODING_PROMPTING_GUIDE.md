# The Complete Novice's Guide to Prompting Coding Agents

## Introduction

This guide teaches you how to get the best results from AI coding agents, even if you're a complete beginner. Whether you're using GitHub Copilot, Claude, ChatGPT, or any other AI assistant, these techniques will help you write prompts that get accurate, useful, and actionable results.

**What you'll learn:**
- How to structure effective coding prompts
- What information to include (and what to skip)
- Common mistakes to avoid
- Templates you can copy and adapt
- Real examples showing good vs. bad prompts

---

## Part 1: The Basics

### What Makes a Good Coding Prompt?

A good coding prompt has five essential elements:

1. **Clear Goal:** What you want to achieve
2. **Context:** What code/project you're working with
3. **Specifics:** Details about the problem or requirement
4. **Expected Output:** What format you want the answer in
5. **Constraints:** Any limitations or requirements

### The Basic Template

```
I want to [GOAL].

I'm working with [CONTEXT].

Specifically, I need to [SPECIFIC REQUIREMENT].

Please provide [EXPECTED OUTPUT].

Important constraints: [CONSTRAINTS]
```

### Example: Bad vs. Good

**Bad Prompt:**
```
Fix my code
```

**Why it's bad:** No context, no specific problem, no code provided, unclear what "fix" means.

**Good Prompt:**
```
I want to fix a bug in my Python function.

I'm working with a function that calculates the average of a list of numbers.
Here's the code:

def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

Specifically, I'm getting an error when I pass an empty list.

Please provide:
1. An explanation of why the error occurs
2. The corrected code
3. An explanation of how the fix works

Important constraints: I'm using Python 3.9 and can't use external libraries.
```

**Why it's good:** Clear goal, complete context with code, specific problem, clear output format, relevant constraints.

---

## Part 2: Different Types of Coding Tasks

### 2.1 Finding Bugs

**Template:**
```
I'm experiencing [PROBLEM] in my [LANGUAGE] code.

Here's the relevant code:
[CODE]

What I expect to happen: [EXPECTED BEHAVIOR]
What actually happens: [ACTUAL BEHAVIOR]
Error message (if any): [ERROR]

Please:
1. Identify the bug
2. Explain why it occurs
3. Provide the corrected code
4. Suggest how to prevent this type of bug in the future
```

**Example:**
```
I'm experiencing incorrect calculation results in my JavaScript code.

Here's the relevant code:
function calculateDiscount(price, discount) {
    return price - price * discount / 100;
}

let finalPrice = calculateDiscount(100, 20);
console.log(finalPrice); // Shows 80

What I expect to happen: With a $100 price and 20% discount, I expect $80
What actually happens: I get 80, which seems right, but my tests are failing
Error message (if any): None, but unit test shows expected 80, got 80.00000000000001

Please:
1. Identify the bug
2. Explain why it occurs
3. Provide the corrected code
4. Suggest how to prevent this type of bug in the future
```

### 2.2 Code Review and Quality

**Template:**
```
Please review the following [LANGUAGE] code for [SPECIFIC CONCERNS].

Code:
[CODE]

Analyze for:
- [CONCERN 1, e.g., "performance issues"]
- [CONCERN 2, e.g., "security vulnerabilities"]
- [CONCERN 3, e.g., "best practices violations"]

For each issue found, provide:
1. Location (line number if possible)
2. Description of the issue
3. Why it's a problem
4. How to fix it
5. Priority (High/Medium/Low)
```

**Example:**
```
Please review the following Python code for security issues and best practices.

Code:
def login_user(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    result = db.execute(query)
    if result:
        return True
    return False

Analyze for:
- Security vulnerabilities
- Best practices violations
- Potential errors

For each issue found, provide:
1. Location (line number if possible)
2. Description of the issue
3. Why it's a problem
4. How to fix it
5. Priority (High/Medium/Low)
```

### 2.3 Adding New Features

**Template:**
```
I want to add [FEATURE] to my [LANGUAGE] project.

Current code:
[EXISTING CODE]

The new feature should:
- [REQUIREMENT 1]
- [REQUIREMENT 2]
- [REQUIREMENT 3]

Please provide:
1. The modified code with the feature added
2. Comments explaining the new parts
3. Example usage showing how to use the feature
4. Any potential issues or edge cases to consider

Keep in mind: [CONSTRAINTS like coding standards, performance requirements, etc.]
```

**Example:**
```
I want to add input validation to my JavaScript form handler.

Current code:
function submitForm(formData) {
    const user = {
        email: formData.email,
        age: formData.age
    };
    saveToDatabase(user);
}

The new feature should:
- Validate that email is in correct format
- Validate that age is a number between 13 and 120
- Show user-friendly error messages for invalid input
- Only save to database if all validations pass

Please provide:
1. The modified code with validation added
2. Comments explaining the validation logic
3. Example usage showing valid and invalid inputs
4. Any potential issues or edge cases to consider

Keep in mind: This needs to work in browsers that don't support the latest JavaScript features (IE11 compatible).
```

### 2.4 Performance Optimization

**Template:**
```
I need to optimize the performance of this [LANGUAGE] code.

Current code:
[CODE]

Performance issue: [DESCRIPTION OF SLOWNESS]

Current metrics (if known):
- [e.g., "Takes 5 seconds to process 1000 items"]
- [e.g., "Uses 500MB memory"]

Please:
1. Identify performance bottlenecks
2. Explain why they're slow
3. Provide optimized version of the code
4. Explain what improvements were made
5. Estimate the performance gain

Constraints: [e.g., "Can't use external libraries", "Must maintain the same API"]
```

**Example:**
```
I need to optimize the performance of this Python code.

Current code:
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

Performance issue: Very slow with large lists (10,000+ items)

Current metrics:
- Takes about 30 seconds with 10,000 items
- CPU usage spikes to 100%

Please:
1. Identify performance bottlenecks
2. Explain why they're slow
3. Provide optimized version of the code
4. Explain what improvements were made
5. Estimate the performance gain

Constraints: Must maintain the same function signature and return type
```

### 2.5 Refactoring Code

**Template:**
```
I want to refactor this [LANGUAGE] code to improve [GOAL].

Current code:
[CODE]

Current issues:
- [ISSUE 1, e.g., "Hard to understand"]
- [ISSUE 2, e.g., "Duplicated logic"]
- [ISSUE 3, e.g., "Too complex"]

Please provide:
1. Refactored version of the code
2. Explanation of what changes were made
3. Why the changes improve the code
4. Any trade-offs or considerations

Requirements:
- [e.g., "Must maintain same functionality"]
- [e.g., "Should follow [CODING STANDARD]"]
```

**Example:**
```
I want to refactor this JavaScript code to improve readability and maintainability.

Current code:
function processOrder(o) {
    if (o.items.length > 0) {
        let t = 0;
        for (let i = 0; i < o.items.length; i++) {
            t += o.items[i].price * o.items[i].qty;
        }
        if (o.customer.type === 'premium') {
            t = t * 0.9;
        }
        if (t > 100) {
            t = t - 10;
        }
        o.total = t;
        return true;
    }
    return false;
}

Current issues:
- Variable names are unclear (o, t, i)
- Logic is hard to follow
- Multiple responsibilities in one function

Please provide:
1. Refactored version of the code
2. Explanation of what changes were made
3. Why the changes improve the code
4. Any trade-offs or considerations

Requirements:
- Must maintain same functionality
- Should follow modern JavaScript best practices
- Should be easy for junior developers to understand
```

### 2.6 Understanding Existing Code

**Template:**
```
I need help understanding this [LANGUAGE] code.

Code:
[CODE]

Specifically, I don't understand:
- [QUESTION 1]
- [QUESTION 2]
- [QUESTION 3]

Please explain:
1. What the code does (high-level overview)
2. How it works (step-by-step breakdown)
3. Answer my specific questions
4. Point out any important details I should know

My background: [e.g., "I'm familiar with basic Python but new to async programming"]
```

**Example:**
```
I need help understanding this Python code.

Code:
@decorator
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

Specifically, I don't understand:
- What the @ symbol does
- How the cache persists between calls
- What *args means
- When would I use this

Please explain:
1. What the code does (high-level overview)
2. How it works (step-by-step breakdown)
3. Answer my specific questions
4. Point out any important details I should know

My background: I'm familiar with basic Python functions but new to decorators
```

### 2.7 Writing Tests

**Template:**
```
I need to write tests for this [LANGUAGE] code.

Code to test:
[CODE]

Please provide:
1. Test cases covering normal usage
2. Test cases for edge cases
3. Test cases for error conditions
4. Explanation of what each test verifies

Testing framework: [e.g., "pytest", "Jest", "JUnit"]
Coverage goal: [e.g., "Test all public methods", "Achieve 80% code coverage"]
```

**Example:**
```
I need to write tests for this JavaScript code.

Code to test:
function validateEmail(email) {
    if (!email) return false;
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

Please provide:
1. Test cases covering normal usage
2. Test cases for edge cases
3. Test cases for error conditions
4. Explanation of what each test verifies

Testing framework: Jest
Coverage goal: Test all code paths and edge cases
```

---

## Part 3: Advanced Techniques

### 3.1 Asking for Explanations

**Always ask for explanations when you want to learn:**

Instead of:
```
Fix this code: [code]
```

Use:
```
Fix this code and explain:
1. What was wrong
2. Why it was wrong
3. How your fix works
4. How to avoid this mistake in the future

Code: [code]
```

### 3.2 Requesting Multiple Options

**Get different approaches to choose from:**

```
I need to [TASK].

Please provide THREE different approaches:

Approach 1: Simplest/most straightforward
Approach 2: Most performant
Approach 3: Most maintainable/elegant

For each approach, provide:
- The code
- Pros and cons
- When to use it
```

**Example:**
```
I need to remove duplicates from an array in JavaScript.

Please provide THREE different approaches:

Approach 1: Simplest/most straightforward
Approach 2: Most performant
Approach 3: Most maintainable/elegant

For each approach, provide:
- The code
- Pros and cons
- When to use it
```

### 3.3 Iterative Refinement

**Build up your prompt in stages:**

**Stage 1: Get basic solution**
```
Create a function that validates passwords.
Requirements:
- At least 8 characters
- Contains uppercase and lowercase
- Contains numbers
```

**Stage 2: Add specifics**
```
Modify the password validator to also:
- Require special characters (!@#$%^&*)
- Provide specific error messages for each failed requirement
- Return both a boolean and error messages
```

**Stage 3: Handle edge cases**
```
Update the password validator to handle:
- Null or undefined input
- Empty strings
- Passwords longer than 128 characters (reject them)
```

### 3.4 Asking for Comprehensive Analysis

**For complex problems, request structured analysis:**

```
Analyze this [LANGUAGE] codebase for [CONCERNS].

[CODE OR REPO STRUCTURE]

Please provide a report with:

1. Executive Summary
   - Overall assessment
   - Key findings (top 3-5 issues)

2. Detailed Analysis
   For each issue:
   - Location (file:line)
   - Severity (High/Medium/Low)
   - Description
   - Impact
   - Recommended solution

3. Prioritized Action Plan
   - Quick wins (easy to fix, high impact)
   - Important improvements (harder but valuable)
   - Future considerations

4. Code Examples
   - Before/after for top 3 issues
```

---

## Part 4: Essential Tips and Best Practices

### Tip 1: Be Specific About Your Environment

Always include:
- **Language and version:** "Python 3.9", "JavaScript ES6", "Java 11"
- **Framework and version:** "React 18", "Django 4.0", "Spring Boot 2.5"
- **Environment:** "Browser", "Node.js", "AWS Lambda"
- **Constraints:** "No external libraries", "Must work in IE11"

**Example:**
```
Environment:
- Python 3.9
- Django 4.0
- PostgreSQL 13
- Deployed on AWS Lambda
- Cannot use additional dependencies (keep it lightweight)
```

### Tip 2: Include Relevant Code

**What to include:**
- The problematic code
- Related functions/classes it depends on
- Error messages (complete stack traces)
- Configuration files if relevant

**What NOT to include:**
- Entire large files (extract relevant parts)
- API keys or sensitive data
- Unrelated code

**How to include code:**
````
```python
# Use code blocks with language specified
def my_function():
    return "something"
```
````

### Tip 3: Describe Expected vs. Actual Behavior

**Template:**
```
Expected behavior:
- [What should happen]

Actual behavior:
- [What actually happens]

Steps to reproduce:
1. [Step 1]
2. [Step 2]
3. [Result]
```

### Tip 4: Ask for Examples

Always request examples:
- "Provide usage examples"
- "Show example input and output"
- "Include sample test cases"
- "Demonstrate with a complete example"

### Tip 5: Request Code Comments

Ask for explanations in the code itself:
- "Include comments explaining complex parts"
- "Add docstrings to functions"
- "Comment each major step"

### Tip 6: Specify Output Format

Be clear about how you want the response:
- "Provide as Python code"
- "Format as a JSON object"
- "Return as a bulleted list"
- "Create a comparison table"

---

## Part 5: Common Mistakes to Avoid

### Mistake 1: Too Vague

**Bad:**
```
Make my code better
```

**Good:**
```
Improve the performance of this sorting function. It currently takes 5 seconds
with 10,000 items. I need it to handle 100,000 items in under 1 second.
```

### Mistake 2: No Context

**Bad:**
```
Why doesn't this work?
[code snippet]
```

**Good:**
```
This Python function should connect to a PostgreSQL database, but I'm getting
"connection refused" error. I'm running PostgreSQL 13 locally on port 5432,
and I can connect using psql command line.

[code snippet]
[complete error message]
```

### Mistake 3: Asking Multiple Unrelated Questions

**Bad:**
```
1. Fix my authentication bug
2. Optimize database queries
3. Add email validation
4. Explain how decorators work
[multiple code snippets]
```

**Good:**
Separate into multiple focused prompts, one per issue.

### Mistake 4: No Error Messages

**Bad:**
```
This code doesn't work
[code]
```

**Good:**
```
This code throws an error:
[code]

Error message:
TypeError: Cannot read property 'length' of undefined
    at validateInput (app.js:42)
    at processForm (app.js:67)
```

### Mistake 5: Assuming Context

**Bad:**
```
The login isn't working
```

**Good:**
```
The login form submission fails with a 401 error. I'm using JWT authentication
with Express.js. The token is being generated correctly (I verified in the database),
but when I send it in the Authorization header, I get 401 Unauthorized.

Here's the authentication code:
[code]

Here's the request being sent:
[request details]

Here's the error response:
[response details]
```

---

## Part 6: Ready-to-Use Prompt Templates

### Template 1: Bug Fix
```
**Bug Report**

Issue: [One-sentence description]

Environment:
- Language/Framework: [e.g., Python 3.9, Django 4.0]
- OS: [if relevant]
- Browser: [if relevant]

Code:
[Insert code here]

Expected Result:
[What should happen]

Actual Result:
[What actually happens]

Error Message (if any):
[Complete error with stack trace]

Steps to Reproduce:
1. [Step 1]
2. [Step 2]
3. [Error occurs]

What I've Tried:
- [Attempt 1]
- [Attempt 2]

Please provide:
1. Root cause explanation
2. Fixed code with comments
3. Prevention strategies
```

### Template 2: Code Review
```
**Code Review Request**

Please review this [LANGUAGE] code for:
- Code quality and best practices
- Potential bugs or errors
- Performance issues
- Security vulnerabilities
- Maintainability concerns

Code:
[Insert code]

Context:
[What this code does, where it's used]

Specific Concerns:
[Any particular areas you're worried about]

Please provide:
1. Issues found (with severity: High/Medium/Low)
2. Specific line-by-line feedback
3. Refactored version addressing main issues
4. General recommendations
```

### Template 3: Feature Implementation
```
**Feature Request**

Goal: [What you want to achieve]

Current State:
[Existing code or system description]

Requirements:
- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] [Requirement 3]

Acceptance Criteria:
- [How to know it works]
- [Edge cases to handle]

Constraints:
- [Technical limitations]
- [Style/pattern requirements]

Please provide:
1. Implementation plan/approach
2. Complete code with comments
3. Usage examples
4. Test cases
5. Potential issues and how to handle them
```

### Template 4: Optimization
```
**Performance Optimization Request**

Code to Optimize:
[Insert code]

Current Performance:
- [Metric 1, e.g., "Processes 1000 items in 5 seconds"]
- [Metric 2, e.g., "Uses 500MB RAM"]

Performance Goal:
- [Target 1, e.g., "Should handle 10,000 items in under 1 second"]
- [Target 2, e.g., "Should use less than 100MB RAM"]

Constraints:
- [e.g., "Must maintain same API"]
- [e.g., "Can't use external libraries"]

Please provide:
1. Performance bottleneck analysis
2. Optimized code with explanations
3. Before/after performance comparison
4. Any trade-offs in the optimization
```

### Template 5: Learning/Understanding
```
**Code Explanation Request**

I'm trying to understand this [LANGUAGE] code:
[Insert code]

My current understanding:
[What you think it does]

What I don't understand:
- [Question 1]
- [Question 2]
- [Question 3]

My background:
[Your experience level with this technology]

Please explain:
1. High-level: What does this code do?
2. Detailed: How does it work? (step-by-step)
3. Answer my specific questions
4. Highlight any advanced concepts used
5. Provide a simpler example if possible
```

### Template 6: Testing
```
**Test Creation Request**

Code to Test:
[Insert code]

Testing Framework: [e.g., Jest, pytest, JUnit]

Please create tests for:
- Happy path (normal usage)
- Edge cases
- Error conditions
- Invalid inputs

For each test, provide:
1. Test name describing what it tests
2. Test code
3. Explanation of what it verifies
4. Why this test is important

Coverage Goal: [e.g., "Test all public methods", "80% code coverage"]
```

---

## Part 7: Real-World Examples

### Example 1: Debugging a React Component

**Effective Prompt:**
```
I have a React component that's not updating when I expect it to.

Environment:
- React 18.2
- Using functional components with hooks
- No state management library

Component code:
```jsx
function TodoList() {
    const [todos, setTodos] = useState([]);

    const addTodo = (text) => {
        todos.push({ id: Date.now(), text: text });
        setTodos(todos);
    };

    return (
        <div>
            <button onClick={() => addTodo('New Todo')}>Add</button>
            <ul>
                {todos.map(todo => <li key={todo.id}>{todo.text}</li>)}
            </ul>
        </div>
    );
}
```

Expected: When I click "Add", a new todo should appear in the list
Actual: Nothing happens when I click the button
Error: None (no console errors)

I've tried:
- Adding console.log in addTodo (it does run)
- Checking the todos array (it does update)

Please:
1. Identify the bug
2. Explain why React isn't re-rendering
3. Provide corrected code
4. Explain the correct pattern for updating state
```

### Example 2: SQL Query Optimization

**Effective Prompt:**
```
I need help optimizing a slow SQL query.

Database: PostgreSQL 13
Table size: users table has 500,000 rows, orders table has 2,000,000 rows

Current query:
```sql
SELECT u.name, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.created_at >= '2024-01-01'
GROUP BY u.id, u.name, u.email
ORDER BY order_count DESC
LIMIT 100;
```

Performance issue:
- Takes 45 seconds to execute
- EXPLAIN shows full table scans

Indexes currently present:
- users: PRIMARY KEY on id
- orders: PRIMARY KEY on id, FOREIGN KEY on user_id

Please:
1. Identify why the query is slow
2. Suggest what indexes to add
3. Provide optimized query if changes needed
4. Explain the performance improvements
5. Show the updated query plan if possible
```

### Example 3: API Error Handling

**Effective Prompt:**
```
I need to add better error handling to my Express.js API endpoint.

Environment:
- Node.js 18
- Express 4.18
- Async/await for handling promises

Current code:
```javascript
app.post('/api/users', async (req, res) => {
    const user = await User.create(req.body);
    res.json(user);
});
```

Issues:
- No validation of input
- Database errors crash the server
- No proper HTTP status codes for errors
- No error messages returned to client

Requirements:
- Validate required fields (name, email)
- Validate email format
- Handle duplicate email errors (unique constraint in database)
- Return appropriate HTTP status codes
- Return user-friendly error messages
- Log errors for debugging

Please provide:
1. Updated code with comprehensive error handling
2. Comments explaining each error case
3. Example responses for different error scenarios
4. Suggestions for further improvements
```

---

## Part 8: Checklist for Great Prompts

Before submitting your prompt, check:

- [ ] **Clear objective** - Can someone understand what you want in one sentence?
- [ ] **Sufficient context** - Have you provided all relevant code and environment info?
- [ ] **Specific problem** - Is it clear exactly what's wrong or what you need?
- [ ] **Expected output** - Have you specified what format you want the answer in?
- [ ] **Error messages** - Have you included complete error messages if applicable?
- [ ] **Code formatting** - Is your code in code blocks with syntax highlighting?
- [ ] **Tried solutions** - Have you mentioned what you've already tried?
- [ ] **Constraints** - Have you specified any limitations or requirements?
- [ ] **Questions listed** - Are your questions numbered and specific?
- [ ] **Background provided** - Have you mentioned your experience level if relevant?

---

## Part 9: Quick Reference

### When You're Stuck

**Start with:**
```
I'm stuck on [PROBLEM].

Here's what I'm trying to do:
[GOAL]

Here's what I've tried:
[ATTEMPTS]

Here's my code:
[CODE]

Error (if any):
[ERROR]

Can you help me understand what's wrong and how to fix it?
```

### When You Need Ideas

**Start with:**
```
I need to [TASK] but I'm not sure of the best approach.

Requirements:
- [REQUIREMENT 1]
- [REQUIREMENT 2]

Constraints:
- [CONSTRAINT 1]
- [CONSTRAINT 2]

Please suggest 2-3 different approaches with pros and cons for each.
```

### When You Want to Learn

**Start with:**
```
I want to understand [CONCEPT/CODE].

My current level: [BEGINNER/INTERMEDIATE/ADVANCED in LANGUAGE]

[CODE OR CONCEPT]

Please explain:
1. What it is
2. How it works
3. When to use it
4. Common pitfalls
5. Simple example I can try
```

---

## Conclusion

Remember the golden rule of prompting coding agents:

**Be as specific and clear as you would when asking a senior developer for help.**

The more context, specifics, and structure you provide, the better the response you'll get. Don't hesitate to include:
- Complete error messages
- All relevant code
- What you've tried
- Your environment details
- What you expect vs. what you get

With practice, writing effective prompts becomes second nature. Start with the templates in this guide, adapt them to your needs, and refine based on the results you get.

Happy coding!

---

## Appendix: Language-Specific Tips

### For Python Developers
- Always specify Python version (2.7, 3.8, 3.9, etc.)
- Mention if using virtual environment
- Include requirements.txt contents if relevant
- Specify if following PEP 8 style guide

### For JavaScript Developers
- Specify ES5, ES6, or modern JavaScript
- Mention if using Node.js (and version) or browser
- Include package.json dependencies if relevant
- Specify if using TypeScript
- Mention framework (React, Vue, Angular) and version

### For Java Developers
- Specify Java version (8, 11, 17, etc.)
- Mention build tool (Maven, Gradle)
- Include relevant pom.xml or build.gradle sections
- Specify framework (Spring Boot, etc.) and version

### For Database Queries
- Always specify database (MySQL, PostgreSQL, SQL Server, etc.) and version
- Include table schemas
- Show EXPLAIN output for slow queries
- Mention index information

### For Web Development
- Specify browsers to support
- Include HTML/CSS if relevant to the problem
- Mention responsive design requirements
- Specify accessibility requirements if any
