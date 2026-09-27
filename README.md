# MGR-FM3 Project 2
# Alzheimer Disease Intelligence Engine

Version: 0.1

## Overview

MGR-FM3 Project 2 is an agentic AI architecture for structured
Alzheimer Disease evidence analysis and decision support.

The system integrates:

Evidence
Evidence Fabric
Knowledge Graph
24 Wisdom Engines
AI Reasoning
Critique and Reasoning Loop
Decision Intelligence
LangSmith Evaluation
Human Review

The system is designed as a controlled scientific workflow rather
than an autonomous scientific decision maker.

## Architecture

Evidence
    |
    v
Evidence Fabric
    |
    v
Knowledge Graph
    |
    v
24 Wisdom Engines
    |
    v
AI Reasoning
    |
    v
Critique Loop
    |
    v
Decision Intelligence
    |
    v
Evaluation and Observability
    |
    v
Human Review

## Current Validation Status

Checkpoints 0 through 18 have been validated.

The validated system currently contains:

- 10 evidence records
- 10 Evidence Fabric records
- 21 Knowledge Graph nodes
- 20 Knowledge Graph edges
- 24 Wisdom Engines
- 24 Wisdom Engine baseline outputs
- 11 reasoning graph nodes
- 12 reasoning graph edges
- 6 critique findings
- 4 decision-support options
- 10 decision criteria

## Safety State

LLM execution: NOT STARTED

Scientific conclusions: DISABLED

Automatic decision: DISABLED

Unsupported inference: BLOCKED

Human review: REQUIRED

Automatic critique iteration: DISABLED

Automatic contradiction resolution: DISABLED

## Evidence and Traceability

The project preserves evidence provenance, uncertainty,
knowledge gaps, contradictions, and decision-support traceability.

Agent-to-source links are not fabricated when unavailable.

## Reproducibility

The project uses:

- Google Drive for persistent project storage
- Colab for execution
- GitHub for version control
- LangChain for intelligence and tool integration
- LangGraph for workflow orchestration
- LangSmith for tracing and evaluation

## Project Structure

config/
data/
evidence/
knowledge_graph/
wisdom_engines/
src/
results/
reports/
logs/
checkpoints/
tests/
docs/
notebooks/

## Scientific Governance

The system is intended to support qualified scientific review.

It does not automatically replace scientific judgment.

Human review remains mandatory for consequential scientific
interpretation and decision support.

## Status

Production repository preparation is being validated through
explicit project checkpoints.

Checkpoint 19: GitHub Production Repository

Checkpoint 20: Final Documentation and Reproducibility
