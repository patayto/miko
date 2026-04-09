---
title: "Markov Chains"
type: concept
tags: [probability, sequencing, modeling]
created: 2026-04-09
updated: 2026-04-09
---

A Markov chain is a probabilistic model in which a system transitions between states, where the probability of the next state depends only on the current state — not on the history of how it got there. This "memoryless" property (the Markov property) makes the model tractable and easy to sample from.

The model is defined by a set of states and a transition matrix encoding the probability of moving from each state to every other. Sampling a sequence means starting at some state and repeatedly drawing the next state from the current state's probability distribution.

## Applications in creative sequencing

Markov chains are well-suited to any domain where there is a natural vocabulary of discrete units and a meaningful sense of "what typically follows what." Examples include:

- Text generation (word or character n-grams)
- Music composition (note-to-note transitions)
- [[Yoga Flow Generation]] (pose-to-pose transitions)

In yoga sequencing, each pose becomes a state and the transition probabilities capture which poses commonly or safely follow each other. A Northwestern study demonstrated this approach and generated novel sequences by sampling from learned transition matrices.

## Style encoding

Transition probabilities can be trained on a specific corpus — a teacher's recorded sequences, a style guide, or a named tradition — allowing the chain to generate output "in the style of" a source. This is the mechanism behind the [[Yoga Flow Generation]] app concept.

---
*My notes - do not edit below this line*
