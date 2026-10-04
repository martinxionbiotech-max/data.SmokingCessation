# Community Data Center

This section of the Data Center documents the **structured community experience database** that powers the experiential layer of Quit Smoking Hub. It describes where the data comes from, how it is processed, what rules protect privacy and safety, and what the aggregate statistics currently show.

## What this dataset is

The community experience database is a collection of structured, de-identified records synthesized from real quit-smoking experiences shared in a large public Chinese-language quit-smoking forum (Baidu Tieba's 戒烟吧 / "Quit Smoking Bar"). The forum has operated for nearly two decades and contains tens of thousands of first-person quit accounts, check-in diaries, relapse reports and Q&A threads.

Each record captures, where the source reports it:

- smoking history (years, cigarettes per day, age group)
- quit method(s) used
- recovery stage and day count
- triggers and cravings
- physical symptoms and emotional state
- strategies and interventions
- outcome and relapse information
- lessons the person drew

## What this dataset is not

!!! warning "Community reports are not scientific evidence"
    Every record is a **community report** — one person's account of their own experience, as posted in a public forum. The records:

    - are **not** clinical data and were not medically verified;
    - are **not** a substitute for research findings, guidelines, or medical advice;
    - may contain selection bias: people who post in a quit-smoking forum are a specific subset of all people who try to quit;
    - cannot support causal claims about any method, symptom, or medication.

    Aggregate statistics below describe *what this forum's members reported*, nothing more.

## Privacy and ethics rules

The ingestion pipeline follows these rules, which are enforced for every record:

1. **No usernames, user IDs, avatars, or contact information** are ever stored or published.
2. **No verbatim copying or wholesale translation** of any post — records are original English editorial syntheses of the reported facts.
3. **Unreported fields are marked "Not reported"** — nothing is inferred to fill gaps.
4. **Thin records** (insufficient information) remain in the internal database and are marked `noindex`; they generate no public pages.
5. **Medical safety gate**: content indicating mental-health high risk (e.g. self-harm, crisis) is held in `review` status and never auto-published.
6. **Non-judgmental language**: the site uses "relapse" and "return to smoking", never "failure" or "weakness".

## Where the records live

The full structured records are maintained in the main site's content repository ([SmokingCessation](https://github.com/martinxionbiotech-max/SmokingCessation), `src/data/experiences/`, `src/data/relapse/`, `src/data/patterns/`). Public pages render at:

- [Community Experiences](https://smokingcessation.pages.dev/experiences/) — individual experience pages
- [Relapse Reports](https://smokingcessation.pages.dev/relapse/) — structured relapse records
- [Community Patterns](https://smokingcessation.pages.dev/patterns/) — patterns observed across multiple reports

See also the ingestion pipeline documentation ([CONTENT-INGESTION.md](https://github.com/martinxionbiotech-max/SmokingCessation/blob/main/CONTENT-INGESTION.md)) and the data model ([DATA-MODEL.md](https://github.com/martinxionbiotech-max/SmokingCessation/blob/main/DATA-MODEL.md)).

## Current statistics

[View the live aggregate statistics](statistics.md), recomputed from the record database after each ingestion batch.
