# Masirah Island Wind Turbine Proposal

# Abstract

Wind-diesel hybrid systems is a power generation scheme that can reduce electricity prices for remote communities that are not connected to a large regional or national grid.  The island of Masirah is a community off the coast of Oman that relies on diesel generators to produce electricity.  Electricity on Masriah is expensive due to the high price of diesel on the island.  The island has a high load in the summer due to air-conditioning, yet also receives high winds during the summer months.  A simulation using Matlab and Homer Energy software was performed for Masirah to determine if wind turbines could be installed to reduce fuel costs.  It was determined that 3 wind turbines could be installed without energy storage, and 8 turbines could be installed with energy storage.  

# Introduction

![map](/png/Figure_7.png)

Remote communities around the world are facing economic and financial challenges due to the high energy prices.  This is typically due to communities not being connected to a large national or regional grid where they would otherwise benefit from cheap and dependable electricity.  This leaves communities facing a difficult situation where they need to overcome geographical, logistical, and economic barriers in order to obtain the required electricity at a reasonable price.  The centralized nature of electricity generation, where large coal, natural gas, and nuclear power plants have typically been the foundation of electrical grids, have left remote communities at a disadvantage due to remote communities.  Centralized power plants are typically located in densely populated areas, which has left remote communities to support themselves.  A typical solution to this dilemma is to install diesel generators that are properly sized to the local electricity demand.  Using diesel generators can mean high fuel costs for operating the generators.  

![candidate wind turbines](/png/Figure_9.png)

One particular community with the potential to utilize the wind-diesel hybrid system is the is Masirah Island.  Masirah is the largest island of Oman, located about 15 km from the coast of the Arabian Peninsula.  The island is about 15 km long and 5 km wide, with a population of 10,000 people.  Transportation between the mainland and the island consists of ferries and air travel.  The electrical demand is supplied entirely by ten diesel generators ranging in size from 265 to 3136 kW.  Fuel costs for the generators are high due to the costly transportation required to ship the fuel to the island.  The price of diesel on Masirah is $0.468/L. The electrical demand is highest in the summer due to higher air-conditioning load, while it decreases during the winter months.  The wind speed relatively matches the electrical demand for the island, with wind speeds highest in the summer.  A wind-diesel hybrid system might be an option for this community, and will be evaluated in this simulation.


# Method

![power curves](/png/Figure_3.png)

For this simulation, one wind turbine will be selected from six candidate turbines to be integrated into a wind-hybrid diesel system on Masirah Island.  Simulations will be performed in Matlab and Homer Energy to select the optimum wind turbine, number of turbines, and if energy storage is a viable option.  Matlab will be used to determine the ideal wind turbine based on which turbine has the highest average coefficient of performance for the wind speed profile of Masirah.  The annualized cost and generated electricity for eight 1000 MW diesel generators and one wind turbine will be calculated using Homer Energy.  The cost of electricity (COE) for each generator can then be calculated, and the price of fuel will be used as a variable to determine the break-even point for diesel generators and wind turbines.  If the price of diesel is above the break-even point, then installing wind turbines will be a worthwhile investment.  Matlab will then be used to determine the maximum number of wind turbines that can be installed with and without energy storage.   

![wind load profiles](/png/Figure_1.png)

![weibull distribution](/png/Figure_2.png)

# Results

![results](/png/Figure_13.png)

The turbine with the lowest COE ($/kWh) is the Enercon E70, and this will be the chosen turbine for this proposal.  Despite having a lower overall efficiency on Masirah Island, the amount of energy generated when compared to the annualized cost.  Enercon's E44, E48, and E82 were also in consideration for the selected turbine model.  A lower COE value for the E70 will allow it to be more profitable when compared to diesel generation on Masirah, even when diesel is at a lower than average fuel price.

# Conclusion

In order for isolated communities like Masirah to reduce energy costs, it would be recommended to install wind turbines to reduce the expensive fuel cost needed to operate diesel generators.  It was determined that without energy storage, 3 turbines could be installed to reduce the fuel costs.  This was determined because 3 wind turbines do not produce excess electricity on Masirah.  For the simulation with energy storage, it was determined that 8 turbines could be used.  This number was determined from comparing the COE of wind turbines with batteries and the COE of diesel generators at the price of diesel on Masirah.  More turbine may be able to be installed on Masirah without energy storage if a dump load is used to divert excess electricity generated during high winds and a low load.  This simulation shows that isolated communities that are not connected to a regional or national grid could utilize wind turbines to reduce electricity costs.  The addition of wind turbines for remote communities not only reduces electricity prices, but also emits fewer greenhouse gases and gives these communities a sense of energy independence.  
