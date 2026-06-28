# Source-to-Binary Reasoning Rubric

## Lab 4 Integrated CTF Challenge (10 points total)

### Dimension 1: Source-to-Binary Mapping & Gap Explanation (4 points)

| Score | Description |
|-------|-------------|
| 4 | Accurately maps source lines to binary addresses; clearly explains the gap (optimization, UB, or FFI); uses correct terminology |
| 3 | Maps most source constructs to binary; explains the gap but with minor inaccuracies |
| 2 | Attempts mapping but misses key constructs; explanation is vague or partially incorrect |
| 1 | Minimal mapping attempt; explanation is unclear or absent |
| 0 | No mapping or explanation provided |

### Dimension 2: Dynamic Trace Evidence (3 points)

| Score | Description |
|-------|-------------|
| 3 | Complete GDB trace with breakpoint, memory dump, and annotation matching the assigned binary hash |
| 2 | Trace present but incomplete (missing breakpoint or memory dump) |
| 1 | Trace present but does not match the assigned binary hash |
| 0 | No trace evidence provided |

### Dimension 3: Mitigation Proposal Quality (3 points)

| Score | Description |
|-------|-------------|
| 3 | Proposes concrete, implementable mitigation specific to the identified gap |
| 2 | Proposes generic mitigation (e.g., "turn off optimizations") without specificity |
| 1 | Mitigation is unrelated to the identified gap |
| 0 | No mitigation proposed |

## Scoring Examples

### Excellent (9-10 points)

- Student correctly identifies dead-store elimination, provides GDB trace showing the missing memset at -O2, and proposes using `volatile` or `__attribute__((optimize("O0")))`.

### Proficient (7-8 points)

- Student identifies the gap but confuses source-level and binary-level terms; provides trace evidence but missing memory dump; proposes generic "use safer functions" mitigation.

### Developing (5-6 points)

- Student finds the flag but cannot explain the source-to-binary gap; trace evidence is present but incomplete; mitigation is unrelated.

### Unsatisfactory (0-4 points)

- Flag found via trial and error; no explanation, trace evidence, or mitigation.