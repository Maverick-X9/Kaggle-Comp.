# Make Data Count (MDC) Data Citation Extraction

## Overview

Make Data Count (MDC) is a global initiative aimed at improving the recognition, reuse, and impact measurement of scientific data. Despite the critical role of data in scientific discoveries, research data remains significantly undervalued and under-cited. This project tackles the challenge of identifying and contextualizing data citations in scientific literature to help establish standardized metrics for data reuse and impact.

## Project Goal

The goal of this project is to build a highly performant model that automatically extracts **data citations** from full-text scientific papers and classifies them as either:

- **Primary Data Citation:** Raw or processed data generated as part of the study.
- **Secondary Data Citation:** Raw or processed data reused or derived from existing datasets or publications.

The model will enrich the Make Data Count Data Citation Corpus by adding high-quality, contextualized links between scientific data and papers.

## Context

- Most research data remains uncited (~86%), making it difficult to track and credit data reuse.
- Data citations appear in diverse and inconsistent ways within papers—ranging from formal references to informal mentions in methods or discussion sections.
- Understanding how data is cited (primary vs. secondary) provides important context for evaluating data’s role in research.

## Why This Problem is Challenging

- Data references are often indirect or embedded in narrative text rather than formal citations.
- Variable language and phrasing complicate automatic detection.
- Existing corpora only cover a fraction of literature without contextual details.

## Impact

A successful model will:

- Enable MDC to update and maintain a comprehensive, open, and high-quality corpus of data citations.
- Support better tools for tracking and rewarding data reuse.
- Help shift scientific culture toward valuing data as a primary research output.
- Promote collaboration, transparency, and innovation in science.
