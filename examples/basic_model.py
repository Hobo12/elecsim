"""
Basic ElecSim Model Example

This script demonstrates the most basic usage of the ElecSim electricity market simulation.
It creates a World model starting in 2018 and runs the simulation for a specified number of years.

ElecSim is an agent-based model of an electricity market. Through simulation, it allows
practitioners to explore the effect of different policy options and starting conditions
on electricity markets.

Usage (local):
    python examples/basic_model.py
    
Usage (Docker):
    docker build -t elecsim .
    docker run elecsim
"""

from elecsim.model.world import World

# Configuration parameters
NUMBER_OF_YEARS = 2  # Number of years to simulate (reduced for quick demo)
MARKET_TIME_SPLICES = 8  # Number of representative days per year (default is 8)
INITIALIZATION_YEAR = 2018  # Starting year for the simulation

if __name__ == "__main__":
    # Calculate total number of steps (years * time_slices)
    number_of_steps = NUMBER_OF_YEARS * MARKET_TIME_SPLICES

    print("=" * 60)
    print("ElecSim Basic Model Example")
    print("=" * 60)
    print(f"Initialization year: {INITIALIZATION_YEAR}")
    print(f"Number of years to simulate: {NUMBER_OF_YEARS}")
    print(f"Market time slices per year: {MARKET_TIME_SPLICES}")
    print(f"Total steps: {number_of_steps}")
    print("-" * 60)

    # Create the World model
    # - initialization_year: Year to begin simulation
    # - log_level: Set to "info" for useful logging information
    # - market_time_splices: Number of representative days per year
    # - number_of_steps: Total number of steps in the simulation
    world = World(
        initialization_year=INITIALIZATION_YEAR,
        log_level="info",
        market_time_splices=MARKET_TIME_SPLICES,
        number_of_steps=number_of_steps
    )

    # Run the simulation
    # The outer loop iterates through years
    # The inner loop iterates through representative days within each year
    for year in range(NUMBER_OF_YEARS):
        for time_step in range(MARKET_TIME_SPLICES):
            # Step the model forward
            # Returns: average_electricity_price, carbon_emitted
            avg_price, carbon = world.step()

    print()
    print("=" * 60)
    print("Simulation Complete!")
    print("=" * 60)
    print(f"Final average electricity price: {avg_price:.2f}")
    print(f"Final carbon emitted: {carbon:.2f}")
    print()
    print("Output data has been saved to 'ElecSim_Output' directory.")
    print("=" * 60)
