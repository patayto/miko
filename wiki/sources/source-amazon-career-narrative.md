---
title: "Amazon Career Narrative: Predictive Demographics and Demographic Targeting"
type: source
tags: [career, amazon, ml, targeting, leadership]
created: 2026-04-09
updated: 2026-04-09
---

## Career Progression

Filipe's Amazon career spans internships (2017–2019) and full-time employment (2020–2025) across four major teams: Alexa Knowledge, Alexa Show devices, Audience Insights/Program Swan, and Demographic Targeting.

**Key roles:**
- Built knowledge ingestion tracking and debugging tools for Alexa
- Developed ML algorithms for image classification and cleaning
- Created fullstack Geographic Insights component for Amazon Advertising
- Designed and shipped the Persona Builder API with public-facing OpenAPI specifications
- Led the resurrection and global scaling of Predictive Demographics (PD)
- Mentored engineers and data scientists; served as Science Manager

## The Predictive Demographics Journey

The core narrative follows PD from crisis to massive scaling (2022–2025):

**Initial crisis:** Inherited a failing ML product (Wibble, built in Java with untyped JSON schemas and poor model architecture). Partnered with principal engineer Evan to refactor the codebase and debug the training pipeline. A botched first launch resulted in a $5M revenue hit when models incorrectly predicted 60% of customers as male/female (vs. expected 20–24%).

**Root cause analysis:** Through overlap analysis and feature investigation, discovered that 1P predictions captured active customers (those in recent bid logs), while 3P data included older, inactive records. This insight reframed the incident as discovery of a massive untapped opportunity rather than failure.

**Production launch strategy:** Designed and built a [[Dial-Up Mechanism]] for A/B-style allocation blending using consistent hashing across 1P and 3P audiences. Created a [[Shadow Publishing Pipeline]] to measure audience size and BDR in production without risk. Launched across US, UK, and JP over two weeks with gradual rollout, monitoring, and metrics—no major incidents.

**Scaling:** Built Kassandra, an Amber stack in Kotlin, implementing:
- ML training on 1P customer signals (view/purchase history) with 3P demographic labels as ground truth
- Configurable lookback periods and threshold-based quality filtering using percentile scoring
- Automated dial-up mechanism to smoothly transition segments from 3P to 1P allocations
- Shadow publishing pipeline for safe experimentation and metric validation

**Global expansion:** Scaled from 3 regions to 17 countries. Added new models (music, Twitch, video). Developed marketplace-level models for better accuracy and cross-marketplace scoring for data-scarce locales. Implemented multi-allocation strategies and conflict resolution via prediction waterfall.

## Technical Contributions

- **API Design:** Persona Builder OpenAPI contract (approved through strict Bar Raiser review process)
- **Data Engineering:** Spark jobs for overlap analysis, audience aggregation, threshold optimization
- **ML Systems:** Transitioned from region-based to marketplace-level models; experimented with AdBERT, linear classifiers, and neural networks; added feature engineering for new data sources
- **Operations:** Built extensive monitoring, drift metrics, and on-call runbooks; implemented Glue table ingestion for cross-team debugging
- **Leadership:** Onboarded diverse team from outside ads; mentored engineers; led weekly science syncs; wrote technical documentation bridging science, engineering, and business metrics

## Team Dynamics

Joined the US-based Demographic Targeting team under SDM Mrunali in 2023. Built and scaled the team from one person (Filipe) to include principal engineer Hunter, applied scientist Vlad, data scientist Beena, and multiple SDE-I/II engineers. Navigated difficult interpersonal dynamics with leadership figures Ravi and Rohan while establishing productive collaboration with Mrunali and Priya. Served as Science Manager alongside individual contribution, earning peer recognition for mentorship and technical direction.

## Key Challenges

- Debugging untyped, poorly-architected ML codebases inherited from predecessor teams
- Tuning lookback periods, thresholds, and aggregation strategies to balance audience size and prediction quality
- Scaling infrastructure to support multiple models, marketplaces, and simultaneous experiments
- Managing cross-timezone collaboration and knowledge transfer with remote teams
- Resolving multi-model conflicts via principled waterfall strategies
- Building visibility and measurement across multiple downstream systems and teams

---
*My notes - do not edit below this line*
