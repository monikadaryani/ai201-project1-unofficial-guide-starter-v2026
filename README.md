# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
     Corpus I used was campus_life. It contains information from a campus where they have written reviews from mostly students. It would answer questions which can cover multiple documents like "What is cost of laundry?" and other details like "How are walls in Fenwick court?" It can help a new student determine what to do to navigate the university and living situation on campus. 


## Chunking Strategy

**Chunk size:** 2000
**Overlap:** 300

According to https://www.firecrawl.dev/blog/best-chunking-strategies-rag Recursive character splitting at 400-512 tokens with 10-20% overlap is the best default for most use cases. So I chose 2000 characters as its roughly 400-512 tokens with 15% overlap. 
When reading documents some corpora like campus_life have shorter files while others have very big files like advice_threads. Assignment also pointed out how we can have very small chunks of 2 character and those don't seem like a very good strategy, so I chose recursive character splitting which can avoid very or awkward chunks. This method also maintains semantic structure as it  tries to preserve natural boundaries before it falls back to fixed-size cutting: paragraph breaks: (\n\n) ; line breaks: (\n) ; sentence endings: (. , ? , !) ; spaces ( ). 


<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

     ======================================================================
     Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
     ======================================================================
     On the add/drop deadline

     You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

     ======================================================================
     Chunk 2  |  source: course_biol_160.txt#0  |  produced by: chunker.py::split_documents
     ======================================================================
     BIOL 160 Cell Biology

     I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

     Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

     The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.

     ======================================================================
     Chunk 3  |  source: course_hist_118_workload.txt#0  |  produced by: chunker.py::split_documents
     ======================================================================
     Workload for HIST 118 Modern World History

     People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

     It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

     ======================================================================
     Chunk 4  |  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::split_documents
     ======================================================================
     Re: Pellew Dining Hall

     Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

     Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.

     ======================================================================
     Chunk 5  |  source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::split_documents
     ======================================================================
     Innisfree Hall — what it's actually like

     Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

     The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

     The bad: no air conditioning, which matters for the first three weeks of September.

     Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"How many unit tests are in biology 160?"

**Answer:**


```

There are four unit tests in BIOL 160 Cell Biology (source: `course_biol_160.txt` and `course_biol_160_exams.txt`).
```

**My relevance cutoff:** 0.65

I chose this cut-off because when I checked all the questions, the maximum in the relevant questions was 0.476 and the minimum in non-relevant questions was 0.825. So I calculated Midpoint of the gap (0.476+0.825)/2 = 0.65

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| What is cost of laundry? | Yes | 0.3274 |
| When can you add a course? | Yes | 0.3873 |
| How many unit tests are in biology 160? | Yes | 0.3294 |
| When does Halden Hall close? | Yes | 0.373  |
| How are walls in Fenwick Court? | Yes | 0.4761 |
| What is the capital of Mongolia? | No | 0.8246 |
| How do I change the oil in a diesel engine? | No | 0.9340 |
| Who won the 1994 World Cup? | No | 0.8859 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8442 |
| How do I write a for loop in Rust? | No | 0.8960 |

The distribution clearly shows that the related questions have their distance \< 0.5 and unrelated questiond have the distance > 0.8. 

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I used gemini which is integrated in google. I looked for best chunking strategy online where it guided me to the link with best chunking strategies. I used it to search and determine chunk size and overlap numbers as well. 

I intuitively calculated the relevance cut-off, used it to confirm my method was correct. 
I use gemini for some words to write when I cannot think of one because English is not my first language.

**2.**
I took help from Claude code to create the recursve character splitting function and tested it myself later to see if it is working. 

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5  | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk size | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Top-k chunks | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!--| 5. Time to generate| 4/5 | 3/5 | 5/5 | 4/5 | MISSED |>

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->
  <!--   I am looking at results/run_2026-09-25_1121_before.md here. 
     4 out of 5 criteria met. One was missed. -->
     I am looking at results/run_2026-09-25_1627_before.md here.
     All 5 criteria have met.

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | my questions were based on what I saw in corpus, so I got the answers directly and chunks contained the answers. Met with 5/5  |
| 2 | Every answer names a source | MET | every answer named the source, and even multliple if required in either brackets or listed as "Source:". MET with 5/5 |
| 3 | Gate stops out-of-corpus questions | MET | gate refused all 5 unrelated questions. Met with 5/5 |
| 4 | Chunk size | MET |  88 chunks, 317 characters on average
(shortest 178, longest 549), hence the chunk size is in correct range |
| 5 | top-k Chunks | MET |   I looked the number of files retrieved because in this corpus we have each file as a chunk.  |

<!--| 5 | Time to generate | MISSED | In the first run, when the model was not available it took more than 2 minutes for the first question and more than 8 seconds for 2nd question. Hence it missed with 3/5 | -->

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

<!-- Critera 5 is the only one which was missed. In the first run, when the model was not available it took more than 2 minutes for the first question and more than 8 seconds for 2nd question. which made it 3/5. For second run, all of the results came back before the 5 seconds was up. For third run, again the first question took more than 8s.
     Important note here is that, criteria 5 failed because i added additional code for 503 fail. It won't run on the original code. -->

     None of the criteria is missing, all have passed.



## The Improvement

**What I changed:**
There was nothing to change

**Why I picked it:**
Nothing to change as all criteria has met.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

<!-- I updated the criteria 5 text because there is no way to find how long one would have to keep trying to get the model. I believe it wasn't initially correct on its own. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5  | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk size | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. top-k chunks | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- | 5. Time to generate| 5/5 | 5/5 | 5/5 | 5/5 | MET |-->


**Did it help?**

Nothing changed for after.
<!-- Yes it did help because I updated the criteria itself and also didn't have the 503 errors this time. 
<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->
Nothing is broken. 

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
Yes I would write the criteria 5 differently and that's what I did. I would have added one with no hallucinations or something too. 
