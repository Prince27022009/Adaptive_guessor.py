# Adaptive_guessor.py

## 📌 Project Overview

This project is a command-line system that identifies an unknown entity using **logical constraints and adaptive questioning**.

Instead of relying on probability or machine learning, the system uses **explicit reasoning**: each user response eliminates inconsistent possibilities until a single valid entity remains [or a contradiction is detected].

The project demonstrates how **decision-making systems** can be built using simple, explainable logic, similar to early symbolic AI and rule-based systems.


## ⚙️ What This Program Does

**Output**:  
A terminal-based interactive session that:

• Displays a list of available entities  
• Asks a series of yes/no questions  
• Narrows down possibilities dynamically  
• Identifies the chosen entity  
• Displays a lesser-known fact about it  

**Process**:

• User silently chooses one entity from a predefined list  
• Entities are represented using binary attributes  
• Each question applies a logical constraint  
• Inconsistent entities are eliminated step by step  
• Questions are chosen adaptively, not in fixed order  
• System either converges to one entity or detects contradiction  


## 🧠 How It Works

### Entity Representation

• Each entity is modeled as a set of boolean attributes  
• Attributes describe high-level properties (place, person, fictional, etc.)  
• All entities share the same attribute space  


### Constraint Elimination Logic

• The system starts with all entities as valid candidates  
• Every answer filters out entities that violate the constraint  
• Filtering is strict and deterministic  
• No guessing or recovery from incorrect answers  


### Adaptive Question Selection

• Unused attributes are evaluated at each step  
• The attribute that best splits remaining entities is selected  
• This minimizes the search space efficiently  
• Prevents unnecessary or redundant questions  


### Contradiction Detection

• If no entity satisfies all imposed constraints, the system detects it  
• This indicates inconsistent or incorrect user answers  
• The system stops instead of forcing a guess  


### Fact Output

• Once an entity is identified, a non-obvious fact is displayed  
• Facts are stored separately from logic  
• Output is deterministic and clean  


## 🌟 Features Demonstrated

• Constraint-based reasoning  
• Adaptive decision-making  
• Explainable symbolic logic  
• Entity elimination using binary attributes  
• Clean separation of data, logic, and interaction  
• Defensive handling of contradictory input  
• Simple but extensible architecture  


## 🎯 Why I Built This

I wanted to explore **decision-making systems without machine learning**.

Modern AI often hides reasoning behind black-box models.  
This project focuses on the opposite approach: **explicit logic**, where every decision can be traced and explained.

By building this project, I aimed to:

• Understand constraint satisfaction in practice  
• Learn how adaptive questioning reduces search space  
• Build explainable reasoning systems  
• Strengthen logical thinking and system design skills  
• Avoid overengineering while keeping the design clean  


## 🤖 AI Assistance Disclaimer

AI was used only as a **support tool**, not as a logic generator.

**AI helped with**:

• Debugging runtime issues  
• Reviewing architecture decisions  
• Improving clarity of explanations  
• Formatting and documentation  

**AI did NOT**:

• Design the reasoning logic  
• Choose attributes or entities  
• Implement the decision system  
• Decide how constraints are applied  

All core logic and system behavior were designed and understood by me.


## ▶️ How to Run the Program

**Requirements**:

• Python 3.x  

**Run from Python shell or another script**:

```python
from game import guess
guess()
