# Community Data — Live Statistics

*Computed from the structured record database on 2026-10-04 (after ingestion batch 7). Figures describe de-identified reports from one public quit-smoking forum — they are not clinical data and not generalizable to all quitters.*

## Database size

| Record type | Count |
|---|---|
| Experience records (total) | **169** |
| — published (public pages) | 133 |
| — noindex (internal database only) | 34 |
| — review (medical safety gate) | 2 |
| Relapse reports | 12 |
| Community patterns | 6 |
| Questions | 12 |

## Quality distribution (published experiences)

| Metric | Value |
|---|---|
| Mean quality score | 7.3 / 10 |
| Minimum (publish threshold) | 6 / 10 |
| Maximum | 9 / 10 |

Quality scoring follows the rubric in [CONTENT-QUALITY.md](https://github.com/martinxionbiotech-max/SmokingCessation/blob/main/CONTENT-QUALITY.md): information density, specificity, honesty about unknowns, and evidence labeling.

## Quit methods reported

Across 133 published experience records (a record may report more than one method):

| Method | Records |
|---|---|
| Cold turkey | 29 |
| Reading-based program (Allen Carr) | 7 |
| Daily community check-ins | 4 |
| Gradual reduction | 3 |
| Exercise | 2 |
| Diet change | 2 |
| Smoking cessation medication (type unspecified) | 1 |
| Removing all smoking devices | 1 |
| Quitting alcohol at the same time | 1 |
| E-cigarette substitution | 1 |
| Nicotine replacement (patch) | 1 |

## Smoking history reported

- 70 of 133 published records (53%) report years of smoking; the rest are marked "Not reported".
- Reported histories range from 3 to 40 years; 39 records fall in the 10–20 year range and 25 in the 21–40 year range.
- Age groups reported: 20s (7), 30s (7), 40s (3), 50s (1) — most records do not state age.
- Gender reported: female (2) — most records do not state gender.

## Relapse

- 13 of 133 published experience records (10%) describe at least one previous relapse.
- The 12 structured relapse reports record time smoke-free before relapse:

| Time smoke-free before relapse | Reports |
|---|---|
| 2–3 months | 5 |
| 100 days | 1 |
| 6 months | 1 |
| 7 months | 2 |
| 9 months | 1 |
| 1 year | 1 |
| 1.5 years | 1 |
| ~4 years | 1 |

One structured report spans two relapses (6 months, then 3 months) and appears in both rows. Beyond the structured reports, one published experience (EXP-2020-005) records a quit of roughly 1,730 days — nearly five years — that was lost, followed by a new attempt: the longest relapse-free period documented in the database.

### Patterns observed across reports

1. **Alcohol and social occasions** — the most reported relapse setting (6 relevant reports), including one report of surviving drinking situations smoke-free (a contradictory case).
2. **Relapse returns a heavier habit** — several reports describe smoking more after relapse than before the quit (3 relevant reports).
3. **The first cigarette is the relapse** — a single cigarette taken as reward or accepted casually was the pivot point of relapse in multiple reports (6 relevant reports), including two near-miss cases in which the slip was contained and the quit continued.
4. **Smoking dreams** — vivid dreams about smoking, usually arriving around a month into the quit and treated by reporters as a passing phase rather than a warning (3 relevant reports; none relapsed).
5. **Health events as the decisive motivation** — quits started from a hospitalization, diagnosis, a relative's smoking-related death or alarming test results, described as feeling different from gradual decisions (9 relevant reports).
6. **Daily check-ins as a commitment device** — daily sign-in rituals maintained for years, in two cases a decade, with the streak and its public visibility anchoring the quit (6 relevant reports).

## Most-reported symptoms (published records)

Symptoms are self-reported withdrawal or health effects, not diagnoses:

| Symptom | Records |
|---|---|
| Chest tightness | 6 |
| Dizziness | 5 |
| Irritability | 4 |
| Shortness of breath | 4 |
| Cough | 3 |
| Phlegm | 3 |
| Blurred vision | 2 |
| Weakness | 2 |
| Anxiety | 2 |
| Drowsiness | 2 |
| Stomach bloating | 2 |
| Insomnia | 2 |
| Poor concentration | 2 |

## Recovery stages represented

| Stage | Records |
|---|---|
| First Week | 22 |
| Long-Term | 18 |
| First Month | 7 |
| First Three Weeks | 6 |
| First Two Months | 4 |
| First Two Weeks | 4 |
| First Three Months | 4 |
| Week 3 | 3 |
| Other stages (2 weeks – 1 year) | 3 |

## Evidence status

Every record in the database is labeled `community-report` (169 of 169). The evidence-status scale (`community-report` → `pattern-supported` → `evidence-aligned` → `evidence-mixed`) is applied when patterns and research alignment are assessed; currently the `pattern-supported` level is in use on the six pattern pages.

## How these numbers change

Statistics are recomputed after each ingestion batch. Each batch:

1. collects source material only from real, public forum posts;
2. applies the privacy filter and de-identification rules;
3. structures records against the published data model;
4. deduplicates against existing records;
5. writes an original English editorial synthesis (no verbatim translation);
6. assigns quality score, confidence level, and editorial status (`published` / `noindex` / `review`);
7. rebuilds the site — noindex and review records never produce public pages.
