#!/usr/bin/env python3
"""Module demonstrating multiple inheritance."""


class Fish:
    """Fish class."""

    def swim(self):
        """Fish swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Bird flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class using multiple inheritance."""

    def fly(self):
        """FlyingFish flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """FlyingFish swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """FlyingFish habitat."""
        print("The flying fish lives both in water and the sky!")
