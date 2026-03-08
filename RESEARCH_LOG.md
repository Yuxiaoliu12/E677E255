# Research Log: E677 → E255

## 2026-03-08: Project initialization

**Goal**: Build a constraint propagation + ML-guided search engine to find a finite magma satisfying E677 but violating E255 (or prove none exists).

**Completed**:
- Read and summarized the full Zulip discussion (~5000 lines, 631 messages from Tao, Le Floch, Brox, Bolan, Tencer, Nielsen, Reinke, McNeil, and others)
- Key takeaway: extensive human effort has ruled out all "natural" construction methods (linear, cohomological, piecewise affine, twisting, gluing). If a counterexample exists, it requires a genuinely new approach.
- Designed 5-phase implementation plan with two-agent architecture
- Built Phase 1 core engine:
  - `core/magma.py` — partial multiplication table with left-bijectivity tracking
  - `core/bijectivity.py` — O(1) partial permutation operations
  - `core/propagator.py` — E677 constraint propagation (4 trigger cases)
  - `core/search.py` — DPLL search with pluggable heuristics
  - `core/heuristics.py` — MRV and row-first heuristics
  - `core/logger.py` — JSONL decision logging for ML training
  - `core/known_models.py` — verified linear model database
  - `verification/` — independent E677, E255, property checkers

**Bug found & fixed**: Propagator state corruption — partial forced assignments weren't rolled back on ContradictionError. This caused the search to exhaust in 27 nodes instead of finding models. See `bugs_and_fixes.md` in memory.

**Benchmark results** (Phase 1, MRV heuristic, no pruning):
| Size | Time | Models | Counterexamples | Notes |
|------|------|--------|-----------------|-------|
| 5 | 0.65s | 6 | 0 | Exhaustive |
| 6 | 60s timeout | 0 | 0 | Correct: no models exist |
| 7 | 60s timeout | 120 | 0 | Not exhaustive |
| 8 | 60s timeout | 0 | 0 | Correct: no models exist |

**Verified linear model coefficients** (brute force over Z/pZ):
- p=5: (2,4); p=7: (4,1),(4,3); p=11: (4,8),(5,7),(6,6),(10,2)
- p=13: (9,11); p=19: (7,3),(7,4); p=31: 5 pairs

**44 tests passing.**

**Next**: Phase 2 — immunity-based pruning rules, stronger heuristics, construction library.
