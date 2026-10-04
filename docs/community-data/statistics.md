# Community Data — Live Statistics

*Computed from the structured record database on 2026-10-04 (after ingestion batch 4). Figures describe de-identified reports from one public quit-smoking forum — they are not clinical data and not generalizable to all quitters.*

## Database size

| Record type | Count |
|---|---|
| Experience records (total) | **82** |
| — published (public pages) | 68 |
| — noindex (internal database only) | 12 |
| — review (medical safety gate) | 2 |
| Relapse reports | 12 |
| Community patterns | 3 |
| Questions | 12 |

## Quality distribution (published experiences)

| Metric | Value |
|---|---|
| Mean quality score | 7.5 / 10 |
| Minimum (publish threshold) | 6 / 10 |
| Maximum | 9 / 10 |

Quality scoring follows the rubric in [CONTENT-QUALITY.md](https://github.com/martinxionbiotech-max/SmokingCessation/blob/main/CONTENT-QUALITY.md): information density, specificity, honesty about unknowns, and evidence labeling.

## Quit methods reported

Across 68 published experience records (a record may report more than one method):

| Method | Records |
|---|---|
| Cold turkey | 27 |
| Daily community check-ins | 4 |
| Reading-based program (Allen Carr) | 4 |
| Gradual reduction | 2 |
| Exercise | 2 |
| Removing all smoking devices | 1 |
| Quitting alcohol at the same time | 1 |
| Smoking cessation medication (type unspecified) | 1 |
| Diet change | 1 |

## Smoking history reported

- 41 of 68 published records (60%) report years of smoking; the rest are marked "Not reported".
- Reported histories range from 9 to 40 years, with many in the 15–30 year range.
- Age groups reported: 20s (3), 30s (5), 40s (2), 50s (1) — most records do not state age.

## Relapse

- 13 of 68 published experience records (19%) describe at least one previous relapse.
- The 12 structured relapse reports record time smoke-free before relapse:

| Time smoke-free before relapse | Reports |
|---|---|
| 2–3 months | 4 |
| 100 days | 1 |
| 6 months | 1 |
| 7 months | 2 |
| 9 months | 1 |
| 1 year | 1 |
| 1.5 years | 1 |
| ~4 years | 1 |

### Patterns observed across reports

1. **Alcohol and social occasions** — the most reported relapse setting (6 relevant reports), including one report of surviving drinking situations smoke-free (a contradictory case).
2. **Relapse returns a heavier habit** — several reports describe smoking more after relapse than before the quit (3 relevant reports).
3. **The first cigarette is the relapse** — a single cigarette taken as reward or accepted casually was the pivot point of relapse in multiple reports (4 relevant reports).

## Most-reported symptoms (published records)

Symptoms are self-reported withdrawal or health effects, not diagnoses:

| Symptom | Records |
|---|---|
| Chest tightness | 6 |
| Irritability | 4 |
| Dizziness | 4 |
| Cough | 3 |
| Phlegm | 3 |
| Shortness of breath | 3 |
| Anxiety | 2 |
| Poor concentration | 2 |
| Stomach bloating | 2 |
| Drowsiness | 2 |
| Weakness | 2 |

## Recovery stages represented

| Stage | Records |
|---|---|
| First Week | 11 |
| Long-Term | 10 |
| First Month | 5 |
| First Two Weeks | 4 |
| First Three Months | 3 |
| Week 3 | 3 |
| Other stages (2 weeks – 6 months) | 5 |

## Evidence status

Every record in the database is labeled `community-report` (82 of 82). The evidence-status scale (`community-report` → `pattern-supported` → `evidence-aligned` → `evidence-mixed`) is applied when patterns and research alignment are assessed; currently only the `pattern-supported` level is in use, on the three pattern pages.

## How these numbers change

Statistics are recomputed after each ingestion batch. Each batch:

1. collects source material only from real, public forum posts;
2. applies the privacy filter and de-identification rules;
3. structures records against the published data model;
4. deduplicates against existing records;
5. writes an original English editorial synthesis (no verbatim translation);
6. assigns quality score, confidence level, and editorial status (`published` / `noindex` / `review`);
7. rebuilds the site — noindex and review records never produce public pages.
