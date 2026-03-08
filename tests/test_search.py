"""Tests for core/search.py — DPLL search engine."""

import pytest

from core.search import DPLLSearch, SearchConfig, search_e677


class TestSearch:
    def test_size_1(self):
        """Size 1 trivially satisfies E677 and E255."""
        result = search_e677(1, max_time=10)
        assert len(result.models) >= 1
        assert len(result.counterexamples) == 0

    def test_size_2_no_model(self):
        """No E677 model of size 2 exists."""
        config = SearchConfig(
            n=2,
            find_all_models=True,
            find_counterexample=False,
            apply_symmetry_breaking=False,
            max_time=30,
        )
        searcher = DPLLSearch(config)
        result = searcher.search()
        # Size 2: no models exist (from Zulip discussion)
        assert len(result.models) == 0

    def test_size_3_no_model(self):
        """No E677 model of size 3 exists."""
        config = SearchConfig(
            n=3,
            find_all_models=True,
            find_counterexample=False,
            apply_symmetry_breaking=False,
            max_time=60,
        )
        searcher = DPLLSearch(config)
        result = searcher.search()
        assert len(result.models) == 0

    def test_size_4_no_model(self):
        """No E677 model of size 4 exists."""
        config = SearchConfig(
            n=4,
            find_all_models=True,
            find_counterexample=False,
            apply_symmetry_breaking=False,
            max_time=120,
        )
        searcher = DPLLSearch(config)
        result = searcher.search()
        assert len(result.models) == 0

    def test_size_5_finds_model(self):
        """Size 5 should find at least one E677 model."""
        config = SearchConfig(
            n=5,
            find_all_models=False,
            find_counterexample=False,
            apply_symmetry_breaking=False,
            max_time=120,
        )
        searcher = DPLLSearch(config)
        result = searcher.search()
        assert len(result.models) >= 1
        # All found models should satisfy E255
        assert len(result.counterexamples) == 0

    def test_no_counterexample_size_5(self):
        """No E677 anti-E255 model of size 5 exists."""
        result = search_e677(5, max_time=60)
        assert len(result.counterexamples) == 0

    def test_search_result_stats(self):
        """Search result should have valid statistics."""
        result = search_e677(3, max_time=10)
        assert result.nodes_explored > 0
        assert result.time_seconds > 0
        assert result.time_seconds < 15  # should finish well within limit
