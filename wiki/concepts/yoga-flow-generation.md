---
title: "Yoga Flow Generation"
type: concept
tags: [yoga, generative, app-idea, markov-chains]
created: 2026-04-09
updated: 2026-04-09
---

Yoga flow generation is the computational problem of producing a sequence of poses that forms a coherent, safe, and stylistically consistent practice. The challenge has both a structural dimension (which poses can follow which) and an aesthetic dimension (what gives a sequence a particular feel or identity).

## Markov chain approach

The most tractable formulation models each pose as a state in a [[Markov Chains|Markov chain]]. Transition probabilities are learned from a corpus of documented sequences. Sampling from the chain produces novel flows that respect the statistical patterns of the training data. A Northwestern study applied this method to yoga and confirmed it generates plausible sequences.

Available datasets for building such a model include:

- Yoga-82 (82-class pose benchmark)
- A PubMed yoga pose classification study
- Kaggle yoga poses dataset

## Style as transition distribution

A key idea is that "style" can be encoded in the transition probabilities themselves. Training on sequences from a particular teacher, tradition, or fictional source produces a chain whose output resembles that source. The specific inspiration noted: generating flows in the style of the waterbending scroll from Avatar: The Last Airbender — implying that a sufficiently specific or characterful source could imprint a recognisable aesthetic on the generated sequence.

## App concept

The project idea is a generative yoga app where the user selects a style reference, and the app produces a complete flow by sampling from the corresponding trained chain. Pose curation and transition safety constraints would need to be layered on top of the raw probabilistic model.

---
*My notes - do not edit below this line*
