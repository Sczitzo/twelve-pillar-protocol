# Contributing to the Twelve-Pillar Protocol

This is an open design project. Contributions are welcome in the following forms.

## How to contribute

### Critique and challenge (most valuable)
Open an Issue with:
1. The specific section, annex, or clause you are challenging
2. The failure mode or gap you have identified
3. Your proposed alternative or mitigation

Vague objections ("this won't work") without specific mechanism analysis will be asked to specify further. Specific adversarial challenges will be taken seriously and addressed in the threat register if warranted.

### Real-world analogues
If you know of a real-world system, historical case, or academic literature that is directly relevant to any patch or threat — open an Issue with the reference and which section it applies to.

### Terminology and plain-language improvements
The White Paper is intended to be accessible to a general audience. If any section is unclear, ambiguous, or uses unnecessary jargon, open an Issue with the specific passage and a suggested rewrite.

### Translation
If you are able to translate the White Paper or the Citizen-Facing Rights Layer into another language, open an Issue to coordinate.

## What is not accepted

- Wholesale redesign proposals that abandon the core LC/EC/DW/CR separation — this is the system's foundational constraint, not a negotiable parameter
- Changes that weaken existing protections without replacing them with stronger ones
- Philosophical objections without mechanism analysis
- Simplifications that break existing constraints

## The hardening methodology

This protocol is developed using adversarial red-teaming. Every threat has:
- A threat ID (T-XXX)
- An I/L/D risk score (Impact × Likelihood × (6 - Detectability))
- A linked patch (P-XXX)
- A residual risk statement

New threats should follow this format. New patches should specify the new risk they introduce.

## Review process

All substantive contributions are reviewed against:
1. Consistency with existing patches and clauses
2. Incentive analysis — what behavior does this create?
3. Bad actor stress test — how would a motivated actor exploit this?
4. Integration notes — what does this affect across the twelve pillars?

## Code of conduct

Technical disagreement is welcome. Personal attack is not. This project is about the design, not the designers.
