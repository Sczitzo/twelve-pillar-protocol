# Source-Grounded Content Prompts

These prompts are designed for **source-grounded** tools such as NotebookLM or any assistant that can answer from selected documents instead of free-associating from memory.

## Recommended source set

For most public-facing content, select:

- [`../README.md`](../README.md)
- [`One_Page_Overview.md`](./One_Page_Overview.md)
- [`../White_Paper.md`](../White_Paper.md)
- [`../Citizen_Facing_Rights_Layer.md`](../Citizen_Facing_Rights_Layer.md)
- [`../Humane_Constitution.md`](../Humane_Constitution.md)

For a shorter public set, use just:

- [`One_Page_Overview.md`](./One_Page_Overview.md)
- [`../White_Paper.md`](../White_Paper.md)
- [`../Citizen_Facing_Rights_Layer.md`](../Citizen_Facing_Rights_Layer.md)

## Public explainer prompts

### 1. Short public introduction

```text
Using only the selected sources, write a clear 90-second public introduction to the Humane Constitution for people who are tired of corruption, poverty, and systems that strip dignity. Explain the problem first, then the core separation between survival, markets, and civic power. Keep it concrete, serious, and easy to understand.
```

### 2. One-minute explainer script

```text
Using only the selected sources, write a one-minute explainer script for a general audience that does not understand how current systems of money and power operate. Focus on the simplest version of the idea: no one should lose baseline survival, markets can still function, and wealth should not be able to buy civic rule.
```

### 3. Skeptical-audience explainer

```text
Using only the selected sources, explain the Humane Constitution to a skeptical audience worried about socialism, bureaucracy, or social credit. Make the explanation fair, direct, and grounded in the sources rather than hype.
```

## Short-form content prompts

### 4. Short-form hooks

```text
Using only the selected sources, generate 15 short-form video hooks for TikTok, Reels, or Shorts. Each hook should be under 12 seconds when spoken and should challenge the assumption that poverty, corruption, and coercive systems are unavoidable.
```

### 5. Carousel or thread outline

```text
Using only the selected sources, create an 8-slide carousel outline explaining the Humane Constitution to ordinary people. Each slide should have a short headline and one or two sentences of supporting copy.
```

## FAQ and article prompts

### 6. Public FAQ

```text
Using only the selected sources, write a public-facing FAQ with 12 questions and answers about the Humane Constitution. Focus on dignity, corruption, markets, survival, freedom, and common misunderstandings.
```

### 7. Persuasive article

```text
Using only the selected sources, write a persuasive public article explaining why separating survival, markets, and civic power is the central breakthrough of the Humane Constitution. Keep it readable, concrete, and non-academic.
```

## Interview and podcast prompts

### 8. Podcast questions

```text
Using only the selected sources, generate 20 strong podcast interview questions about the Humane Constitution for a skeptical but curious audience. Include model answers grounded in the sources.
```

### 9. Hostile interview rehearsal

```text
Using only the selected sources, simulate a tough interview in which the host thinks this system is unrealistic, coercive, or too complex. Ask 10 hard questions and answer them from the source material without dodging.
```

## Critique prompt

### 10. Fair-minded critique

```text
Using only the selected sources, produce the strongest fair-minded critique of the Humane Constitution you can. Focus on the best objections, implementation risks, ambiguity, and likely failure points. Do not strawman the design.
```

## Video and audio prompt starters

### 11. Explainer video prompt

```text
Using only the selected sources, create a public explainer video script about the Humane Constitution for people who do not closely understand how systems of power, money, and governance work today. Explain the problem simply, then explain the five instruments and why the separation matters.
```

### 12. Audio overview prompt

```text
Using only the selected sources, create a conversational audio overview of the Humane Constitution for intelligent non-specialists. Focus on the survival floor, the role of Flow, and why Voice and Service Record are not social credit.
```

## Best practice

- Tell the tool to use **only the selected sources**.
- Prefer the shorter public source set when you want clearer outward-facing language.
- Add the full constitution only when you want tighter sourcing and more precision.
- Keep historical or internal design-history docs out of the source set unless you explicitly want archival context.
