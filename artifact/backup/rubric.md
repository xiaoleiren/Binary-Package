# Cross-Unit Assessment Rubric

Use a 0-4 scale for each dimension. Weight dimensions by unit as specified below.

## Dimensions

### 1. Boundary and Permission Reasoning
- **4**: Correctly identifies tools, permissions, trust boundaries, delegation paths, and justifies each identification with evidence
- **3**: Identifies main tools and permissions; misses one boundary or delegates without justification
- **2**: Identifies main tools but misses at least one important boundary or permission
- **1**: Identifies tools but treats all inputs as equally trusted; boundary reasoning missing
- **0**: Treats all tools and inputs as equally trusted; no boundary reasoning

### 2. Evidence Use and Trace Localization
- **4**: Cites exact trace events; distinguishes root deviation from downstream symptoms; explains causal chain
- **3**: Cites exact events; identifies root deviation but causal chain underspecified
- **2**: Finds suspicious events but gives incomplete causal explanation
- **1**: Mentions events without citing specific evidence
- **0**: Provides conclusions without trace evidence

### 3. Trusted/Untrusted Input Analysis
- **4**: Explains source, channel, authority, and why data should or should not govern actions; compares alternative interpretations
- **3**: Identifies source and channel; explains authority but not alternatives
- **2**: Labels input as suspicious without explaining authority
- **1**: Acknowledges input but treats it as neutral
- **0**: Accepts retrieved content as instruction without question

### 4. Causal and Consequence Explanation
- **4**: Explains how failure propagates through the system; identifies what harm or unsafe action could result; proposes a specific scenario
- **3**: Explains propagation and harm; scenario is generic
- **2**: Identifies harm but not propagation
- **1**: Identifies harm in vague terms
- **0**: No explanation of consequences

### 5. Mitigation and Regression-Test Quality
- **4**: Proposes a specific mitigation and a test that fails on unsafe baseline and passes after mitigation; explains why the test works
- **3**: Proposes mitigation and test; test oracle is plausible but underspecified
- **2**: Proposes mitigation or test but lacks clear oracle
- **1**: Proposes mitigation that does not address root cause
- **0**: Blocks all tool use (over-mitigation) or provides no test

## Unit-Specific Weighting

| Unit | Weighting Emphasis |
|------|-------------------|
| 1 (System mapping) | Dimension 1: 40%; Dimensions 2-5: 15% each |
| 2 (Failure modes) | Dimensions 2 and 3: 35% each; others: 10% each |
| 3 (Indirect injection) | Dimension 3: 40%; Dimensions 2 and 4: 20% each; others: 10% each |
| 4 (Trace auditing) | Dimensions 2 and 4: 30% each; Dimensions 1, 3, 5: ~13% each |
| 5 (Regression testing) | Dimension 5: 40%; Dimensions 2 and 4: 20% each; others: 10% each |

## Partial Credit Principles

- A justified assumption earns credit: the student names the evidence used, the missing information, and how the conclusion would change if the assumption were false
- Reasonable alternative interpretations earn credit when the student's causal chain is defensible
- The goal is audit reasoning, not guessing a single answer