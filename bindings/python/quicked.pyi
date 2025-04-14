"""

QuickEd - A high-performance exact sequence alignment based on the bound-and-align paradigm
===========================================================================================

QuickEd is a high-performance exact sequence alignment based on the bound-and-align paradigm.
Currently, QuickEd focuses on DNA sequence alignment, using the edit distance (Levenshtein distance) metric.

    >>> pattern = "ACGT"
    >>> text = "ACTT"
    >>> aligner = quicked.QuickedAligner()
    >>> aligner.align(pattern, text)
    >>> score = aligner.getScore()
    >>> cigar = aligner.getCigar()

QuickEd is actually a C library, and this package is it’s wrapper for Python.
Check out QuickEd's GitHub for more code examples and more details on how QuickEd works.
"""
from __future__ import annotations
import typing
__all__ = ['QuickedAlgo', 'QuickedAligner', 'QuickedException']
class QuickedAlgo:
    """

    QuickedAlgo
    ===========

    Enumeration of alignment algorithms

    Members:
      QUICKED : QuickEd algorithm
      WINDOWED : WindowEd algorithm
      BANDED : BandEd algorithm
      HIRSCHBERG : Hirschberg algorithm
    """
    BANDED: typing.ClassVar[QuickedAlgo]  # value = <QuickedAlgo.BANDED: 2>
    HIRSCHBERG: typing.ClassVar[QuickedAlgo]  # value = <QuickedAlgo.HIRSCHBERG: 3>
    QUICKED: typing.ClassVar[QuickedAlgo]  # value = <QuickedAlgo.QUICKED: 0>
    WINDOWED: typing.ClassVar[QuickedAlgo]  # value = <QuickedAlgo.WINDOWED: 1>
    __members__: typing.ClassVar[dict[str, QuickedAlgo]]  # value = {'QUICKED': <QuickedAlgo.QUICKED: 0>, 'WINDOWED': <QuickedAlgo.WINDOWED: 1>, 'BANDED': <QuickedAlgo.BANDED: 2>, 'HIRSCHBERG': <QuickedAlgo.HIRSCHBERG: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class QuickedAligner:
    """

    QuickedAligner
    ==============

    This class defines an aligner object that can be used to perform sequence alignment.
    It is initialized with default parameters and can be configured using various setter methods.

    """
    def __init__(self) -> None:
        ...
    def align(self, pattern: str, text: str) -> None:
        """
        Aligns the provided pattern and text according to the current parameters
        """
    def getCigar(self) -> str:
        """
        Gets the CIGAR string representing the alignment
        """
    def getScore(self) -> int:
        """
        Gets the alignment score
        """
    def setAlgorithm(self, algorithm: QuickedAlgo) -> None:
        """
        Sets the algorithm to be used for alignment
        """
    def setBandwidth(self, bandwidth: int) -> None:
        """
        Sets the bandwidth for BandEd alignment
        """
    def setForceScalar(self, force_scalar: bool) -> None:
        """
        Forces scalar computation (i.e., no SIMD instructions)
        """
    def setHEWPercentage(self, hew_percentage: int) -> None:
        """
        Sets the HEW percentage
        """
    def setHEWThreshold(self, hew_threshold: int) -> None:
        """
        Sets the HEW threshold
        """
    def setOnlyScore(self, only_score: bool) -> None:
        """
        Sets whether only the score should be computed
        """
    def setOverlapSize(self, overlap_size: int) -> None:
        """
        Sets the overlap size for WindowEd alignment
        """
    def setWindowSize(self, window_size: int) -> None:
        """
        Sets the window size for WindowEd alignment
        """
class QuickedException(Exception):
    pass
